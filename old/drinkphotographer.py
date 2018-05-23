import pyautogui, time

for i in range(3):
    time.sleep(1)
    print(3-i)

print('Go.')
for i in range(18):
    print(i)
    pyautogui.screenshot('friesimg'+str(i)+'.png', region=(480,840,400,1))
    time.sleep(.5)
    pyautogui.press('ctrlleft')
    time.sleep(.5)
print('done')
