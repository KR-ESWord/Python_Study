from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

date = input("날짜입력 yyyymmdd: ")

url_base = 'https://movie.naver.com'
url_sub = '/movie/sdb/rank/rmovie.nhn?sel=cur&date=' + date

url = url_base + url_sub

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_movie_name = soup.find_all('div', 'tit5')
list_movie_point = soup.find_all('td', 'point')

for i in range(len(list_movie_name)):
    print(list_movie_name[i].a.string, list_movie_point[i].string)