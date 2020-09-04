import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def rice(num):
	

	food[num-1] = 'rice'
	while True:

		riceimg = None
		for riceType in range(14):
			if riceType == 13:
				break
			riceimg = pyautogui.locateOnScreen('riceimg' + str(riceType) + '.png', region=recipe_region, grayscale=True)
			if riceimg:
				break
		
		if riceType == 0:
			print('Classic Fried Rice')
			pyautogui.press('f')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		elif riceType == 1:
			print('Lite Fried Rice')
			pyautogui.press('f')
			pyautogui.press('p')
			pyautogui.press('c')
			break

		elif riceType == 2:
			print('Sour Fried Rice')
			pyautogui.press('f')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		elif riceType == 3:
			print('Sweet Fried Rice')
			pyautogui.press('f')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			break

		elif riceType == 4:
			print('Classic White Rice')
			pyautogui.press('w')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		elif riceType == 5:
			print('Yellow White Rice')
			pyautogui.press('w')
			pyautogui.press('e')
			pyautogui.press('n')
			break

		elif riceType == 6:
			print('Crunchy White Rice')
			pyautogui.press('w')
			pyautogui.press('e')
			pyautogui.press('o')
			pyautogui.press('n')
			break

		elif riceType == 7:
			print('Special White Rice')
			pyautogui.press('w')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			pyautogui.press('n')
			break

		elif riceType == 8:
			print('Classic Brown Rice')
			pyautogui.press('b')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		elif riceType == 9:
			print('Deluxe Brown Rice')
			pyautogui.press('b')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			pyautogui.press('n')
			pyautogui.press('r')
			break

		elif riceType == 10:
			print('Delight White Rice')
			pyautogui.press('w')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('e')
			pyautogui.press('o')
			pyautogui.press('n')
			pyautogui.press('r')
			break

		elif riceType == 11:
			print('Lite Rice')
			pyautogui.press('w')
			pyautogui.press('n')
			pyautogui.press('r')
			break

		elif riceType == 12:
			print('Brown Sour Rice')
			pyautogui.press('b')
			pyautogui.press('e')
			pyautogui.press('o')
			break

		else:
			print('No rice found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return