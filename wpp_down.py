import requests
import bs4 as bs
import re
import urllib.request
import shutil
import os

dir_name = "downloads"

if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

os.mkdir(dir_name)

url = "https://unsplash.com/t/wallpapers"

resp = requests.get(url)

soup = bs.BeautifulSoup(resp.content, "html.parser")

l = soup.find_all(href=re.compile(".*download\?force=true"))

links = []
for tag in l:
    links.append(tag['href'])

for i in range(0, len(links)):
    name = "downloads/wpp" + str(i) + ".jpeg"
    urllib.request.urlretrieve(links[i], name)


    
