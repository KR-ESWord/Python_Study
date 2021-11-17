import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

my_list_1 = []
my_list_2 = []

print('장르 유형')
print('1. 드라마 | 2. 판타지 | 3. 서부 | 4. 공포')
print('5. 멜로/로맨스 | 6. 모험 | 7. 스릴러 | 8. 느와르')
print('9. 컬트 | 10. 다큐멘터리 | 11. 코미디 | 12. 가족')
print('13. 미스터리 | 14. 전쟁 | 15. 애니메이션 | 16. 범죄')
print('17. 뮤지컬 | 18. SF | 19. 액션 | 20. 무협')
print('21. 에로 | 22. 서스펜션 | 23. 서사 | 24. 블랙코미디')
print('25. 실험 | 26. 공연실황')

url_head = "https://movie.naver.com/movie"
genre_num = input('장르 유형 선택 : ')
url_mid = "/sdb/browsing/bmovie.nhn?genre=" + str(genre_num)

for page_num in range(44,53):
    url_tail = "&page=" + str(page_num)

    soup_1 = BeautifulSoup(urlopen(url_head + url_mid + url_tail), "html.parser")
    print(page_num, '페이지 다운로드 진행 중 입니다.')
    for link in soup_1.findAll("a"):
        if 'href' in link.attrs: # 내부에 있는 항목들을 리스트로 가져옵니다 ex) {u'href': u'//www.wikimediafoundation.org/'}
            if '/movie/bi/mi/basic.nhn' in link.attrs['href'] :
                my_list_1.append(link.attrs['href'])

    for i in range(len(my_list_1)) :
        soup_2 = BeautifulSoup(urlopen("https://movie.naver.com" + my_list_1[i]), "html.parser")
        soup = soup_2.find("div",class_="poster")
        try:
            imgUrl = soup.find("img")["src"]
            file_name = soup.find("img")["alt"]
            file_name = "".join(i for i in file_name if i not in "\/:*?<>|")
            urllib.request.urlretrieve(imgUrl, file_name + '.png')
        except:
            continue
    print(page_num, '페이지 다운로드 완료되었습니다.')
