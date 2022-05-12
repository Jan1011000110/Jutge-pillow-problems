#En aquest programa, la imatge té sempre 600 punts d’amplada i 400 punts d’alçada. 
#El punt de la cantonada superior esquerra és el (0,0),
#i el punt de la cantonada inferior dreta és el (599,399).

from PIL import Image, ImageDraw

img = Image.new('RGB', (600, 400), 'White')
dib = ImageDraw.Draw(img)

dib.ellipse([150, 50, 449, 349], 'Crimson')

#img.save('output.png') obligatori

img.show()