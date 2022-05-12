from re import A
from PIL import Image, ImageDraw
from easyinput import read

f = read(str)
c = read(str)
n = read(int)
a = 0
b = 0

for i in range(2,n+1):
    if n % i == 0:
        a = i
        b = int(n/i)
        break


img = Image.new('RGB', (a*50,b*50), f)
dib = ImageDraw.Draw(img)


for i in range(a):
    for j in range(b):
        dib.ellipse([50*i, 50*j, 49+(50*i), 49+(50*j)], c)
        

img.save("output.png")