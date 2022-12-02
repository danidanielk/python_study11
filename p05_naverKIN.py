#네이버 지식인 크롤링
from urllib.parse import quote
import requests

#지식인 들어가서 검색했을때 나오는 요청 주소 복사
# https://kin.naver.com/search/list.naver?query=
# cmd -> pip install requests 다운(http요청을 하기위해 사용하는 모듈)
q=quote(input("검색어 : "))
print(q)

url= f"https://kin.naver.com/search/list.naver?query={q}"
response = requests.get(url) #여기서 get는 겟방식요청
# print(response.status_code) ----print 해서 200나오면 정상