import math

def bezier (pontosControle, linha, grauCurva):
    resultado = []
    for t in range(0,101):
        t /= 100
        x = 0
        y = 0
        t_pot = 1
        
        for i in range(grauCurva + 1):
            coefBinomial = math.comb(grauCurva, i )
            blend = coefBinomial * pow(1-t, grauCurva - i) * pow(t, i)
            
            x += pontosControle[i][0] * blend
            y += pontosControle[i][1] * blend
            t_pot *= t
            
        linha.append((int(x), int(y)))
        
    return linha