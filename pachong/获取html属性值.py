from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     server = 'http://www.biqukan.com/'
     target = 'http://www.biqukan.com/1_1094/'
     req = requests.get(url = target) 
     req.encoding = req.apparent_encoding
     shtml = req.text
     div_bf = BeautifulSoup(shtml, 'html.parser')
     div = div_bf.find_all('div', class_ = 'listmain')
     a_bf = BeautifulSoup(str(div[0]))
     a = a_bf.find_all('a')
     for each in a:
          print(each.string, server + each.get('href'))