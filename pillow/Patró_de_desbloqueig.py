from PIL import Image, ImageDraw
from easyinput import read

dic1 = {1: (42,42),2:(107,42), 3:(172,42),4: (42,107), 5:(107,107), 6:(172,107),7: (42,172), 8:(107,172), 9:(172,172),}

n = read(int)
f = read(str)
a = read(str)
b = read(str)

img = Image.new("RGB", (215, 215), f)
dib = ImageDraw.Draw(img)

nums = []
for i in range(n):
    x = read(int)
    nums.append(x)

k = 1
# 20 marge entre rodones, diametre = 45
for i in range(3):
    for j in range(3):
        if k in nums:
            col = a
        else:
            col = b

        dib.ellipse([65 * j + 20, 65 * i + 20, 44 + (65 * j + 20), 44 + (65 * i + 20) ],col)
        k += 1

for i in range(len(nums)-1):
    dib.line([dic1[nums[i]],dic1[nums[i+1]]],fill = a, width = 3)


img.save("output.png")


