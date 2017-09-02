'''
Created on 2017年8月6日

@author: I314070
'''
import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

login_infos = [
    {
    "user_name":"user1",
    "start_time":"2017-06-01",
    "end_time":"2017-08-31",
    "cookie_str":""    
        },
    {
    "user_name":"user2",
    "start_time":"2017-06-01",
    "end_time":"2017-08-31",
    "cookie_str":""    
        }
    ]

url = "http://pay.duowan.com/listUserPayLog.action"

timestr = datetime.now().strftime("%Y%m%d%H%M%S")

fileName = timestr+"duowan.csv"
csvFile = open(fileName,'wt', newline='' ,encoding = 'utf-16')
writer = csv.writer(csvFile)

session = requests.Session()
try:
    idx_login_info = 1
    for login_info in login_infos:
        idx_page = 0
        pages = [1]
        while idx_page < len(pages):
            data = {
                "endTime":login_info["end_time"],
                "pageNum": str(pages[idx_page]),
                "startTime": login_info["start_time"]
                }
            header = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
                "Referer":"http://pay.duowan.com/listUserPayLog.action",
                "Host":"pay.duowan.com",
                "Content-Type":"application/x-www-form-urlencoded",
                "Connection":"Keep-Alive",
                "Cache-Control":"no-cache",
                "Accept-Language":"zh-Hans-CN,zh-Hans;q=0.5",
                "Accept-Encoding":"gzip, deflate",
                "Accept":"application/json, text/javascript, */*",
                "Cookie": login_info["cookie_str"]
                }            
            resp = session.post(url,headers = header,data = data)
            bsObj = BeautifulSoup(resp.text,"html.parser")
            table = bsObj.find("table",{"class":"table"})
            rows = table.findAll("tr")
    # 只导出第一页的表头行，其他页的表头跳过       
            row_idx = 1 
            for row in rows:
                if row_idx == 1 and (pages[idx_page] != 1 or idx_login_info != 1):
                    row_idx = row_idx + 1
                    continue
                csvRow=[]
                # 第一页的第一行在末尾增加User_Name列表头    
                if row_idx == 1 and pages[idx_page] == 1 and idx_login_info == 1:
                    csvRow.append("用户名")
                else:
                # 当不是第一页的第一行的时候填写实际的用户名
                    csvRow.append(login_info["user_name"])                
                for cell in row.findAll(['td','th']):
                    csvRow.append(cell.get_text().strip().replace('=','').replace('给',','))

                    
                row_idx = row_idx + 1
                writer.writerow(csvRow)
    # 查找有效的页数            
            numOfPage = bsObj.find("div",{"class":"pagination"}).findAll("a")
            for a in numOfPage:
                text_a = a.text.strip()
                if text_a.isdigit():
                    if  int(text_a) not in pages:
                        pages.append(int(text_a))
            idx_page = idx_page + 1
        idx_login_info = idx_login_info + 1
finally:
    csvFile.close()
    
print(os.path.abspath(fileName))
