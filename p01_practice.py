import urllib.request as req
#위에거 임포트 해야함.

# 웹 크로링/ 웹 스크래핑

# url 이미지 주소
# https://img.insight.co.kr/static/2018/11/17/700/c21832z125k305076kc1.jpg

# 다운받을 폴더 경로
# C:\Users\NT731QCJ-K582D\Desktop\test\pythonFile

img="https://img.insight.co.kr/static/2018/11/17/700/c21832z125k305076kc1.jpg"
html = "https://www.youtube.com"

path1="C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/panda.jpg"
path2="C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/youtube.html"

#f1,h1= req.urlretrieve(url, filename) 다운받을 파일 정보를 리턴해주는 기능.
f1,h1= req.urlretrieve(img, path1)
f2,h2= req.urlretrieve(html, path2)

print(h1)
print("-------")
print(h2)