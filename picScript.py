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
#15: steak
#16: sopapillas
#17: friedchicken
#
#17: hamburger
#18: lasagna
#19: nachos
#20: thumb

center_region = (760,555,30,30)
recipe_region = (470,840,850,1)
offset_center_region = (860,500,30,30) # for the frier
upper_center_region = (760,450,30,30) # for corndog, pretzel
ingr_center_region = (1290,213,400,1)



def snapLibImage(input_string, quantity):

	for i in range(3):
		print(3-i)
		time.sleep(1)
	comeback = pyautogui.position()
	pyautogui.click((800,125))
	pyautogui.moveTo(comeback)
	print('Go.')
	
	for i in range(quantity):
		# /food/foodimg0.png
		pyautogui.screenshot(input_string + 'img' + str(i) + '.png', region=recipe_region)
		time.sleep(.5)
		print(i+1)
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
	
def snapIngrLibImage(variable):

	for i in range(3):
		print(3-i)
		time.sleep(0.5)
	print('Go.')
	
	pyautogui.screenshot(variable+'.png', region=ingr_center_region)
	
	print('Done')
	return

import pyautogui, time, sys

while True:
	print('\nStart.')
	photo = input('1 for taking Lib pictures, 2 for Center WhichTask pictures, 3 Ingr_Center WhichTask pictures: ')
	
	if photo == '1':
		input_string = input('Which food or task: ')
		quantity = input('How many recipes: ')
		snapLibImage(input_string, int(quantity))
	
	elif photo == '2':
		number = input('Which food or task number is it? <FoodTaskImg[number].png>: ')
		snapCenterLibImage(number)
		
	elif photo == '3':
		choice = input('Is this a 1)FoodTaskImg or a 2)string input?: ')
		if choice == '1':
			number = input('FoodTaskImg. Which index number?: ')
			snapIngrLibImage('FoodTaskImg' + number)
		elif choice == '2':
			string = input('What food is it?: ')
			snapIngrLibImage(string)
		
	else:
		print('Try again.')
