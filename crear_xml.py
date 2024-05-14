#!/usr/bin/python3

from bs4 import BeautifulSoup


soup = BeautifulSoup(features='xml')

etiqueta = soup.new_tag('cosa', id=1)

otra_cosa = soup.new_tag('otra_cosa', value="papafrita")

otra_cosa.string = "esto es el texto de otra cosa"

etiqueta.append(otra_cosa)

soup.append(etiqueta)

file = open("archivo.faix", "w")
file.write(soup.prettify())
file.close()
