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



def bresenham(selected_cells, rendered_cells, parameters):
     ponto1 = selected_cells[0]
     ponto2 = selected_cells[1]
  
        
   