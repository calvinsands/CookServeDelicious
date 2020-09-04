import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def friedchicken(num):

	friedchickenimg = None
	
	"""
	for friedchickenType in range(3):
		#print(friedchickenType)
		if friedchickenType == 2:
			print('No friedchicken type found.')
			pyautogui.screenshot('friedchickenimg'+str(friedchickenType)+'.png', region=recipe_region)
			print('New friedchicken saved as friedchickenimg'+str(friedchickenType)+'.png')
			print('Exiting.')
			sys.exit()
		friedchickenimg = pyautogui.locateOnScreen('friedchickenimg' + str(friedchickenType) + '.png', region=recipe_region, grayscale=True)
		if friedchickenimg:
			break
	"""
	
	
	pyautogui.keyDown('down')
	time.sleep(3.5)
	pyautogui.keyUp('down')
	pyautogui.press('p')
	
	pyautogui.press('enter')
	return