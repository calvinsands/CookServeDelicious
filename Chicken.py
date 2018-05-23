import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def chicken(num):
	global food
	global clock
	
	food[num-1] = 'chicken'

	for chindex in range(6):
		pyautogui.press('t')
		time.sleep(0.11)
	pyautogui.press('s')
	pyautogui.press('enter')
	temp = time.time()
	temp = float(temp)
	clock[num-1] = temp
	return