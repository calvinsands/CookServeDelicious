import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def lasagna(num):
	global food
	global clock

	lasagnaimg = None
	for lasagnaType in range(2):
		#print(lasagnaType)
		lasagnaimg = pyautogui.locateOnScreen('lasagnaimg' + str(lasagnaType) + '.png', region=recipe_region, grayscale=True)
		if lasagnaimg:
			break
		if lasagnaType == 1:
			print('No lasagna type found')
			return

	food[num-1] = 'lasagna'

	while True:
		
		if lasagnaType == 0:
			for lasindex in range(3):
				pyautogui.press('p')
				pyautogui.press('s')
				pyautogui.press('c')
				pyautogui.press('r')
			break

		if lasagnaType == 1:
			for lasindex in range(2):
				pyautogui.press('p')
				pyautogui.press('s')
				pyautogui.press('m')
				pyautogui.press('c')
				pyautogui.press('r')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('c')
			pyautogui.press('r')
			break
	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return