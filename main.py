# Import Grid class
from grid import Grid
from algoritimos.bresenham import bres
from algoritimos.circulo import circ


# Initialize grid
grid = Grid(extent=10, size=500)

# Defines an algorithm
def my_render_cells_algorithm(selected_cells, rendered_cells, parameters):
    for cell in selected_cells:
        grid.render_cell(cell)

# Adds the algorithm to the grid
# grid.add_algorithm(name="Desenhar pontos", parameters=None, algorithm=my_render_cells_algorithm)

def bresenham(selected_cells, rendered_cells, parameters):
    ponto1 = selected_cells[0]
    ponto2 = selected_cells[1]
    resultado = bres(ponto1, ponto2)
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)
        
def circulo(selected_cells, rendered_cells, parameters):
    centro = selected_cells[0]
    raio =  int(parameters['raio'])
    resultado = circ(centro, raio)
    for ponto in resultado:
        new_cell = (ponto)
        grid.render_cell(new_cell)


# Defines another algorithm
def translate(selected_cells, rendered_cells, parameters):
    # This one needs x and y parameters, so they will be specified when calling add_algorithm
    x_offset = int(parameters['x']) # Gets the value of the 'x' parameter
    y_offset = int(parameters['y']) # Gets the value of the 'y' parameter
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)
    for cell in rendered_cells:
        if min_x <= cell[0] <= max_x and min_y <= cell[1] <= max_y:
            grid.clear_cell(cell)
            new_cell = (cell[0] + x_offset, cell[1] + y_offset)
            grid.render_cell(new_cell)

# Adds the algorithm to the grid (notice how this one specifies 'x' and 'y')
# grid.add_algorithm(name='Translate', parameters=['x', 'y'], algorithm=translate)
grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham)
grid.add_algorithm(name='Circulo', parameters=['raio'], algorithm=circulo)

# Complete the script by displaying the grid
grid.show()