# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'https://www.op.gg/summoner/userName=SKT+T1+Gumayusl'
     req = requests.get(url = target)
     req.encoding = req.apparent_encoding
     html = req.text
     bf = BeautifulSoup(html, 'html.parser')
     texts = bf.find_all('div', class_ = 'FollowPlayers Names')
     print(texts)

