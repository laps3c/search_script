#!/usr/bin/python
#coding: utf-8
#creator: laps3
#contact: Telegram:@laps3c
from datetime import datetime
import os
import shodan
import wikipedia
from geopy.geocoders import Nominatim
import time

#	GREEN =
#	RED =

class banner:
	index = '''
                          _     
                         | |    
  ___  ___  __ _ _ __ ___| |__  
 / __|/ _ \/ _` | '__/ __| '_ \ 
 \__ \  __/ (_| | | | (__| | | |
 |___/\___|\__,_|_|  \___|_| |_|
                                
                                

'''

	options = '''
[geocode] Maps
[wikipedia] Search
[shodan] Search
[exit] Exit
'''	
	
	separator = '''#################'''

os.system('clear')
now = datetime.now()
print(banner.index)
print(banner.options)

api_key = ''
api = shodan.Shodan(api_key)
def main():
	text2 = input('O que deseja usar: shodan, wikipedia or geocode: ')
	if text2 == 'shodan':
		try:
			inp = input('O que deseja pesquisar: ')
			print('')
			results = api.search(inp)
			print(['total'])
			for result in results['matches']:
				IP = result['ip_str']
				data = result['data']
				print('IP: ', IP)
				print('Data: ', data)
				print(banner.separator)
				aes = input('Continue [enter] or for exit [ctrl + c]')
				print('')
		except:
			print('')
	elif text2 == 'wikipedia':
		text1 = input('O que deseja pesquisar: ')
		a = wikipedia.search(text1)
		print(a)
		page = input('Page: ')
		b = wikipedia.page(page)
		print(b)
		print(b.title, b.content, b.links[0])
		wikipedia.set_lang=('en')
		print(banner.separator)
		af = input('Deseja fazer outra pesquisa: s/n ')
		if af == 's':
			time.sleep(2)
			print(banner.separator)
			main()
		elif af == 'exit':
			print('Exiting')
			time.sleep(3)
			exit()
		else:
			print('Command not found')
	elif text2 == 'geocode':
		geolocator = Nominatim()
		geocodee = input('Address: ')
		location = geolocator.geocode(geocodee)
		print(location.address)
		print((location.latitude, location.longitude))
		print(banner.separator)
		abc = input('Deseja fazer outra pesquisar: s/n ')
		if abc == 's':
			time.sleep(2)
			print(banner.separator)
			main()
		elif abc == 'exit':
			print('Exiting')
			time.sleep(3)
			exit()
		else:
			print('Command not found')		
	elif text2 == 'exit':
		print('thank u for use this script!')
	else:
		print('Command not found')	
main()
