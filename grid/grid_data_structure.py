class GridDataStructure:
    def __init__(self, extent):
        self.extent = extent
        self.dimension = 2 * extent + 1
        self.rendered_cells = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.selected_cells = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.fill_cells = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.selected_count = 0

    def render_cell(self, cell):
        if self._cell_is_in_bounds(cell):
            x, y = self.coordinate_to_index(cell)
            self.rendered_cells[x][y] = 1
        else:
            print(f'Aviso: Comando render_cell ignorado. Célula {cell} está fora dos limites.')

    def fill_cell(self, cell):
        if self._cell_is_in_bounds(cell):
            x, y = self.coordinate_to_index(cell)
            self.fill_cells[x][y] = 2
        else:
            print(f'Aviso: Comando fill_cell ignorado. Célula {cell} está fora dos limites.')

    def clear_cell(self, cell):
        if self._cell_is_in_bounds(cell):
            x, y = self.coordinate_to_index(cell)
            self.rendered_cells[x][y] = 0
        else:
            print(f'Aviso: Comando clear_cell ignorado. Célula {cell} está fora dos limites.')

    def select_cell(self, cell):
        if self._cell_is_in_bounds(cell):
            x, y = self.coordinate_to_index(cell)
            if not self.selected_cells[x][y]:
                self.selected_count += 1
                self.selected_cells[x][y] = self.selected_count
        else:
            print(f'Aviso: Comando select_cell ignorado. Célula {cell} está fora dos limites.')

    def clear_all(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.rendered_cells[i][j] = 0
                self.selected_cells[i][j] = 0
                self.fill_cells[i][j] = 0
        self.selected_count = 0

    def clear_selected_cells(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.selected_cells[i][j] = 0
        self.selected_count = 0
        
    def clear_rendered_cells(self):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.rendered_cells[i][j] = 0
        
        
    def clear_fill_cells(self):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.fill_cells[i][j] = 0
            


    def _cell_is_in_bounds(self, cell):
        x, y = cell
        return -self.extent <= x <= self.extent and -self.extent <= y <= self.extent
    
    def get_selected_cells(self):
        selected_cells = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.selected_cells[i][j]:
                    selected_cells.append((i, j))
        selected_cells.sort(key=lambda cell: self.selected_cells[cell[0]][cell[1]])
        return list(map(self.index_to_coordinate, selected_cells))
    
    def get_rendered_cells(self):
        rendered_cells = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.rendered_cells[i][j]:
                    rendered_cells.append((i, j))
        return list(map(self.index_to_coordinate, rendered_cells))
    
    def get_fill_cells(self):
        fill_cells = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.fill_cells[i][j]:
                    fill_cells.append((i, j))
        return list(map(self.index_to_coordinate, fill_cells))
    
    
    def index_to_coordinate(self, index):
        return (index[0] - self.extent, index[1] - self.extent)
    
    def coordinate_to_index(self, coordinate):
        return (coordinate[0] + self.extent, coordinate[1] + self.extent)