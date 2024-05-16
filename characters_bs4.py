#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

file.close()

title ="Bienvenido a Fary's Adventure"

print(title)
print("="*len(title))

print("\n¿Quién quieres ser?\n")

for character in characters:
	print(f"{character['id']}\t {character.find('name').text}")

encontrado = False
while not encontrado:
	id = input("\nIntroduce un número: ")

	file = open('characters.facx', 'r')

	soup = BeautifulSoup(file, 'xml')

	file.close()

	character = soup.find('character', {'id': id})

	if not character:
		print("Error: id no encontrado")
	else:
		encontrado = True

print("\nEl personaje escogido es:\n")
print(f"\tNombre: {character.find('name').text}")
print(f"\tEdad: {character.find('age').text}")
print(f"\tGénero: {character.find('gender')['value']}")
print(f"\tNivel: {character.find('level')['value']}")

file = open('characters_items.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()
characters_items = soup.find_all('character_item')
items_ids = []

for character_item in characters_items:
	id_character = character_item.find("character")["id"]
	
	if  id_character == id:
		
		id_item = character_item.find("item")["id"]
		
		items_ids.append(id_item)

file = open('items.faix', 'r')

soup = BeautifulSoup(file, 'xml')

file.close()

items = soup.find_all('item', {'id':True})

for item in items:
	if item['id'] in items_ids:
		print("\tItems:\t"+item.find("item").text)

file = open('characters_weapons.facix', 'r')
soup = BeautifulSoup(file, 'xml')
file.close()
characters_weapons = soup.find_all('character_weapon')
weapons_ids = []

for character_weapon in characters_weapons:
    id_character = character_weapon.find("character")["id"]

    if id_character == id:

        id_weapon = character_weapon.find("weapon")["id"]

        weapons_ids.append(id_weapon)

file = open('weapons.faix', 'r')

soup = BeautifulSoup(file, 'xml')

file.close()

weapons = soup.find_all('weapon', {'id':True})

for weapon in weapons:
    if weapon['id'] in weapons_ids:
        print("\tDaño:\t"+weapon.find("damage")['value'])

matar = True
while matar:
	respuesta = input("\nQuieres matar a algún personaje (R: si/no)? ")
	if respuesta == "no":
		matar = False
	else:
		id = input("\nIntroduce el número del personaje: ")
		file = open('characters.facx', 'r')
		soup = BeautifulSoup(file, 'xml')
		file.close()

		eliminar = soup.find('character', {'id': id})
		if eliminar:
			print(f"Se ha matado al personaje: {eliminar.find('name').text}")
			eliminar.extract()

			edicion = str(soup)
			file = open('characters.facx', 'w')
			file.write(edicion)
			file.close()

		else:
			print("No se encontró el personaje que has marcado")
		
