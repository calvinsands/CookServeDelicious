import pyautogui, time, sys
import WhichTask

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder



pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True



#global center_region
#global recipe_region

#global MAX_ORDERS
#global clock
#global food
#global foodOrder


for i in range(3):
	print(3-i)
	time.sleep(1)
print('Go!')

######### main ############

while True:
	print('Awaiting new orders', end="")
	for index in range(MAX_ORDERS):
		if food[index] != None:
			print(', ' + food[index] + ' on ' + str(index+1), end="")
	print('')

	for mainIndex in range(MAX_ORDERS):
		number = None
		number = pyautogui.locateCenterOnScreen('on'+str(mainIndex+1)+'.png', region=(70,130,80,500), grayscale=True)
		if number:
			if food[mainIndex] == None:
				pyautogui.press(str(mainIndex+1))
				WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'hamburger':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'soup':
				if float(time.time()) - clock[mainIndex] >= 11:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'lasagna':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'chicken':
				if float(time.time()) - clock[mainIndex] > 15:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'fish':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'pizza':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'nachos':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
