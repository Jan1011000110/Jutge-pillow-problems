from PIL import Image, ImageDraw
from easyinput import read

c = read(str)
r = read(int)
g = read(int)
b = read(int)
k = read(int)

f = [0,1]
for i in range(2,k+2):
    x = f[i-1] + f[i-2]
    f.append(x)


lowx = 0
lowy = 0
highx = f[k+1]
highy = f[k]
img = Image.new('RGB', (f[k+1], f[k]),c)
dib = ImageDraw.Draw(img)

f.pop(0)
f.reverse()
f.pop(0)
c = 0
pos = 1


# pos 1 canvia low x
# pos 2 canvia low y
# pos 3 canvia high x
# pos 4 canvia high x

for i in f:
    
    if pos == 1:
        dib.polygon([(lowx, lowy + i - 1), (lowx + i - 1, lowy), (lowx + i - 1, lowy + i - 1)], ((k-c)*r, (k-c)*g, (k-c)*b))
        lowx += i
    elif pos == 2:
        dib.polygon([(lowx, lowy), (lowx, lowy + i - 1), (highx - 1, lowy + i - 1)], ((k-c)*r, (k-c)*g, (k-c)*b))
        lowy += i
    elif pos == 3:
        dib.polygon([(highx - i, lowy), (highx - 1, lowy), (highx - i, highy - 1)], ((k-c)*r, (k-c)*g, (k-c)*b))
        highx -= i
    elif pos == 4:
        dib.polygon([(lowx, highy - i), (lowx + i - 1, highy - i), (lowx + i - 1, highy - 1)], ((k-c)*r, (k-c)*g, (k-c)*b))
        highy -= i 


    if pos == 4:
        pos = 1
    else:
        pos += 1
    c += 1


img.save("output.png")

