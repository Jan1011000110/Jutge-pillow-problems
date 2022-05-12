from easyinput import read
from PIL import Image, ImageDraw

col = read(str)


img = Image.new("RGB", (500,500))
dib = ImageDraw.Draw(img)

dib.polygon([(0,0), (499, 0),(499,499),(0,499)], col)
dib.polygon([(0,0), (399, 0),(399,399),(0,399)], "Green")
dib.polygon([(0,0), (399, 0),(399,399),(0,399)], (200.5, 100, 300))
img.save("output.png")
