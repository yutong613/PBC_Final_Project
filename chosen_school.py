import urllib.request as req
import ssl
import bs4

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://oia.ntu.edu.tw/ch/outgoing/school.list/country_sn/0"  # 國際處出國交換學校一覽表的網頁

with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
urls = root.find_all("td", class_="_decoration")        

all_school = []  # 總資料庫
 
for url in urls:
    url = "https://oia.ntu.edu.tw"+url.a["href"]  # 各個學校的申請資料網頁
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    school_name = root.find("h1")  # 校名
    titles = root.find_all("th")  # 申請資料項目：申請資格、名額、學校年曆、註冊繳費、注意事項、住宿資訊
    infos = root.find_all("td")  # 申請資料項目的內容
    select = infos[0].text.strip()
   
    qualify = select.split("組")  # 以組分類
    qualify.pop(0)
  
    for r in range(len(qualify)):  # 將申請資格以學校裡面的跑
        information = []  # 每個學校的組都會有一筆資料（如果學校有兩個組，那麼以此學校為開頭的資料將有兩筆）
        information.append(school_name.text)  # 資料的第一項為學校名稱
        if qualify[r].find("本校") != -1:  # 年級前的關鍵字為學校
            grade = qualify[r][qualify[r].find("本校")+2:qualify[r].find("本校")+4]
        else:  # 如果沒有學校限制則預設為0
            grade = 0
            
        if grade == "大二":  # 將國字轉為數字
            grade = 2
        elif grade == "大一":
            grade = 1
        elif grade == "大三":
            grade = 3
        # if grade == "大四":
        #     grade = 4
        # if grade == "大五":
        #     grade = 5
        elif grade == "碩一":
            grade = 6
        elif grade == "碩二":
            grade = 7
        # if grade == "碩三":
        #     grade = 8
        elif grade == "博一":
            grade = 9
        elif grade == "博二":
            grade = 10
        # if grade == "博三":  怕程式太慢所以先格式化
        #     grade = 11
        # if grade == "博四":
        #     grade = 12
        # if grade == "博五":
        #     grade = 13
        # if grade == "博六":
        #     grade = 14
        information.append(grade)  # 將第二項年級加入資料
    
        if qualify[r].find("GPA")!= -1:  # GPA為關鍵字
            record = qualify[r].find("GPA")
            GPA = float(qualify[r][(record + 5):(record + 9)])
        else:
            GPA = 0
        information.append(GPA)  # 把第三項GPA的分數加入資料
        
        if qualify[r].find("TOEFL iBT")!= -1:  # TOEFL iBT為關鍵字
            TOEFL = int(qualify[r][qualify[r].find("TOEFL iBT")+10:qualify[r].find("TOEFL iBT")+12])
        else:
            TOEFL = 0
        information.append(TOEFL)  # 將第四項托福成績加入資料
        
        
        if qualify[r].find("IELTS")!= -1:  # IELTS為關鍵字
            IELTS = float(qualify[r][qualify[r].find("IELTS")+6:qualify[r].find("IELTS")+9])
        else:
            IELTS = 0 
        information.append(IELTS)  # 將第五項IELTS成績加入資料
        
        if qualify[r].find("全民英檢")!= -1:  # 此為全民英檢的分級
            if qualify[r].find("全民英檢中級")!= -1:  # 中級為1，中高級為2，高級為3
                e_test = 1
            elif qualify[r].find("全民英檢中高級")!= -1:
                e_test = 2
            elif qualify[r].find("全民英檢高級")!= -1:
                e_test = 3
        else:
            e_test = 0
        information.append(e_test)  # 將第六項全民英檢量化加入資料
        
        if qualify[r].find("日文檢定") != -1:  # 日文檢定為關鍵字
            japan = int(qualify[r][qualify[r].find("日文檢定")+7])*(-1)  # 因為日文為數字越低越高級，故乘以-1，方便以後比較大小
        else:
            japan = 0
        information.append(japan)  # 將第七項日文檢定成績加入
        
        if qualify[r].find("韓語檢定") != -1:  # 韓語檢定為關鍵字
            korea = int(qualify[r][qualify[r].find("韓語檢定")+14])
        else:
            korea = 0
        information.append(korea)  # 將第八項韓語檢定量化加入資料
        
        if qualify[r].find("法語檢定") != -1:  # 法語檢定為關鍵字
            france = qualify[r][qualify[r].find("法語檢定")+7:qualify[r].find("法語檢定")+9]
            if france == "B1":  # 分級由大到小為A1,A2,B1,B2,C1,C2，量化從1~6
                france = 3
            elif france == "B2":
                france = 4
            elif france == "A1":
                france = 1
            elif france == "A2":
                france = 2
            elif france == "C1":
                france = 5 
            elif france == "C2":
                france = 6 
        else:
            france = 0
        information.append(france)  # 將第九項法語檢定量化加入資料
        
        if qualify[r].find("德語檢定") != -1:  # 德語檢定為關鍵字
            germeny = qualify[r][qualify[r].find("德語檢定")+7:qualify[r].find("德語檢定")+9]
            if germeny == "B1":  # 分級由大到小為A1,A2,B1,B2,C1,C2，量化從1~6
               germeny = 3
            elif germeny == "B2":
               germeny = 4
            elif germeny == "A1":
               germeny = 1
            elif germeny == "A2":
               germeny = 2
            elif germeny == "C1":
               germeny = 5
            elif germeny == "C2":
               germeny = 6    
        else:
            germeny = 0  
        information.append(germeny)  #  將第十項法語檢定量化加入資料
        
        all_school.append(information)  # 將各個學校的資料加入總資料庫內

    # for i in range(len(titles)):  # 印出各個申請資料項目及對應的內容
    #     if i != 0:
            
    #         print(titles[i].text, infos[i+len(infos)-len(titles)].text.strip())
    #         print("\n")
    #     else:
    #         print(titles[i].text, infos[i].text.strip())

#先將資料按照1.學校名稱 2.年級 3.GPA 4.TOEFL 5.IELTS 6.英檢 7.日檢 8.韓檢 9.法檢 10.德檢 排列

# 篩選資料
you = input().split(",")  # 假設輸入資料為一串用逗號分開的字串（輸入的資料只有九項，不用輸入學校名稱）

for i in range(len(you)):
    you[i] = float(you[i])  # 將數值浮點數化

okay = []  # 有達到標準的學校

all_school.pop(161)  # 因為今年不招收學生

for a in range(len(all_school)):  # 將所有學校有小於輸入資格的都挑選出來
    if (you[0] >= all_school[a][1]) and (you[1] >= all_school[a][2]):  # 先比年級跟GPA
        compare = 0
        for b in range(3,10):  # 語文檢定目前看到都是擇一就行
            if you[b-1] >= float(all_school[a][b]):
                compare += 1
        if compare != 0:  # 如果輸入資料都大於此學校的話
            okay.append(all_school[a])  # 就加入有達到標準的學校內

print(okay)









