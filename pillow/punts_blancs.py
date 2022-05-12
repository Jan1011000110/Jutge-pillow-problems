from PIL import Image, ImageDraw

n = int(input())

img = Image.new('RGB', (n*175-25, n*175-25), 'Grey')
dib = ImageDraw.Draw(img)

for i in range(n):
    for j in range(n):
        dib.polygon([(i*175, j*175), (i*175+149, j*175), (i*175+149, j*175+149), (i*175, j*175+149)], 'Black')

for i in range(n-1):
    for j in range(n-1):
        dib.ellipse([i*175+150, j*175+150, 25+i*175+150-1, 25+j*175+150-1], 'White')



img.save('output.png')