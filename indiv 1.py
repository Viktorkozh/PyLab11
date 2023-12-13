#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def add_person(people):
    """
    Добавление нового человека в список.
    Список сортируется по знаку зодиака после добавления нового элемента.
    """
    name = input("Фамилия: ")
    surname = input("Имя: ")
    date_of_birth = datetime.strptime(
        input("Введите дату рождения (в формате ДД.ММ.ГГГГ через точку): "), '%d.%m.%Y')
    zodiac_sign = input("Знак зодиака: ")

    person = {
        'name': name,
        'surname': surname,
        'date_of_birth': date_of_birth,
        'zodiac_sign': zodiac_sign
    }

    people.append(person)
    people.sort(key=lambda item: item.get('zodiac_sign', ''))


def list_people(people):
    """
    Вывод таблицы людей.
    """
    line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 20,
        '-' * 15,
        '-' * 13
    )
    print(line)
    print(
        '| {:^4} | {:^20} | {:^20} | {:^15} | {:^12} |'.format(
            "№",
            "Имя",
            "Фамилия",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)

    for idx, person in enumerate(people, 1):
        birth_date_str = person.get('date_of_birth').strftime('%d.%m.%Y')
        print(
            '| {:^4} | {:<20} | {:<20} | {:<15} | {:<13} |'.format(
                idx,
                person.get('name', ''),
                person.get('surname', ''),
                person.get('zodiac_sign', ''),
                birth_date_str
            )
        )

    print(line)


def select_people(people, month):
    """
    Вывести список людей, родившихся в заданном месяце.
    """
    count = 0
    for person in people:
        if person.get('date_of_birth').month == month:
            count += 1
            print('{:>4}: {} {}'.format(count, person.get(
                'name', ''), person.get('surname', '')))

    if count == 0:
        print("Люди, родившиеся в указанном месяце, не найдены.")


def show_help():
    """
    Вывести справку по командам программы.
    """
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <месяц> - вывод на экран информации о людях, родившихся в указанный месяц (цифра)")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    """
    Терминал.
    """
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            add_person(people)
        elif command == 'list':
            list_people(people)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            month = int(parts[1])
            select_people(people, month)
        elif command == 'help':
            show_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
