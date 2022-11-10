import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.commom.keys import Keys

contatos = pd.read_excel('ARQUIVO.XLS')

nav = webdriver.chrome()
nav.get('https://web.whatsapp.com')

'''
esperar achar um elemento da pg do wpp
'''
while len(nav.find_elements_by_id('side')) < 1:
    time.sleep(1)

