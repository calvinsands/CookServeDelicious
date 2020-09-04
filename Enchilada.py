import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def enchilada(num):
	enchiladaimg = None
	while True:
		for enchiladaType in range(10):
			if enchiladaType == 9:
				break
			enchiladaimg = pyautogui.locateOnScreen('enchiladaimg' + str(enchiladaType) + '.png', region=recipe_region, grayscale=True)
			if enchiladaimg:
				break
		
		
		if enchiladaType == 0:
			print('Junior Stack')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			break

		elif enchiladaType == 1:
			print('Double Stack')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			break

		elif enchiladaType == 2:
			print('Triple w/Egg')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('e')
			break

		elif enchiladaType == 3:
			print('Triple Stack')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			break

		elif enchiladaType == 4:
			print('Triple w/Onion')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif enchiladaType == 5:
			print('Triple Works')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		elif enchiladaType == 6:
			print('Junior w/Onion')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif enchiladaType == 7:
			print('Double Onion')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif enchiladaType == 8:
			print('Double Works')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('down')
			pyautogui.press('up')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		else:
			print('No enchilada found')


	pyautogui.press('enter')
	return