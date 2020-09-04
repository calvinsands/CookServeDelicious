import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def pizza(num):
	global food
	global clock
	
	pizzaimg = None

	food[num-1] = 'pizza'
	while True:
	
		for pizzaType in range(37):
			if pizzaType == 36:
				break
			pizzaimg = pyautogui.locateOnScreen('pizzaimg' + str(pizzaType) + '.png', region=recipe_region, grayscale=True)
			if pizzaimg:
				break

		
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

		elif pizzaType == 12:
			print('Anchovy Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('a')
			break

		elif pizzaType == 13:
			print('Deluxe Anchovy Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('a')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			break

		elif pizzaType == 14:
			print('Meaty Anchovy Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('a')
			break

		elif pizzaType == 15:
			print('Dairy-Lite Pizza')
			pyautogui.press('t')
			pyautogui.press('a')
			pyautogui.press('u')
			break

		elif pizzaType == 16:
			print('Pineapple and Ham Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('h')
			pyautogui.press('i')
			break

		elif pizzaType == 17:
			print('The Hawaiian Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('b')
			pyautogui.press('h')
			pyautogui.press('n')
			pyautogui.press('i')
			break

		elif pizzaType == 18:
			print('Sweet Veggie P.')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('i')
			break

		elif pizzaType == 19:
			print('Extra Meat Lovers Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('h')
			break

		elif pizzaType == 20:
			print('Super Supreme Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('a')
			pyautogui.press('h')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			pyautogui.press('i')
			break

		elif pizzaType == 21:
			print('The H.A.M. Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('a')
			pyautogui.press('h')
			pyautogui.press('u')
			break

		elif pizzaType == 22:
			print('Tomato Lovers Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('o')
			break

		elif pizzaType == 23:
			print('Tomato & Anchovy Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('a')
			pyautogui.press('o')
			break

		elif pizzaType == 24:
			print('Tomato & Anchovy Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('i')
			pyautogui.press('o')
			break

		elif pizzaType == 25:
			print('The All-Meat-Tomato Pizza')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('a')
			pyautogui.press('h')
			pyautogui.press('o')
			break

		elif pizzaType == 26:
			print('Pesto Pepperoni Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('p')
			break

		elif pizzaType == 27:
			print('All Veggie Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			pyautogui.press('i')
			pyautogui.press('o')
			break

		elif pizzaType == 28:
			print('Super Deluxe Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('a')
			pyautogui.press('h')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			pyautogui.press('i')
			pyautogui.press('o')
			break

		elif pizzaType == 29:
			print('Anchovy Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('a')
			pyautogui.press('u')
			break

		elif pizzaType == 30:
			print('Meat Lovers Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('m')
			pyautogui.press('b')
			pyautogui.press('h')
			break

		elif pizzaType == 31:
			print('Pineapple and Ham Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('h')
			pyautogui.press('i')
			break

		elif pizzaType == 32:
			print('Sweet Veggie Pesto P')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('i')
			break

		elif pizzaType == 33:
			print('Cheesy Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			break

		elif pizzaType == 34:
			print('Piggy Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('h')
			pyautogui.press('u')
			pyautogui.press('n')
			break

		elif pizzaType == 35:
			print('Italian Pesto Pizza')
			pyautogui.press('g')
			pyautogui.press('c')
			pyautogui.press('p')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('n')
			pyautogui.press('o')
			break

		else:
			print('No pizza found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return