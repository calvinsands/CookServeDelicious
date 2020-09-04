import pyautogui, time, sys

from constants import center_region
from constants import recipe_region
from constants import full_recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True



def robber(num):
	robberimg = None
	while True:
		for robberType in range(9):
			#print(robberType)
			if robberType == 8:
				print('No robber type found.')
				pyautogui.screenshot('robberimg'+str(robberType)+'.png', region=full_recipe_region)
				print('New robber saved as robberimg'+str(robberType)+'.png')
				print('Exiting.')
				sys.exit()
			robberimg = pyautogui.locateOnScreen('robberimg' + str(robberType) + '.png', region=full_recipe_region, grayscale=True)
			if robberimg:
				break
		
		if robberType == 0:
			pyautogui.press('h')
			
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			break
			
		if robberType == 1:
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			pyautogui.press('y')
			pyautogui.press('y')
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			break
		
		if robberType == 2:
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			pyautogui.press('y')
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			pyautogui.press('l')
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			break
		
		if robberType == 3:
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			break

		if robberType == 4:
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			
			pyautogui.press('l')
			pyautogui.press('l')
			
			pyautogui.press('f')
			break

		if robberType == 5:
			pyautogui.press('h')
			
			pyautogui.press('y')
			pyautogui.press('y')
			
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			break

		if robberType == 6:
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			pyautogui.press('y')
			pyautogui.press('y')
			pyautogui.press('y')
			
			pyautogui.press('e')
			pyautogui.press('e')
			
			pyautogui.press('n')
			pyautogui.press('n')
			
			pyautogui.press('l')
			
			pyautogui.press('f')
			pyautogui.press('f')
			pyautogui.press('f')
			break

		if robberType == 7:
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			pyautogui.press('h')
			
			pyautogui.press('y')
			pyautogui.press('y')
			
			pyautogui.press('e')
			
			pyautogui.press('n')
			
			pyautogui.press('l')
			pyautogui.press('l')
			pyautogui.press('l')
			
			pyautogui.press('f')
			break

	pyautogui.press('enter')
	time.sleep(1)
	return