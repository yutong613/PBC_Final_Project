import urllib.request as req
url = "https://oia.ntu.edu.tw/ch/outgoing/school.list/country_sn/0"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
urls = root.find_all("td", class_="_decoration")

for url in urls:
    url = "https://oia.ntu.edu.tw"+url.a["href"]
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    school_name = root.find("h1")
    titles = root.find_all("th")
    infos = root.find_all("td")
    print("\n")
    print(school_name.text)
    for i in range(len(titles)):
        if i != 0:
            print(titles[i].text, infos[i+len(infos)-len(titles)].text.strip())
        else:
            print(titles[i].text, infos[i].text.strip())
