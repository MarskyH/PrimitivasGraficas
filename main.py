'''
Dupla: 
Marcus Huriel Lira Loureiro - 202004940010
João Paulo de Souza Rodrigues - 202004940039
'''

import math
import numpy as np
from grid import Grid
from algoritmos.bresenham import bres
from algoritmos.circulo import circ
from algoritmos.polilinha import poli
from algoritmos.preenchimento import flood_fill, var
from algoritmos.transformacao import transl, escal, rotac
from algoritmos.curva import bezier


grid = Grid(extent=10, size=600)


def bresenham(selected_cells, rendered_cells, parameters):
    ponto1 = selected_cells[0]
    ponto2 = selected_cells[1]
    resultado = bres(ponto1, ponto2)
    print(resultado)
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def circulo(selected_cells, rendered_cells, parameters):
    ponto1 = selected_cells[0]
    ponto2 = selected_cells[1]
    x1 = ponto1[0]
    y1 = ponto1[1]
    x2 = ponto2[0]
    y2 = ponto2[1]
    centro = ponto1
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    raio = int(distancia)
    print(centro, raio, distancia)
    resultado = circ(centro, raio)
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def polilinha(selected_cells, rendered_cells, parameters):
    resultado = poli(selected_cells)
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def preenchimento(selected_cells, rendered_cells, parameters):
    fill_cells = []
    resultado = flood_fill(selected_cells[0][0], selected_cells[0][1],
                           rendered_cells, fill_cells)
    for ponto in resultado:
        new_fill_cell = (ponto)
        grid.fill_cell(new_fill_cell)


def translacao(selected_cells, rendered_cells, parameters):
    translacao = list(parameters.values())
    
    x = int(translacao[0])
    y = int(translacao[1])
    
    translacao = (x, y)

    resultado = transl(translacao, rendered_cells)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def rotacao(selected_cells, rendered_cells, parameters):
    
    xp = int(selected_cells[0][0])
    yp = int(selected_cells[0][1])
    pivo = (xp, yp)
    
    angulo = np.deg2rad(float(parameters['angulo']))
    
    resultado = rotac(angulo, rendered_cells, pivo)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def escala(selected_cells, rendered_cells, parameters):
    print('parameters:', parameters)
    x = int(parameters['x'])
    y = int(parameters['y'])
    escala = (x, y)
    resultado = poli(escal(selected_cells, escala, selected_cells[0]))
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)
        
def curva(selected_cells, rendered_cells, parameters):
    print(rendered_cells)
    grauCurva = len(selected_cells)  - 1
    resultado  = bezier(selected_cells, rendered_cells, grauCurva)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)

def varredura(selected_cells, rendered_cells, parameters):
    pontos = rendered_cells
    resultado = var(pontos)
    for ponto in resultado:
        new_cell = (ponto)
        grid.fill_cell(new_cell)
   
                
def recorte(selected_cells, rendered_cells, parameters):
    xmin = int(parameters['xmin'])
    ymin = int(parameters['ymin'])
    xmax = int(parameters['xmax'])
    ymax = int(parameters['ymax'])
    grid.clip_window = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    grid._redraw()
                
grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham)

grid.add_algorithm(name='Círculo', parameters=None, algorithm=circulo)

grid.add_algorithm(name='Polilinhas', parameters=None, algorithm=polilinha)

grid.add_algorithm(name='Preenchimento',parameters=None, algorithm=preenchimento)

grid.add_algorithm(name='Varredura',parameters=None, algorithm=varredura)

grid.add_algorithm(name='Translação', parameters=['x', 'y'], algorithm=translacao)

grid.add_algorithm(name='Escala', parameters=['x', 'y'], algorithm=escala)

grid.add_algorithm(name='Rotação', parameters=['angulo'], algorithm=rotacao)

grid.add_algorithm(name='Curva', parameters=None, algorithm=curva)

grid.add_algorithm(name='Recorte', parameters=['xmin', 'ymin', 'xmax', 'ymax'], algorithm=recorte)

grid.add_algorithm(name='Projeções', parameters=[], algorithm=None)

grid.show()


# Coordenadas dos vértices 
vertices = [
    (1, 1, 1),  # Vértice A
    (2, 1, 1),  # Vértice B
    (2, 2, 1),  # Vértice C
    (1, 2, 1),  # Vértice D
    (1, 1, 10),  # Vértice E
    (10, 1, 10),  # Vértice F
    (10, 10, 10),  # Vértice G
    (1, 10, 10)   # Vértice H
]

