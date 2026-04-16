import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def convolve2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    
    output = np.zeros_like(image, dtype=np.float64)
    
    for y in range(image_height):
        for x in range(image_width):
            region = padded_image[y:y+kernel_height, x:x+kernel_width]
            output[y, x] = np.sum(region * kernel)
            
    return output

def laplacian_edges(image_path, tolerance=0.0001):
    # --- Passo 0: Carregar a imagem ---
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float64) 

    # --- Passo 1: Suavizar a imagem (Filtro Gaussiano) ---
    gaussian_kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16.0
    
    smoothed_image = convolve2d(img_array, gaussian_kernel)

    # --- Passo 2: Filtro convolucional de Laplace ---
    # Kernel de Laplace Padrão (3x3)
    laplacian_kernel = np.array([
        [ 0,  1,  0],
        [ 1, -4,  1],
        [ 0,  1,  0]
    ])
    
    # Gera a matriz A
    A = convolve2d(smoothed_image, laplacian_kernel)

    # --- Passo 3: Gerar matriz B com base na tolerância ---
    B = np.zeros_like(A) # Cria matriz cheia de zeros
    
    # Cria uma máscara onde a condição |A| <= tolerancia é verdadeira
    mask_is_zero = np.abs(A) <= tolerance
    
    # Aplica as regras solicitadas:
    # Áreas lisas (dentro da tolerância) -> Fundo -> Branco (255)
    B[mask_is_zero] = 255
    
    # Áreas com variação (fora da tolerância) -> Borda -> Preto (0)
    B[~mask_is_zero] = 0 

    return img_array, B

# ==========================================
# Execução:
# ==========================================
image_file = 'carro02.webp' 
tol = 0.0001 # Ajuste a tolerância. 0.0001 pode ser muito restrito dependendo da imagem.

try:
    original, edges_laplace = laplacian_edges(image_file, tolerance=tol)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title('Imagem Original')
    axes[0].axis('off')
    
    axes[1].imshow(edges_laplace, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title(f'Laplace (Tolerância = {tol})')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Por favor, certifique-se de que o arquivo existe.")
