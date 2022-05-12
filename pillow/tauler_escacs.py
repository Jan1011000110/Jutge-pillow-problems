from PIL import Image, ImageDraw
c = int(input())
f = int(input())

img = Image.new('RGB', [100*c, 100*f], c)
dib = ImageDraw.Draw(img)

for i in range(c):
    for j in range(f):
        if i%2 == 0:
            if j%2 == 0:
                col = "Yellow"
            else:
                col = "Green"
        elif i%2 == 1:
            if j%2 == 0:
                col = "Green"
            else:
                col = "Yellow"
            
        dib.polygon([
            (100*i, 100*j),
            (100*i + 99, 100*j),
            (100*i + 99, 100*j + 99),
            (100*i, 100*j + 99)], col)

img.save("output.png")
