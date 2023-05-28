def reflexao(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
        
    condicoes = {
        'xy': False,
        'x': False,
        'y': False,
    }
        
    if (dx >= dy and dx >= 0 and dy >= 0):
        return (ponto1, ponto2, False)
    
    else:
        if (m > 1 or m < -1):
          x1, y1 = y1, x1
          x2, y2 = y2, x2
          condicoes['xy'] = True
          
        if (x1 > x2):
            x1 *= -1
            x2 *= -1
            condicoes['x'] = True


        if (y1 > y2):
            y1 *= -1
            y2 *= -1
            condicoes['y'] = True
            
    return ((x1, y1), (x2, y2), condicoes)

def inverteReflexao(pontos: list, refletidos: dict) -> list:
      novosPontos = []

      for ponto in pontos:
        x, y = ponto
        if refletidos['y']:
            y *= -1

        if refletidos['x']:
            x *= -1

        if refletidos['xy']:
            x, y = y, x

        novosPontos.append((x, y))

      return novosPontos

def bres(p1 , p2):
  if (p2[0] - p1[0] == 0 and p2[1] - p1[1] == 0):
    return [p1]

  p1, p2, refletir = reflexao(p1, p2)

  x1, y1 = p1
  x2, y2 = p2

  dX = x2 - x1
  dY = y2 - y1
  m = dY / dX
  e = m - (1/2)
  pontos = [(x1, y1)]

  while (x1 < x2):
    if (e > 0):
      y1 += 1
      e -= 1

    x1 += 1
    e += m
    pontos.append((x1, y1))

  if refletir:
    pontos = inverteReflexao(pontos, refletir)
  
  return pontos


        
   