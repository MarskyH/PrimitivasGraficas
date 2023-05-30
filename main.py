import math
from grid import Grid
from algoritimos.bresenham import bres
from algoritimos.circulo import circ
from algoritimos.polilinha import poli
from algoritimos.preenchimento import flood_fill
from algoritimos.transformacao import transl
from algoritimos.transformacao import escal
from algoritimos.transformacao import rotac

grid = Grid(extent=10, size=500)


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
    
    angulo = list(parameters.values())
    valor = int(angulo[0])
  
    resultado = rotac(valor, rendered_cells)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


def escala(selected_cells, rendered_cells, parameters):
    escala = list(parameters.values())

    x = int(escala[0])
    y = int(escala[1])

    escala = (x, y)
    resultado = escal(escala, rendered_cells)
    grid.clear_all()
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham)
grid.add_algorithm(name='Circulo', parameters=None, algorithm=circulo)

grid.add_algorithm(name='Polilinhas', parameters=None, algorithm=polilinha)

grid.add_algorithm(name='Preenchimento',
                   parameters=None,
                   algorithm=preenchimento)

grid.add_algorithm(name='Translacao', parameters=None, algorithm=translacao)

grid.add_algorithm(name='Escala', parameters=['x', 'y'], algorithm=escala)

grid.add_algorithm(name='rotacao', parameters=['angulo'], algorithm=rotacao)

grid.show()
