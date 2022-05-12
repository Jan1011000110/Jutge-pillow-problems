from PIL import Image, ImageDraw
from easyinput import read

n = read(int)
x = read(int)
y = read(int)
vp = read(float)
vg = read(float)

img = Image.new("RGB", (10*n, 10*n), "LawnGreen")
dib = ImageDraw.Draw(img)

#r = 

dib.polygon([(0,0),(5*n - 1, 0),(5*n - 1, 10*n-1),(0, 10*n-1)], "Aqua")
dib.line([(0, 0), (5*n, '''r''' )], "Black")

img.save("output.png")