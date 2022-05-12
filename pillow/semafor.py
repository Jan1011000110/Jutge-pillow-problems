from PIL import Image, ImageDraw
from easyinput import read

img = Image.new('RGB', (600, 900), 'SkyBlue')
dib = ImageDraw.Draw(img)

n = read(str)

def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)

def circle(m_lr, m_tb, dh, dv,col):
    dib.ellipse([m_lr, m_tb, dh, dv], col)

# GENERAL
# semafor (300 , 800) x1 = 50 y1 = 50 x2 = 350 y2= 850
rect(50, 50, 349, 849, 'Orange')

# barra (250, 100) x1 = 350 y1= 400  x2= 599  y2 = 500
rect(350, 400, 599, 499, 'DimGrey')

#VARIANTS

if n == "AC":
    circle(100, 100, 300-1, 300-1, 'Black')
    circle(100, 350, 300-1, 550-1, 'Black') # 100 + 200 = 300 - 1; 350 + 200 = 550 - 1
    circle(100, 600, 300-1, 800-1, 'Green')

elif n == "PE":
    circle(100, 100, 300-1, 300-1, 'Black')
    circle(100, 350, 300-1, 550-1, 'Yellow')
    circle(100, 600, 300-1, 800-1, 'Black')

else:
    circle(100, 100, 300-1, 300-1, 'Red')
    circle(100, 350, 300-1, 550-1, 'Black')
    circle(100, 600, 300-1, 800-1, 'Black')

img.save('output.png')


