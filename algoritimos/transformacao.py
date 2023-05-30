from math import sin, cos
import numpy as np


def transl(p_translacao, vetor):

    xT = p_translacao[0][0]
    yT = p_translacao[0][1]

    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (x + xT, y + yT)

    return vetor


def escal(p_escala, vetor):
    print("lenVetor", len(vetor))
    xE = p_escala[0]
    yE = p_escala[1]

    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]
        print(x * xE, y * yE)
        vetor[i] = (x * xE, y * yE)

    return vetor


def rotac(angulo, vetor):
    for i in range(len(vetor)):
        x = vetor[i][0]
        y = vetor[i][1]

        vetor[i] = (int(round(x * cos(angulo) - y * sin(angulo))),
                    int(round(x * sin(angulo) + y * cos(angulo))))

    return vetor
