# 從國際處網站爬蟲交換學校資料
import urllib.request as req
url = "https://oia.ntu.edu.tw/ch/outgoing/school.list/country_sn/0"  # 國際處出國交換學校一覽表的網頁
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
urls = root.find_all("td", class_="_decoration")

for url in urls:
    url = "https://oia.ntu.edu.tw"+url.a["href"]  # 各個學校的申請資料網頁
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    school_name = root.find("h1")  # 校名
    titles = root.find_all("th")  # 申請資料項目：申請資格、名額、學校年曆、註冊繳費、注意事項、住宿資訊
    infos = root.find_all("td")  # 申請資料項目的內容
    print("\n")
    print(school_name.text)  # 印出校名
    for i in range(len(titles)):  # 印出各個申請資料項目及對應的內容
        if i != 0:
            print(titles[i].text, infos[i+len(infos)-len(titles)].text.strip())
        else:
            print(titles[i].text, infos[i].text.strip())
