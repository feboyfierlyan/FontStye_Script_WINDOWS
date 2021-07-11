 # -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def bannerstyle():
	f1 = open('graffiti.txt', 'r')
	f1_contents = f1.read()
	print(f1_contents)
	print('')
	print('[1] Graffiti')
	print('')
	print('')

	f2 = open('shadow.txt', 'r', encoding="utf8")
	f2_contents = f2.read()
	print(f2_contents)
	print('')
	print('[2] Shadow')
	print('')
	print('')

	f3 = open('bloddy.txt', 'r', encoding="utf8")
	f3_contents = f3.read()
	print(f3_contents)
	print('')
	print('[3] Bloddy')
	print('')
	print('')

	f4 = open('delta.txt', 'r', encoding="utf8")
	f4_contents = f4.read()
	print(f4_contents)
	print('')
	print('[4] Delta')
	print('')
	print('')

	f5 = open('elite.txt', 'r', encoding="utf8")
	f5_contents = f5.read()
	print(f5_contents)
	print('')
	print('[5] Elite')
	print('')
	print('')



def main():
	global webdriver
	global font
	global PATH

	chrome_options = Options()
	chrome_options.add_argument("--headless")

	PATH = "chromedriver.exe"

	webdriver = webdriver.Chrome(options=chrome_options, executable_path=PATH)

	i = 0

	print("")
	font = input("[*] The text : ")
	bannerstyle()
	style = input("[*] Select the style : ")
	print("[*] Please Wait...")
	print('')

	if style == '1':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Graffiti&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

	elif style == 'graffiti':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Graffiti&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'Graffiti':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Graffiti&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == '2':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'shadow':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'Shadow':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == '3':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Bloody&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'bloddy':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Bloody&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'Bloddy':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Bloody&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == '4':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Delta%20Corps%20Priest%201&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'delta':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Delta%20Corps%20Priest%201&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'Delta':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Delta%20Corps%20Priest%201&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == '5':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Elite&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'elite':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Elite&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	elif style == 'Elite':
		time.sleep(1)
		url = "https://patorjk.com/software/taag/#p=display&f=Elite&t=" + font

		webdriver.get(url)
		time.sleep(1)

		isi = webdriver.find_element_by_id('taag_output_text').text
		print('')
		print(isi)

		print('')
		print("[*] Complete!")

		webdriver.quit()

	else:
		print('')
		print("[*] Error!")
		print('')

		exit()

if __name__ == '__main__':
	main()