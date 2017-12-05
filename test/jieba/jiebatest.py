#!/usr/bin/env python
#coding:utf-8
import os,sys,shutil
import subprocess
import pyautogui
import pyperclip

reload(sys)
sys.setdefaultencoding( "utf-8" )

print(pyautogui.size())

# pyautogui.moveTo(147,49,duration=0.5)
pyautogui.click(147,49)
pyautogui.click(147,49)
pyperclip.copy("fenglishuai")
pree=pyautogui.hotkey('command', 'v')
pyautogui.moveTo(185,144,duration=0.5)
pyautogui.click(185,144)
pyautogui.click(185,144)
pyautogui.click(728,496)
pyautogui.click(408,564)
pyperclip.copy("你干嘛呢")
pree=pyautogui.hotkey('command', 'v')
pyautogui.hotkey('return')

# pyautogui.typewrite('曾宪明')
# pyautogui.hotkey('return')
# pyautogui.click(386,562)
# pyautogui.typewrite('自动测试')
# pyautogui.hotkey('return')


# print(pyautogui.position())

# pyautogui.dragTo(288,503,duration=0.5)

# pree=pyautogui.hotkey('command', 'c')

# # pyautogui.moveTo(594,48,duration=0.5)
# pyautogui.click(594,48)

# pyautogui.click(261,146)


# pree=pyautogui.hotkey('return', 'v')














