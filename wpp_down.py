import requests
import bs4 as bs
import re
import urllib.request


url = "https://unsplash.com/wallpaper/1065396/desktop-wallpapers"

resp = requests.get(url)

soup = bs.BeautifulSoup(resp.content, "html.parser")

l = soup.find_all(href=re.compile(".*download\?force=true"))

links = []
for tag in l:
    links.append(tag['href'])

for i in range(0, len(links)):
    name = "wpp" + str(i) + ".jpeg"
    urllib.request.urlretrieve(links[i], name)


    
