import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def salad(num):
	saladimg = None
	while True:
		for saladType in range(12):
			#print(saladType)
			saladimg = pyautogui.locateOnScreen('saladimg' + str(saladType) + '.png', region=recipe_region, grayscale=True)
			if saladimg:
				break
			if saladType == 17:
				print('No salad type found')
				return
		
		if saladType == 0:
			print('House Salad')
			pyautogui.press('r')
			pyautogui.press('c')
			pyautogui.press('b')
			break

		elif saladType == 1:
			print('Cheesy Leaves')
			pyautogui.press('r')
			pyautogui.press('c')
			break

		elif saladType == 2:
			print('Pepper Ranch')
			pyautogui.press('r')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif saladType == 3:
			print('The Dry Greens')
			pyautogui.press('g')
			break

		elif saladType == 4:
			print('The Dry Deluxe')
			pyautogui.press('m')
			pyautogui.press('g')
			break

		elif saladType == 5:
			print('Kids Delight')
			pyautogui.press('r')
			pyautogui.press('c')
			break

		elif saladType == 6:
			print('The Manhattan')
			pyautogui.press('r')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			pyautogui.press('m')
			pyautogui.press('g')
			break

		elif saladType == 7:
			print('The Mix')
			pyautogui.press('r')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			break

		elif saladType == 8:
			print('Tomato Ranch')
			pyautogui.press('r')
			pyautogui.press('c')
			pyautogui.press('m')
			break

		elif saladType == 9:
			print('The Big Salad')
			pyautogui.press('c')
			pyautogui.press('g')
			break

		elif saladType == 10:
			print('Cheesy Peppers')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif saladType == 11:
			print('Salad Verde')
			pyautogui.press('r')
			pyautogui.press('g')
			break

		else:
			print('No salad found')


	pyautogui.press('enter')
	return