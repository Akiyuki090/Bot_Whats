import time
import urllib
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

for i, mensagem in enumerate(contatos['COLUNA DO EXCEL PARA MENSAGEM']):
    pessoa = contatos.loc[i, "COLUNA COM O NOME DA PESSOA"]
    numero = contatos.loc[i, "COLUNA COM O NUMERO DA PESSOA"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    nav.get(link)
    while len(nav.find_elements_by_id("side")) < 1:
        time.sleep(1)
    nav.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
