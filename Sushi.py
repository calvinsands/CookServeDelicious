import pyautogui, time, sys

from constants import center_region
from constants import recipe_region


pyautogui.FAILSAFE = True


def sushi(num):

	pyautogui.PAUSE = 0.05
	
	sushiimg = None
	while True:
		for sushiType in range(22):
			if sushiType == 21:
				break
			sushiimg = pyautogui.locateOnScreen('sushiimg' + str(sushiType) + '.png', region=recipe_region, grayscale=True)
			if sushiimg:
				break
		
		if sushiType == 0:
			print('Standard Sampler')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			break

		elif sushiType == 1:
			print('Roe Special')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			break

		elif sushiType == 2:
			print('Tuna Platter')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('u')
			break

		elif sushiType == 3:
			print('Ebi Special')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			break

		elif sushiType == 4:
			print('Ocean Plate')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			break

		elif sushiType == 5:
			print('Sea Spirit')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			break

		elif sushiType == 6:
			print('Mixed Delicious')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			break

		elif sushiType == 7:
			print('Toro Special')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			break

		elif sushiType == 8:
			print('Salmon Special')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 9:
			print('Fives Delight')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 10:
			print('Delight Platter')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 11:
			print('Plate of Great')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 12:
			print('ETS Tray')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 13:
			print('Shogun Plate')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 14:
			print('East Sampler')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('s')
			break

		elif sushiType == 15:
			print('Mackerel Special')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			break

		elif sushiType == 16:
			print('Gourmet Platter')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('m')
			pyautogui.press('m')
			break

		elif sushiType == 17:
			print('Special Sampler')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('m')
			pyautogui.press('m')
			break

		elif sushiType == 18:
			print('The Mix')
			pyautogui.press('e')
			pyautogui.press('t')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('m')
			pyautogui.press('m')
			pyautogui.press('m')
			break

		elif sushiType == 19:
			print('Rice Sampler')
			pyautogui.press('e')
			pyautogui.press('e')
			pyautogui.press('t')
			pyautogui.press('t')
			pyautogui.press('s')
			pyautogui.press('s')
			pyautogui.press('m')
			pyautogui.press('m')
			break

		elif sushiType == 20:
			print('Chomper Plate')
			pyautogui.press('e')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('r')
			pyautogui.press('u')
			pyautogui.press('u')
			pyautogui.press('s')
			pyautogui.press('m')
			break

		else:
			print('No sushi found')


	pyautogui.press('enter')
	pyautogui.PAUSE = 0.075
	return