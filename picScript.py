#0: corndog,
#1: soda,
#2: soup,
#3: chicken,
#4: fish,
#5: salad,
#6: icecream,
#7: wine,
#8: pizza,
#9: fries,
#10: robber,
#11: toilet,
#12: rat,
#13: trash,
#14: dishes
#
#15: hamburger
#16: lasagna
#17: nachos
#18: thumb

center_region = (760,555,30,30)
recipe_region = (470,840,850,1)

def snapLibImage(input_string, quantity):

	for i in range(3):
		time.sleep(1)
		print(3-i)
	print('Go.')
	
	for i in range(quantity):
		print(i)
		# /food/foodimg0.png
		pyautogui.screenshot(input_string + 'img' + str(i) + '.png', region=recipe_region)
		time.sleep(.5)
		pyautogui.press('ctrlleft')
		time.sleep(.5)
	print('Done')
	return

def snapCenterLibImage(number):

	for i in range(3):
		print(3-i)
		time.sleep(0.5)
	print('Go.')
	
	pyautogui.screenshot('FoodTaskImg'+str(number)+'.png', region=center_region)
	
	print('Done')
	return

import pyautogui, time, sys

while True:
	print('\nStart.')
	photo = input('1 for taking Lib pictures, 2 for Center WhichTask pictures: ')
	
	if photo == '1':
		input_string = input('Which food or task: ')
		quantity = input('How many recipes: ')
		snapLibImage(input_string, int(quantity))
	
	elif photo == '2':
		number = input('Which food or task number is it? <FoodTaskImg[number].png>: ')
		snapCenterLibImage(number)
		
	else:
		print('Try again.')
