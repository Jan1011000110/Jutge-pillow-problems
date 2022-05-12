from PIL import Image, ImageDraw
from easyinput import read

n = read(int)

img = Image.new('RGB', (8*n, 8*n), 'White')
dib = ImageDraw.Draw(img)
s = 8
for i in range(4):
    if i == 0:
        col = 'Blue'
    elif i == 1:
        col = 'Yellow'
    elif i == 2:
        col = 'Red'
    else:
        col = 'Green'
    dib.ellipse([i*n, i*n, s*n+ i*n-1, s*n+ i*n-1], col)
    s-=2
img.save('output.png')