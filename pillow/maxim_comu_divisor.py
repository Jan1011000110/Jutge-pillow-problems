from PIL import Image, ImageDraw
from math import gcd

c1 = str(input())
c2 = str(input())
n = int(input())
m = int(input())

img = Image.new('RGB', (n,m))
dib = ImageDraw.Draw(img)

mcd = gcd(m,n)
nx = int(n/mcd)
ny = int(m/mcd)

for y in range(ny):
    for x in range(nx):
        if y%2 == 0:
            if x%2 == 0:
                col = c1
            else:
                col = c2
        elif y%2 == 1:
            if x%2 == 0:
                col = c2
            else:
                col = c1
                
        dib.polygon([(mcd * x, mcd * y), (mcd * x + mcd - 1, mcd * y), (mcd * x + mcd - 1, mcd * y + mcd - 1), (mcd * x, mcd * y + mcd - 1)], col)

img.save("output.png")
