from PIL import Image, ImageDraw

n = int(input())
p = int(input())

lx = []
ly = []

img = Image.new("RGB", (n,n), "Beige")
dib = ImageDraw.Draw(img)

for i in range(p):
    x = int(input())
    y = int(input())
    lx.append(x)
    ly.append(y)

mxX = max(lx)
mnX = min(lx)
mxY = max(ly)
mnY = min(ly)

dib.polygon([
    (mnX, mnY),
    (mxX, mnY),
    (mxX, mxY),
    (mnX, mxY)], "Red")

for i in range(p):
    x = lx[i]
    y = ly[i]
    dib.point([x,y], "Black")


img.save("output.png")
