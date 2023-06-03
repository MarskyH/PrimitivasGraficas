from tkinter import Tk, ttk, Canvas, Label, Frame, Button, Entry, Toplevel, StringVar, OptionMenu, colorchooser
from .grid_data_structure import GridDataStructure
from algoritmos.projecoes import Projection

class Grid:
    
    # constantes
    SELECT_COLOR = '#0CEBB2'
    DEFAULT_COLOR = '#FFFFFF'
    PRINT_COLOR = '#4F4F4F'
    FILL_COLOR = '#EBBE3B'
    MARGIN_SIZE = 10

    def __init__(self, extent, size, grid_columns=2):
        # Criando estrutura da grade
        self.raster = GridDataStructure(extent)
        self.window_size = size, size
        self.grid_size = size - 2 * Grid.MARGIN_SIZE, size - 2 * Grid.MARGIN_SIZE
        dimension = 2 * extent + 1
        self.cell_size = self.grid_size[0] / dimension, self.grid_size[1] / dimension
        self.root = Tk()
        self.clip_window = None
        
        style = ttk.Style()
        style.configure('Custom.TButton', foreground='#FCAB05', borderwidth=1, borderradius=10, width=20, height=10)


        # frame principal
        self.main_frame = Frame(self.root)
        self.main_frame.pack(anchor='center', expand=True)

        # frame de limpar células
        self.grid_frame = Frame(self.main_frame)
        self.grid_frame.pack(side='left', padx=10, pady=10)
        
        clear_frame = Frame(self.grid_frame)
        clear_frame.pack(padx=5, pady=10)
        ttk.Button(clear_frame, text='Limpar tudo', command=self._clear_all, width=30, style='Custom.TButton').grid(row=0, column=0) 
        ttk.Button(clear_frame, text='Limpar células Selecionadas', width=30, command=self._clear_selected_cells, style='Custom.TButton').grid(row=0, column=1) 
        ttk.Button(clear_frame, text='Limpar células rasterizadas', width=30, command=self._clear_rendered_cells, style='Custom.TButton').grid(row=1, column=0) 
        ttk.Button(clear_frame, text='Limpar células preenchidas',  width=30, command=self._clear_fill_cells, style='Custom.TButton').grid(row=1, column=1) 
        ttk.Button(clear_frame, text='Alterar cor',  width=30, command=self.choose_color, style='Custom.TButton').grid(row=0, column=2) 

        # frame dos algoritmos
        self.controls_frame = Frame(self.main_frame)
        self.controls_frame.pack(side='right', padx=10, pady=10)

        self.grid_columns = grid_columns
        self.next_row = 0
        self.next_column = 0

        self.canvas = Canvas(self.grid_frame, width=size, height=size)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self._on_canvas_click)
        
        self.colorFill = self.FILL_COLOR

    def add_algorithm(self, name, parameters=None, algorithm=None):
        frame = Frame(self.controls_frame)
        frame.pack(side='top', pady=5)
        entries = []
        if name == "Projeções":
            run_button = ttk.Button(frame, text=name, style='Custom.TButton', width=25, command=lambda: self.projection())
            run_button.pack(side='left')
        if parameters:
            params = parameters  # Armazena os parâmetros em uma variável local
            open_params_button = ttk.Button(frame, text=name, style='Custom.TButton', width=25, command=lambda: self._open_params_window(name, params, entries[:], algorithm))
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
        if self.clip_window == None:
            self.raster.fill_cell(cell)
        else:
            if self._is_inside_clip_window(cell):
                self.raster.fill_cell(cell)

    def render_cell(self, cell):
        if self.clip_window == None:
                self.raster.render_cell(cell)
        else:
            if self._is_inside_clip_window(cell):
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
        
    def choose_color(self):
        color = colorchooser.askcolor(title="Selecione uma cor")
        if color[1]:
            self.colorFill = color[1]
        color = []    
        
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
                    color = self.colorFill
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
        
        if self.clip_window:
            xmin, ymin = self.clip_window[0]
            xmax, ymax = self.clip_window[2]
            x1 = zero_x + (xmin - 0.5) * self.cell_size[0]
            y1 = zero_y - (ymin - 0.5) * self.cell_size[1]
            x2 = zero_x + (xmax + 0.5) * self.cell_size[0]
            y2 = zero_y - (ymax + 0.5) * self.cell_size[1]
            self.canvas.create_rectangle(x1, y1, x2, y2, outline='red', width=2)

      

    def _is_inside_clip_window(self, cell):
        if self.clip_window is None:
            return True

        x, y = cell
        xmin, ymin = self.clip_window[0]
        xmax, ymax = self.clip_window[2]
        return xmin <= x <= xmax and ymin <= y <= ymax


    def _on_run_click(self, action, entries):
        selected_cells = self.raster.get_selected_cells()
        rendered_cells = self.raster.get_rendered_cells()
        parameters = {}
        for entry in entries:
            variable = entry[0]
            value = entry[1].get()
            parameters[variable] = value
        action(selected_cells, rendered_cells, parameters)
        self._clear_selected_cells()


    def _clear_all(self):
        self.raster.clear_all()
        self.clip_window = None
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
        # Obtém as dimensões do monitor
        screen_width = self.params_window.winfo_screenwidth()
        screen_height = self.params_window.winfo_screenheight()

        # Calcula as coordenadas para centralizar a janela
        width = 300
        height = 60 + len(parameters) * 50
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Define a geometria da janela
        self.params_window.geometry(f'{width}x{height}+{x}+{y}')

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

        confirm_button = ttk.Button(confirm_frame, text='Confirmar', command=lambda: self._on_run_click(algorithm, entries[:]))
        confirm_button.pack()

        self.param_values = []  # Armazena os valores das entradas

        def close_params_window():
            self.params_window.destroy()

        close_button = ttk.Button(confirm_frame, text='Fechar', command=close_params_window)
        close_button.pack()

        self.params_window.protocol("WM_DELETE_WINDOW", close_params_window)

        self.params_window.mainloop()

        return self.param_values
    
    def projection(self):
        pointList = []
        projection_type = StringVar(value="Ortogonal")
        popup = Toplevel(self.root, padx=5, pady=5)
        self.params_window = popup
        self.params_window.title(f'Parâmetros para projeções')
        labelCount = Label(popup, text="Pontos inseridos: []")
        labelx = Label(popup, text="Coordenada x do ponto: ")
        labely = Label(popup, text="Coordenada y do ponto: ")
        labelz = Label(popup, text="Coordenada z do ponto: ")
        label_recuo = Label(popup, text="Recuo: ")
        label_dist = Label(popup, text="Distância: ")
        label_ddmenu = Label(popup, text="Tipo de projeção: ")

        entryx = Entry(popup)
        entryy = Entry(popup)
        entryz = Entry(popup)
        entry_recuo = Entry(popup)
        entry_dist = Entry(popup)
        entry_ddmenu = OptionMenu(popup, projection_type, "Ortogonal", "Pespectiva")
      

        labelx.grid(row=1, column=1)
        labely.grid(row=2, column=1)
        labelz.grid(row=3, column=1)
        label_recuo.grid(row=4, column=1)
        label_dist.grid(row=5, column=1)
        label_ddmenu.grid(row=6, column=1)

        entryx.grid(row=1, column=2)
        entryy.grid(row=2, column=2)
        entryz.grid(row=3, column=2)
        entry_recuo.grid(row=4, column=2)
        entry_dist.grid(row=5, column=2)
        entry_ddmenu.grid(row=6, column=2)
        labelCount.grid(row=7, column=1)

        #Executar projeção ortogonal ou perpectiva
        def run():
            self.clear_all()
            nonlocal pointList
            if len(pointList) != 0:
                obj = Projection(pointList, int(entry_recuo.get()))
                if projection_type.get() == "Ortogonal":
                    obj.ortogonal()
                else:
                    obj.perspectiva(int(entry_dist.get()))
                for ponto in obj.resultado:
                    print(ponto)
                    self.render_cell(ponto)
                pointList = []
                labelCount.config(text=f"Pontos inseridos: {pointList}")
                self._redraw()

        #Função de adicionar um elemento na lista de elementos.
        def add():
            nonlocal pointList
            point = [int(entryx.get()), int(entryy.get()), int(entryz.get())]
            pointList.append(point)
            labelCount.config(text=f"Pontos inseridos: {pointList}")

        #Função de remover um elemento da lista de elementos.
        def rem():
            nonlocal pointList
            pointList = pointList[:-1]
            labelCount.config(text=f"Pontos inseridos: {pointList}")
            
            
        #Botões exclusivos da janela de Projeções
        btnAdd = ttk.Button(popup, text="Adicionar", command=add, style='Custom.TButton')
        btnRem = ttk.Button(popup, text="Remover", command=rem, style='Custom.TButton')
        btnDraw = ttk.Button(popup, text="Executar", command=run, style='Custom.TButton')
        
        #Organizando os 3 botões em grid.
        btnAdd.grid(row=8, column=1)
        btnRem.grid(row=8, column=2)
        btnDraw.grid(row=8, column=3)
