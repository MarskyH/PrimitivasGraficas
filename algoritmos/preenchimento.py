def flood_fill(x, y, pontosBorda, pontosPreenchidos):
    ponto = (x,y)
    if x > 10 or x < -10 or y > 10 or y <-10:
      return 'Fora do escopo'
      
    if ponto in pontosBorda:
        return 'Ponto faz parte da borda'
      
    if ponto in pontosPreenchidos:
        return 'Ponto já preenchido'
    
    pontosPreenchidos.append(ponto)
    
    flood_fill(x+1, y, pontosBorda, pontosPreenchidos)
    flood_fill(x-1, y, pontosBorda, pontosPreenchidos)
    flood_fill(x, y+1, pontosBorda, pontosPreenchidos)
    flood_fill(x, y-1, pontosBorda, pontosPreenchidos)

    return pontosPreenchidos

def var(pontos):
    resultado = []
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
                resultado.append((x, y))
    return resultado
    
