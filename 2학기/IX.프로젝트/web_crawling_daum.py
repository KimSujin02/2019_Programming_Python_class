import json

from bs4 import BeautifulSoup       #html 구조적으로 변환하기
from urllib.request import urlopen  #url에 해당하는 html 가져오기

if __name__ == '__main__':
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read())
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        thumnail = cartoon_title["thumbnailImage"]["url"]
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/" + str(url)
        html += "<a href='{}'><img src='{}' />{}</a>".format(url, thumnail, title)
    html += "</body></html>"

    output = BeautifulSoup(html, "lxml")    #htmlstring -> BeautifulSoup 객체
    prettyHtml = str(output.prettify())     #html 줄 예쁘게
    with open("취향저격그녀.html", mode="w", encoding="utf-8") as f:
        f.write(prettyHtml)

    # cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title">
    # html = "<html><head><meta charset='utf-8'></head><body>"
    # for title in cartoon_titles:
    #     t = title.find('a').text            #제목
    #     link = "http://comic.naver.com/" + title.find('a').get('href')  #링크
    #     html += "<a href=%s>%s</a><br>" % (link, t)
    # html += "</body></html>"
    # output = BeautifulSoup(html, "lxml")    #htmlstring -> BeautifulSoup 객체
    # prettyHtml = str(output.prettify())     #html 줄 예쁘게
    #
    # with open("cellsOfYumi.html", mode="w", encoding="utf-8") as f:
    #     f.write(prettyHtml)