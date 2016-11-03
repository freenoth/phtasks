#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    DOCSTRING FOR MODULE
"""

# py_ver    : [3.5.2]

# date      : [03.11.2016]
# author    : Aleksey Yakovlev
# email     : nothscr@gmail.ru
# contacts  : github: freenoth

# license   : WTFPL v2

# [ LICENSE_COMMENT ]
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it
# under the terms of the Do What The Fuck You Want To Public License Version 2
# See http://www.wtfpl.net/ for more details.


# imports
import sys
import time


class Timer(object):
    """ Service class, needed to control running time. """
    def __init__(self):
        self.start_time = time.time()

    def __str__(self):
        current_time = time.time()
        return '{:.3f} sec'.format(current_time - self.start_time)


def calc(n):
    # n - количество квадратов в сетке, вершин для переходов на одну больше
    points = n + 1

    # сначала рассчитаем количество возможных путей в точках на главной диагонали
    # двигаться будем по диагоналям, начиная с конечной вершины
    diagonal = [1]
    for i in range(0, points - 1):
        next_diagonal = [0 for x in range(0, len(diagonal) + 1)]
        for j in range(0, len(diagonal)):
            next_diagonal[j] += diagonal[j]
            next_diagonal[j+1] += diagonal[j]
        diagonal = next_diagonal

    # теперь двигаемся от главной диагонали к начальной точке, схлапывая суммы
    while len(diagonal) > 1:
        next_diagonal = [0 for x in range(0, len(diagonal) - 1)]
        for j in range(0, len(next_diagonal)):
            next_diagonal[j] = diagonal[j] + diagonal[j + 1]
        diagonal = next_diagonal

    return diagonal[0]


def _main():
    print('Print "quit" for exiting...\n')

    while True:
        s = input('n = ')
        if s == 'quit':
            break

        try:
            n = int(s)

            timer = Timer()

            result = calc(n)
            print('result = {0}\ncalculated over {1}\n'.format(result, timer))
        except ValueError as err:
            print(err)


if __name__ == '__main__':
    print('using python {0}.{1}.{2}\n'.format(sys.version_info[0],
                                              sys.version_info[1],
                                              sys.version_info[2]))

    _main()
