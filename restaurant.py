# coding=utf8

import random
import Tkinter
from Tkinter import *
import tkMessageBox
import time


def restaurant():
        r = random.randint(0,11)
        t = random.randint(0,3)
        selections = [u"紫荆",u"桃李",u"玉树",u"芝兰",u"清芬",u"听涛",u"万人",u"荷园",u"闻馨",u"丁香",u"寓园",u"澜园"]
        #selections = [u"吐司",u"汉堡",u"次坞打面",u"兰州拉面",u"河南烩面",u"自己煮面",u"麻辣烫",u"面疙瘩",u"黄焖鸡",u"骨头饭",u"青椒肉丝盖饭",u"牛肉炒饭",u"下馆子"]
        cheers = ["GO GO GO ",u"走起！",u"赶紧的，到饭点了",u"别忘了请杜逸康吃饭"]
        if selections[r]:
                tkMessageBox.showinfo(u"餐厅选择",u"目标："+selections[r]+"\n"+cheers[t])


root=Tk()
root.title(u'妈妈再也不用担心我在清华吃什么')

time_string = time.strftime('%H:%M:%S')
myvar=Tkinter.Label(root, text = u"现在时间: "+time_string, compound = Tkinter.CENTER,fg="blue")
myvar.pack()
#myvar.place(relx=0, rely=0, relwidth=1, relheight=1)

f = Frame(root, height=300, width=300)
f.pack_propagate(0) # don't shrink
f.pack()

b= Button(root, text=u"点击随机选择",command=restaurant)
b.place(relx=0.5, rely=0.5, anchor=CENTER)
#b.pack()  
        
root.mainloop()

        
#if __name__ == '__main__':
    #random_restaurant()
    
