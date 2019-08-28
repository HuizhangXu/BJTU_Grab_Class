#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter
import info
import qiangke
import time

root = tkinter.Tk()
# 进入消息循环
root.title('BJTU选课软件 别依赖这个软件抢课')
root.geometry('600x550')
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True


frm = tkinter.Frame(root)



frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1, text='学号:', font=('Arial', 15)).pack(side=tkinter.LEFT)

var1 = tkinter.StringVar()
e1 = tkinter.Entry(frm_1, textvariable = var1)
var1.set("19114059")
e1.pack(side=tkinter.RIGHT)

frm_1.pack(side=tkinter.TOP)
#2
frm_2 = tkinter.Frame(frm)
tkinter.Label(frm_2, text='密码:', font=('Arial', 15)).pack(side=tkinter.LEFT)
var2 = tkinter.StringVar()
e2 = tkinter.Entry(frm_2, textvariable = var2)
var2.set("请输入你的密码")
e2.pack(side=tkinter.RIGHT)

frm_2.pack(side=tkinter.TOP)

#3
frm_3 = tkinter.Frame(frm)
tkinter.Label(frm_3, text='最多重复:', font=('Arial', 15)).pack(side=tkinter.LEFT)
var3 = tkinter.StringVar()
e3 = tkinter.Entry(frm_3, textvariable = var3)
var3.set("3000")
e3.pack(side=tkinter.LEFT)
tkinter.Label(frm_3, text='次停止', font=('Arial', 15)).pack(side=tkinter.LEFT)
frm_3.pack(side=tkinter.TOP)

#3—2
frm_3_2 = tkinter.Frame(frm)
tkinter.Label(frm_3_2, text='每次重复间隔:', font=('Arial', 15)).pack(side=tkinter.LEFT)
var3_2 = tkinter.StringVar()
e3_2 = tkinter.Entry(frm_3_2, textvariable = var3_2)
var3_2.set("2")
e3_2.pack(side=tkinter.LEFT)
tkinter.Label(frm_3_2, text='秒', font=('Arial', 15)).pack(side=tkinter.LEFT)
frm_3_2.pack(side=tkinter.TOP)


#4
frm_4 = tkinter.Frame(frm)
tkinter.Label(frm_4, text='课程value值:', font=('Arial', 15)).pack(side=tkinter.LEFT)
var4 = tkinter.StringVar()
e4 = tkinter.Entry(frm_4, textvariable = var4)
var4.set("26090")#城市交通分析与设计'26090'
e4.pack(side=tkinter.LEFT)
tkinter.Label(frm_4, text='(不是课程编号！目前得从浏览器源代码查看)', font=('Arial', 15)).pack(side=tkinter.LEFT)
frm_4.pack(side=tkinter.TOP)


frm.pack()

t = tkinter.Text()
t.pack()

def run():
    user = e1.get()
    #t.insert(tkinter.END, 'user:' + user+'\n')
    password = e2.get()
    #t.insert(tkinter.END,'password:' + password+'\n')
    times = e3.get()
    #t.insert(tkinter.END, 'time:' + time3 + '\n')
    coursevalue = e4.get()
    #t.insert(tkinter.END, 'coursevalue:' + coursevalue + '\n')
    times =  int(times)
    #更改用户名和密码
    interval = e3_2.get()
    interval = int(interval)
    im = info.PersonalInfo()
    im.set_info(user,password)
    #设置选课字典
    dict1 = {'checkbox':coursevalue}


    for i in range(times):
        str = qiangke.qiang(dict1)
        t.insert(tkinter.END, '第%i次结果:' % (i + 1) + str + '\n')
        t.update()
        if str == '验证码错误！':
            t.insert(tkinter.END, '验证码识别失败，让我再试一次' + '\n' + '\n')
            t.update()
            time.sleep(interval)
        elif str == '课程重复！':
            t.insert(tkinter.END, '最终结果：这课程都重复了，你都自己选好了还让我帮你选？！'+ '\n' + '\n')
            t.update()
            break
        elif str == '选课成功！':
            t.insert(tkinter.END, '接种结果：成功啦~快去瞅一眼有没有选上！' + '\n' + '\n')
            t.update()
            break

        if i == times-1:
            t.insert(tkinter.END, '已经结束了貌似还是没有选成功，你多设置点次数好不好' + '\n' + '\n')
            t.update()

    #dic2 = t.get()
def clear():
    t.delete(1.0, tkinter.END)



frm5 = tkinter.Frame(root)
tkinter.Button(frm5, text="开始", command = run).pack(side=tkinter.LEFT)
tkinter.Button(frm5, text="清空", command = clear).pack()
frm5.pack(side=tkinter.BOTTOM)


root.mainloop()