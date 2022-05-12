from ast import Return
from PIL import Image, ImageDraw



def color(j):
    if j == 'P':
        return "Pink"
    elif j == 'G':
        return "Green"
    elif j == 'R':
        return "Red"
    elif j == 'Y':
        return "Yellow"
    elif j == 'O':
        return "Orange"
    elif j == 'B':
        return "Blue"

def check(j,c,f):
    if sol[c] == j:
        dib.ellipse([c*100 + 500, f*100, 99+(c*100 + 500), 99+(f*100)], "Black")
    else:
        for k in sol:
            if k == j:
                dib.ellipse([c*100 + 500, f*100, 99+(c*100 + 500), 99+(f*100)], "White")


sol = input()
t = int(input())
g = []
ok = True
for i in range(t):
    x = input()
    if x == sol:
        g.append(x)
        ok = False
    if (ok):
        g.append(x)


img = Image.new('RGB', (900, len(g) * 100), "Sienna")
dib = ImageDraw.Draw(img)

f = 0
for i in g:
    c = 0
    for j in i:
        col = color(j)
        dib.ellipse([c*100, f*100, 99+(c*100), 99+(f*100)], col)
        ans = check(j,c,f)
        c+=1
    f+=1
        


img.save("output.png")