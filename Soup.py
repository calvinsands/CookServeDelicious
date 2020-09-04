import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def soup(num):
	
	soupimg = None

	food[num-1] = 'soup'
	while True:
		
		for soupType in range(12):
			if soupType == 11:
				break
			soupimg = pyautogui.locateOnScreen('soupimg' + str(soupType) + '.png', region=recipe_region, grayscale=True)
			if soupimg:
				break
		
		if soupType == 0:
			print('Chicken Soup')
			pyautogui.press('k')
			pyautogui.press('w')
			pyautogui.press('u')
			pyautogui.press('space')
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		elif soupType == 1:
			print('Soup Du Jour')
			pyautogui.press('w')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('space')
			pyautogui.press('t')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('a')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		elif soupType == 2:
			print('Vegetable Soup')
			pyautogui.press('t')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('a')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('l')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('d')
			break

		elif soupType == 3:
			print('Baristobo Soup')
			pyautogui.press('k')
			pyautogui.press('w')
			pyautogui.press('s')
			pyautogui.press('p')
			pyautogui.press('a')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('l')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		elif soupType == 4:
			print('Creamy Potato')
			pyautogui.press('s')
			pyautogui.press('p')
			pyautogui.press('b')
			pyautogui.press('c')
			break

		elif soupType == 5:
			print('Louisiana Delight')
			pyautogui.press('k')
			pyautogui.press('m')
			pyautogui.press('i')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('b')
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			break

		elif soupType == 6:
			print('Hearty Meat Soup')
			pyautogui.press('k')
			pyautogui.press('m')
			pyautogui.press('i')
			pyautogui.press('h')
			pyautogui.press('p')
			pyautogui.press('c')
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('g')
			break

		elif soupType == 7:
			print('One Bean Soup')
			pyautogui.press('i')
			pyautogui.press('s')
			pyautogui.press('p')
			pyautogui.press('y')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('e')
			break

		elif soupType == 8:
			print('Broccoli Soup')
			pyautogui.press('s')
			pyautogui.press('b')
			pyautogui.press('c')
			pyautogui.press('a')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('r')
			break

		elif soupType == 9:
			print('Italian Soup')
			pyautogui.press('m')
			pyautogui.press('i')
			pyautogui.press('b')
			pyautogui.press('c')
			pyautogui.press('t')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('z')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('o')
			break

		elif soupType == 10:
			print('Suino Stew')
			pyautogui.press('h')
			pyautogui.press('w')
			pyautogui.press('c')
			pyautogui.press('l')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('z')
			for cut in range(3):
				pyautogui.press('down')
				time.sleep(0.15)
			pyautogui.press('g')
			pyautogui.press('o')
			break

		else:
			print('No soup found.')

	
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return