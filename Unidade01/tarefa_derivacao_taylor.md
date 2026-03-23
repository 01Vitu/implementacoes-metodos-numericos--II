# Derivada Segunda com Erro de Ordem 4 e Filosofia Central

<h3>Dados:</h3>

- Ordem p = 2
- Erro n = 4 
- Total de pontos = (p + n - 1) = 5

<h3>Expansão dos Termos:</h3>

1. $$f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \frac{h^4}{24}f^{(4)}(x) + \frac{h^5}{120}f^{(5)}(x) + \frac{h^6}{720}f^{(6)}(x)$$

2. $$f(x-h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f'''(x) + \frac{h^4}{24}f^{(4)}(x) - \frac{h^5}{120}f^{(5)}(x) + \frac{h^6}{720}f^{(6)}(x)$$

3. $$f(x+2h) = f(x) + 2hf'(x) + \frac{(2h)^2}{2}f''(x) + \frac{(2h)^3}{6}f'''(x) + \frac{(2h)^4}{24}f^{(4)}(x) + \frac{(2h)^5}{120}f^{(5)}(x) + \frac{(2h)^6}{720}f^{(6)}(x)$$

4. $$f(x-2h) = f(x) - 2hf'(x) + \frac{(-2h)^2}{2}f''(x) + \frac{(-2h)^3}{6}f'''(x) + \frac{(-2h)^4}{24}f^{(4)}(x) + \frac{(-2h)^5}{120}f^{(5)}(x) + \frac{(-2h)^6}{720}f^{(6)}(x)$$

5. $$f(x) = f(x)$$

<h3>Combinação Linear:</h3>

$$ CL = A f(x-2h) + B f(x-h) + C f(x) + D f(x+h) + E f(x+2h)  $$

$$ CL = h^2 f''(x)$$

$$f''(x) \approx \frac{ A f(x-2h) + B f(x-h) + C f(x) + D f(x+h) + E f(x+2h) }{h^2}$$

onde os coeficientes $A, B, C, D, E$ são desconhecidos.

<h3>Multiplicando as expansões de Taylor por coeficientes:</h3>

1. $$A f(x-2h) = A f(x) - 2Ahf'(x) + \frac{4A h^2}{2}f''(x) - \frac{8A h^3}{6}f'''(x) + \frac{16A h^4}{24}f^{(4)}(x) - \frac{32A h^5}{120}f^{(5)}(x) + \frac{64A h^6}{720}f^{(6)}(x)$$

2. $$B f(x-h) = B f(x) - Bhf'(x) + \frac{B h^2}{2}f''(x) - \frac{B h^3}{6}f'''(x) + \frac{B h^4}{24}f^{(4)}(x) - \frac{B h^5}{120}f^{(5)}(x) + \frac{B h^6}{720}f^{(6)}(x)$$

3. $$C f(x) = C f(x)$$

4. $$D f(x+h) = D f(x) + Dhf'(x) + \frac{D h^2}{2}f''(x) + \frac{D h^3}{6}f'''(x) + \frac{D h^4}{24}f^{(4)}(x) + \frac{D h^5}{120}f^{(5)}(x) + \frac{D h^6}{720}f^{(6)}(x)$$

5. $$E f(x+2h) = E f(x) + 2Ehf'(x) + \frac{4E h^2}{2}f''(x) + \frac{8E h^3}{6}f'''(x) + \frac{16E h^4}{24}f^{(4)}(x) + \frac{32E h^5}{120}f^{(5)}(x) + \frac{64E h^6}{720}f^{(6)}(x)$$

<h3>Somando as expansões de Taylor:</h3>

$$ f(x)[A + B + C + D + E] $$
$$ + hf'(x)[-2A - B + D + 2E] $$
$$ + \frac{h^2}{2}f''(x)[4A + B + D + 4E] $$
$$ + \frac{h^3}{6}f'''(x)[-8A - B + D + 8E] $$
$$ + \frac{h^4}{24}f^{(4)}(x)[16A + B + D + 16E] $$
$$ + \frac{h^5}{120}f^{(5)}(x)[-32A - B + D + 32E] $$
$$ + \frac{h^6}{720}f^{(6)}(x)[64A + B + D + 64E] $$

<h3>Sistema de Equações:</h3>

1. $$ f(x) = A + B + C + D + E = 0 $$

2. $$ f'(x) = -2A - B + D + 2E = 0 $$

3. $$ f''(x) = 4A + B + D + 4E = 2 $$

4. $$ f'''(x) = -8A - B + D + 8E = 0 $$

5. $$ f^{(4)}(x) = 16A + B + D + 16E = 0 $$

6. $$ f^{(5)}(x) = -32A - B + D + 32E = 0 $$

7. $$ f^{(6)}(x) = 64A + B + D + 64E = 0 $$

<h3>Resolvendo o Sistema de Equações:</h3>

<p> Os pontos de uma derivada de ordem par usando a filosofia central são sempre simétricos em relação ao ponto central, assim como seus coeficientes: </p>

$$ A = E $$
$$ B = D $$

<h4> Substituindo nas Equações: </h4>

2. $$ -2A - B + B + 2A = 0 $$
$$ 0 = 0 $$

<br>

4. $$ -8A - B + B + 8A = 0 $$
$$ 0 = 0 $$

<br>

5. $$ 16A + B + B + 16A = 0 $$
$$ 32A + 2B = 0 $$
$$ B = -16A $$

<br>

3. $$ 4A + B + D + 4E = 2 $$
$$ 8A + 2B = 2 $$
$$ 4A + B = 1 $$
$$ 4A - 16A = 1 $$
$$ -12A = 1 $$
$$ A = -1/12 $$

<br>

$$ B = -16A = -16(-1/12) = 16/12 = 4/3 $$

<br>

1. $$ C = -A - B - D - E $$
$$ C = -A - B - B - A $$
$$ C = -2A - 2B $$
$$ C = -2(-1/12) - 2(4/3) $$
$$ C = 1/6 - 8/3 $$
$$ C = 1/6 - 16/6 $$
$$ C = -15/6 $$
$$ C = -5/2 $$

6. $$ f^{(5)}(x) = -32A - B + D + 32E = 0 $$
$$ -32A - B + B + 32A = 0 $$
$$ 0 = 0 $$

7. $$ f^{(6)}(x) = 64A + B + D + 64E = 0 $$
$$ 64A + B + B + 64A = 0 $$
$$ 128A + 2B = 0 $$

<h3> Erro de Ordem 4: </h3>

$$ f^{(6)}(x) = 64A + B + D + 64E $$
$$ f^{(6)}(x) = 64A + B + B + 64A $$
$$ f^{(6)}(x) = 128A + 2B $$

$$ f^{(6)}(x) = 128(-1/12) + 2(4/3) $$
$$ f^{(6)}(x) = -128/12 + 8/3 $$
$$ f^{(6)}(x) = -32/3 + 8/3 $$
$$ f^{(6)}(x) = -24/3 $$
$$ f^{(6)}(x) = -8 $$

<br>

$$ h^6 \frac{f^{(6)}(x)}{720} = h^6 \frac{-8}{720} = -h^6 / 90 $$

<br>

## Derivada segunda central de ordem 4

$$CL = -1/12 f(x-2h) + 4/3 f(x-h) - 5/2 f(x) + 4/3 f(x+h) - 1/12 f(x+2h)$$

$$CL = h^2 f''(x) + \frac{h^6}{720}f^{(6)}(x)[-8]$$

$$CL = h^2 f''(x) - \frac{h^6}{90}f^{(6)}(x)$$

$$h^2 f''(x) = CL + \frac{h^6}{90}f^{(6)}(x)$$

$$f''(x) = \frac{ -1/12 f(x-2h) + 4/3 f(x-h) - 5/2 f(x) + 4/3 f(x+h) - 1/12 f(x+2h) }{h^2} + \frac{h^4}{90}f^{(6)}(x)$$

$$f''(x) = \frac{-f(x-2h) + 16f(x-h) - 30f(x) + 16f(x+h) - f(x+2h)}{12h^2} + \frac{h^4}{90}f^{(6)}(x)$$