from fake_useragent.fake import UserAgent
import urllib.request as req
from json import loads
#fake-useragent 설치 필요
#    cmd -> pip install fake-useragent
# 어떤 브라우저는 GET,POST 방식을 날리는 상대방이 컴퓨터인것을 알게 되면 해당 웹에 접속하는것을 차단하는 경우가 있다.
#    방금 설치한 라이브러리는 나 컴퓨터 아니야 라고 사람인척 해주는 라이브러이 임.

ua = UserAgent()
#이런것들로 사람인척 한다. . 무슨말인지 정확히는 모르겠지만
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)

#헤더 선언 : dict 형태 (key :value) 형태로
#        ex. {"name":"김비버", "age":100}

h={
    "User-Agent":ua.chrome,
    "referer":"https://finance.daum.net/"
    }
# daum 주식 금융 요청 url
# https://finance.daum.net/api/search/ranks?limit=10
url="https://finance.daum.net/api/search/ranks?limit=10"

#요청
res= req.urlopen(req.Request(url,headers=h)).read().decode()

#응답,데이터확인
# print('res: ',res) #json파일로  ㄱㄱ

#파이썬 스트링 형태로 변환.
ranking=loads(res)

for i in ranking["data"]:
    print(i["rank"],i["name"],i["tradePrice"])