import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def bananas(num):
	

	food[num-1] = 'bananas'
	while True:

		bananasimg = None
		for bananasType in range(2):
			if bananasType == 1:
				break
			bananasimg = pyautogui.locateOnScreen('bananasimg' + str(bananasType) + '.png', region=recipe_region, grayscale=True)
			if bananasimg:
				break
		
		if bananasType == 0:
			print('Bananas Foster')
			pyautogui.press('b')
			pyautogui.press('s')
			time.sleep(2.1)
			pyautogui.press('a')
			break

		else:
			print('No bananas found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return