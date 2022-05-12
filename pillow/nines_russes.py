from PIL import Image, ImageDraw
from easyinput import read

n = read(int)
k = read(int)
c = []
if n % 2 == 0:
    r = int(n/2)
else:
    r = int(n/2) + 1
print(r)

for i in range(k):
    col = read(str)
    c.append(col)

img = Image.new("RGB", (50*n, 50*n), c[0])
dib = ImageDraw.Draw(img) 


img.save("output.png")

