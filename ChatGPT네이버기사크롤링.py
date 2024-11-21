import requests
from bs4 import BeautifulSoup

# URL 설정
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# HTTP 요청 보내기
response = requests.get(url)
response.raise_for_status()  # 요청에 문제가 있을 경우 예외 발생

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 제목 크롤링
# 예시: 'news_tit' 클래스가 기사 제목에 사용되는 경우
titles = soup.find_all("a", class_="news_tit")  # 적절한 클래스명을 선택하세요

# 출력
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title.get_text()}")  # 제목 텍스트 추출
    print(f"링크: {title['href']}")      # 해당 기사 링크
