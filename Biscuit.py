import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def biscuit(num):
	

	food[num-1] = 'biscuit'
	while True:

		biscuitimg = None
		for biscuitType in range(7):
			if bscuitType == 6:
				break
			biscuitimg = pyautogui.locateOnScreen('biscuitimg' + str(biscuitType) + '.png', region=recipe_region, grayscale=True)
			if biscuitimg:
				break
		
		if biscuitType == 0:
			print('Egg Biscuit')
			pyautogui.press('e')
			break

		elif biscuitType == 1:
			print('The Deluxe')
			pyautogui.press('s')
			pyautogui.press('e')
			break

		elif biscuitType == 2:
			print('Double AM')
			pyautogui.press('s')
			pyautogui.press('e')
			pyautogui.press('b')
			break

		elif biscuitType == 3:
			print('Morning Fuel')
			pyautogui.press('s')
			pyautogui.press('b')
			break

		elif biscuitType == 4:
			print('Sunrise Sandwich')
			pyautogui.press('s')
			break

		elif biscuitType == 5:
			print('The Classic')
			pyautogui.press('e')
			pyautogui.press('b')
			break

		else:
			print('No biscuit found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	time.sleep(0.5)
	return