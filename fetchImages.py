import requests
import re
import os
import time



ipma = "https://www.ipma.pt/"

url = "https://www.ipma.pt/pt/maritima/sst/index.jsp?area=cont-e-ilhas"

response = requests.get(url)

images = re.findall(r'resources.www/transf/mar/mercator/sst-cont-e-ilhas-[^"]*', response.text )

#os.system('rm images/*')
#os.system('output.gif')

counter = 0
for i in images:
    #time.sleep(0.3)
    os.system("curl " + ipma + i + f" --output images/img-{str(counter).zfill(3)}.png")
    counter += 1


os.system('ffmpeg -framerate 15 -i img-%03d.png -c:v libx264 -pix_fmt yuv420p tempertura_mar.mp4')
#os.system('ffmpeg -framerate 15 -pattern_type glob -i "images/*.png" -vf "palettegen" palette.png')
#os.system('ffmpeg -framerate 15 -pattern_type glob -i "images/*.png" -i palette.png -lavfi "paletteuse" output.gif')


cartasMetereologicas = "https://www.ipma.pt/pt/otempo/prev.numerica/index.jsp"




#print(images, len(images))
