import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def fish(num):
	print('Fishy.')
	
	fishimg = None
	while True:
		for fishType in range(3):
			if fishType == 2:
				break
			fishimg = pyautogui.locateOnScreen('fishimg' + str(fishType) + '.png', region=recipe_region, grayscale=True)
			if fishimg:
				break
		
		if fishimg:
			break
		if fishType == 2:
			print('No fish found')
		
	
	food[num-1] = 'fish'

	pyautogui.press('left')
	pyautogui.press('down')
	pyautogui.press('right')
	pyautogui.press('s')
	if fishType == 1:
		pyautogui.press('l')
	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return