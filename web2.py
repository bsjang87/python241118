# web2.py
#크롤링 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request
#정규표현식 사용
import re

#파일로 저장
f = open("clien.txt", "wt", encoding="utf-8")
for i in range(0, 10):
    #페이징처리
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    #print(url)
    #주소를 입력
    response = urllib.request.urlopen(url)
    #묹자열을 받아서 디코딩
    page = response.read().decode("utf-8")
    #검색이 용이한 객체 생성
    soup = BeautifulSoup(page, "html.parser")
    list = soup.find_all("a", attrs={"class":"list_subject"})
    for item in list:
        try:
            title = item.find("span", attrs={"class":"subject_fixed"})
            title = title.text.strip()
            #print(title)
            if re.search("아이폰", title):
                #print(title)
                f.write(title + "\n")
        except:
            pass

f.close()


# <a class="list_subject" href="/service/board/sold/18843936?od=T31&po=0&category=0&groupCd=" data-role="cut-string">
#	    <span class="category fixed" title="판매">판매</span>
# 	    <span class="subject_fixed" data-role="list-title-text" title="맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.">
# 		    맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.
# 		</span>
# </a>