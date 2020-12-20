import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk
# import tkMessageBox
class ExchangeStd (tk.Frame):
    shouldReset = True
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.variable1.trace("w", self.callback)
    def callback(self, *args):
        test = self.variable1.get()
        tof = ["<70", "70-79", "80-89", "90-99", ">=100"]
        iel = ["<6.0", "6.0-7.0", ">7.0"]
        gept = ["全民英檢中級", "全民英檢中高級", "全民英檢高級"]
        fra = ["A1", "A2", "B1", "B2", "C1", "C2"]
        deu = ["A1", "A2", "B1", "B2", "C1", "C2"]
        if test == "TOEFL iBT":
            self.variable1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.variable1, *tof)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=8, column=3)
        if test == "IELTS":
            self.variable1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.variable1, *iel)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=8, column=3)
        if test == "全民英檢":
            self.variable1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.variable1, *gept)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=8, column=3)
        if test == "法語檢定":
            self.variable1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.variable1, *fra)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=8, column=3)
        if test == "德語檢定":
            self.variable1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.variable1, *deu)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=8, column=3)
    def select(self, *args):
        country = self.var.get()
        print(self.var.get())
        asia = ["香港", "以色列", "日本", "南韓", "澳門", "大陸地區", "馬來西亞", "蒙古", "俄羅斯", "泰國", "新加坡"]
        europe = ["土耳其", "奧地利", "比利時", "捷克", "丹麥", "法國", "德國", "義大利", "匈牙利", "冰島", "拉脫維亞", "立陶宛", "荷蘭", "葡萄牙", "盧森堡", "挪威", "芬蘭", "波蘭", "斯洛維尼亞", "西班牙", "瑞典", "瑞士", "英國"]
        america_N = ["加拿大", "美國"]
        america_S = ["巴西", "智利", "墨西哥"]
        ocean = ["澳大利亞", "紐西蘭"]
        african = ["南非"]
        if country == "1":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *asia)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
        if country == "2":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *europe)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
        if country == "3":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *america_N)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
        if country == "4":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *america_S)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
        if country == "5":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *african)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
        if country == "6":
            self.var1 = tk.StringVar(self)
            self.toefl = tk.OptionMenu(self, self.var1, *ocean)
            self.toefl.config(width=10, font=('Helvetica', 12))
            self.toefl.grid(row=3, column=3)
    def createWidgets(self):
        college = ["文", "理", "社科", "醫", "工", "生農", "管理", "公衛", "電資", "法", "生命科學"]
        language = ["TOEFL iBT", "IELTS", "全民英檢", "日文檢定", "韓語檢定", "法語檢定", "德語檢定"]
        imgname = Image.open("Desktop/h.png")
        imgname = imgname.resize((50,50), Image.ANTIALIAS)
        f1 = tkFont.Font(family="Lucida Grande", size=30)
        self.image1 = ImageTk.PhotoImage(imgname)
        self.pic = tk.Label(self, image=self.image1)
        self.label = tk.Label(self, text="台大交換生看過來!!", bg="red", font=f1)

        self.label2 = tk.Label(self, text="洲別：", bg="pink")
        self.label4 = tk.Label(self, text="語言檢定：", bg="pink")
        self.label5 = tk.Label(self, text="GPA：", bg="pink")
        self.label6 = tk.Label(self, text="你是什麼學院：", bg="pink")
        self.button = tk.Button(self, text = "Search", bg="yellow", command=self.clickBtn)

        self.txtNum_GPA = tk.Text(self, height=1, bg="white")
        self.var = tk.IntVar(self)
        self.checkNum1 = tk.Checkbutton(self, text="亞洲", variable=self.var, offvalue=0, onvalue=1, height=1, width=10, bg="pink", command=self.select)
        self.checkNum2 = tk.Checkbutton(self, text="歐洲", variable=self.var, offvalue=0, onvalue=2, height=1, width=10, bg="pink", command=self.select)
        self.checkNum3 = tk.Checkbutton(self, text="北美洲", variable=self.var, offvalue=0, onvalue=3, height=1, width=10, bg="pink", command=self.select)
        self.checkNum4 = tk.Checkbutton(self, text="中南美洲", variable=self.var, offvalue=0, onvalue=4, height=1, width=10, bg="pink", command=self.select)
        self.checkNum5 = tk.Checkbutton(self, text="非洲", variable=self.var, offvalue=0, onvalue=5, height=1, width=10, bg="pink", command=self.select)
        self.checkNum6 = tk.Checkbutton(self, text="大洋洲", variable=self.var, offvalue=0, onvalue=6, height=1, width=10, bg="pink", command=self.select)
        self.variable = tk.StringVar(self)
        self.variable.set(college[0])
        self.opt = tk.OptionMenu(self, self.variable, *college)
        self.opt.config(width=10, font=('Helvetica', 12))
        self.opt.grid(row=10, column=1)
        self.variable1 = tk.StringVar(self)
        self.variable1.set(language[0])
        self.lang = tk.OptionMenu(self, self.variable1, *language, command=self.callback)
        
        self.lang.config(width=10, font=('Helvetica', 12))
        self.lang.grid(row=8, column=1)

    
        self.pic.grid(row=0, column=0)
        self.label.grid(row=0, column=1, columnspan=6, sticky="NW"+"SE")

        self.label2.grid(row=2, column=0, sticky="E")
        self.label4.grid(row=8, column=0, sticky="E")
        self.label5.grid(row=9, column=0, sticky="E")
        self.label6.grid(row=10, column=0, sticky="E")
        self.button.grid(row=11, column=6)
        self.txtNum_GPA.grid(row=9, column=1,columnspan=5, sticky="NW")
        self.checkNum1.grid(row=2, column=1, sticky="NW"+"SE")
        self.checkNum2.grid(row=3, column=1, sticky="NW"+"SE")
        self.checkNum3.grid(row=4, column=1, sticky="NW"+"SE")
        self.checkNum4.grid(row=5, column=1, sticky="NW"+"SE")
        self.checkNum5.grid(row=6, column=1, sticky="NW"+"SE")
        self.checkNum6.grid(row=7, column=1, sticky="NW"+"SE")
        # self.college.grid(row=6, column=1, columnspan=2, sticky="NW"+"SE")
        # self.lang.grid(row=4, column=1, columnspan=2, sticky="NW"+"SE")
    # def setNumStr(self, content):
    #     if self.shouldReset == True:
    #         self.txtNum.delete("1.0", tk.END)
    #         self.txtNum.insert("1.0", content)
    #     else:
    #         self.txtNum.insert("1.0", content)

    def clickBtn(self):
        self.variable1.get()
    #     # self.checkNum1.cget()
    #     # self.checkNum2.cget()
    #     # self.checkNum3.cget()
    #     # self.checkNum4.cget()
    #     # self.checkNum5.cget()
    #     # self.checkNum6.cget()
    #     self.college.get()

    # self.variable1.trace("w", callback)    

exstd = ExchangeStd()
# exstd.geometry("200x400")
exstd.configure(bg="pink")
exstd.master.title("台大交換生看過來")
exstd.mainloop()