# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'https://www.op.gg/summoner/userName=SKT+T1+Gumayusl'
     req = requests.get(url = target)
     req.encoding = req.apparent_encoding
     html = req.text
     bf = BeautifulSoup(html, 'html.parser')
     div = bf.find_all('div', class_ = 'Win')
     team_List = []
     member_List = []
     for div_item in div:
          div1 = BeautifulSoup(str(div_item), 'html.parser')
          heros = div1.find_all('div', class_ = 'Team')
          for hero in heros:
               div2 = BeautifulSoup(str(hero), 'html.parser')
               hero_item = div2.find_all('div', class_ = 'Image16')
               for each in hero_item:
                    member_List.append(each.get('title'))
          team_List.append(member_List)
          member_List = []
     print(team_List[4])
