from cmath import sin
from PIL import Image, ImageDraw
from easyinput import read
from math import sin

m = read(int)
n = read(int)
d = read(int)
rx = read(int)
ry = read(int)
gx = read(int)
gy = read(int)
bx = read(int)
by = read(int)


img = Image.new("RGB", (m, n))
dib = ImageDraw.Draw(img)


for x in range(m):
    for y in range(n):
        r = int(rx * sin(x/d) + ry * sin(y/d)) % 256
        g = int(gx * sin(x/d) + gy * sin(y/d)) % 256
        b = int(bx * sin(x/d) + by * sin(y/d)) % 256
        dib.point((x,y), (r,g,b))
    
img.save("output.png")