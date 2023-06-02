# Função para realizar o recorte de uma linha usando o algoritmo de Sutherland-Hodgman
def sutherland_hodgman(selected_cell, vertices):

    x_min = min(selected_cell, key=lambda v: v[0])[0]
    y_min = min(selected_cell, key=lambda v: v[1])[1]
    x_max = max(selected_cell, key=lambda v: v[0])[0]
    y_max = max(selected_cell, key=lambda v: v[1])[1]

    recortados = []
    n = len(vertices)

    # Verificar cada aresta da janela de visualização
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        # Verificar se o vértice está dentro da janela de visualização
        if x1 >= x_min and x1 <= x_max and y1 >= y_min and y1 <= y_max:
            recortados.append((x1, y1))

        # Verificar se a aresta cruza a janela de visualização
        if (x2 - x1) != 0:
            m = (y2 - y1) / (x2 - x1)

            # Verificar interseção com o lado esquerdo da janela
            if x1 < x_min:
                y = y1 + (x_min - x1) * m
                recortados.append((x_min, y))

            # Verificar interseção com o lado direito da janela
            if x2 > x_max:
                y = y1 + (x_max - x1) * m
                recortados.append((x_max, y))

        # Verificar interseção com o lado superior da janela
        if (y2 - y1) != 0:
            m_inv = (x2 - x1) / (y2 - y1)
            if y1 < y_min:
                x = x1 + (y_min - y1) * m_inv
                recortados.append((x, y_min))

        # Verificar interseção com o lado inferior da janela
        if y2 > y_max:
            if (y2 - y1) != 0:
                m_inv = (x2 - x1) / (y2 - y1)
                x = x1 + (y_max - y1) * m_inv
                recortados.append((x, y_max))

    recortados = [(round(x), round(y)) for x, y in recortados]

    return recortados
