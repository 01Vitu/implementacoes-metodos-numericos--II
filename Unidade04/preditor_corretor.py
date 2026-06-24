from utils import gerar_malha
import rk4

def calcular(f, t0, y0, tf, h):
    t = gerar_malha(t0, tf, h)
    n_pontos = len(t)
    

    if n_pontos < 4:
        return rk4.calcular(f, t0, y0, tf, h)
    _, y_rk = rk4.calcular(f, t0, y0, t[3], h)
    y = list(y_rk[:4])

    fn = [f(t[i], y[i]) for i in range(4)]

    for i in range(3, n_pontos - 1):

        y_pred = y[i] + (h / 24.0) * (55*fn[3] - 59*fn[2] + 37*fn[1] - 9*fn[0])
        

        f_pred = f(t[i+1], y_pred)
        y_corr = y[i] + (h / 24.0) * (9*f_pred + 19*fn[3] - 5*fn[2] + fn[1])

        y.append(y_corr)
        fn.pop(0)
        fn.append(f(t[i+1], y_corr))

    return t, y