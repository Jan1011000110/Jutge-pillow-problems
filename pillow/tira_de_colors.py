from easyinput import read
from PIL import Image, ImageDraw

n = read(int)

img = Image.new('RGB', (50*n, 50))
dib = ImageDraw.Draw(img)

x1 = 0
x2 = 50
y1 = 0
y2 = 50

for i in range(n):
    c = read(str)
    dib.polygon([
        (x1,y1),
        (x2, y1),
        (x2,y2),
        (x1,y2)
    ], c)

    x1 += 50
    x2 += 50

img.save('output.png')