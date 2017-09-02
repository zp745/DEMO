'''
Created on 2017年8月16日

@author: I314070
'''

import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime


header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Referer":"http://data.eastmoney.com/cjsj/consumerpriceindex.aspx?p=6",
    "Host":"data.eastmoney.com",
    "Content-Type":"application/x-www-form-urlencoded",
    "Connection":"Keep-Alive",
    "Accept-Language":"zh-Hans-CN,zh-Hans;q=0.5",
    "Accept-Encoding":"gzip, deflate, peerdist",
    "Accept":"text/html, application/xhtml+xml, image/jxr, */*",
    #"Cookie": login_info["cookie_str"]
    } 
session = requests.Session()


timestr = datetime.now().strftime("%Y%m%d%H%M%S")
fileName = "cpi.csv"

csvFile = open(fileName,'wt', newline='' ,encoding = 'utf-16')
writer = csv.writer(csvFile)
pages = [1]
page_num = 0
try:
    while page_num < len(pages):
        url = "http://data.eastmoney.com/cjsj/consumerpriceindex.aspx?p=" + str(page_num+1)
        resp = session.get(url,headers = header)
        bsObj = BeautifulSoup(resp.text,"html.parser")
        table = bsObj.find("table",{"id":"tb"})
        rows = table.findAll("tr")  
        row_index = 1      
        for row in rows:   
            if page_num != 0 and (row_index == 1 or row_index == 2):
                row_index = row_index + 1
                continue
            csvRow=[]
            cells = row.findAll(['td','th'])   
            
            for cell in cells:
                cell_content = cell.get_text().strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')
                if cell_content.find('pageit') == -1:
                    csvRow.append(cell_content)
                else:
                    index_str = cell_content.find('pageit')
                    start = cell_content.find("('") + 2
                    end = cell_content.find("')")
                    max_page = cell_content[start:end]
                    if max_page.isdigit():
                        max_page_num = int(max_page)
                        pages = range(0,max_page_num)
            if row.id != 'moretr' and csvRow != []: 
                writer.writerow(csvRow)
            row_index = row_index + 1
        page_num = page_num + 1
finally:
    csvFile.close()
    
print(os.path.abspath(fileName))
