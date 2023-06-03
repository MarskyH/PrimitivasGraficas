from algoritmos.bresenham import bres
from algoritmos.polilinha import poli
import numpy as np

class Rasterizacao:
    def __init__(self, entrada):
        self.entrada = entrada  # lista de pontos do polígono de entrada
        self.resultado = []  # lista de pontos para serem rasterizados

class Projection(Rasterizacao):
    def __init__(self, entrada, recuo):
        for coordenada in entrada:
            coordenada[2] += recuo
        super().__init__(entrada)

    def ortogonal(self):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_projecao = [
            [0 for i in range(len(self.entrada[0]))]
            for i in range(len(self.entrada[0]))
        ]

        missed_diagonal = 2
        x_saida = 0
        y_saida = 1

        for i in range(0, len(self.entrada[0])):
            if i != missed_diagonal:
                matriz_projecao[i][i] = 1

        for ponto in self.entrada:
            projecao = np.dot(matriz_projecao, ponto)
            self.resultado.append([projecao[x_saida], projecao[y_saida]])

        self.resultado = poli(self.resultado)
      

    def perspectiva(self, distancia):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_perspectiva = [
            [0 for i in range(len(self.entrada[0]))]
            for i in range(len(self.entrada[0]))]

        for i in range(0, len(self.entrada[0])):
            if i != len(self.entrada[0]) - 1:
                matriz_perspectiva[i][i] = distancia

        matriz_perspectiva[len(matriz_perspectiva) - 1][len(matriz_perspectiva) - 2] = 1

        for ponto in self.entrada:
            projecao = np.dot(matriz_perspectiva, ponto)
            projecao = np.multiply(projecao, 1 / ponto[2])
            self.resultado.append([round(projecao[0]), round(projecao[1])])

        self.resultado = poli(self.resultado)
   

        unicos = []

        for ponto in self.resultado:
            if ponto[0] == ponto[1]:
                if [ponto[0], ponto[1]] not in unicos:
                    unicos.append([ponto[0], ponto[1]])
                    
        unicos.pop(0)
        
        if len(unicos) >= 2: #impedir erros de index da lista
            self.resultado += bres(unicos[0], unicos[1])
        
