import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def fries(num):

	friesimg = None
	for friesType in range(10):
		if friesType == 9:
			print('No fries type found.')
			pyautogui.screenshot('friesimg'+str(friesType)+'.png', region=recipe_region)
			print('New fries saved as friesimg'+str(friesType)+'.png')
			print('Exiting.')
			sys.exit()
		friesimg = pyautogui.locateOnScreen('friesimg' + str(friesType) + '.png', region=recipe_region, grayscale=True)
		if friesimg:
			break

	pyautogui.keyDown('down')
	time.sleep(3.05)
	pyautogui.keyUp('down')
	pyautogui.press('p')
	
	while True:
		
		if friesType == 0:
			print('SALT THOSE FRIES BRUH')
			pyautogui.press('a')
			break

		elif friesType == 1:
			print('MY LOVE IS THE SEA')
			pyautogui.press('e')
			break

		elif friesType == 2:
			print('SWEETNSALTY')
			pyautogui.press('a')
			pyautogui.press('s')
			break

		elif friesType == 3:
			print('SUGAR. IN. WATER')
			pyautogui.press('s')
			break
		
		# event salt fries
		elif friesType == 4:
			print('salted')
			pyautogui.press('a')
			break
		
		# event no salt fries
		elif friesType == 5:
			break
		
		# thick event no salt fries
		elif friesType == 6:
			break
			
		# thick event salt fries
		elif friesType == 7:
			print('salted')
			pyautogui.press('a')
			break
			
		# thick event sea salt fries
		elif friesType == 8:
			print('salted')
			pyautogui.press('e')
			break

		else:
			print('No fries found.')

	
	pyautogui.press('enter')
	return