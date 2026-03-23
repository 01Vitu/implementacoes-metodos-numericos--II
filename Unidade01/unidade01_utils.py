import math

def criar_funcao(expr):
    def f(x):
        return eval(expr, {"__builtins__": {}}, {"x": x, "math": math})
    return f
