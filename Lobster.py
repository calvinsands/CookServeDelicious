import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def lobsterIngredients(num):
	print('lobster Step 2')
	food[num-1] = None
	clock[num-1] = 0.0

	if foodOrder[num-1] == 'Classic Lite Lobster':
		pass

	elif foodOrder[num-1] == 'Classic Lobster':
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Buttery Lobster':
		pyautogui.press('b')
		pyautogui.press('b')

	elif foodOrder[num-1] == 'Lobster Cocktail':
		pyautogui.press('c')

	elif foodOrder[num-1] == 'Buttery Cocktail':
		pyautogui.press('b')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'Double Cocktail':
		pyautogui.press('c')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'Garlic Lobster':
		pyautogui.press('a')

	elif foodOrder[num-1] == 'Garlic Cocktail':
		pyautogui.press('a')
		pyautogui.press('c')

	elif foodOrder[num-1] == 'Buttery Garlic':
		pyautogui.press('b')
		pyautogui.press('a')
		
	else:
		print('No order found.')

	print(foodOrder[num-1])
	foodOrder[num-1] = None
	pyautogui.press('enter')
	return


def lobsterCook(num):

	print('lobster Boil')
	food[num-1] = 'lobster'

	lobsterType = None

	while True:
		lobsterimg = None
		for lobsterType in range(10):
			if lobsterType == 9:
				break
			lobsterimg = pyautogui.locateOnScreen('lobsterimg' + str(lobsterType) + '.png', region=recipe_region, grayscale=True)
			if lobsterimg:
				break
		
		
		if lobsterType == 0:
			foodOrder[num-1] = 'Classic Lite Lobster'
			break

		elif lobsterType == 1:
			foodOrder[num-1] = 'Classic Lobster'
			break

		elif lobsterType == 2:
			foodOrder[num-1] = 'Buttery Lobster'
			break

		elif lobsterType == 3:
			foodOrder[num-1] = 'Lobster Cocktail'
			break

		elif lobsterType == 4:
			foodOrder[num-1] = 'Buttery Cocktail'
			break

		elif lobsterType == 5:
			foodOrder[num-1] = 'Double Cocktail'
			break

		elif lobsterType == 6:
			foodOrder[num-1] = 'Garlic Lobster'
			break

		elif lobsterType == 7:
			foodOrder[num-1] = 'Garlic Cocktail'
			break

		elif lobsterType == 8:
			foodOrder[num-1] = 'Buttery Garlic'
			break
	
		print('No lobster type found.')
	
	
	print(foodOrder[num-1])
	pyautogui.press('l')
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return

