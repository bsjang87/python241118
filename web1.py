# web1.py
#웹크롤링 예제
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인 형식)
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체를 생성
soup = BeautifulSoup(page, "html.parser")

#전체 페이지 출력
# print(soup.prettify())

#<p> 태그를 전체 검색
# print(soup.find_all("p"))

#<p> 태그를 한개 검색
# print(soup.find("p"))

#<p> 태그 중에서 class 속성이 inner-text인 것만 검색
#<p class="inner-text"> 필터링 조건
# print(soup.find_all("p", class_="inner-text"))    

#attrs 속성을 사용하는 경우(attributes)
# print(soup.find_all("p", attrs={"class":"inner-text"}))   

#태그 내부에 존재하는 텍스트만 출력 : .text 속성
#<p> 내부 문자열 </p>
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)
