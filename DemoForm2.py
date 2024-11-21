# DemoForm2.py
# DemoForm2.ui(화면) + DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#크롤링 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request
#정규표현식 사용
import re

#디자인 파일 로딩(DemoForm2.ui)
form_class = uic.loadUiType("DemoForm2.ui")[0]   

#윈도우 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯 메소드 추가
    def firstClick(self):
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
        self.label.setText("중고장터 크롤링 완료!!")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭!!")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭!!")


#메인 영역
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()

