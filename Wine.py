import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def wine(num):

	wineimg = None
	for wineType in range(6):
		#print(wineType)
		if wineType == 5:
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

	for windex in range(29):
		pyautogui.press('up')
		
	pyautogui.press('enter')
	return
