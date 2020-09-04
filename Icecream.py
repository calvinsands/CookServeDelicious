import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def icecream(num):
	icecreamimg = None
	while True:
		for icecreamType in range(7):
			if icecreamType == 6:
				break
			icecreamimg = pyautogui.locateOnScreen('icecreamimg' + str(icecreamType) + '.png', region=recipe_region, grayscale=True)
			if icecreamimg:
				break
		
		if icecreamType == 0:
			print('Plain Vanilla')
			pyautogui.press('v')
			pyautogui.press('v')
			pyautogui.press('v')
			break

		elif icecreamType == 1:
			print('Plain Chocolate')
			pyautogui.press('c')
			pyautogui.press('c')
			pyautogui.press('c')
			break

		elif icecreamType == 2:
			print('Vanilla and Chocolate')
			pyautogui.press('v')
			pyautogui.press('c')
			break

		elif icecreamType == 3:
			print('The Yin and Yang')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('h')
			pyautogui.press('p')
			break

		elif icecreamType == 4:
			print('Cherry Vanilla')
			pyautogui.press('v')
			pyautogui.press('v')
			pyautogui.press('h')
			break

		elif icecreamType == 5:
			print('Chocolate Sprinkles')
			pyautogui.press('c')
			pyautogui.press('c')
			pyautogui.press('p')
			break

		else:
			print('No ice cream found')


	pyautogui.press('enter')
	return
