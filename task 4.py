#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Запрашивает ввод с клавиатуры и возвращает в основную программу полученную строку.
    """
    return input("Введите данные: ")


def test_input(value):
    """
    Проверяет, можно ли переданное значение преобразовать к целому числу.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    """
    Преобразовывает переданное значение к целочисленному типу.
    """
    return int(value)


def print_int(value):
    """
    Не выводит переданное значение на экран и ничего не возвращает.
    """
    print(value)


if __name__ == '__main__':
    user_input = get_input()

    if test_input(user_input):
        integer = str_to_int(user_input)
        print_int(integer)
    else:
        print("Введенные данные не могут быть преобразованы в целое число.")
