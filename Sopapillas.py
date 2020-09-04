import pyautogui, time, sys

from constants import center_region
from constants import recipe_region

pyautogui.PAUSE = 0.075
pyautogui.FAILSAFE = True


def sopapillas(num):

	sopapillasimg = None
	for sopapillasType in range(5):
		#print(sopapillasType)
		if sopapillasType == 4:
			print('No sopapillas type found.')
			pyautogui.screenshot('sopapillasimg'+str(sopapillasType)+'.png', region=recipe_region)
			print('New sopapillas saved as sopapillasimg'+str(sopapillasType)+'.png')
			print('Exiting.')
			sys.exit()
		sopapillasimg = pyautogui.locateOnScreen('sopapillasimg' + str(sopapillasType) + '.png', region=recipe_region, grayscale=True)
		if sopapillasimg:
			break

	pyautogui.keyDown('down')
	time.sleep(2.75)
	pyautogui.keyUp('down')
	pyautogui.press('p')
	
	while True:
		
		if sopapillasType == 0 or sopapillasType == 3:
			print('AZUCAR')
			pyautogui.press('s')
			break

		elif sopapillasType == 1 or sopapillasType == 2:
			print('YOU GET NOTHING.')
			break
	
	pyautogui.press('enter')
	return