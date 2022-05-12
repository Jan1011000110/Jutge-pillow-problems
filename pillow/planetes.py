from ast import Str
from easyinput import read
from PIL import Image, ImageDraw

dia = []
colors = []
width = 0

n = read(int)

for i in range(n):
    x = read(int)
    c = read(str)
    dia.append(x)
    colors.append(c)
    width += x

height = max(dia)
img = Image.new('RGB', (width, height),'Black')
dib = ImageDraw.Draw(img)

def circle(m_lr, m_tb, dh, dv, col):
    dib.ellipse([m_lr, m_tb, dh, dv], col)

m_lr = 0

z = 0
for i in dia:
    m_tb = int(height/2 - i/2)
    dh = i+m_lr
    dv = i+m_tb
    col = colors[z]
    z += 1
    circle(m_lr, m_tb, dh-1, dv-1, col)
    m_lr += i
    
img.save('output.png')