from rembg import remove
from PIL import Image, ImageEnhance

imagemEntrada = 'linus-torvalds-entrada.jpg'

input = Image.open(imagemEntrada)

#Melhorar o resultado da remoção
# Ajustar o brilho
enhancer = ImageEnhance.Brightness(input)
input = enhancer.enhance(1.2)  # Ajuste o valor conforme necessário

# Ajustar o contraste
enhancer = ImageEnhance.Contrast(input)
input = enhancer.enhance(1.3)  # Ajuste o valor conforme necessário

output = remove(input)

# Convertendo a imagem de RGBA para RGB
output = output.convert("RGB")

output.save("linus-torvalds-saida.jpg")