from urllib.parse import quote
from bs4 import BeautifulSoup
import requests

#네이버 검색어 입력했을때 뉴스 제목 5페이지까지 전체 긁어오기

#가짜뉴스라고 검색후 뉴스 2페이지의 주소
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B0%80%EC%A7%9C%EB%89%B4%EC%8A%A4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11

def getTitle(addr, q):
    for i in range(0,5):
        print(f"================={i+1}페이지")
        start=10*i+1
        address = addr+q+"&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start="+str(start)
        res=requests.get(address)
        soup = BeautifulSoup(res.text,'html.parser')
        news = soup.select('.news_tit')
        for i in news:
            print(i.get_text())
            
if __name__=='__main__':
    address= "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" 
    query = quote(input("검색어 : "))
    
getTitle(address,query)