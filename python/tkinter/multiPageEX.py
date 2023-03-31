
import tkinter as tk
from tkinter import messagebox

# 主页，可以选择鼠标生成或者随机生成
class Page_start:
    def __init__(self,window) -> None:
        self.window = window
        self.window.title("最近点对")
        self.btnMouseGen = tk.Button(self.window,text="鼠标画点",command=self.mousePage)
        self.btnMouseGen.pack()
        self.btnRandomGen= tk.Button(self.window,text="随机生成",command=self.randomPage)
        self.btnRandomGen.pack()
    
    # 切换到鼠标生成点页面
    def mousePage(self):
        self.btnRandomGen.destroy()
        self.btnMouseGen.destroy()
        Page_mouse(root)

    # 切换到随机生成点页面
    def randomPage(self):
        self.btnRandomGen.destroy()
        self.btnMouseGen.destroy()
        Page_random(root)

# 鼠标生成点页面
class Page_mouse:
    def __init__(self,window) -> None:
        self.window = window
        self.window.title("鼠标点击")

        # 画布ui
        self.w = tk.Canvas(root,width=400,height=200,background='white')
        self.w.pack()
        self.w.bind('<Button-1>',self.paintPoint)

        # 按钮部分ui
        self.btnBack = tk.Button(self.window,text="返回主页",command=self.returnP1)
        self.btnBack.pack()
        self.btnForce = tk.Button(self.window,text="暴力算法",command=self.forceCal)
        self.btnForce.pack()
        self.btnFast = tk.Button(self.window,text="nlgn算法",command=self.nlgnCal)
        self.btnFast.pack()

        # 私有变量  
        self.pointList = []     # 生成的点对列表
        self.time = 0       # 算法用时

    # 返回主页
    def returnP1(self):
        self.btnBack.destroy()
        self.w.destroy()
        self.btnFast.destroy()
        self.btnForce.destroy()
        Page_start(root)

    # 在鼠标点击处画点
    def paintPoint(self,event):
        x1,y1 = (event.x-1),(event.y-1)
        x2,y2 = (event.x+1),(event.y+1)
        self.pointList.append((event.x,event.y))
        self.w.create_oval(x1,y1,x2,y2,fill='red')

    # 暴力求解    
    def forceCal(self):
        text = self.pointList
        text = "最近点对是\n用时："+str(self.time)+"ms!"
        messagebox.showinfo("暴力算法",text)

    # nlgn求解
    def nlgnCal(self):
        text = self.pointList
        text = "最近点对是：" + str(self.pointList)+"\n用时："+str(self.time)+"ms!"
        messagebox.showinfo("nlgn算法",text)

# 随机生成点页面，可以输入生成点数
class Page_random:
    def __init__(self,window) -> None:
        self.window = window
        self.window.title("随机生成")
        # 输入生成点数部分ui
        self.label1 = tk.Label(text="请输入1~1000000的数字，表示生成点数：")
        self.label1.pack()
        self.entry1 = tk.Entry()
        self.entry1.pack()
        # 按钮部分ui
        self.btnBack = tk.Button(self.window,text="返回主页",command=self.returnP1)
        self.btnBack.pack()
        self.btnGenPoint = tk.Button(self.window,text="生成点对",command=self.genPoint)
        self.btnGenPoint.pack()
        self.btnForce = tk.Button(self.window,text="暴力求解",command=self.forceCal)
        self.btnForce.pack()
        self.btnFast = tk.Button(self.window,text="nlgn算法",command=self.nlgnCal)
        self.btnFast.pack()
        # 私有变量
        self.pointNum = 0     # 生成点数
        self.ifInput = False    # 是否生成点数
        self.pointList = []     # 生成的点对列表
        self.points = [(0,0),(1,1)]    # 最近点对
        self.time = 0    # 算法用时

    # 返回主页    
    def returnP1(self):
        self.btnBack.destroy()
        self.label1.destroy()
        self.entry1.destroy()
        self.btnFast.destroy()
        self.btnForce.destroy()
        self.btnGenPoint.destroy()
        Page_start(root)

    # 生成随机点
    def genPoint(self):
        # 输入为空的处理
        if self.entry1.get() == "":
            messagebox.showinfo("警告","请输入生成点数！")
            return
        self.pointNum = int(self.entry1.get())

        text = "成功生成"+str(self.pointNum)+"个点！"
        self.ifInput = True
        messagebox.showinfo("成功",text)
        return

    # 暴力算法
    def forceCal(self):
        # 输入为空的处理
        if not self.ifInput:
            messagebox.showinfo("警告","请先生成随机点！")
            return
        text ="最近点对是："+ str(self.points)+"\n耗时："+str(self.time)+"ms!"
        messagebox.showinfo("暴力算法",text)

    # nlgn 算法
    def nlgnCal(self):
        # 输入为空的处理
        if not self.ifInput:
            messagebox.showinfo("警告","请先生成随机点！")
            return
        text ="最近点对是："+ str(self.points)+"\n耗时："+str(self.time)+"ms!"
        messagebox.showinfo("nlgn算法",text)
    
root = tk.Tk()
p1=Page_start(root)
root.mainloop()

