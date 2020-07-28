import pyautogui
#printing the current mouse position
print(pyautogui.position())
def common():
    pyautogui.click(21,1057)
    pyautogui.sleep(2)
    pyautogui.typewrite('google chorme')
    pyautogui.sleep(2)
    pyautogui.click(263,503)
    pyautogui.sleep(2)
    pyautogui.click(367,55)
    pyautogui.sleep(2)


#facebook login
common()
pyautogui.typewrite('https://www.facebook.com/')
pyautogui.click(1132,151)
pyautogui.typewrite(name)
pyautogui.click(1265,146)
pyautogui.typewrite(password)
pyautogui.click(1418,147)

#youtube
common()
pyautogui.typewrite('https://www.youtube.com/')
pyautogui.sleep(2)
pyautogui.typewrite(['enter'])
pyautogui.sleep(5)

#email
common()
pyautogui.typewrite('https://www.gmail.com/')
pyautogui.doubleClick(999,542)
pyautogui.typewrite(['backspace'])
pyautogui.typewrite(email_id)
pyautogui.typewrite(['enter'])
pyautogui.click(1095,727)
pyautogui.doubleClick(999,542)
pyautogui.typewrite(['backspace'])
pyautogui.typewrite(email_pass)
pyautogui.typewrite(['enter'])

#twitter
common()
pyautogui.typewrite('https://www.gmail.com/')
pyautogui.doubleClick(1201,516)
pyautogui.typewrite(['backspace'])
pyautogui.typewrite(twitter_id)
pyautogui.typewrite(['enter'])
pyautogui.click(1530,610)
pyautogui.typewrite(['backspace'])
pyautogui.typewrite(twitter_pass)
pyautogui.typewrite(['enter'])


