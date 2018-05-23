import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def pizza(num):
	global food
	global clock
	
	pizzaimg = None
	for pizzaType in range(12):
		#print(pizzaType)
		pizzaimg = pyautogui.locateCenterOnScreen('pizzaimg' + str(pizzaType) + '.png', region=recipe_region, grayscale=True)
		if pizzaimg:
			break
		if pizzaType == 11:
			print('No pizza type found')
			return

	food[num-1] = 'pizza'
	while True:
		
		if pizzaType == 0:
			print('Pepperoni Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			break

		elif pizzaType == 1:
			print('Cheese Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			break

		elif pizzaType == 2:
			print('Meat Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('m')
			break

		elif pizzaType == 3:
			print('P&M Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			break

		elif pizzaType == 4:
			print('Cheesy Bread')
			pyautogui.press('c')
			break

		elif pizzaType == 5:
			print('Meatlovers Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			break

		elif pizzaType == 6:
			print('Veggie Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			break

		elif pizzaType == 7:
			print('Deluxe Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			break

		elif pizzaType == 8:
			print('Italian Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('m')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			break

		elif pizzaType == 9:
			print('Bacon and Mushroom Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('u')
			break

		elif pizzaType == 10:
			print('Olives and Onions Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('v')
			pyautogui.press('n')
			break

		elif pizzaType == 11:
			print('The PCGB Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('b')
			pyautogui.press('n')
			break

		else:
			print('No pizza found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return