#coding: utf-8
import pyautogui
import tkinter as tk
from tkinter.constants import *
pyautogui.FAILSAFE = True #設置開啟pyautogui的例外輸出

window = tk.Tk()
window.title('Instagram自動按讚By YangNianen')
window.geometry('400x300') #視窗大小
var = tk.StringVar()
focus = False
def start():
    i=0
    count=0
    global focus
    if focus == False:
        focus = True
        
        try:
            pyautogui.size()

            width, height = pyautogui.size()

            print("你目前的螢幕解析度:",width,height)
            
            while(count<100):
                love = pyautogui.locateOnScreen('love.png')
                
                if(love!=None):
                    Xp, Yp = pyautogui.center(love)
                    i = i+1
                    print('找到第',i,'個讚')
                    var.set('找到第',i,'個讚')
                    pyautogui.click(Xp,Yp,button='left')
                    pyautogui.PAUSE = 0.5
                    pyautogui.press('pagedown')
                    pyautogui.PAUSE = 0.5
                else:
                    print('沒有找到讚!')
                    pyautogui.PAUSE = 0.5
                    pyautogui.press('pagedown')
                    pyautogui.PAUSE = 0.5
                    

    

        except:
            print('總共按了',i,'個讚')
def end():
    global count
    count = 100
    window.mainloop()#啟用或更新Windows介面

startbutton = tk.Button(window,
                  text='開始',
                  width=15,height=2,
                  command=start)
startbutton.pack()

countlabel = tk.Label(window,
                    textvariable=var,
                    width=15,height=2)
countlabel.pack()

endbutton = tk.Button(window,
                  text='結束',
                  width=15,height=2,
                  command=end)
endbutton.pack()

window.mainloop()#啟用或更新Windows介面
