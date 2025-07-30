import requests
import re
import os

#os.system('rm images/continente_ilhas/*')
#os.system('rm images/peninsula_iberica/*')

ipma = "https://www.ipma.pt/"



# Temperatura da agua do mar

continente_ilhas  = "https://www.ipma.pt/pt/maritima/sst/index.jsp?area=cont-e-ilhas"
peninsula_iberica = "https://www.ipma.pt/pt/maritima/sst/index.jsp?area=iberia"

response_continente_ilhas  = requests.get(continente_ilhas)
response_peninsula_iberica = requests.get(peninsula_iberica)

images_continente_ilhas_temperatura = re.findall(r'resources.www/transf/mar/mercator/sst-cont-e-ilhas-[^"]*', response_continente_ilhas.text )
images_peninsula_iberica_tempertura = re.findall(r'resources.www/transf/mar/nemo/sst-iberia-[^"]*', response_peninsula_iberica.text )

#counter = 0
#for i in images_continente_ilhas_temperatura:
#    #time.sleep(0.3)
#    os.system("curl " + ipma + i + f" --output images/continente_ilhas/img-{str(counter).zfill(3)}.png")
#    counter += 1
#
#counter = 0
#for i in images_peninsula_iberica_tempertura:
#    #time.sleep(0.3)
#    os.system("curl " + ipma + i + f" --output images/peninsula_iberica/img-{str(counter).zfill(3)}.png")
#    counter += 1
#

os.system('ffmpeg -framerate 15 -i images/continente_ilhas/img-%03d.png  -c:v libx264 -pix_fmt yuv420p temperatura_mar_continente_ilhas.mp4')
os.system('ffmpeg -framerate 15 -i images/peninsula_iberica/img-%03d.png -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p temperatura_mar_peninsula_iberica.mp4')


# Precipitacão 

precipitacao_continente_ilhas = "https://www.ipma.pt/pt/otempo/prev.numerica/index.jsp?selModelo=5&selParam=23&selNivel=-1&selArea=2"

response_precipitacao = requests.post(precipitacao_continente_ilhas)

images_continete_ilhas_precipitacao = re.findall(r'resources.www/data/previsao/numerica/cartas/20250730/[^/]*/[^\.]+.gif ',response_precipitacao.text)

print(len(images_peninsula_iberica_tempertura), len(images_continente_ilhas_temperatura), len(images_continete_ilhas_precipitacao))
#print(images, len(images))
