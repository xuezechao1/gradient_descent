#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import math
import numpy as np
from xzc_tools import tools
from matplotlib import pyplot as plt

@tools.funcRunTime
def gradient_descent():
    try:
        x_before = float(input('请输出初始x的值(-9,9):'))
        step = float(input('请输入步长(0,1):'))
        stop_value = float(input('请输入梯度下降的停止值:'))

        if x_before <= -9 or x_before >= 9 or step <= 0 or step >= 1:
            tools.printInfo(3, '输入有误')
            sys.exit()

        x = [i for i in range(-10, 11)]
        y = [i ** 2 for i in x]

        x_temp = []
        y_temp = []

        OK = True
        while OK:
            x_after = x_before - step * 2 * x_before
            y_before = x_before*x_before
            y_after = x_after*x_after
            y_change = math.fabs(y_before - y_after)
            if y_change < stop_value:
                OK = False
            else:
                x_temp.extend([x_before, x_after, x_after])
                y_temp.extend([y_before, y_before, y_after])
                x_before = x_after

        plt.title("gradient descent")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x, y)
        plt.plot(x_temp, y_temp, 'r')
        plt.show()

    except Exception as msg:
        tools.printInfo(2, msg)

if __name__ == '__main__':
    gradient_descent()