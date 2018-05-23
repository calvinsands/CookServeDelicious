import pyautogui, time, sys
import Corndog, Soda, Soup, Chicken, Fish, Salad, Icecream, Wine, Pizza, Fries
import Robber
import Hamburger, Lasagna, Nachos

from constants import center_region
from constants import recipe_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True


def toilet(num):
	print('Toilet')
	pyautogui.press('down')
	pyautogui.press('s')
	pyautogui.press('enter')
	time.sleep(1)
	return

def rat(num):
	print('Rat')
	pyautogui.press('right')
	pyautogui.press('down')
	pyautogui.press('c')
	pyautogui.press('s')
	pyautogui.press('enter')
	time.sleep(1)
	return
	
def trash(num):
	print('Trash')
	for itrash in range(2):
		pyautogui.press('up')
		time.sleep(0.32)
		pyautogui.press('right')
		time.sleep(0.32)
	pyautogui.press('s')
	pyautogui.press('enter')
	time.sleep(1)
	return
	
def dishes(num):
	print('Dishes')
	for idish in range(3):
		pyautogui.press('left')
		pyautogui.press('right')
		pyautogui.press('left')
		pyautogui.press('right')
		pyautogui.press('up')
	time.sleep(1)
	return



taskDict = {
	0: Corndog.corndog,
	1: Soda.soda,
	2: Soup.soup,
	3: Chicken.chicken,
	4: Fish.fish,
	5: Salad.salad,
	6: Icecream.icecream,
	7: Wine.wine,
	8: Pizza.pizza,
	9: Fries.fries,
	10: Robber.robber,
	11: toilet,
	12: rat,
	13: trash,
	14: dishes
}

def whichTask(num):
	print('Found notification at ' + str(num))

	while True:
		food_type = None

		run_time = list()
		
		
		# Center pic loop, #0-#14
		for task_index in range(len(taskDict)):
			start = time.time()
			food_type = pyautogui.locateOnScreen('FoodTaskImg'+str(task_index)+'.png', region=center_region)
			run_time.append(time.time() - start)
			if food_type:
				taskDict[task_index](num)
				return
		

		#15
		start = time.time()
		food_type = pyautogui.locateOnScreen('hamburger'+str(num)+'.png', region=(140,(40+83*num),280,90), grayscale=True)
		run_time.append(time.time() - start)
		if food_type:
			if food[num-1] == 'hamburger':
				Hamburger.hamburgerIngredients(num)
			else:
				Hamburger.hamburgerMeat(num)
			return

		#16
		start = time.time()
		food_type = pyautogui.locateOnScreen('lasagna.png', region=(1290,213,400,1), grayscale=True)
		run_time.append(time.time() - start)
		if food_type:
			Lasagna.lasagna(num)
			return

		#17
		start = time.time()
		food_type = pyautogui.locateOnScreen('nachos'+str(num)+'.png', region=(140,(40+83*num),280,90), grayscale=True)
		run_time.append(time.time() - start)
		print(food_type)
		if food_type:
			if food[num-1] == 'nachos':
				Nachos.nachosIngredients(num)
			else:
				Nachos.nachosMeat(num)
			return

		#18
		start = time.time()
		#food_type = pyautogui.locateOnScreen('thumb.png', region=recipe_region, grayscale=True)
		run_time.append(time.time() - start)
		if food_type:
			pyautogui.press('t')
			pyautogui.press('enter')
			time.sleep(1)
			return

		print('Failing to find order/task.')
		for i in range(18):
			if run_time[i] > run_time[i+1]:
				worst = i
		print('Worst run_time was ' + str(i) + ' at ' + str(run_time[i]) + ' seconds.')
	
	return