from utils import gerar_malha

def calcular(f, t0, y0, tf, h):
    t = gerar_malha(t0, tf, h)
    y = [y0]
    
    for i in range(len(t) - 1):
        ti, yi = t[i], y[i]
        k1 = f(ti, yi)
        k2 = f(ti + h/2.0, yi + (h/2.0)*k1)
        k3 = f(ti + h/2.0, yi + (h/2.0)*k2)
        k4 = f(ti + h, yi + h*k3)
        
        y_next = yi + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
        y.append(y_next)
        
    return t, y