from PIL import Image, ImageDraw

img = Image.new('RGB', (500,500), "Blue")
dib = ImageDraw.Draw(img)

dib.ellipse([50, 10, 300, 300], "Red")


img.save("output.png")

