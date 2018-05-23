import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True



def hamburgerIngredients(num):
	print('Hamburger Step 2')
	global food
	global foodOrder
	global clock
	food[num-1] = None
	clock[num-1] = 0.0

	if foodOrder[num-1] == 'The Original':
		print('The Original: Meat, Lettuce, Bacon, Cheese, Tomatoes')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'The Double':
		print('The Double: Meat (2x), Lettuce, Bacon, Cheese, Tomatoes')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'The HEARTSTOPPER!':
		print('The HEARTSTOPPER!: Meat (2x), Bacon (2x), Cheese')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('b')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'The Lite Delight':
		print('The Lite Delight: Meat and Lettuce only')
		pyautogui.press('m')
		pyautogui.press('l')

	elif foodOrder[num-1] == 'The Ryan Davis':
		print('The Ryan Davis: Meat, Bacon, Cheese (2x), Tomatoes')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('c')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'The Lonely Patty':
		print('The Lonely Patty: Meat only')
		pyautogui.press('m')

	elif foodOrder[num-1] == 'The Triple':
		print('The Triple: Meat (3x) and Cheese')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'The Triple with Bacon':
		print('The Triple: Meat (3x), Bacon and Cheese')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'The RED':
		print('The RED: Meat and Tomatoes only')
		pyautogui.press('m')
		pyautogui.press('t')
		
	else:
		print('No order found.')

	
	foodOrder[num-1] = None
	pyautogui.press('enter')
	time.sleep(0.5)
	return


def hamburgerMeat(num):
	print('Hamburger Step 1')
	global food
	global foodOrder
	global clock
	food[num-1] = 'hamburger'

	burgerType = None

	while True:
		burgerimg = None
		for burgerType in range(12):
			#print(burgerType)
			burgerimg = pyautogui.locateOnScreen('hamburgerimg' + str(burgerType) + '.png', region=recipe_region, grayscale=True)
			if burgerimg:
				break
			if burgerType == 11:
				print('No burger type found')
		
		if burgerType == 0:
			print('The Original: One meat patty')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Original'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 1:
			print('The Double: Two meat patties')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Double'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 2:
			print('BLT: Bacon, lettuce, tomatoe')
			pyautogui.press('b')
			pyautogui.press('l')
			pyautogui.press('t')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 3:
			print('BLT & C: Bacon, lettuce, tomatoe, cheese')
			pyautogui.press('b')
			pyautogui.press('l')
			pyautogui.press('t')
			pyautogui.press('c')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 4:
			print('The HEARTSTOPPER!: Two meat patties')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The HEARTSTOPPER!'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 5:
			print('The Lite Delight: One meat patty')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Lite Delight'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 6:
			print('The Ryan Davis: One meat patty')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Ryan Davis'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 7:
			print('The Tumbleweed: Bacon and cheese')
			pyautogui.press('b')
			pyautogui.press('c')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 8:
			print('The Lonely Patty: One meat patty')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Lonely Patty'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 9:
			print('The Triple: Three meat patties')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Triple'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 10:
			print('The Triple with Bacon: Three meat patties')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Triple with Bacon'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 11:
			print('The RED: One meat patty')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The RED'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return
	
		print('No burger meat type found.')
