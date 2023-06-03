def geraProjecao(vertices):
    # Extrair as coordenadas x e y dos vértices
    x_coords = [vertex[0] for vertex in vertices]
    y_coords = [vertex[1] for vertex in vertices]

    # Criar as projeções ortogonais nos três planos
    projection_xy = [(x, y) for x, y in zip(x_coords, y_coords)]
    projection_xz = [(x, 0) for x in x_coords]
    projection_yz = [(0, y) for y in y_coords]

    return projection_xy, projection_xz, projection_yz