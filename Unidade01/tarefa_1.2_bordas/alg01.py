import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Função auxiliar para aplicar a convolução de uma matriz (imagem) com um filtro (kernel)
def convolve2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    
    # Adiciona um preenchimento (padding) nas bordas para não diminuir o tamanho da imagem
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    
    output = np.zeros_like(image, dtype=np.float64)
    
    # Desliza o filtro por cada pixel da imagem
    for y in range(image_height):
        for x in range(image_width):
            # Recorta a região correspondente ao tamanho do filtro
            region = padded_image[y:y+kernel_height, x:x+kernel_width]
            # Multiplica os elementos correspondentes e soma tudo
            output[y, x] = np.sum(region * kernel)
            
    return output

def detect_edges(image_path, threshold):
    # --- Passo 0: Carregar a imagem e converter para tons de cinza (matriz 2D) ---
    img = Image.open(image_path).convert('L')
    # Converte para float para evitar cortes nos cálculos matemáticos
    img_array = np.array(img, dtype=np.float64) 

    # --- Passo 1: Suavizar a imagem aplicando um filtro Gaussiano ---
    # Kernel Gaussiano 3x3 simples
    gaussian_kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16.0
    
    smoothed_image = convolve2d(img_array, gaussian_kernel)

    # --- Passo 2: Filtro convolucional de Gradiente (Sobel) ---
    # 2.1) Sobel na direção X
    sobel_x = np.array([
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ])
    A = convolve2d(smoothed_image, sobel_x)
    
    # 2.2) Sobel na direção Y
    sobel_y = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])
    B = convolve2d(smoothed_image, sobel_y)

    # 2.3) Elevar ao quadrado os valores dos elementos de A e B
    A_sq = A ** 2
    B_sq = B ** 2

    # 2.4) Somar e tirar a raiz quadrada para obter a matriz C (Magnitude do Gradiente)
    C = np.sqrt(A_sq + B_sq)
    
    # Opcional: Normalizar a matriz C para que os valores fiquem entre 0 e 255
    # Isso facilita a escolha de um threshold previsível (ex: entre 0 e 255)
    C_normalized = (C / np.max(C)) * 255.0

    # --- Passo 3 e 4: Threshold e geração da matriz Final D ---
    D = np.zeros_like(C_normalized)
    
    # Se C < threshold -> Não é borda -> Fundo Branco (255)
    # Se C >= threshold -> É borda -> Pixel Preto (0)
    for y in range(D.shape[0]):
        for x in range(D.shape[1]):
            if C_normalized[y, x] < threshold:
                D[y, x] = 255 # Fundo (Branco)
            else:
                D[y, x] = 0   # Borda (Preto)

    return img_array, D

# ==========================================
# Execução:
# ==========================================
# Substitua pelo caminho da sua imagem
image_file = 'carro.webp' 
threshold_value = 25.0  # Escolha o valor float para o threshold (ajuste conforme a imagem)

try:
    original, edges = detect_edges(image_file, threshold_value)

    # Exibindo os resultados usando matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title('Imagem Original')
    axes[0].axis('off')
    
    axes[1].imshow(edges, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title(f'Bordas (Threshold = {threshold_value})')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Por favor, certifique-se de que o arquivo 'sua_imagem.jpg' existe no mesmo diretório ou passe o caminho correto.")