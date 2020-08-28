# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def drawling(point, angle, length):
        angle_in = 180-int(180*(n-2)/n)
        print(angle_in)
        a=0
        for angle in range(angle, angle + 180*(n-2), angle_in):
            a += 1
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
            v1.draw()
            point = v1.end_point

    return drawling


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=15, length=100)


sd.pause()
