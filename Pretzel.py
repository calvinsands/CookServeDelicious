import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def pretzel(num):

	pretzelimg = None
	for pretzelType in range(7):
		if pretzelType == 6:
			print('No pretzel type found.')
			pyautogui.screenshot('pretzelimg'+str(pretzelType)+'.png', region=recipe_region)
			print('New pretzel saved as pretzelimg'+str(pretzelType)+'.png')
			print('Exiting.')
			sys.exit()
		pretzelimg = pyautogui.locateOnScreen('pretzelimg' + str(pretzelType) + '.png', region=recipe_region, grayscale=True)
		if pretzelimg:
			break

	while True:
		
		if pretzelType == 0:
			print('Saltyboi')
			pyautogui.press('s')
			break

		elif pretzelType == 1:
			print('YOU GET NOTHING.')
			break

		elif pretzelType == 2:
			print('Saltybutteryboi')
			pyautogui.press('s')
			pyautogui.press('b')
			break

		elif pretzelType == 3:
			print('My Buttery Curves')
			pyautogui.press('b')
			break

		elif pretzelType == 4:
			print('Cinneboi')
			pyautogui.press('c')
			break

		elif pretzelType == 5:
			print('Slipperycinneboi')
			pyautogui.press('b')
			pyautogui.press('c')
			break
	
	pyautogui.press('enter')
	return