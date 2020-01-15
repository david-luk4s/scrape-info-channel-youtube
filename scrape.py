import requests
from bs4 import BeautifulSoup

def scrape(link):
    data = []
    link = link + '/videos'
    r = requests.get(link)
    s = BeautifulSoup(r.text, 'lxml')

    for i in s.find_all('h3', class_='yt-lockup-title')[:3]:
        title = i.a.attrs['title']
        v_link = 'https://www.youtube.com/' + i.a.attrs['href']
        data.append([title, v_link])
    
    return data

link = 'https://www.youtube.com/user/schafer5'
data = scrape(link)
print(data)