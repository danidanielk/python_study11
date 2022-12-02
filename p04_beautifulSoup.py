#cmd -> pip install bs4
from bs4 import BeautifulSoup

htmlEX="""
<html>
<head>
<meta charset="UTF-8">
<title>우리는 beautifulSoup4 :BS4 로 Web Crawling을 할거에요</title>
</head>
<body>
<p><b>beautifulSoup</b></p>
<p> python에서 Crawling 할 때 유용하게 사용할 수 있는 Library
<a href="#">구글</a>
<a href="#">네이버</a>
<a href="#">유튜브</a>
</p>
</body>
</html>
"""

#bs4 초기화
#html.parser:html문법 규칙에 따른문자열, 해당문법을 바탇으로 단어의 의미나 구조를 분석하는 프로그램
soup = BeautifulSoup(htmlEX,"html.parser")

#title 부분찾기
title=soup.html.head.title
print(title)

#h1태그 찾기
h1=soup.html.body.p
for i in h1:
    print(i)