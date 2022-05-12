from PIL import Image, ImageDraw


def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)

bx = []
by = []
mx = []
my = []

n = int(input())

for i in range(2*n):
    x = int(input())
    if i % 2 == 0:
        bx.append(x)
    else:
        by.append(x)
    
m = int(input())

for i in range(2*m):
    x = int(input())
    if i % 2 == 0:
        mx.append(x)
    else:
        my.append(x)



img = Image.new("RGB", (101, 71), "Green")
dib = ImageDraw.Draw(img)



# calcul de fora de joc

x1 = bx[0]

for i in bx:
    if i < x1:
        x1 = i

x2 = mx[0]

for i in mx:
    if i < x2:
        x2 = i

if x1 > 50:
    pass

elif x1 < 50 and x1 < x2:
    rect(0, 0, x1, 70,"Red")

elif x1 < 50 and x1 > x2:
    rect(0, 0, x2, 70,"Orange")






# circumferencia del centre del camp
dib.arc([40, 25, 60, 45], 0, 360, 'White')

# ratlla del mig del camp
rect(50, 0, 50, 70, 'White')

# area gran de l'esquerra
rect(16, 16, 16, 54, 'White')
rect(0, 16, 16, 16, 'White')
rect(0, 54, 16, 54, 'White')

# area petita de l'esquerra
rect(6, 25, 6, 45, 'White')
rect(0, 25, 6, 25, 'White')
rect(0, 45, 6, 45, 'White')

# area petita de la dreta
rect(84, 16, 84, 54, 'White')
rect(100, 16, 84, 16, 'White')
rect(100, 54, 84, 54, 'White')

# area gran de la dreta
rect(94, 25, 94, 45, 'White')
rect(100, 25, 94, 25, 'White')
rect(100, 45, 94, 45, 'White')

for i in range(n):
    dib.ellipse([bx[i] - 3 , by[i] - 3 , 3 + bx[i], 3 + by[i]], "Blue")

for i in range(m):
    dib.ellipse([mx[i] - 3 , my[i] - 3 , 3 + mx[i], 3 + my[i]], "Magenta")


img.save("output.png")
