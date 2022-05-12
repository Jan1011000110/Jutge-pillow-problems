from PIL import Image, ImageDraw
n = int(input())

img = Image.new('RGB', [50*n, 50*n])
dib = ImageDraw.Draw(img)

for i in range(n):
    for j in range(n):
        if i%2 == 0:
            if j%2 == 0:
                col = "Beige"
            else:
                col = "Brown"
        elif i%2 == 1:
            if j%2 == 0:
                col = "Brown"
            else:
                col = "Beige"
            
        dib.polygon([
            (50*i, 50*j),
            (50*i + 49, 50*j),
            (50*i + 49, 50*j + 49),
            (50*i, 50*j + 49)], col)




img.save("output.png")