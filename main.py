import math
import numpy as np
from grid import Grid
from algoritmos.bresenham import bres
from algoritmos.circulo import circ
from algoritmos.polilinha import poli
from algoritmos.preenchimento import flood_fill
from algoritmos.transformacao import transl, escal, rotac, draw_polygon
from algoritmos.curva import bezier
from algoritmos.recorte import sutherland_hodgman
from algoritmos.projecoes import geraProjecao

grid = Grid(extent=10, size=800)


def my_render_cells_algorithm(selected_cells, rendered_cells, parameters):
    for cell in selected_cells:
        grid.render_cell(cell)


def bresenham(selected_cells, rendered_cells, parameters):
    ponto1 = selected_cells[0]
    ponto2 = selected_cells[1]
    resultado = bres(ponto1, ponto2)
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
    resultado = transl(selected_cells, rendered_cells)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def rotacao(selected_cells, rendered_cells, parameters):
    
    angulo = np.deg2rad(float(parameters['angulo']))
    
    resultado = rotac(angulo, rendered_cells)
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
    print(resultado)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)

def varredura(selected_cells, rendered_cells, parameters):
    pontos = rendered_cells
    y_min = min(point[1] for point in pontos)
    y_max = max(point[1] for point in pontos)
    for y in range(y_min, y_max + 1):
        intersecoes = []
        for i in range(len(pontos)):
            x1, y1 = pontos[i]
            x2, y2 = pontos[(i+1) % len(pontos)] 
            if (y1 <= y < y2) or (y2 <= y < y1):
                x_interscao = int(x1 + (float(y - y1) / (y2 - y1)) * (x2 - x1))
                intersecoes.append(x_interscao)
        intersecoes.sort()
        for i in range(0, len(intersecoes), 2):
            x_inicio = intersecoes[i]
            x_fim = intersecoes[i+1] if i+1 < len(intersecoes) else x_inicio
            for x in range(x_inicio, x_fim + 1):
                grid.fill_cell((x, y))
                
def recorte(selected_cells, rendered_cells, parameters):
    resultado = sutherland_hodgman(selected_cells, rendered_cells)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)
        
def projecoes(selected_cells, rendered_cells, parameters):
    resultado = geraProjecao(rendered_cells)
    projecao = []
    print(resultado)
    for ponto in resultado[0]:
        projecao.append(ponto)
    for ponto in resultado[1]:
        projecao.append(ponto)
    for ponto in resultado[2]:
        projecao.append(ponto)
    for pontoProjecao in projecao:
        new_cell = (pontoProjecao)
        grid.render_cell(new_cell)
  
        

grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham)

grid.add_algorithm(name='Círculo', parameters=None, algorithm=circulo)

grid.add_algorithm(name='Polilinhas', parameters=None, algorithm=polilinha)

grid.add_algorithm(name='Preenchimento',parameters=None, algorithm=preenchimento)

grid.add_algorithm(name='Varredura',parameters=None, algorithm=varredura)

grid.add_algorithm(name='Translação', parameters=None, algorithm=translacao)

grid.add_algorithm(name='Escala', parameters=['x', 'y'], algorithm=escala)

grid.add_algorithm(name='rotação', parameters=['angulo'], algorithm=rotacao)

grid.add_algorithm(name='Curva', parameters=None, algorithm=curva)

grid.add_algorithm(name='Recorte', parameters=None, algorithm=recorte)

grid.add_algorithm(name='Projeção', parameters=None, algorithm=projecoes)

grid.show()
