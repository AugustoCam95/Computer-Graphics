from objectcg import ObjectCG

import numpy as np
import math

class Window:

    def __init__(self, d, w, h, n, m):
        self.d = d
        self.w = w
        self.h = h
        self.n = n
        self.m = m

        self.usersWindow = []

        for i in range(n):
            self.usersWindow.append([0] * m)

        self.deltaX = w / m
        self.deltaY = h / n

        self.calculatePixelsPositions()

    def calculatePixelsPositions(self):

        for i in range(self.n):  # [0..n-1]
            y = (self.h / 2) - (self.deltaY / 2) - (i * self.deltaY)
            for j in range(self.m):  # [0..m-1]
                x = -(self.w / 2) + (self.deltaX / 2) + (j * self.deltaX)
                self.usersWindow[i][j] = [x, y, - self.d]

    def getUsersWindow(self):
        return self.usersWindow

    def n(self):
        return self._n

    def m(self):
        return self._m

    def getPosPixel(self, n, m):
        return self.usersWindow[n][m]