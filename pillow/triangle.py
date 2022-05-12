from PIL import Image, ImageDraw
from easyinput import read

col_f = read(str)
col_p = read(str)

width = read(int)
height = read(int)

x = read(int)

img = Image.new("RGB", (width,height), col_f)

dib = ImageDraw.Draw(img)
dib.polygon([(width-1, height-1), (0, height-1), (x, 0)], col_p) #DIBUIXEM ELS TRES PUNTS DEL TRIANGLE RESTANT 1 A LES COMPLETES

img.save('output.png')