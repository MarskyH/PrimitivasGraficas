from tkinter import Tk, ttk, Canvas, Label, Frame, Button, Entry, Toplevel, StringVar
from .grid_data_structure import GridDataStructure

class Grid:
    
    # constantes
    SELECT_COLOR = 'red'
    DEFAULT_COLOR = 'white'
    PRINT_COLOR = 'black'
    FILL_COLOR = 'blue'
    MARGIN_SIZE = 10

    def __init__(self, extent, size, grid_columns=2):
        # Criando estrutura da grade
        self.raster = GridDataStructure(extent)
        self.window_size = size, size
        self.grid_size = size - 2 * Grid.MARGIN_SIZE, size - 2 * Grid.MARGIN_SIZE
        dimension = 2 * extent + 1
        self.cell_size = self.grid_size[0] / dimension, self.grid_size[1] / dimension
        self.root = Tk()
        
        style = ttk.Style()
        style.configure('Custom.TButton', foreground='#FCAB05', borderwidth=1, borderradius=10, width=30, height=10)

        # frame principal
        self.main_frame = Frame(self.root)
        self.main_frame.pack(anchor='center', expand=True)

        # frame de limpar células
        self.grid_frame = Frame(self.main_frame)
        self.grid_frame.pack(side='left', padx=10, pady=10)
        
        clear_frame = Frame(self.grid_frame)
        clear_frame.pack(padx=5, pady=10)
        ttk.Button(clear_frame, text='Limpar tudo', command=self._clear_all, style='Custom.TButton').grid(row=0, column=0) 
        ttk.Button(clear_frame, text='Limpar células Selecionadas', command=self._clear_selected_cells, style='Custom.TButton').grid(row=0, column=1) 
        ttk.Button(clear_frame, text='Limpar células rasterizadas', command=self._clear_rendered_cells, style='Custom.TButton').grid(row=1, column=0) 
        ttk.Button(clear_frame, text='Limpar células preenchidas', command=self._clear_fill_cells, style='Custom.TButton').grid(row=1, column=1) 

        # frame dos algoritmos
        self.controls_frame = Frame(self.main_frame)
        self.controls_frame.pack(side='right', padx=10, pady=10)

        self.grid_columns = grid_columns
        self.next_row = 0
        self.next_column = 0

        self.canvas = Canvas(self.grid_frame, width=size, height=size)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self._on_canvas_click)

    def add_algorithm(self, name, parameters=None, algorithm=None):
        frame = Frame(self.controls_frame)
        frame.pack(side='top', pady=5)
        entries = []
        if parameters:
            params = parameters  # Armazena os parâmetros em uma variável local
            open_params_button = ttk.Button(frame, text=name, style='Custom.TButton', width=25, command=lambda: self._open_params_window(name, params, entries, algorithm))
            open_params_button.pack(side='left')
        if algorithm and parameters is None:
            run_button = ttk.Button(frame, text=name, style='Custom.TButton', width=25, command=lambda: self._on_run_click(algorithm, entries))
            run_button.pack(side='left')
     
        self.next_column += 1
        if self.next_column >= self.grid_columns:
            self.next_column = 0
            self.next_row += 1
        return frame

    def fill_cell(self, cell):
        self.raster.fill_cell(cell)

    def render_cell(self, cell):
        self.raster.render_cell(cell)


    def clear_cell(self, cell):
        self.raster.clear_cell(cell)
        self._redraw()

    def clear_all(self):
        self.raster.clear_all()
        self._redraw()

    def show(self):
        self._redraw()
        self.root.mainloop()


    def _select_cell(self, cell):
        self.raster.select_cell(cell)
        
    def _on_canvas_click(self, event):
        x = event.x - Grid.MARGIN_SIZE
        raw_y = event.y - Grid.MARGIN_SIZE
        y = (self.grid_size[1]) - raw_y

        if 0 <= x <= self.grid_size[0] and 0 <= y <= self.grid_size[1]:
            print(x, y)
            cell_x = int(x // self.cell_size[0]) - self.raster.extent
            cell_y = int(y  // self.cell_size[1]) - self.raster.extent
            self._select_cell((cell_x, cell_y))
            self._redraw()


    def _redraw(self):
        self.canvas.delete('all')

        dimension = 2 * self.raster.extent + 1
        for i in range(dimension):
            for j in range(dimension):
                x1 = i * self.cell_size[0] + Grid.MARGIN_SIZE
                y1 = (dimension - j - 1) * self.cell_size[1] + Grid.MARGIN_SIZE
                x2 = x1 + self.cell_size[0]
                y2 = y1 + self.cell_size[1]
                x, y = i - (self.raster.extent*2 + 1), j - (self.raster.extent*2 + 1)
                if self.raster.selected_cells[x][y]:
                    color = Grid.SELECT_COLOR
                    text_color = Grid.DEFAULT_COLOR
                    text = str(self.raster.selected_cells[x][y])
                elif self.raster.rendered_cells[x][y]:
                    color = Grid.PRINT_COLOR
                    text_color = ''
                    text = ''
                elif self.raster.fill_cells[x][y]:
                    color = Grid.FILL_COLOR
                    text_color = ''
                    text =  ''
                else:
                    color = Grid.DEFAULT_COLOR
                    text_color = ''
                    text = ''
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='gray')
                if text:
                    x_center = (x1 + x2) / 2
                    y_center = (y1 + y2) / 2
                    font_size = int(min(self.cell_size) * 0.8)
                    font = f'Helvetica {font_size} bold'
                    self.canvas.create_text(x_center, y_center, text=text, fill=text_color, font=font)

                zero_x = self.raster.extent * self.cell_size[0] + Grid.MARGIN_SIZE + self.cell_size[0] / 2
                zero_y = self.raster.extent * self.cell_size[1] + Grid.MARGIN_SIZE + self.cell_size[1] / 2
                self.canvas.create_line(zero_x, Grid.MARGIN_SIZE, zero_x, self.window_size[1] - Grid.MARGIN_SIZE, fill='#222222', width=3)
                self.canvas.create_line(Grid.MARGIN_SIZE, zero_y, self.window_size[0] - Grid.MARGIN_SIZE, zero_y, fill='#222222', width=3)


    def _on_run_click(self, action, entries):
        selected_cells = self.raster.get_selected_cells()
        rendered_cells = self.raster.get_rendered_cells()
        parameters = {entry[0]: entry[1].get() for entry in entries}
        action(selected_cells, rendered_cells, parameters)
        self._clear_selected_cells()

    def _clear_all(self):
        self.raster.clear_all()
        self._redraw()

    def _clear_selected_cells(self):
        self.raster.clear_selected_cells()
        self._redraw()
        
    def _clear_rendered_cells(self):
        self.raster.clear_rendered_cells()
        self._redraw()
        
    def _clear_fill_cells(self):
        self.raster.clear_fill_cells()
        self._redraw()
        
    def _open_params_window(self, name, parameters, entries, algorithm):
        self.params_window = Toplevel(self.root)
        self.params_window.title(f'Parâmetros para {name}')
        width = 300  # Largura inicial
        height = 50 + len(parameters) * 30  # Altura inicial
        self.params_window.geometry(f'{width}x{height}')

        params_frame = Frame(self.params_window)
        params_frame.pack(padx=10, pady=10)

        for variable in parameters:
            var_label = Label(params_frame, text=variable)
            var_label.pack(side='left')

            var_entry = Entry(params_frame, width=5)
            var_entry.pack(side='left')

            # Adicione a entrada à lista 'entries'
            entries.append((variable, var_entry))

        confirm_frame = Frame(self.params_window)
        confirm_frame.pack(pady=10)

        confirm_button = ttk.Button(confirm_frame, text='Confirmar', command=lambda: self._on_run_click(algorithm, self._get_params(entries)))
        confirm_button.pack()

        self.params_window.return_values = lambda entries: self._get_params(entries)


    def _get_params(self, entries):
        params = {variable: entry.get() for variable, entry in entries}
        print(params)
        self.params_window.destroy()
        # Chame _on_run_click passando a lista 'params' como argumento
        self._on_run_click(algorithm, params)