'''
Created on 2017年9月27日

@author: Mi
'''
from tkinter import *
import regeditor

def click(root,opt):
    regeditor.set(opt)
    root.withdraw()

def UI_proxy():    
    top = Tk()
    top.geometry("300x200+100+100")
    B_on = Button(top,text = 'On',command=lambda: click(top,'On'),width = 10, height = 2)
    B_on.place(x=30,y=66)
    B_off = Button(top, text="Off", command=lambda:click(top,'Off'),width = 10, height = 2)
    B_off.place(x=172, y=66)
    # 进入消息循环
    top.mainloop()

if __name__ == '__main__':
    UI_proxy()

