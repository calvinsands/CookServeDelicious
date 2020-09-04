import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def steak(num):
	

	food[num-1] = 'steak'
	while True:

		steakimg = None
		for steakType in range(11):
			if steakType == 10:
				break
			steakimg = pyautogui.locateOnScreen('steakimg' + str(steakType) + '.png', region=recipe_region, grayscale=True)
			if steakimg:
				break
		
		if steakType == 0:
			print('Seasony.')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('j')
			break

		elif steakType == 1:
			print('Juicy.')
			pyautogui.press('s')
			pyautogui.press('j')
			pyautogui.press('j')
			pyautogui.press('c')
			break

		elif steakType == 2:
			print('Spicy.')
			pyautogui.press('s')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('j')
			pyautogui.press('j')
			break

		elif steakType == 3:
			print('Dry.')
			pyautogui.press('s')
			pyautogui.press('p')
			pyautogui.press('p')
			break

		elif steakType == 4:
			print('Bacony.')
			pyautogui.press('s')
			pyautogui.press('j')
			pyautogui.press('j')
			pyautogui.press('b')
			pyautogui.press('b')
			break

		elif steakType == 5:
			print('Spicy Bacony.')
			pyautogui.press('s')
			pyautogui.press('j')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('b')
			pyautogui.press('b')
			break

		elif steakType == 6:
			print('Spicy Smokey.')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('d')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('j')
			pyautogui.press('j')
			break

		elif steakType == 7:
			print('Spicy Orangey.')
			pyautogui.press('s')
			pyautogui.press('d')
			pyautogui.press('j')
			pyautogui.press('c')
			pyautogui.press('c')
			break

		elif steakType == 8:
			print('Hickory.')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('j')
			pyautogui.press('j')
			pyautogui.press('j')
			pyautogui.press('j')
			break

		elif steakType == 9:
			print('Texasy.')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('j')
			pyautogui.press('j')
			pyautogui.press('b')
			pyautogui.press('b')
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('p')
			pyautogui.press('p')
			pyautogui.press('d')
			pyautogui.press('d')
			break

		else:
			print('No steak found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return