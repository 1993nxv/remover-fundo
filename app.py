from rembg import remove
from PIL import Image, ImageEnhance

imagemEntrada = 'linus-torvalds-entrada.jpg'

input = Image.open(imagemEntrada)

brilho = ImageEnhance.Brightness(input)
input = brilho.enhance(1.2)

contraste = ImageEnhance.Contrast(input)
input = contraste.enhance(1.3)

output = remove(input)

output.save("linus-torvalds-saida.png", format='PNG')

print("Imagem processada e salva com sucesso.")