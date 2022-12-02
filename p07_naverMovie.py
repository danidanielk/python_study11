# 크롤링 해서 1~10 페이지까지 영화제목 평점 감상평 의 형태로 csv 파일에 넣기
import requests
from bs4 import BeautifulSoup


# https://movie.naver.com/movie/point/af/list.naver?&page=2
# score=star_score
# contents=score_reple
# title=h_movie

with open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/movie.csv","w",encoding="UTF-8")as f:
    for i in range(1,11):
        addr="https://movie.naver.com/movie/point/af/list.naver?&page="+str(i)
        res = requests.get(addr)
        soup=BeautifulSoup(res.text,'html.parser')
        movies=soup.select('.title')#여러개가져올때는 select
        for i in movies:
            print(i.get_text().split("\n")[1])
            print(i.get_text().split("\n")[3].split("중")[1])
            print(i.get_text().split("\n")[5])
            print("--------------------------------------")
            f.write(i.get_text().split("\n")[1]+",\n")
            f.write(i.get_text().split("\n")[3].split("중")[1]+",\n")
            f.write(i.get_text().split("\n")[5]+"\n")
            f.write("-------------------------------\n")
            