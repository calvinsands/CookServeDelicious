import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def potatoIngredients(num):
	print('Potato Step 2')
	food[num-1] = None
	clock[num-1] = 0.0

	potatoType = None

	while True:
		potatoimg = None
		for potatoType in range(11):
			if potatoType == 10:
				break
			potatoimg = pyautogui.locateOnScreen('potatoimg' + str(potatoType) + '.png', region=recipe_region, grayscale=True)
			if potatoimg:
				break
		
		if potatoType == 0:
			print('Classic Baked Potato')
			pyautogui.press('c')
			pyautogui.press('s')
			pyautogui.press('y')
			break

		elif potatoType == 1:
			print('Classic Potato w/Bacon')
			pyautogui.press('c')
			pyautogui.press('s')
			pyautogui.press('y')
			pyautogui.press('b')
			break

		elif potatoType == 2:
			print('Deluxe Potato')
			pyautogui.press('c')
			pyautogui.press('s')
			pyautogui.press('y')
			pyautogui.press('h')
			pyautogui.press('b')
			pyautogui.press('o')
			break

		elif potatoType == 3:
			print('Plain Potato')
			pyautogui.press('y')
			break

		elif potatoType == 4:
			print('Sour Potato')
			pyautogui.press('s')
			pyautogui.press('o')
			break

		elif potatoType == 5:
			print('Lite Potato')
			pyautogui.press('s')
			pyautogui.press('h')
			pyautogui.press('o')
			break

		elif potatoType == 6:
			print('The Dry Potato')
			break

		elif potatoType == 7:
			print('Sour Potato w/Bacon')
			pyautogui.press('s')
			pyautogui.press('b')
			pyautogui.press('o')
			break

		elif potatoType == 8:
			print('Lite n Cheesy Potato')
			pyautogui.press('c')
			pyautogui.press('s')
			break

		elif potatoType == 9:
			print('Chives & Bacon Potato')
			pyautogui.press('y')
			pyautogui.press('h')
			pyautogui.press('b')
			break
	
		print('No potato type found.')

	pyautogui.press('enter')
	return


def potatoCook(num):
	print('Bake the potato!')
	food[num-1] = 'potato'
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return