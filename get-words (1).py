#!/usr/bin/python3
# Author: F1uWh3n

import requests
from bs4 import BeautifulSoup
import string
import sys
import os.path

def remove_characters(text):
	rem = string.printable[62:94]
	d = text
	f = ''.join( c for c in d if c not in rem )
	return f

def create_book(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	strings = soup.find_all('p')
	all_p = ''
	
	for i in strings:
		all_p += i.get_text()
	print(all_p)
	clean = remove_characters(all_p)
	words = clean.split()
	return words

def main():
	if len(sys.argv) != 3 :
		print('[*] Use : $ python3 <links_file> <out_file>')
	else:
		output = sys.argv[2]
		if os.path.isfile(output):
			print('[*] El archivo de salida ya existe')
		else:
			file_rute = sys.argv[1]
			f = open(file_rute,'r',encoding='ISO-8859-1')
			urls = f.readlines()
			f.close()
			lis = []
			for i in urls :
				print('')
				print('[*] link: '+i.rstrip('\n'))
				print('')
				lis += create_book(i.rstrip('\n'))
				print('')
			f = open(output,'w')
			for i in set(lis):
				f.write(i)
				f.write('\n')	
			f.close()

if __name__=='__main__':
	main()
		
	
