import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def wine(num):

	wineimg = None
	for wineType in range(3):
		#print(wineType)
		if wineType == 2:
			print('No wine type found.')
			pyautogui.screenshot('wineimg'+str(wineType)+'.png', region=(480,840,400,1))
			print('New wine saved as wineimg'+str(wineType)+'.png')
			print('Exiting.')
			sys.exit()
		wineimg = pyautogui.locateOnScreen('wineimg' + str(wineType) + '.png', region=recipe_region, grayscale=True)
		if wineimg:
			break

	for windex in range(wineType):
		pyautogui.press('w')

	for windex in range(27):
		pyautogui.press('up')
		
	pyautogui.press('enter')
	return
