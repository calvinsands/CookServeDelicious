import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def beer(num):

	"""
	beerimg = None
	for beerType in range(3):
		#print(beerType)
		if beerType == 2:
			print('No beer type found.')
			pyautogui.screenshot('beerimg'+str(beerType)+'.png', region=(480,840,400,1))
			print('New beer saved as beerimg'+str(beerType)+'.png')
			print('Exiting.')
			sys.exit()
		beerimg = pyautogui.locateOnScreen('beerimg' + str(beerType) + '.png', region=recipe_region, grayscale=True)
		if beerimg:
			break
	"""
	pyautogui.PAUSE = 0.0
	
	print('Beer me.')
	
	pyautogui.keyDown('down')
	time.sleep(1.43)
	pyautogui.keyUp('down')
	
	pyautogui.PAUSE = 0.075
	
	pyautogui.press('enter')
	return
