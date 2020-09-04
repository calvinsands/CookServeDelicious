import pyautogui, time, sys
import Corndog, Soda, Soup, Chicken, Fish, Salad, Icecream, Wine, Pizza, Fries, Steak, Sopapillas, Friedchicken
import Beer, Pretzel, Lasagna, Sushi, Kabob, Coffee, Enchilada, Rice, Hash, Biscuit, Bananas
import Robber
import Hamburger, Nachos, Potato, Pasta, Pancake, Lobster

from constants import center_region
from constants import recipe_region
from constants import offset_center_region
from constants import upper_center_region
from constants import ingr_center_region

from constants import MAX_ORDERS

from constants import clock
from constants import food
from constants import foodOrder

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 400  # Set Duration To 1000 ms == 1 second

pyautogui.PAUSE = 0.075
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
		pyautogui.press('up')
	time.sleep(1)
	return



taskDict = {
	0: Wine.wine,
	1: Soda.soda,
	2: Soup.soup,
	3: Chicken.chicken,
	4: Fish.fish,
	5: Salad.salad,
	6: Steak.steak,
	7: Lasagna.lasagna,
	8: Pizza.pizza,
	9: Sushi.sushi,
	10: Kabob.kabob,
	11: Rice.rice,
	12: Bananas.bananas,
	13: trash,
	14: dishes,
	15: Icecream.icecream,
	16: Sopapillas.sopapillas,
	17: Friedchicken.friedchicken,
	18: Beer.beer,
	19: Pretzel.pretzel,
	20: Robber.robber,
	21: Lasagna.lasagna, # event lasagna
	22: Fries.fries,
	23: Corndog.corndog,
	24: Coffee.coffee,
	25: Fries.fries, # event fries
	26: Enchilada.enchilada,
	27: toilet,
	28: Hash.hash,
	29: Biscuit.biscuit,
	30: rat,
	31: Fries.fries # more event fries
}

def whichTask(num):
	print('Found notification at ' + str(num))

	while True:
		food_type = None

		
		food_type = pyautogui.locateOnScreen('hamburger.png', region=(1356,213,124,1), grayscale=True)
		if food_type:
			if food[num-1] == 'hamburger':
				Hamburger.hamburgerIngredients(num)
			else:
				Hamburger.hamburgerMeat(num)
			return
		
		
		food_type = pyautogui.locateOnScreen('lobster.png', region=upper_center_region)
		if food_type:
			if food[num-1] == 'lobster':
				Lobster.lobsterIngredients(num)
				return
		food_type = pyautogui.locateOnScreen('lobstercook.png', region=ingr_center_region)
		if food_type:
			Lobster.lobsterCook(num)
			return
		
		
		food_type = pyautogui.locateOnScreen('pasta.png', region=center_region)
		if food_type:
			if food[num-1] == 'pasta':
				Pasta.pastaIngredients(num)
				return
		food_type = pyautogui.locateOnScreen('pastacook.png', region=ingr_center_region)
		if food_type:
			Pasta.pastaCook(num)
			return
		
		
		
		# This loop uses the dictionary index above ^
		for task_index in range(len(taskDict)):
		
			if (task_index==22 or task_index==16 or task_index==17 or task_index==25 or task_index==28 or task_index==31):
				food_type = pyautogui.locateOnScreen('FoodTaskImg'+str(task_index)+'.png', region = offset_center_region, grayscale=True)
			elif (task_index==23 or task_index==19):
				food_type = pyautogui.locateOnScreen('FoodTaskImg'+str(task_index)+'.png', region = upper_center_region, grayscale=True)
			elif (task_index==2 or task_index==7 or task_index==21 or task_index==10):
				food_type = pyautogui.locateOnScreen('FoodTaskImg'+str(task_index)+'.png', region = ingr_center_region, grayscale=True)
			else:
				food_type = pyautogui.locateOnScreen('FoodTaskImg'+str(task_index)+'.png', region = center_region, grayscale=True)

			if food_type:
				taskDict[task_index](num)
				return
			
			
		food_type = pyautogui.locateOnScreen('pancake.png', region=center_region)
		if food_type:
			if food[num-1] == 'pancake':
				Pancake.pancakeIngredients(num)
				return
		food_type = pyautogui.locateOnScreen('pancakeCook.png', region=ingr_center_region)
		if food_type:
			Pancake.pancakeCook(num)
			return
			
			
		food_type = pyautogui.locateOnScreen('nachos.png', region=center_region, grayscale=True)
		if food_type:
			if food[num-1] == 'nachos':
				Nachos.nachosIngredients(num, 1)
			else:
				Nachos.nachosIngredients(num, 0)
			return
		food_type = pyautogui.locateOnScreen('nachosMeat.png', region=ingr_center_region)
		if food_type:
			Nachos.nachosMeat(num)
			return
		food_type = pyautogui.locateOnScreen('nachosMeatevent.png', region=ingr_center_region)
		if food_type:
			Nachos.nachosMeat(num)
			return
		
		
		food_type = pyautogui.locateOnScreen('potato.png', region=center_region)
		if food_type:
			if food[num-1] == 'potato':
				Potato.potatoIngredients(num)
				return
		food_type = pyautogui.locateOnScreen('potatocook.png', region=(1750,150,15,15))
		if food_type:
			Potato.potatoCook(num)
			return

			
		food_type = pyautogui.locateOnScreen('thumb.png', region=recipe_region, grayscale=True)
		if food_type:
			pyautogui.press('t')
			pyautogui.press('enter')
			time.sleep(1)
			return

			
		food_type = pyautogui.locateOnScreen('love.png', region=recipe_region, grayscale=True)
		if food_type:
			pyautogui.press('z')
			time.sleep(1)
			pyautogui.press('x')
			"""
			while True:
				print('I NEED AN ADULT')
				winsound.Beep(frequency, duration)
				time.sleep(0.5)
				if pyautogui.locateOnScreen('potatocook.png', region=(1750,150,15,15)):
					break
			"""
			time.sleep(1)
			return
		
		
		
		print('Failing to find order/task.')
		"""
		for i in range(18):
			if run_time[i] > run_time[i+1]:
				worst = i
		print('Worst run_time was ' + str(i) + ' at ' + str(run_time[i]) + ' seconds.')
		"""
	
	return