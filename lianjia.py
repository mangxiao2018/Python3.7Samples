# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

i=0

with open('haidian-lianjia.csv','a') as file:
     for j in range(1,100,1):
          i+=1
          url = 'https://bj.lianjia.com/ershoufang/haidian/pg+str(i)'
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
          resp = requests.get(url,headers = headers).text
          # print(resp)

          soup = BeautifulSoup(resp,'lxml')
          infos = soup.find('ul',{'class':'sellListContent'}).find_all('li')
          # print(infos)

          for info in infos:
               name = info.find('div',{'class':'title'}).find('a').get_text()
               price = info.find('div',{'class':'totalPrice'}).find('span').get_text()
               address = info.find('div',{'class':'address'}).get_text()
               print(address)
               area = re.split(r'\|',address)[2]
               print(area)
               file.write('{},{},{},{}\n'.format((name),(price),(address),area))


