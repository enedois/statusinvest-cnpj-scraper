from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
import os
import datetime
from bs4 import BeautifulSoup
##import pandas
##import mysql.connector

##mydb = mysql.connector.connect(
##  host="localhost",
##  user="root",
##  password="",
##  database="fii-data"
##)

##carrega os papeis de stocksList.csv
stocksList = open('FIIsList_Carteira.csv', 'r')
papeis = stocksList.read().split(';')
#print(papeis)
#papeis = ["xppr11"]
stocksList.close()

def getpapel(papel_):
    try:
                    url = "https://statusinvest.com.br/fundos-imobiliarios/"
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    soup = BeautifulSoup(html, 'html.parser')
                    #print(soup.prettify())
                    result = soup.find_all("h3", string="CNPJ")[0].find_parent().find_all("strong")[0].getText()
                    
                    print(papel_+"|"+result)
                    
                    #

                    #print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel_," ", str(e))
        print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
        papeis.remove(papel_)
        #print(papeis)
    
while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)

            


