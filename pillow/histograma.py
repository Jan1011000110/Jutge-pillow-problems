from PIL import Image, ImageDraw
from easyinput import read

c1 = read(str)
c2 = read(str)
n = read(int)
l = []

for i in range(n):
    x = read(int)
    l.append(x)

w = n*50 + 100
h = max(l)*50 + 100

img = Image.new("RGB", (w, h), c1)
dib = ImageDraw.Draw(img)

for i in range(1,n+1):
    x1 = 50 * i
    x2 = 50 * i + 50 - 1
    y1 = h - 50 - 1
    y2 = h - (50*(l[i-1])) - 50 
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], c2)
    

img.save("output.png")