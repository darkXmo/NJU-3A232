# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys

for ix in range(2, 6):
    input = open("data"+str(ix)+".txt", 'a', encoding='utf-8')
    target = 'https://www.op.gg/ranking/ladder/page='+str(ix)
    req = requests.get(url = target)
    req.encoding = req.apparent_encoding
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    td = bf.find_all('td', class_ = 'select_summoner')
    url_List = []
    for td_item in td:
        a_bf = BeautifulSoup(str(td_item), 'html.parser')
        a = a_bf.find_all('a')
        for each in a:
            url_List.append(each.get('href'))
    for url in url_List:
        print(url)

        target = 'http:' + url
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
                hero_item = div2.find_all('div', class_ = 'Image20')
                for each in hero_item:
                    member_List.append(each.get('title'))
            team_List.append(member_List)
            member_List = []

        for each in team_List:
            input.write(str(each)[1:-1])
            input.write("\n")
            print(str(each)[1:-1])


    input.close()