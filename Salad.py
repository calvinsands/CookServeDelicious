import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def salad(num):
	saladimg = None
	while True:
		for saladType in range(25):
			if saladType == 24:
				break
			saladimg = pyautogui.locateOnScreen('saladimg' + str(saladType) + '.png', region=recipe_region, grayscale=True)
			if saladimg:
				break
		
		
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

		elif saladType == 12:
			print('The Thousand Salad')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('g')
			break

		elif saladType == 13:
			print('The Thousand Peppers')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif saladType == 14:
			print('Thousand House')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('b')
			break

		elif saladType == 15:
			print('Thousand Tomatoes')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('m')
			break

		elif saladType == 16:
			print('Three Thousand')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			pyautogui.press('g')
			break

		elif saladType == 17:
			print('A Thousand Flavors')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			pyautogui.press('m')
			pyautogui.press('g')
			break

		elif saladType == 18:
			print('A Thousand Flavors')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('o')
			break

		elif saladType == 19:
			print('The Oil Bleu')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			pyautogui.press('m')
			pyautogui.press('g')
			break

		elif saladType == 20:
			print('Vinaigrette House')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('b')
			break

		elif saladType == 21:
			print('The Oily Greens')
			pyautogui.press('v')
			pyautogui.press('m')
			pyautogui.press('g')
			break

		elif saladType == 22:
			print('Cheesy Vinaigrette')
			pyautogui.press('v')
			pyautogui.press('c')
			break

		elif saladType == 23:
			print('Vinaigrette Classic')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('o')
			pyautogui.press('m')
			break

		else:
			print('No salad found')


	pyautogui.press('enter')
	return