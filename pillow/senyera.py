from PIL import Image, ImageDraw
from easyinput import read

n = read(int)
m = read(int)

img = Image.new('RGB', (n, 9*m))
dib = ImageDraw.Draw(img)

def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)

x1 = 0
y1 = 0
x2 = n-1
y2 = m-1

Y = True
for i in range(9):
    if Y is True:
        rect(x1, y1, x2, y2, 'Yellow')
        Y = False
    
    elif Y is not True:
        rect(x1, y1, x2, y2, 'Red')
        Y = True
    
    y1 += m
    y2 += m


img.save('output.png')