import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def pastaIngredients(num):
	print('Pasta Step 2')
	food[num-1] = None
	clock[num-1] = 0.0

	if foodOrder[num-1] == 'Cheese Pasta':
		pyautogui.press('c')

	elif foodOrder[num-1] == 'Classic Spaghetti':
		pyautogui.press('r')
		pyautogui.press('m')

	elif foodOrder[num-1] == 'Red Veggie Pasta':
		pyautogui.press('r')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'The Meaty Pasta':
		pyautogui.press('r')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Hot Bacon Pasta':
		pyautogui.press('r')
		pyautogui.press('b')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'Cheesy Onion Pasta':
		pyautogui.press('c')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'Cheesy Meaty Pasta':
		pyautogui.press('c')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Cheesy Deluxe Pasta':
		pyautogui.press('c')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'Red Deluxe Pasta':
		pyautogui.press('r')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'Cheesy Chicken Pasta':
		pyautogui.press('c')
		pyautogui.press('k')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Spaghetti Deluxe':
		pyautogui.press('r')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('u')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'Cheesy Veggie Pasta':
		pyautogui.press('c')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')
		
	elif foodOrder[num-1] == 'Creamy Alfredo':
		pyautogui.press('w')
		pyautogui.press('k')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Carbonara':
		pyautogui.press('w')
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('i')

	elif foodOrder[num-1] == 'Creamy Meat Pasta':
		pyautogui.press('w')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('u')

	elif foodOrder[num-1] == 'Creamy Veggie Pasta':
		pyautogui.press('w')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'Spicy Bacon Pasta':
		pyautogui.press('r')
		pyautogui.press('b')
		pyautogui.press('i')

	elif foodOrder[num-1] == 'Spicy Spaghetti':
		pyautogui.press('r')
		pyautogui.press('m')
		pyautogui.press('i')

	elif foodOrder[num-1] == 'The Dry Tomato':
		pyautogui.press('m')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'Red Pasta Rally':
		pyautogui.press('r')
		pyautogui.press('p')
		pyautogui.press('i')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'Dry Veggie Pasta':
		pyautogui.press('p')
		pyautogui.press('s')
		pyautogui.press('i')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'Cheesy Tomato':
		pyautogui.press('c')
		pyautogui.press('i')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'Spaghetti Pesto':
		pyautogui.press('g')
		pyautogui.press('m')

	elif foodOrder[num-1] == 'Manhattan Pesto':
		pyautogui.press('g')
		pyautogui.press('m')
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('p')
		pyautogui.press('u')
		pyautogui.press('s')
		pyautogui.press('o')
		pyautogui.press('i')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'Chicken Pesto':
		pyautogui.press('g')
		pyautogui.press('k')
		pyautogui.press('u')
		pyautogui.press('i')

	elif foodOrder[num-1] == 'Verde Pesto':
		pyautogui.press('g')
		pyautogui.press('s')
		pyautogui.press('i')
		
	else:
		print('No order found.')

	print(foodOrder[num-1])
	foodOrder[num-1] = None
	pyautogui.press('enter')
	return


def pastaCook(num):

	print('Pasta Boil')
	food[num-1] = 'pasta'

	pastaType = None

	while True:
		pastaimg = None
		for pastaType in range(27):
			if pastaType == 26:
				break
			pastaimg = pyautogui.locateOnScreen('pastaimg' + str(pastaType) + '.png', region=recipe_region, grayscale=True)
			if pastaimg:
				break
		
		
		if pastaType == 0:
			foodOrder[num-1] = 'Cheese Pasta'
			break

		elif pastaType == 1:
			foodOrder[num-1] = 'Classic Spaghetti'
			break

		elif pastaType == 2:
			foodOrder[num-1] = 'Red Veggie Pasta'
			break

		elif pastaType == 3:
			foodOrder[num-1] = 'The Meaty Pasta'
			break

		elif pastaType == 4:
			foodOrder[num-1] = 'Hot Bacon Pasta'
			break

		elif pastaType == 5:
			foodOrder[num-1] = 'Cheesy Onion Pasta'
			break

		elif pastaType == 6:
			foodOrder[num-1] = 'Cheesy Meaty Pasta'
			break

		elif pastaType == 7:
			foodOrder[num-1] = 'Cheesy Deluxe Pasta'
			break

		elif pastaType == 8:
			foodOrder[num-1] = 'Red Deluxe Pasta'
			break

		elif pastaType == 9:
			foodOrder[num-1] = 'Cheesy Chicken Pasta'
			break

		elif pastaType == 10:
			foodOrder[num-1] = 'Spaghetti Deluxe'
			break

		elif pastaType == 11:
			foodOrder[num-1] = 'Cheesy Veggie Pasta'
			break

		elif pastaType == 12:
			foodOrder[num-1] = 'Creamy Alfredo'
			break

		elif pastaType == 13:
			foodOrder[num-1] = 'The Carbonara'
			break

		elif pastaType == 14:
			foodOrder[num-1] = 'Creamy Meat Pasta'
			break

		elif pastaType == 15:
			foodOrder[num-1] = 'Creamy Veggie Pasta'
			break

		elif pastaType == 16:
			foodOrder[num-1] = 'Spicy Bacon Pasta'
			break

		elif pastaType == 17:
			foodOrder[num-1] = 'Spicy Spaghetti'
			break

		elif pastaType == 18:
			foodOrder[num-1] = 'The Dry Tomato'
			break

		elif pastaType == 19:
			foodOrder[num-1] = 'Red Pasta Rally'
			break

		elif pastaType == 20:
			foodOrder[num-1] = 'Dry Veggie Pasta'
			break

		elif pastaType == 21:
			foodOrder[num-1] = 'Cheesy Tomato'
			break

		elif pastaType == 22:
			foodOrder[num-1] = 'Spaghetti Pesto'
			break

		elif pastaType == 23:
			foodOrder[num-1] = 'Manhattan Pesto'
			break

		elif pastaType == 24:
			foodOrder[num-1] = 'Chicken Pesto'
			break

		elif pastaType == 25:
			foodOrder[num-1] = 'Verde Pesto'
			break
	
		print('No pasta type found.')
	
	
	print(foodOrder[num-1])
	pyautogui.press('r')
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return

