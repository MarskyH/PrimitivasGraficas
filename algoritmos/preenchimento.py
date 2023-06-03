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
