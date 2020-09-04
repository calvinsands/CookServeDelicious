import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder


pyautogui.FAILSAFE = True


def lasagna(num):
	global food
	global clock

	lasagnaimg = None
	for lasagnaType in range(4):
		#print(lasagnaType)
		lasagnaimg = pyautogui.locateOnScreen('lasagnaimg' + str(lasagnaType) + '.png', region=recipe_region, grayscale=True)
		if lasagnaimg:
			break

	food[num-1] = 'lasagna'
	
	pyautogui.PAUSE = 0.05
	
	while True:
		
		if lasagnaType == 0:
			print('Cheese Lasagna.')
			for lasindex in range(3):
				pyautogui.press('p')
				pyautogui.press('s')
				pyautogui.press('c')
				pyautogui.press('r')
			break

		elif lasagnaType == 1:
			print('Beef Lasagna.')
			for lasindex in range(2):
				pyautogui.press('p')
				pyautogui.press('s')
				pyautogui.press('m')
				pyautogui.press('c')
				pyautogui.press('r')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('c')
			pyautogui.press('r')
			break

		elif lasagnaType == 2:
			print('Veggie Lasagna.')
			for lasindex in range(2):
				pyautogui.press('p')
				pyautogui.press('s')
				pyautogui.press('v')
				pyautogui.press('c')
				pyautogui.press('r')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('c')
			pyautogui.press('r')
			break

		elif lasagnaType == 3:
			print('Stuffed Piza Lasagna.')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('m')
			pyautogui.press('c')
			pyautogui.press('r')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('v')
			pyautogui.press('c')
			pyautogui.press('r')
			pyautogui.press('p')
			pyautogui.press('s')
			pyautogui.press('c')
			pyautogui.press('r')
			break
	
	pyautogui.press('enter')
	
	pyautogui.PAUSE = 0.075
	
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return