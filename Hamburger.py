import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def hamburgerIngredients(num):
	print('Hamburger Step 2')
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

	elif foodOrder[num-1] == 'The Pickler':
		print('The Pickler')
		pyautogui.press('m')
		pyautogui.press('c')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Trio':
		print('The Trio')
		pyautogui.press('m')
		pyautogui.press('t')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The P-D':
		print('The P-D')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Stacked':
		print('The Stacked')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('t')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Greens':
		print('The Greens')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'The Super Sour':
		print('The Super Sour')
		pyautogui.press('m')
		pyautogui.press('t')
		pyautogui.press('p')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'The Aroma!!!':
		print('The Aroma!!!')
		pyautogui.press('m')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'The POWER!':
		print('The POWER!')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('o')

	elif foodOrder[num-1] == 'The MELT!':
		print('The MELT!')
		pyautogui.press('m')
		pyautogui.press('c')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Swiss':
		print('The Swiss')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('t')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Holy Burger':
		print('The Holy Burger')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('o')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'Chubigans Special':
		print('Chubigans Special')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Double Melt':
		print('The Double Melt')
		pyautogui.press('m')
		pyautogui.press('m')
		pyautogui.press('c')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Chick-a':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Chick-a Deluxe':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('l')
		pyautogui.press('t')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Chick-a Surpreme':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('t')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Chick-a Melt':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('p')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Three Cs':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('c')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The Double Cs':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('k')
		pyautogui.press('l')
		pyautogui.press('p')

	elif foodOrder[num-1] == 'The Meat Lovers':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('m')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'The MIX':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('c')
		pyautogui.press('t')

	elif foodOrder[num-1] == 'The American':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('m')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('o')
		pyautogui.press('s')

	elif foodOrder[num-1] == 'The EVERYTHING':
		print(foodOrder[num-1])
		pyautogui.press('k')
		pyautogui.press('m')
		pyautogui.press('l')
		pyautogui.press('b')
		pyautogui.press('c')
		pyautogui.press('t')
		pyautogui.press('p')
		pyautogui.press('o')
		pyautogui.press('s')
		
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
		for burgerType in range(41):
			#print(burgerType)
			burgerimg = pyautogui.locateOnScreen('hamburgerimg' + str(burgerType) + '.png', region=recipe_region, grayscale=True)
			if burgerimg:
				break
		
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

		elif burgerType == 12:
			print('The Veggie')
			pyautogui.press('l')
			pyautogui.press('t')
			pyautogui.press('p')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 13:
			print('The Pickler')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Pickler'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 14:
			print('The Trio')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Trio'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 15:
			print('The P-D')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The P-D'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 16:
			print('The Stacked')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Stacked'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 17:
			print('The Greens')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Greens'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 18:
			print('The Super Sour')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Super Sour'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 19:
			print('The Armoa!!!')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Aroma!!!'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 20:
			print('The Extra Veggies')
			pyautogui.press('l')
			pyautogui.press('t')
			pyautogui.press('p')
			pyautogui.press('o')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 21:
			print('The POWER!')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The POWER!'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 22:
			print('The BLOT')
			pyautogui.press('b')
			pyautogui.press('l')
			pyautogui.press('o')
			pyautogui.press('t')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 23:
			print('The C-BLOT')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('l')
			pyautogui.press('o')
			pyautogui.press('t')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 24:
			print('The Cheesy Bread')
			pyautogui.press('c')
			pyautogui.press('b')
			pyautogui.press('s')
			pyautogui.press('enter')
			food[num-1] = None
			time.sleep(0.5)
			return

		elif burgerType == 25:
			print('The MELT!')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The MELT!'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 26:
			print('The Swiss')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Swiss'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 27:
			print('The Holy Burger')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Holy Burger'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 28:
			print('Chubigans Special')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'Chubigans Special'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 29:
			print('The Double Melt')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Double Melt'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 30:
			print('The Chick-a')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Chick-a'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 31:
			print('The Chick-a Deluxe')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Chick-a Deluxe'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 32:
			print('The Chick-a Surpreme')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Chick-a Surpreme'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 33:
			print('The Chick-a Melt')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Chick-a Melt'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 34:
			print('The Three Cs')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Three Cs'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 35:
			print('The Double Cs')
			pyautogui.press('k')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Double Cs'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 36:
			print('The Meat Lovers')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The Meat Lovers'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 37:
			print('The MIX')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The MIX'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 38:
			print('The American')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The American'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return

		elif burgerType == 39:
			print('The EVERYTHING')
			pyautogui.press('m')
			pyautogui.press('k')
			pyautogui.press('enter')
			foodOrder[num-1] = 'The EVERYTHING'
			temp = time.time()
			temp = float(temp)
			clock[num-1] = temp
			return
	
		print('No burger meat type found.')
