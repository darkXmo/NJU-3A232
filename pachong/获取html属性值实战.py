# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'https://www.op.gg/ranking/ladder/'
     req = requests.get(url = target)
     req.encoding = req.apparent_encoding
     html = req.text
     bf = BeautifulSoup(html, 'html.parser')
     td = bf.find_all('td', class_ = 'select_summoner')
     aList = []
     for td_item in td:
        a_bf = BeautifulSoup(str(td_item), 'html.parser')
        a = a_bf.find_all('a')
        for each in a:
            aList.append(each.get('href'))
     for each in aList:
          print(each)
