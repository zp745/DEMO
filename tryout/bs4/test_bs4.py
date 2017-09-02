'''
Created on 2017年8月6日

@author: I314070
'''

from urllib.request import  urlopen
from bs4 import  BeautifulSoup
'''
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
namelist = bsObj.find_all("span", {"class":"green"})
for name in namelist:
    print(name)


html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
trs = bsObj.find("table",{"id":"giftList"}).tr
namelist = trs.next_siblings
for name in namelist:
    print(name)

import re
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
imgs = bsObj.findAll("img",{"src":re.compile("\.\./img/gifts/img.*\.jpg")})
for name in imgs:
    print(name.attrs)
'''
import csv
html=urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html.parser")
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("edtors.csv",'wt',newline='',encoding = 'utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
    