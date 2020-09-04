import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def kabob(num):

	food[num-1] = 'kabob'
	while True:
	
		kabobimg = None
		for kabobType in range(15):
			if kabobType == 14:
				break
			kabobimg = pyautogui.locateOnScreen('kabobimg' + str(kabobType) + '.png', region=recipe_region, grayscale=True)
			if kabobimg:
				break
		
		if kabobType == 0:
			print('Classic Kabob')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('g')
			pyautogui.press('r')
			break

		elif kabobType == 1:
			print('Meaty Kabob')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('m')
			pyautogui.press('k')
			break

		elif kabobType == 2:
			print('Pepper Kabob')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('g')
			pyautogui.press('r')
			break

		elif kabobType == 3:
			print('Red Kabob')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('r')
			break

		elif kabobType == 4:
			print('Kabobber')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			break

		elif kabobType == 5:
			print('Chicken Kabob')
			pyautogui.press('t')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('k')
			pyautogui.press('r')
			pyautogui.press('k')
			pyautogui.press('t')
			pyautogui.press('k')
			break

		elif kabobType == 6:
			print('Onion Kabob')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('k')
			pyautogui.press('o')
			pyautogui.press('g')
			pyautogui.press('o')
			pyautogui.press('r')
			pyautogui.press('o')
			break

		elif kabobType == 7:
			print('Tower Kabob')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			break

		elif kabobType == 8:
			print('Tangy Kabob')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			break

		elif kabobType == 9:
			print('Juicy Kabob')
			pyautogui.press('o')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('o')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('o')
			break

		elif kabobType == 10:
			print('Hawaiian Kabob')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('o')
			pyautogui.press('p')
			pyautogui.press('k')
			pyautogui.press('o')
			pyautogui.press('p')
			break

		elif kabobType == 11:
			print('Pineapple Kabob')
			pyautogui.press('t')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('p')
			pyautogui.press('k')
			pyautogui.press('p')
			pyautogui.press('o')
			pyautogui.press('p')
			break

		elif kabobType == 12:
			print('Kabomber')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('p')
			break

		elif kabobType == 13:
			print('Kabob Sampler')
			pyautogui.press('p')
			pyautogui.press('t')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('g')
			pyautogui.press('r')
			pyautogui.press('o')
			pyautogui.press('p')
			break

		else:
			print('No kabob found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return