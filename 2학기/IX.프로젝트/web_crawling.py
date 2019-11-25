from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버 웹툰에서 바연길 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=703852")
    soup = BeautifulSoup(data, "lxml")
    # print(data)
    cartoon_titles = soup.find_all("td", attrs={"class" : "title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        link = cartoon_title.find("a").get("href")
        link = "http://conmic.naver.com" + link
        print(title)
        print(link)