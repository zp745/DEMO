'''
Created on 2017年8月6日

@author: I314070
'''
from urllib.request import  urlopen
from bs4 import  BeautifulSoup
import csv

html=urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html.parser")
table = bsObj.find("table",{"class":"wikitable"})
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
print("Done")