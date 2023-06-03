from math import sin, cos
from algoritmos.bresenham import bres
import numpy as np


def transl(p_translacao, vetor):

    xT = p_translacao[0]
    yT = p_translacao[1]

    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (x + xT, y + yT)

    return vetor


def escal(points, factors, fixed_point):
    print(points)
    xE = factors[0]
    yE = factors[1]
    scaledPoints = []
    
    for point in points:
        x = point[0]
        y = point[1]
        scaledX = fixed_point[0] + (x - fixed_point[0]) * xE
        scaledY = fixed_point[1] + (y - fixed_point[1]) * yE
        scaledPoint = (scaledX, scaledY)
        scaledPoints.append(scaledPoint)
  
    return scaledPoints



def rotac(angulo, vetor, pivo):
    xp = pivo[0]
    yp = pivo[1]

    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (int(round(xp + (x - xp) * cos(angulo) - (y - yp) * sin(angulo))),
                    int(round(yp + (x - xp) * sin(angulo) + (y - yp) * cos(angulo))))
    return vetor
