from PIL import Image, ImageDraw
c = str(input())
f = str(input())
n = int(input())

img = Image.new('RGB', [16*n, 16*n], c)
dib = ImageDraw.Draw(img)

dib.ellipse([0, 0, 16*n - 1, 16*n - 1], c)
dib.chord([0, 0, 16*n - 1, 16*n - 1], 90, 270, f, c)

img.save('output.png')