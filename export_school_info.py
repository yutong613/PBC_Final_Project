import urllib.request as req
import ssl
import bs4
import re
import csv

# 抓取國際處交換學校一覽表的原始網頁
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://oia.ntu.edu.tw/ch/outgoing/school.list/country_sn/0"  # 國際處出國交換學校一覽表的網址
with req.urlopen(url) as response:  # 讀取
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")

countries = root.find_all("option")
country_list = []
for i in range(1, len(countries)):
    country_list.append(countries[i].text)

# 建立一個country_dict涵蓋所有學校對應的國家
country_dict = {}
country_dict1 = dict.fromkeys(["聖保羅大學", "里約熱內盧天主教大學", "坎皮納斯州立大學"], "巴西")
country_dict.update(country_dict1)
country_dict2 = dict.fromkeys(["魁北克大學蒙特婁分校", "愛德華王子島大學", "蒙特婁大學", "拉法爾大學", "女王大學", "滑鐵盧大學", "西門菲沙大學", "渥太華大學", "多倫多大學", "維多利亞大學", "加拿大英屬哥倫比亞大學"], "加拿大")
country_dict.update(country_dict2)
country_dict3 = dict.fromkeys(["智利天主教大學"], "智利")
country_dict.update(country_dict3)
country_dict4 = dict.fromkeys(["蒙特雷科技大學", "墨西哥國立自治大學"], "墨西哥")
country_dict.update(country_dict4)
country_dict5 = dict.fromkeys(["斯克蘭頓大學", "北卡羅來納大學格林斯伯勒分校", "奧瑞岡州立大學", "匹茲堡大學", "康乃狄克大學", "喬治梅森大學", "新澤西州立羅格斯大學", "南卡羅來納大學", "伊利諾大學香檳分校", "北卡羅來納大學教堂山分校", "威斯康辛大學麥迪遜分校", "天普大學", "猶他大學", "夏威夷太平洋大學", "夏威夷大學希羅分校", "紐約州立大學", "亞利桑那州立大學", "伊利諾大學芝加哥分校", "馬里蘭大學", "奧瑞岡大學", "北卡羅來納州立大學", "夏威夷大學瑪諾亞分校", "喬治亞大學", "奧克拉荷瑪大學", "加州州立大學", "華盛頓大學", "加州大學", "加州大學戴維斯分校", "夏威夷大學希羅分校", "奧瑞岡大學", "夏威夷大學瑪諾亞分校"], "美國")
country_dict.update(country_dict5)
country_dict6 = dict.fromkeys(["香港恒生大學", "嶺南大學", "香港大學", "香港理工大學", "香港城市大學", "香港中文大學"], "香港")
country_dict.update(country_dict6)
country_dict7 = dict.fromkeys(["以色列理工學院"], "以色列")
country_dict.update(country_dict7)
country_dict8 = dict.fromkeys(["兵庫縣立大學", "近畿大學", "秋田大學", "一橋大學", "廣島大學", "名古屋外國語大學", "日本大學", "立命館大學", "關西學院大學", "長崎大學", "東京工業大學", "橫濱國立大學", "金澤大學", "神奈川大學", "青山學院大學", "同志社大學", "上智大學", "大阪大學", "名古屋大學", "神戶大學", "岡山大學", "筑波大學", "東京大學", "國際教養大學", "北海道大學", "京都大學", "關西大學", "琉球大學", "東京學藝大學", "九州大學", "慶應義塾大學", "東北大學", "御茶水女子大學", "東京外國語大學", "明治大學", "早稻田大學", "創價大學"], "日本")
country_dict.update(country_dict8)
country_dict9 = dict.fromkeys(["韓國科學技術院", "延世大學", "高麗大學", "國立釜山大學", "成均館大學", "漢陽大學", "梨花女子大學", "順天國立大學", "浦項工科大學", "首爾國立大學"], "南韓")
country_dict.update(country_dict9)
country_dict10 = dict.fromkeys(["澳門大學"], "澳門")
country_dict.update(country_dict10)
country_dict11 = dict.fromkeys(["武漢理工大學", "北京航空航天大學", "華中科技大學", "貴州大學", "東南大學", "四川大學", "天津大學", "蘭州大學", "北京師範大學", "武漢大學", "內蒙古大學", "重慶大學", "西安交通大學", "哈爾濱工業大學", "大連理工大學", "廈門大學", "上海交通大學", "山東大學", "南京大學", "清華大學", "浙江大學", "中國科學技術大學", "復旦大學", "北京大學", "中國人民大學", "吉林大學", "南開大學"], "大陸地區")
country_dict.update(country_dict11)
country_dict12 = dict.fromkeys(["馬來西亞諾丁漢大學", "拉曼大學", "馬來亞大學", "馬來西亞理工大學", "馬來西亞理科大學"], "馬來西亞")
country_dict.update(country_dict12)
country_dict13 = dict.fromkeys(["蒙古國立大學"], "蒙古")
country_dict.update(country_dict13)
country_dict14 = dict.fromkeys(["聖彼得堡國立大學", "莫斯科國立大學"], "俄羅斯")
country_dict.update(country_dict14)
country_dict15 = dict.fromkeys(["耶魯", "新加坡科技與設計大學", "新加坡管理大學", "南洋理工大學", "新加坡國立大學"], "新加坡")
country_dict.update(country_dict15)
country_dict16 = dict.fromkeys(["馬希竇大學", "國立法政大學", "朱拉隆功大學", "亞洲理工學院"], "泰國")
country_dict.update(country_dict16)
country_dict17 = dict.fromkeys(["薩邦哲大學", "海峽大學", "畢爾肯大學", "中東科技大學", "柯克大學"], "土耳其")
country_dict.update(country_dict17)
country_dict18 = dict.fromkeys(["維也納大學", "林茲大學"], "奧地利")
country_dict.update(country_dict18)
country_dict19 = dict.fromkeys(["托馬斯莫爾應用科技大學", "布魯塞爾自由大學"], "比利時")
country_dict.update(country_dict19)
country_dict20 = dict.fromkeys(["查理士大學", "馬薩里克大學"], "捷克")
country_dict.update(country_dict20)
country_dict21 = dict.fromkeys(["奧胡斯大學", "哥本哈根大學"], "丹麥")
country_dict.update(country_dict21)
country_dict22 = dict.fromkeys(["拉瑞爾應用科技大學", "赫爾辛基大學"], "芬蘭")
country_dict.update(country_dict22)
country_dict23 = dict.fromkeys(["波爾多大學", "奧爾良大學", "南巴黎大學", "巴黎高等農業學院", "巴黎高等礦業學院", "雷恩第一大學", "巴黎第十三大學", "巴黎西大學農泰爾拉德芳斯", "巴黎薩克雷高等師範學校", "巴黎中央理工學院", "里爾天主教大學", "法國女性高等綜合理工學院", "特魯瓦科技大學", "索邦大學", "巴黎高等政治學院", "尚慕蘭里昂第三大學", "科諾伯勒阿爾卑斯大學"], "法國")
country_dict.update(country_dict23)
country_dict24 = dict.fromkeys(["明斯特大學", "達姆施塔特工業大學", "康斯坦茨大學", "柏林洪堡大學", "斯圖加特大學", "弗萊堡大學", "柏林工業大學", "魯耳波洪大學", "慕尼黑大學", "曼漢姆大學", "漢堡大學", "亞亨工業大學", "慕尼黑工業大學", "杜賓根大學", "烏爾姆大學", "波昂大學", "卡爾斯魯爾理工學院", "艾朗根紐倫堡大學", "多特蒙德工業大學", "海德堡大學", "柏林自由大學"], "德國")
country_dict.update(country_dict24)
country_dict25 = dict.fromkeys(["羅蘭大學", "布達佩斯考文紐斯大學", "布達佩斯科技經濟大學"], "匈牙利")
country_dict.update(country_dict25)
country_dict26 = dict.fromkeys(["冰島大學"], "冰島")
country_dict.update(country_dict26)
country_dict27 = dict.fromkeys(["聖心天主教大學", "波隆納大學"], "義大利")
country_dict.update(country_dict27)
country_dict28 = dict.fromkeys(["拉脫維亞大學"], "拉脫維亞")
country_dict.update(country_dict28)
country_dict29 = dict.fromkeys(["考納斯理工大學", "維爾紐斯大學"], "立陶宛")
country_dict.update(country_dict29)
country_dict30 = dict.fromkeys(["盧森堡大學"], "盧森堡")
country_dict.update(country_dict30)
country_dict31 = dict.fromkeys(["奈梅亨大學", "阿姆斯特丹自由大學", "馬斯垂克大學", "葛洛寧恩大學", "烏特列茲大學", "萊頓大學"], "荷蘭")
country_dict.update(country_dict31)
country_dict32 = dict.fromkeys(["奧斯陸大學"], "挪威")
country_dict.update(country_dict32)
country_dict33 = dict.fromkeys(["華沙理工大學", "華沙大學"], "波蘭")
country_dict.update(country_dict33)
country_dict34 = dict.fromkeys(["波爾圖大學"], "葡萄牙")
country_dict.update(country_dict34)
country_dict35 = dict.fromkeys(["盧比安納大學"], "斯洛維尼亞")
country_dict.update(country_dict35)
country_dict36 = dict.fromkeys(["巴塞隆納大學", "薩拉曼卡大學", "馬德里大學", "聖地牙哥", "龐貝法布拉大學", "馬德里自治大學", "巴塞隆納自治大學", "馬德里技術大學"], "西班牙")
country_dict.update(country_dict36)
country_dict37 = dict.fromkeys(["林雪平大學", "皇家理工學院", "烏普薩拉大學", "優密歐大學", "斯德哥爾摩大學", "隆德大學"], "瑞典")
country_dict.update(country_dict37)
country_dict38 = dict.fromkeys(["蘇黎世大學", "洛桑大學", "伯恩大學", "聖加倫大學"], "瑞士")
country_dict.update(country_dict38)
country_dict39 = dict.fromkeys(["伯明罕大學", "諾丁漢大學", "倫敦大學瑪麗王后學院", "肯特大學", "愛丁堡大學", "薩塞克斯大學", "曼徹斯特大學", "南安普頓大學"], "英國")
country_dict.update(country_dict39)
country_dict40 = dict.fromkeys(["阿德雷德大學", "雪梨大學", "蒙納許大學", "昆士蘭大學", "格里菲斯大學", "汀肯大學", "新南威爾斯大學", "馬奎里大學", "澳洲國立大學", "墨爾本大學"], "澳大利亞")
country_dict.update(country_dict40)
country_dict41 = dict.fromkeys(["坎特伯雷大學", "威靈頓維多利亞大學", "奧克蘭大學"], "紐西蘭")
country_dict.update(country_dict41)
country_dict42 = dict.fromkeys(["開普敦大學", "斯泰倫博斯大學"], "南非")
country_dict.update(country_dict42)

all_school = []  # 總資料庫

# 尋找所有class="_decoration"的 td 標籤
urls = root.find_all("td", class_="_decoration")        

# 解析原始碼，取得每間學校的網址，並進入該網址取得詳細資料
for url in urls:
    url = "https://oia.ntu.edu.tw"+url.a["href"]  # 各個學校的申請資料的網址
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")

    school_name = root.find("h1")  # 尋找校名的標籤
    titles = root.find_all("th")  # 尋找申請資料項目的標籤：申請資格、名額、學校年曆、註冊繳費、注意事項、住宿資訊
    infos = root.find_all("td")  # 尋找申請資料項目的內容的標籤
    select = infos[0].text.strip()
   
    qualify = select.split("組")  # 以組分類
    qualify.pop(0)
  
    for r in range(len(qualify)):  # 將申請資格以學校裡面的組跑
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
        
        pattern="[\u4e00-\u9fa5]+"  # 編碼
        regex = re.compile(pattern)
        school_name_chinese = regex.findall(school_name.text)  # 只取中文
        country = country_dict.get(school_name_chinese[0])
        information.append(country)  # 將國家加入各個學校的第十一項
        
        all_school.append(information)  # 將各個學校的資料加入總資料庫內

with open('all_school.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['學校名稱', '年級', 'GPA', 'TOEFL', '雅思', '全民英檢', '日文檢定', '韓文檢定', '法文檢定', '德文檢定', '國家'])
    writer.writerows(all_school)

    # for i in range(len(titles)):  # 印出各個申請資料項目及對應的內容
    #     if i != 0:
            
    #         print(titles[i].text, infos[i+len(infos)-len(titles)].text.strip())
    #         print("\n")
    #     else:
    #         print(titles[i].text, infos[i].text.strip())

#先將資料按照1.學校名稱 2.年級 3.GPA 4.TOEFL 5.IELTS 6.英檢 7.日檢 8.韓檢 9.法檢 10.德檢 排列

# # 篩選資料
# you = input().split(",")  # 假設輸入資料為一串用逗號分開的字串（輸入的資料只有九項，不用輸入學校名稱）

# for i in range(len(you)):
#     you[i] = float(you[i])  # 將數值浮點數化

# okay = []  # 有達到標準的學校

# all_school.pop(161)  # 因為今年不招收學生

# for a in range(len(all_school)):  # 將所有學校有小於輸入資格的都挑選出來
#     if (you[0] >= all_school[a][1]) and (you[1] >= all_school[a][2]):  # 先比年級跟GPA
#         compare = 0
#         for b in range(3,10):  # 語文檢定目前看到都是擇一就行
#             if you[b-1] >= float(all_school[a][b]):
#                 compare += 1
#         if compare != 0:  # 如果輸入資料都大於此學校的話
#             okay.append(all_school[a])  # 就加入有達到標準的學校內

# print(okay)
print(all_school)
