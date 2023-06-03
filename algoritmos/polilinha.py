from algoritmos.bresenham import bres

def poli(pontos):
    pontos.append(pontos[0])
    if(len(pontos) > 3):   
        resultados = []
    for i in range(len(pontos) - 1):
        par_atual = pontos[i]
        par_seguinte = pontos[i + 1]
        print(par_atual,par_seguinte)
        resultados += bres(par_atual, par_seguinte)
    return resultados
        

       