from PIL import Image, ImageDraw

f = str(input())
c1 = str(input())
c2 = str(input())
c3 = str(input())
n = int(input())
w = 25*(2**n)
img = Image.new('RGB', (w,w), f)
dib = ImageDraw.Draw(img)

for i in range(1,n+1):
    dib.ellipse([w-(25*(2**i)), w-(12.5*(2**i)), ((12.5*(2**i)) + (w-(25*(2**i)))) - 1,((12.5*(2**i)) + (w-(12.5*(2**i)))) - 1], c1)
    dib.ellipse([w-(25*(2**i)), w-(25*(2**i)), ((12.5*(2**i)) + (w-(25*(2**i)))) - 1, ((12.5*(2**i)) + (w-(25*(2**i)))) - 1], c2)
    dib.ellipse([w-(12.5*(2**i)), w-(25*(2**i)),((12.5*(2**i)) + (w-(12.5*(2**i)))) - 1,((12.5*(2**i)) + (w-(25*(2**i)))) - 1 ], c3)
    n-=1

img.save('output.png')