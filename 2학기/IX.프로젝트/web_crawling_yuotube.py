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