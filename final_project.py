import urllib.request as req
url = "https://oia.ntu.edu.tw/ch/outgoing/view/sn/1115"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
school_name = root.find("h1")
titles = root.find_all("th")
infos = root.find_all("td")
print(school_name.text)
for title in titles:
    print(title.text)
for info in infos:
    print(info.text)
