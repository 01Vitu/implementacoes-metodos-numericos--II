from utils import gerar_malha

def calcular(f, t0, y0, tf, h):
    t = gerar_malha(t0, tf, h)
    y = [y0]
    
    for i in range(len(t) - 1):
        t_next = t[i+1]
        y_atual = y[i]
        
        def g(Y):
            return Y - y_atual - h * f(t_next, Y)

        Y0 = y_atual
        Y1 = y_atual + h * f(t[i], y_atual) # Chute inicial via Euler Explícito

        for _ in range(100):
            g0, g1 = g(Y0), g(Y1)
            if abs(g1 - g0) < 1e-15:
                break
            
            Y_next = Y1 - g1 * ((Y1 - Y0) / (g1 - g0))
            if abs(Y_next - Y1) < 1e-9:
                Y1 = Y_next
                break
            Y0, Y1 = Y1, Y_next

        y.append(Y1)
        
    return t, y