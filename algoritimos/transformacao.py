from math import sin, cos
from algoritimos.bresenham import bres
import numpy as np


def transl(p_translacao, vetor):

    xT = p_translacao[0][0]
    yT = p_translacao[0][1]

    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (x + xT, y + yT)

    return vetor


def escal(points, factors):
    print(points)
    xE = factors[0]
    yE = factors[1]

    scaledPoints = []
    for point in points:
        x = point[0]
        y = point[1]
        scaledX = x * xE
        scaledY = y * yE
        scaledPoint = (scaledX, scaledY)
        print(scaledPoint)
        scaledPoints.append(scaledPoint)

    return scaledPoints

def draw_polygon(points):
    num_points = len(points)
    novoPoligno = []
    for i in range(num_points):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % num_points]
        line_points = bres((x0, y0), (x1, y1))
        for point in line_points:
            novoPoligno.append(point)
            
    return novoPoligno


def rotac(angulo, vetor):
    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (int(round(x * cos(angulo) - y * sin(angulo))),
                    int(round(x * sin(angulo) + y * cos(angulo))))

    return vetor
