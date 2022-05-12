from PIL import Image, ImageDraw
from easyinput import read

c_down = read(str)
c_up = read(str)

width = read(int)
height = read(int)

img = Image.new('RGB', (width,height), c_down)
dib = ImageDraw.Draw(img)

h = int(width/2)

dib.polygon([
    (0, 0),
    (width-1, 0),
    (h,h)], c_up)

img.save('output.png')

