import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def pancakeIngredients(num):
	print('Pancake Step 2')
	food[num-1] = None
	clock[num-1] = 0.0

	if foodOrder[num-1] == 'Junior Classic':
		pyautogui.press('p')
		pyautogui.press('m')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Triple Maple':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('m')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Dual Maple Stack':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('m')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Junior Redberry':
		pyautogui.press('p')
		pyautogui.press('s')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Triple Red Stack':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('s')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Double Strawberry':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('s')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Dry Single':
		pyautogui.press('p')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Triple Dry':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Double Desert':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Junior Blueberry':
		pyautogui.press('p')
		pyautogui.press('l')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Blue Double Stack':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('l')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Triple Berry Blue':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('l')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'The Lonely Pancake':
		pyautogui.press('p')

	elif foodOrder[num-1] == 'Junior Pecan':
		pyautogui.press('p')
		pyautogui.press('e')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Double Pecan Stack':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('e')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Triple Pecan Stack':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('e')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Lite Double Pecan':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('e')

	elif foodOrder[num-1] == 'Lite Maple Classic':
		pyautogui.press('p')
		pyautogui.press('p')
		pyautogui.press('m')
		
	else:
		print('No order found.')

	print(foodOrder[num-1])
	foodOrder[num-1] = None
	pyautogui.press('enter')
	return


def pancakeCook(num):

	print('Cook Pancake')
	food[num-1] = 'pancake'

	pancakeType = None

	while True:
		pancakeimg = None
		for pancakeType in range(19):
			if pancakeType == 18:
				break
			pancakeimg = pyautogui.locateOnScreen('pancakeimg' + str(pancakeType) + '.png', region=recipe_region, grayscale=True)
			if pancakeimg:
				break
		
		if pancakeType == 0:
			foodOrder[num-1] = 'Junior Classic'
			pcount=1
			break

		elif pancakeType == 1:
			foodOrder[num-1] = 'Triple Maple'
			pcount=3
			break

		elif pancakeType == 2:
			foodOrder[num-1] = 'Dual Maple Stack'
			pcount=2
			break

		elif pancakeType == 3:
			foodOrder[num-1] = 'Junior Redberry'
			pcount=1
			break

		elif pancakeType == 4:
			foodOrder[num-1] = 'Triple Red Stack'
			pcount=3
			break

		elif pancakeType == 5:
			foodOrder[num-1] = 'Double Strawberry'
			pcount=2
			break

		elif pancakeType == 6:
			foodOrder[num-1] = 'Dry Single'
			pcount=1
			break

		elif pancakeType == 7:
			foodOrder[num-1] = 'Triple Dry'
			pcount=3
			break

		elif pancakeType == 8:
			foodOrder[num-1] = 'Double Desert'
			pcount=2
			break

		elif pancakeType == 9:
			foodOrder[num-1] = 'Junior Blueberry'
			pcount=1
			break

		elif pancakeType == 10:
			foodOrder[num-1] = 'Blue Double Stack'
			pcount=2
			break

		elif pancakeType == 11:
			foodOrder[num-1] = 'Triple Berry Blue'
			pcount=3
			break

		elif pancakeType == 12:
			foodOrder[num-1] = 'The Lonely Pancake'
			pcount=1
			break

		elif pancakeType == 13:
			foodOrder[num-1] = 'Junior Pecan'
			pcount=1
			break

		elif pancakeType == 14:
			foodOrder[num-1] = 'Double Pecan Stack'
			pcount=2
			break

		elif pancakeType == 15:
			foodOrder[num-1] = 'Triple Pecan Stack'
			pcount=3
			break

		elif pancakeType == 16:
			foodOrder[num-1] = 'Lite Double Pecan'
			pcount=2
			break

		elif pancakeType == 17:
			foodOrder[num-1] = 'Lite Maple Classic'
			pcount=2
			break
	
		print('No pancake type found.')
	
	
	print(foodOrder[num-1])
	
	for i in range(pcount):
		pyautogui.press('p')
	
	pyautogui.press('enter')
	
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return

