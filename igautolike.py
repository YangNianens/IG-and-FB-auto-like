#coding: utf-8
import pyautogui
import time

i=0
count=0

try:
            pyautogui.size()

            width, height = pyautogui.size()
            print("Powered by YangNianen  #2018/10/19 IG自動按讚 for MEGA2.0低調分享")
            print("--------------使用教學-------------")
            print("1.開啟本程式後五秒內切換到IG網頁便會開始按讚")
            print("2.欲停止按讚請直接將滑鼠移動至左上角一秒後便會停止並於五秒後自動關閉")
            print("你目前的螢幕解析度:",width,'x',height)
            print("五秒後開始按讚，請立即切換至IG網頁")
            time.sleep(5)
            while(count<100):
                love = pyautogui.locateOnScreen('love.png')
                count
                if(love!=None):
                    Xp, Yp = pyautogui.center(love)
                    i = i+1
                    print('找到第',i,'個讚')
                    pyautogui.moveTo(Xp, Yp, 0.3, pyautogui.easeInOutQuad)
                    pyautogui.click(Xp,Yp,button='left')
                    pyautogui.PAUSE = 0.5
                    pyautogui.scroll(-1200)
                    #pyautogui.press('pagedown')
                    pyautogui.PAUSE = 0.5
                else:
                    print('沒有找到讚!')
                    pyautogui.PAUSE = 0.5
                    #pyautogui.press('pagedown')
                    pyautogui.scroll(-1200)
                    pyautogui.PAUSE = 0.5
                    

    

except:
            print('總共按了',i,'個讚，五秒後關閉視窗')
            time.sleep(5)


