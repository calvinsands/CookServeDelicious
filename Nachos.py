import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def nachosIngredients(num, meatflag):
	print('Nachos Step 2')
	
	if meatflag == 1:
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

		elif foodOrder[num-1] == 'Shrimp Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'Deluxe Shrimp Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('g')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'New Orleans Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('t')
			pyautogui.press('b')
			pyautogui.press('r')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'Classic Shrimp Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'Beef Fajita Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('f')

		elif foodOrder[num-1] == 'Chicken Fajita Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('k')

		elif foodOrder[num-1] == 'Combo Fajita Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('k')
			pyautogui.press('f')

		elif foodOrder[num-1] == 'EXTREME FAJITAS!!!!!':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'Chubigans Deluxe Special':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('b')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('r')

		elif foodOrder[num-1] == 'Classic American':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('g')

		elif foodOrder[num-1] == 'Fiery Fiesta Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('o')
			pyautogui.press('r')
			pyautogui.press('k')
			pyautogui.press('s')

		elif foodOrder[num-1] == 'All Meat Special':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('b')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('s')
			pyautogui.press('g')

		elif foodOrder[num-1] == 'Beefy Surpreme':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('u')
			pyautogui.press('b')
			pyautogui.press('f')
			pyautogui.press('g')

		elif foodOrder[num-1] == 'Fully Loaded Nachos':
			print(foodOrder[num-1])
			pyautogui.press('q')
			pyautogui.press('c')
			pyautogui.press('u')
			pyautogui.press('v')
			pyautogui.press('j')
			pyautogui.press('t')
			pyautogui.press('o')
			pyautogui.press('b')
			pyautogui.press('r')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('s')
			pyautogui.press('g')
			
		else:
			print('No order found.')

		
		foodOrder[num-1] = None
		pyautogui.press('enter')
		return
	
	else:
		nachosType = None

		while True:
			nachosimg = None
			for nachosType in range(19):
				nachosimg = pyautogui.locateOnScreen('nachosimg' + str(nachosType) + '.png', region=recipe_region, grayscale=True)
				if nachosimg:
					break
			
			if nachosType == 3:
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

			elif nachosType == 11:
				print('Scoops of Plenty')
				pyautogui.press('q')
				pyautogui.press('c')
				pyautogui.press('u')
				pyautogui.press('o')
				pyautogui.press('enter')
				food[num-1] = None
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
	
	
def nachosMeat(num):
	print('Cook Nachos Meat')
	
	food[num-1] = 'nachos'

	nachosType = None

	while True:
		nachosimg = None
		for nachosType in range(33):
			if nachosType == 32:
				break
			nachosimg = pyautogui.locateOnScreen('nachosimg' + str(nachosType) + '.png', region=recipe_region, grayscale=True)
			if nachosimg:
				break
		
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

		elif nachosType == 10:
			print('Italian Style Nachos')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Italian Style Nachos'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
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

		elif nachosType == 16:
			print('Beef and Beans')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Beef and Beans'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 18:
			pyautogui.press('s')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Shrimp Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 19:
			pyautogui.press('s')
			pyautogui.press('g')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Deluxe Shrimp Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 20:
			pyautogui.press('s')
			pyautogui.press('enter')
			foodOrder[num-1] = 'New Orleans Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 21:
			pyautogui.press('s')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Classic Shrimp Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 22:
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Beef Fajita Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 23:
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Chicken Fajita Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 24:
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Combo Fajita Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 25:
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('s')
			pyautogui.press('enter')
			foodOrder[num-1] = 'EXTREME FAJITAS!!!!!'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 26:
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Chubigans Deluxe Special'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 27:
			pyautogui.press('g')
			pyautogui.press('k')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Classic American'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 28:
			pyautogui.press('k')
			pyautogui.press('s')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Fiery Fiesta Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 29:
			pyautogui.press('k')
			pyautogui.press('s')
			pyautogui.press('g')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'All Meat Special'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 30:
			pyautogui.press('g')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Beefy Surpreme'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif nachosType == 31:
			pyautogui.press('k')
			pyautogui.press('s')
			pyautogui.press('g')
			pyautogui.press('f')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Fully Loaded Nachos'
			print(foodOrder[num-1])
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return
	
		print('No nachos meat type found.')