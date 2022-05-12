from PIL import Image, ImageDraw
from easyinput import read

col = read(str)

n = read(int)
a = read(int)

r1 = read(int)
g1 = read(int)
b1 = read(int)

r2 = read(int)
g2 = read(int)
b2 = read(int)

width = a * n
height = a * n

img = Image.new("RGB", (width, height), col)
dib = ImageDraw.Draw(img)
ñ = 0

x1 = 0
x2 = a-1
y1 = 0
y2 = a-1

while ñ <= n:
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], (r1,g1,b1))
    x1 += a
    x2 += a
    y1 += a
    y2 += a
    ñ += 1

ñ = 0

x1 = 0
x2 = a-1
y1 = height - 1 
y2 = height - a


while ñ <= n:
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], (r2,g2,b2))
    x1 += a
    x2 += a
    y1 -= a
    y2 -= a
    
    ñ += 1

x = int(n/2)
x1 = x * a
x2 = (x+1) * (a)-1
y1 = x * a
y2 = (x+1) * (a)-1

if n % 2 == 1:
    r3 = int((r1 + r2)/2)
    g3 = int((g1 + g2)/2)
    b3 = int((b1 + b2)/2)

    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], (r3,g3,b3))

else:
    pass

img.save("output.png")
