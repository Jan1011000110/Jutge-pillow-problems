from easyinput import read
from PIL import Image, ImageDraw

try:
    n = read(int)
    width = 3*n
    height = 3*n
    img = Image.new("RGB", (width,height), "Beige")
    dib = ImageDraw.Draw(img)

    dib.polygon([
        (n, 0),
        (2*n-1, 0),
        (3*n-1, n),
        (3*n-1, 2*n-1),
        (2*n-1,3*n-1),
        (n,3*n-1),
        (0,2*n-1),
        (0,n)],
        "Red" ) 
    
    img.save("output.png")

except:
    pass