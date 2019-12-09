import json

from bs4 import BeautifulSoup       #html 구조적으로 변환하기
from urllib.request import urlopen  #url에 해당하는 html 가져오기

import requests

if __name__ == '__main__':
    url = "https://www.youtube.com/channel/UCoUDrzyCl1IwU602xdTsM-g/videos"
    with requests.get(url) as response:
        soup = BeautifulSoup(response.text, "lxml")
    # print(soup)

    # youtube_titles = soup.find_all("a", attrs={"class" : "yt-uix-tile-link"})
    youtube_titles = soup.select("a.yt-uix-tile-link") #위게 것을 css셀렉터로 더 쉽게 쓴거임
    for youtube_title in youtube_titles:
        print(youtube_title.text)




    #
    # with urlopen("https://www.youtube.com/channel/UCoUDrzyCl1IwU602xdTsM-g/videos") as data:
    #     j = json.loads(data.read())
    # html = "<html><head><meta charset='utf-8'></head><body>"
    # cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    # for cartoon_title in cartoon_titles:
    #     title = cartoon_title["title"]
    #     thumnail = cartoon_title["thumbnailImage"]["url"]
    #     url = cartoon_title["id"]
    #     url = "http://webtoon.daum.net/webtoon/viewer/" + str(url)
    #     html += "<a href='{}'><img src='{}' />{}</a>".format(url, thumnail, title)
    # html += "</body></html>"
    #
    # output = BeautifulSoup(html, "lxml")    #htmlstring -> BeautifulSoup 객체
    # prettyHtml = str(output.prettify())     #html 줄 예쁘게
    # with open("취향저격그녀.html", mode="w", encoding="utf-8") as f:
    #     f.write(prettyHtml)
    #
    # # cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title">
    # # html = "<html><head><meta charset='utf-8'></head><body>"
    # # for title in cartoon_titles:
    # #     t = title.find('a').text            #제목
    # #     link = "http://comic.naver.com/" + title.find('a').get('href')  #링크
    # #     html += "<a href=%s>%s</a><br>" % (link, t)
    # # html += "</body></html>"
    # # output = BeautifulSoup(html, "lxml")    #htmlstring -> BeautifulSoup 객체
    # # prettyHtml = str(output.prettify())     #html 줄 예쁘게
    # #
    # # with open("cellsOfYumi.html", mode="w", encoding="utf-8") as f:
    # #     f.write(prettyHtml)