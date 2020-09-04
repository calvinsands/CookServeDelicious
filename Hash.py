import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def hash(num):

	hashimg = None
	for hashType in range(3):
		if hashType == 2:
			print('No hash type found.')
			pyautogui.screenshot('hashimg'+str(hashType)+'.png', region=recipe_region)
			print('New hash saved as hashimg'+str(hashType)+'.png')
			print('Exiting.')
			sys.exit()
		hashimg = pyautogui.locateOnScreen('hashimg' + str(hashType) + '.png', region=recipe_region, grayscale=True)
		if hashimg:
			break

	pyautogui.keyDown('down')
	time.sleep(1.9)
	pyautogui.keyUp('down')
	pyautogui.press('p')
	
	while True:
		
		if hashType == 0:
			print('SALTY')
			pyautogui.press('s')
			break

		elif hashType == 1:
			print('YOU GET NOTHING.')
			break
	
	pyautogui.press('enter')
	return