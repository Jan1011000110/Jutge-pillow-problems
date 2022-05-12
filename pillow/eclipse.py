from gzip import READ
from PIL import Image,ImageDraw
from easyinput import read

x1 = read(int)
y1 = read(int)
d1 = read(int)
x2 = read(int)
y2 = read(int)
d2 = read(int)

img = Image.new('RGB', (500,500), 'Black')
dib = ImageDraw.Draw(img)

dib.ellipse([x1, y1, d1+x1-1, d1+y1-1], 'White')
dib.ellipse([x2, y2, d2+x2-1, d2+y2-1], 'Black')


img.save('output.png')