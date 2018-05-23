import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def soup(num):
	global food
	global clock
	
	soupimg = None
	for soupType in range(2):
		#print(soupType)
		soupimg = pyautogui.locateOnScreen('soupimg' + str(soupType) + '.png', region=recipe_region, grayscale=True)
		if soupimg:
			break
		if soupType == 1:
			print('No soup type found')
			return

	food[num-1] = 'soup'
	while True:
		
		if soupType == 0:
			pyautogui.press('k')
			pyautogui.press('w')
			pyautogui.press('u')
			pyautogui.press('space')
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		elif soupType == 1:
			pyautogui.press('w')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('space')
			pyautogui.press('t')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('a')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		else:
			print('No soup found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return