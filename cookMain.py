import pyautogui, time, sys
import WhichTask

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

from constants import onOne_dimension
from constants import onTwo_dimension
from constants import onThree_dimension
from constants import onFour_dimension
from constants import onFive_dimension
from constants import onSix_dimension
from constants import onSeven_dimension
from constants import onEight_dimension

orderDict = {
	0: onOne_dimension,
	1: onTwo_dimension,
	2: onThree_dimension,
	3: onFour_dimension,
	4: onFive_dimension,
	5: onSix_dimension,
	6: onSeven_dimension,
	7: onEight_dimension
}

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


"""
for i in range(3):
	print(3-i)
	time.sleep(1)
"""
input("Press Enter to run...")
print('Go!')
comeback = pyautogui.position()
pyautogui.click((800,5))
#pyautogui.moveTo(comeback)

######### main ############

while True:
	print('Awaiting new orders', end="")
	for index in range(MAX_ORDERS):
		if food[index] != None:
			print(', ' + food[index] + ' on ' + str(index+1), end="")
	print('')

	for mainIndex in range(MAX_ORDERS):
		number = None
		number = pyautogui.locateOnScreen('on'+str(mainIndex+1)+'.png', region=(orderDict[mainIndex]), grayscale=True)
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
			elif food[mainIndex] == 'steak':
				if float(time.time()) - clock[mainIndex] >= 17.5:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'potato':
				if float(time.time()) - clock[mainIndex] >= 8:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'pasta':
				if float(time.time()) - clock[mainIndex] >= 11:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'pancake':
				if float(time.time()) - clock[mainIndex] >= 6.8:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'kabob':
				if float(time.time()) - clock[mainIndex] > 6.65:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'lobster':
				if float(time.time()) - clock[mainIndex] > 11.5:
					pyautogui.press(str(mainIndex+1))
					WhichTask.whichTask(mainIndex+1)
			elif food[mainIndex] == 'rice':
				if float(time.time()) - clock[mainIndex] >= 6.2:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'biscuit':
				if float(time.time()) - clock[mainIndex] >= 7.25:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None
			elif food[mainIndex] == 'bananas':
				if float(time.time()) - clock[mainIndex] >= 6.7:
					pyautogui.press(str(mainIndex+1))
					food[mainIndex] = None