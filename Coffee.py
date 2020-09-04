import pyautogui, time, sys

from constants import center_region
from constants import recipe_region
from constants import full_recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def coffee(num):

	coffeeimg = None
	for coffeeType in range(12):
		if coffeeType == 11:
			print('No coffee type found.')
			pyautogui.screenshot('coffeeimg'+str(coffeeType)+'.png', region=full_recipe_region)
			print('New coffee saved as coffeeimg'+str(coffeeType)+'.png')
			print('Exiting.')
			sys.exit()
		coffeeimg = pyautogui.locateOnScreen('coffeeimg' + str(coffeeType) + '.png', region=full_recipe_region, grayscale=True)
		if coffeeimg:
			break
	
	pyautogui.press('down')
	
	if coffeeType == 0:
		print('BLACK CUOAHFFEE')
		
	elif coffeeType == 1:
		print('ONE CREAM')
		pyautogui.press('c')
		
	elif coffeeType == 2:
		print('MILKN THREE SUGAR')
		pyautogui.press('c')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 3:
		print('FOAR SUGAR')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 4:
		print('CREAMY SUGAR')
		pyautogui.press('c')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 5:
		print('ONE LUMP PLZ')
		pyautogui.press('s')
		
	elif coffeeType == 6:
		print('TWO LUMP PLZ')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 7:
		print('CREAM AND A LUMP')
		pyautogui.press('c')
		pyautogui.press('s')
		
	elif coffeeType == 8:
		print('CREAM AND FOUR LUMPS')
		pyautogui.press('c')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 9:
		print('THREEEEEEE LUMPS')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		
	elif coffeeType == 10:
		print('CREAM AND FIVE LUMPS')
		pyautogui.press('c')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		pyautogui.press('s')
		
		
	pyautogui.press('enter')
	return
