#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('characters.facx', 'r')

soup = BeautifulSoup(file, 'xml')

characters = soup.find_all("character")

for character in characters:
	print(f"{character['id']}\t {character.find('name').text}\t\t{character.find('age').text}\t{character.find('level')['value']}")


