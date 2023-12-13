#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    """
    Вычисляет площадь цилиндра.
    """
    def circle(rad):
        """
        Вычисляет площадь круга.
        """
        return math.pi * rad ** 2

    rad = float(input("Введите радиус основания цилиндра: "))
    hgt = float(input("Введите высоту цилиндра: "))

    side = 2 * math.pi * rad * hgt
    full = input(
        "Желаете ли получить полную площадь цилиндра? (y/n): ").strip().lower()

    if full == "y":
        # Добавляем площадь двух оснований к площади боковой поверхности
        side += 2 * circle(rad)

    return side


if __name__ == '__main__':
    print(f"Площадь цилиндра: {cylinder()}")
