import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def corndog(num):
	print('Corndog found')
	dogType = None

	while True:
		dogType = pyautogui.locateOnScreen('corndogimg0.png', region=recipe_region, grayscale=True)
		if dogType:
			print('Classic: ketchup, mustard.')
			pyautogui.press('k')
			pyautogui.press('m')
			pyautogui.press('enter')
			return

		dogType = pyautogui.locateOnScreen('corndogimg1.png', region=recipe_region, grayscale=True)
		if dogType:
			print('Yellow: mustard.')
			pyautogui.press('m')
			pyautogui.press('enter')
			return

		dogType = pyautogui.locateOnScreen('corndogimg2.png', region=recipe_region, grayscale=True)
		if dogType:
			print('Red: ketchup.')
			pyautogui.press('k')
			pyautogui.press('enter')
			return

		dogType = pyautogui.locateOnScreen('corndogimg3.png', region=recipe_region, grayscale=True)
		if dogType:
			print('Red: ketchup.')
			pyautogui.press('k')
			pyautogui.press('enter')
			return

		print('No corndog type found.')
