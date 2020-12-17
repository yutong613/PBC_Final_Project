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
    qualifications = root.find("h3")
    titles = root.find_all("th")
    infos = root.find_all("td")
    print(school_name.text)
    print(len(titles))
    print(len(infos))
    print(titles[0].text)
    print(qualifications.text)
    for i in range(1, len(infos)):
    #for title in titles:
        print(titles[i].text)
    #for info in infos:
        print("index:", i, infos[i].text)
