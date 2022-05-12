from PIL import Image, ImageDraw
from easyinput import read

r = read(int)
g = read(int)
b = read(int)

img = Image.new('RGB', (900,300))
dib = ImageDraw.Draw(img)
z = 5

for i in range(7):
    dib.polygon([(i*150, 0),
    (i*150+150, 0), 
    (i*150+150, 300),
    (i*150, 300)], 
    fill=(int(z*r/5), int(z*g/5), int(z*b/5)))
    z-=1

img.save('output.png')