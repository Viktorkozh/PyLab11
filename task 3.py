#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mult():
    """
    Cчитывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
    """
    a, inp = 1, 1

    while inp != 0:
        a *= inp
        inp = int(input("Введите число: "))

    return a


if __name__ == '__main__':
    print(f"Полученное произведение: {mult()}")
