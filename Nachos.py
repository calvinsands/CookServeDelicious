import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def nachosIngredients(num):
	print('Nachos Step 2')
	global food
	global foodOrder
	global clock
	food[num-1] = None
	clock[num-1] = 0.0

	if foodOrder[num-1] == 'Classic Nachos':
		print('Classic Nachos')
		pyautogui.press('q')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'Supreme Nachos':
		print('Supreme Nachos')
		pyautogui.press('q')
		pyautogui.press('c')
		pyautogui.press('j')
		pyautogui.press('t')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'Royal Nachos':
		print('Royal Nachos')
		pyautogui.press('q')
		pyautogui.press('c')
		pyautogui.press('u')
		pyautogui.press('v')
		pyautogui.press('j')
		pyautogui.press('t')
		pyautogui.press('o')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'Italian Style Nachos':
		print('Italian Style Nachos')
		pyautogui.press('q')
		pyautogui.press('v')
		pyautogui.press('o')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'The Chubigans Special':
		print('The Chubigans Special')
		pyautogui.press('q')
		pyautogui.press('b')
		pyautogui.press('r')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'Mexican Siesta':
		print('Mexican Siesta')
		pyautogui.press('q')
		pyautogui.press('u')
		pyautogui.press('b')
		pyautogui.press('r')
		pyautogui.press('g')

	elif foodOrder[num-1] == 'Beef and Beans':
		print('Beef and Beans')
		pyautogui.press('q')
		pyautogui.press('b')
		pyautogui.press('g')
		
	else:
		print('No order found.')

	
	foodOrder[num-1] = None
	pyautogui.press('enter')
	return

	
def nachosMeat(num):
	print('Nachos Step 1')
	global food
	global foodOrder
	global clock
	food[num-1] = 'nachos'

	nachosType = None

	while True:
		nachosimg = None
		for nachosType in range(18):
			#print(nachosType)
			nachosimg = pyautogui.locateCenterOnScreen('nachosimg' + str(nachosType) + '.png', region=recipe_region, grayscale=True)
			if nachosimg:
				break
			if nachosType == 17:
				print('No nachos type found')
		
		if nachosType == 0:
			print('Classic Nachos')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Classic Nachos'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 1:
			print('Supreme Nachos')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Supreme Nachos'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 2:
			print('Royal Nachos')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Royal Nachos'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 3:
			print('Veggie Nachos')
			pyautogui.press('q')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 4:
			print('Sour Veggie Nachos')
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 5:
			print('Guac a Nachos')
			pyautogui.press('q')
			pyautogui.press('u')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 6:
			print('Fiesty Nachos')
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('j')
			pyautogui.press('o')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 7:
			print('Guac and Chips')
			pyautogui.press('u')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 8:
			print('Jalanacho')
			pyautogui.press('q')
			pyautogui.press('j')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 9:
			print('Bowl of Chips')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 10:
			print('Italian Style Nachos')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Italian Style Nachos'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 11:
			print('Scoops of Plenty')
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('o')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 12:
			print('The Chubigans Special')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Chubigans Special'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 13:
			print('Mexican Siesta')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Mexican Siesta'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 14:
			print('Mexican Fiesta')
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('r')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 15:
			print('Rice and Beans')
			pyautogui.press('q')
			pyautogui.press('b')
			pyautogui.press('r')
			pyautogui.press('enter')
			food[num-1] = None
			return

		elif nachosType == 16:
			print('Beef and Beans')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Beef and Beans'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 17:
			print('Spicy Rice Special')
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('r')
			pyautogui.press('enter')
			food[num-1] = None
			return
	
		print('No nachos meat type found.')