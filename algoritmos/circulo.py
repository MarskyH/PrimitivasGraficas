def desenha8(ponto, centro):
  x, y = ponto
  xc, yc = centro
  pontos = []
  pontos.append((x+xc,y+yc))
  pontos.append((y+xc,x+yc))  
  pontos.append((y+xc,-x+yc))
  pontos.append((x+xc,-y+yc))
  pontos.append((-x+xc,-y+yc))
  pontos.append((-y+xc,-x+yc))
  pontos.append((-y+xc,x+yc))
  pontos.append((-x+xc,y+yc))
  return pontos

def circ(centro, raio):
    x = 0
    y = raio
    e = -raio
    pontos = []
    
    pontos.append(desenha8((x,y), centro))
    while x <= y:
        e += (2*x) + 1
        x += 1
        if (e >= 0):
            e += 2 - (2*y)
            y -= 1
        pontos.append(desenha8((x, y), centro))

    resultado = []
    for p in pontos:
        resultado += p

    return resultado