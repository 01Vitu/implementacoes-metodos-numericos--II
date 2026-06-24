from utils import gerar_malha

def calcular(f, t0, y0, tf, h):
    t = gerar_malha(t0, tf, h)
    y = [y0]
    
    for i in range(len(t) - 1):
        y_next = y[i] + h * f(t[i], y[i])
        y.append(y_next)
        
    return t, y