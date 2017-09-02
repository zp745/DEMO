'''
Created on 2017年8月19日

@author: I314070
'''
import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

class KPI(object):

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
    def __init__(self,url='',FileName=''):
        self._url = url
        self._FileName = FileName
        
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self,url):
        self._url = url

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self,FileName):
        self._FileName = FileName
    
    def export(self):
        csvFile = open(self.FileName,'wt', newline='' ,encoding = 'utf-16')
        writer = csv.writer(csvFile)
        pages = [1]
        page_num = 0
        try:
            while page_num < len(pages):
                url = self.url + str(page_num+1)
                resp = self.session.get(url,headers = self.header)
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
            
        file_path = os.path.abspath(self.FileName)
        return file_path  
         

if __name__ == '__main__':
    kpi = KPI()
    tobe_dict = {
        'CPI.csv':'http://data.eastmoney.com/cjsj/consumerpriceindex.aspx?p=',
        'PPI.csv':'http://data.eastmoney.com/cjsj/productpricesindex.aspx?p='
        }
    for filename,url in tobe_dict.items():
        kpi.FileName = filename
        kpi.url = url
        print(kpi.export())
    print('Done at ' + datetime.now().strftime("%Y%m%d%H%M%S"))
    