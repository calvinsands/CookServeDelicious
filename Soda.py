import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True

def soda(num):
	sodaimg = None
	while True:
		for sodaType in range(43):
			if sodaType == 42:
				break
			sodaimg = pyautogui.locateOnScreen('sodaimg' + str(sodaType) + '.png', region=recipe_region, grayscale=True)
			if sodaimg:
				break
		
		if sodaType == 0:
			print('Small Cola')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 1:
			print('Small Grape')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 2:
			print('Small Diet')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 3:
			print('Small Cola (no ice)')
			pyautogui.press('down')
			break

		elif sodaType == 4:
			print('Small Water')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 5:
			print('Small Tea')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 6:
			print('Medium Cola')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 7:
			print('Medium Grape')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 8:
			print('Medium Diet')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 9:
			print('Medium Cola (no ice)')
			pyautogui.press('up')
			pyautogui.press('down')
			break

		elif sodaType == 10:
			print('Medium Water')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 11:
			print('Medium Tea')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 12:
			print('Large Cola')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 13:
			print('Large Grape')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 14:
			print('Large Diet')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 15:
			print('Large Cola (no ice)')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('down')
			break

		elif sodaType == 16:
			print('Large Water')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 17:
			print('Large Tea')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 18:
			print('Jumbo Cola')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 19:
			print('Jumbo Grape')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 20:
			print('Jumbo Diet')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 21:
			print('Jumbo Cola (no ice)')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('down')
			break

		elif sodaType == 22:
			print('Jumbo Water')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 23:
			print('Jumbo Tea')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			break

		elif sodaType == 24:
			print('Jumbo Cola w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 25:
			print('Jumbo Grape w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 26:
			print('Jumbo Diet w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 27:
			print('Jumbo Cola (no ice) w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 28:
			print('Jumbo Water w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 29:
			print('Jumbo Tea w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 30:
			print('Small Cola w/Flavor Blast')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 31:
			print('Small Grape w/Flavor Blast')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 32:
			print('Small Diet w/Flavor Blast')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 33:
			print('Small Cola (no ice) w/Flavor Blast')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 34:
			print('Small Water w/Flavor Blast')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 35:
			print('Small Tea w/Flavor Blast')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 36:
			print('Medium Cola w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 37:
			print('Medium Grape w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 38:
			print('Medium Diet w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 39:
			print('Large Cola w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 40:
			print('Large Grape w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		elif sodaType == 41:
			print('Large Diet w/Flavor Blast')
			pyautogui.press('up')
			pyautogui.press('up')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('i')
			pyautogui.press('down')
			pyautogui.press('f')
			break

		else:
			print('No soda found')


	pyautogui.press('enter')
	return
