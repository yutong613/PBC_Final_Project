import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk  # 圖片
class ExchangeStd (tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master=exs, bg="#E0FFFF")
        self.grid()
        self.createWidgets()
        self.variable1.trace("w", self.callback)
    def callback(self, *args):
        test = self.variable1.get()
        jpn = ["N1", "N2", "N3", "N4", "N5"]
        kor = ["1級", "2級", "3級", "4級", "5級", "6級"]
        iel = ["<6.0", "6.0", "6.5", "7.0", ">=7.5"]
        gept = ["全民英檢中級", "全民英檢中高級", "全民英檢高級"]
        fra = ["A1", "A2", "B1", "B2", "C1", "C2"]
        deu = ["A1", "A2", "B1", "B2", "C1", "C2"]
        if test == "日文檢定":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *jpn)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "韓語檢定":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *kor)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "TOEFL iBT":
            self.variables = tk.StringVar(self)
            self.test = tk.Text(self, height=1, width=20, bg="white")
            self.test.config(width=13, height= 1, font=('Malgun Gothic', 12))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "IELTS":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *iel)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "全民英檢":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *gept)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "法語檢定":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *fra)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
        if test == "德語檢定":
            self.variables = tk.StringVar(self)
            self.test = tk.OptionMenu(self, self.variables, *deu)
            self.test.config(width=11, font=('Malgun Gothic', 10))
            self.test.grid(row=10, column=3, sticky="W")
    def select(self, *args):
        country = self.var1.get()
        asia = ["香港", "以色列", "日本", "南韓", "澳門", "大陸地區", "馬來西亞", "蒙古", "俄羅斯", "泰國", "新加坡", "土耳其"]
        europeW = ["奧地利", "比利時",  "法國", "德國", "荷蘭", "盧森堡", "瑞士", "英國"]
        europeS = ["義大利", "西班牙", "葡萄牙"]
        europeE = ["拉脫維亞", "立陶宛", "波蘭", "斯洛維尼亞", "捷克", "匈牙利",]
        europeN = ["丹麥","冰島", "挪威", "芬蘭", "瑞典"]
        america = ["加拿大", "美國", "巴西", "智利", "墨西哥"]
        other = ["澳大利亞", "紐西蘭", "南非"]
        if country == 1:
            self.var = tk.StringVar(self)
            self.choice = tk.OptionMenu(self, self.var, *asia)
            self.choice.config(width=8, font=('Malgun Gothic', 12))
            self.choice.grid(row=4, column=3)
        if country == 2:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *europeW)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
        if country == 3:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *europeS)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
        if country == 4:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *europeE)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
        if country == 5:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *europeN)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
        if country == 6:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *america)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
        if country == 7:
            self.var = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var, *other)
            self.toefl.config(width=8, font=('Malgun Gothic', 12))
            self.toefl.grid(row=4, column=3)
    def addingC(self):
        want = self.var.get()
        self.LB.insert("end", want)
    def deleteC(self):
        sel = self.LB.curselection()
        for index in sel[::-1]:
            self.LB.delete(index)
    def addingL(self):
        want = self.variable1.get()
        if want != "TOEFL iBT":
            want1 = self.variables.get()
        else:
            want1 = self.test.get("1.0", tk.END)
        t = want + "," + want1
        self.LB1.insert("end", t)
    def deleteL(self):
        sel = self.LB1.curselection()
        for index in sel[::-1]:
            self.LB1.delete(index)
    def createWidgets(self):
        grade = ["大二", "大三", "大四", "大五", "碩一", "碩二", "碩三", "博一", "博二", "博三", "博四", "博五", "博六"] 
        language = ["TOEFL iBT", "IELTS", "全民英檢", "日文檢定", "韓語檢定", "法語檢定", "德語檢定"]
        imgname = Image.open("Desktop/e.png")  # 圖片
        country_img = Image.open("Desktop/a.png")  # 圖片
        language_img = Image.open("Desktop/d.png")  # 圖片
        GPA_img = Image.open("Desktop/c.png")  # 圖片
        grade_img = Image.open("Desktop/b.png")  # 圖片
        imgname = imgname.resize((50,50), Image.ANTIALIAS)  # 圖片
        country_img = country_img.resize((40,40), Image.ANTIALIAS)  # 圖片
        language_img = language_img.resize((40,40), Image.ANTIALIAS)  # 圖片
        GPA_img = GPA_img.resize((40,40), Image.ANTIALIAS)  # 圖片
        grade_img = grade_img.resize((40,40), Image.ANTIALIAS)  # 圖片
        f1 = tkFont.Font(family="微軟正黑體", size=24)
        f2 = tkFont.Font(family="微軟正黑體", size=18)
        f3 = tkFont.Font(family="Malgun Gothic", size=18)
        f4 = tkFont.Font(family="Malgun Gothic", size=14)
        self.image = ImageTk.PhotoImage(imgname)  # 圖片
        self.image1 = ImageTk.PhotoImage(country_img)  # 圖片
        self.image2 = ImageTk.PhotoImage(language_img)  # 圖片
        self.image3 = ImageTk.PhotoImage(GPA_img)  # 圖片
        self.image4 = ImageTk.PhotoImage(grade_img)  # 圖片
        self.pic = tk.Label(self, image=self.image, bg="#E0FFFF")  # 圖片
        self.picA = tk.Label(self, image=self.image, bg="#E0FFFF")  # 圖片
        self.pic1 = tk.Label(self, image=self.image1, bg="#E0FFFF")  # 圖片
        self.pic2 = tk.Label(self, image=self.image2, bg="#E0FFFF")  # 圖片
        self.pic3 = tk.Label(self, image=self.image3, bg="#E0FFFF")  # 圖片
        self.pic4 = tk.Label(self, image=self.image4, bg="#E0FFFF")  # 圖片
        self.label = tk.Label(self, text="台大交換生看過來", font=f1, bg="#E0FFFF")
        self.label2 = tk.Label(self, text="國家：", bg="#E0FFFF", font=f2)
        self.label4 = tk.Label(self, text="語言檢定：", bg="#E0FFFF", font=f2)
        self.label5 = tk.Label(self, text="GPA：", bg="#E0FFFF", font=f3)
        self.label6 = tk.Label(self, text="已選國家", bg="#E0FFFF", font=f3)
        self.label7 = tk.Label(self, text="已選語檢", bg="#E0FFFF", font=f3)
        self.label8 = tk.Label(self, text="年級：", bg="#E0FFFF", font=f3)
        self.button = tk.Button(self, text = "Search", bg="white", activebackground="yellow", command=self.clickBtn, font=f3)
        self.LB1 = tk.Listbox(self)
        self.LB_ad1 = tk.Button(self, text="+", width=3, activebackground="yellow", command=self.addingL, font=f4)
        self.LB_de1 = tk.Button(self, text="-", width=3, activebackground="yellow", command=self.deleteL, font=f4)
        self.LB = tk.Listbox(self)
        self.LB_ad = tk.Button(self, text="+", width=3, activebackground="yellow", command=self.addingC, font=f4)
        self.LB_de = tk.Button(self, text="-", width=3, activebackground="yellow", command=self.deleteC, font=f4)
        self.txtNum_GPA = tk.Text(self, height=1, width=5, bg="white", font=f2)
        self.var1 = tk.IntVar(self)
        self.checkNum1 = tk.Checkbutton(self, text="亞洲", variable=self.var1, offvalue=0, onvalue=1, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum2 = tk.Checkbutton(self, text="西歐", variable=self.var1, offvalue=0, onvalue=2, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum3 = tk.Checkbutton(self, text="南歐", variable=self.var1, offvalue=0, onvalue=3, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum4 = tk.Checkbutton(self, text="東歐", variable=self.var1, offvalue=0, onvalue=4, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum5 = tk.Checkbutton(self, text="北歐", variable=self.var1, offvalue=0, onvalue=5, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum6 = tk.Checkbutton(self, text="美洲", variable=self.var1, offvalue=0, onvalue=6, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.checkNum7 = tk.Checkbutton(self, text="其他", variable=self.var1, offvalue=0, onvalue=7, height=1, width=5, bg="#E0FFFF", command=self.select, font=f2)
        self.variable1 = tk.StringVar(self)
        self.lang = tk.OptionMenu(self, self.variable1, *language, command=self.callback)
        self.lang.config(width=8, font=('Malgun Gothic', 12))
        self.lang.grid(row=10, column=2, sticky="W")
        self.variable2 = tk.StringVar(self)
        self.gra = tk.OptionMenu(self, self.variable2, *grade)
        self.gra.config(width=8, font=('Malgun Gothic', 12))
        self.gra.grid(row=12, column=2, sticky="W")
        self.pic.grid(row=0, column=14, sticky="W")  # 圖片
        self.picA.grid(row=0, column=2, sticky="W")  # 圖片
        self.pic1.grid(row=1, column=0, sticky="E", padx=30)  # 圖片
        self.pic2.grid(row=10, column=0, sticky="E", padx=30)  # 圖片
        self.pic3.grid(row=11, column=0, sticky="E", padx=30)  # 圖片
        self.pic4.grid(row=12, column=0, sticky="E", padx=30)  # 圖片
        self.LB.grid(row=2, column=13, columnspan=3, rowspan=3, sticky="E")
        self.LB1.grid(row=10, column=13, columnspan=3, rowspan=2, sticky="E")
        self.label.grid(row=0, column=2, columnspan=13,pady=20)
        self.label2.grid(row=1, column=1, sticky="E", padx=10)
        self.label4.grid(row=10, column=1, sticky="E", padx=10)
        self.label5.grid(row=11, column=1, sticky="E", padx=10)
        self.label6.grid(row=1, column=13, pady=5, sticky="E", padx=10)
        self.label7.grid(row=9, column=13, pady=5, sticky="E", padx=10)
        self.label8.grid(row=12, column=1, pady=5, sticky="E", padx=10)
        self.button.grid(row=14, padx=20, pady=20, column=3, sticky="W")
        self.LB_ad1.grid(row=10, padx=5, column=16, sticky="W"+"S")
        self.LB_de1.grid(row=11, padx=5, column=16, sticky="W")
        self.LB_ad.grid(row=2, padx=5, pady=10, column=16, sticky="W")
        self.LB_de.grid(row=3, padx=5, pady=10, column=16, sticky="W")
        self.txtNum_GPA.grid(row=11, column=2, columnspan=1, sticky="W")
        self.checkNum1.grid(row=1, column=3, padx=10, pady=1, sticky="W")
        self.checkNum2.grid(row=2, column=2, padx=10, pady=1, sticky="W")
        self.checkNum3.grid(row=3, column=2, padx=10, pady=1, sticky="W")
        self.checkNum4.grid(row=4, column=2, padx=10, pady=1, sticky="W")
        self.checkNum5.grid(row=1, column=2, padx=10, pady=1, sticky="W")
        self.checkNum6.grid(row=2, column=3, padx=10, pady=1, sticky="W")
        self.checkNum7.grid(row=3, column=3, padx=10, pady=1, sticky="W")
    def clickBtn(self):
        level_dict = {"A1":1, "A2":2, "B1":3, "B2":4, "C1":5, "C2":6, "N1":-1, "N2":-2, "N3":-3, "N4":-4, "N5":-5, "1級":1, "2級":2, "3級":3, "4級":4, "5級":5, "6級":6, "<6.0":5.9, "6.0":6.0, "6.5":6.5, "7.0":7.0, ">=7.5":7.5, "全民英檢中高級":2, "全民英檢中級":1, "全民英檢高級":3}
        grade_dict = {"大二":2, "大三":3, "大四":4, "大五":5, "碩一":6, "碩二":7, "碩三":8, "博一":9, "博二":10, "博三":11, "博四":12, "博五":13, "博六":14}
        gradevalue = self.variable2.get()
        GPA = self.txtNum_GPA.get("1.0", tk.END)
        valueidx = list(self.LB.get(0, "end"))
        valueidx1 = list(self.LB1.get(0, "end"))
        new = []
        new_grade = grade_dict[gradevalue]
        for i in valueidx1:
            x = i.split(",")
            new.append(x)
        for j in new:
            level = str(j[1])
            if level in level_dict:
                num = level_dict[level]
                j[1] = num
            else:
                j[1] = int(j[1].strip("\n"))

exs = tk.Tk()
exs.geometry("900x900")  # 視窗大小
exs.resizable(0, 0)
exstd = ExchangeStd()
exstd.pack_propagate(0)
exstd.pack(fill=tk.BOTH, expand=1) 
exstd.master.title("台大交換生看過來")
exstd.mainloop()