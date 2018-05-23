# 130 - 210
# 210 - 300
# 300 - 390
# 390 - 480
# 890, 270
# 1000, 380

#710,280
#880,450

#740,520
#850,580

import pyautogui, time, sys

MAX_ORDERS = 6

pyautogui.PAUSE = 0.09
pyautogui.FAILSAFE = True

for i in range(3):
    print(3-i)
    time.sleep(1)
print('Go!')

def whichFood(num):
    print('Found food/task at ' + str(num))

    while True:
        foodType = None

        runTime = list()

        #1
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('corndog.png', region=(660,500,120,150), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            corndog()
            return

        #2
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('hamburger'+str(num)+'.png', region=(140,(40+83*num),280,90), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            if food[num-1] == 'hamburger':
                hamburgerIngredients(num)
            else:
                hamburgerMeat(num)
            return

        #3
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('soda.png', region=(400,220,200,200), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            soda()
            return

        #4
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('soup.png', region=(700,350,100,200), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            soup(num)
            return

        #5
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('lasagna.png', region=(1290,190,400,60), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            lasagna(num)
            return

        #6
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('chicken.png', region=(680,470,50,40), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            chicken(num)
            return

        #7
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('fish.png', region=(412,649,40,40), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            fish(num)
            return

        #8
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('salad.png', region=(635,252,50,50), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            salad()
            return

        #9
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('icecream.png', region=(776,675,35,55), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            icecream()
            return

        #10
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('wine.png', region=(795,607,20,80), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            wine()
            return

        #11
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('pizza.png', region=(920,630,15,40), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            pizza(num)
            return

        #12
        start = time.time()
        foodType = pyautogui.locateOnScreen('fries.png', region=(880,610,30,40), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            fries()
            return

        #13
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('nachos'+str(num)+'.png', region=(140,(40+83*num),280,90), grayscale=True)
        runTime.append(time.time() - start)
        print(foodType)
        if foodType:
            if food[num-1] == 'nachos':
                nachosIngredients(num)
            else:
                nachosMeat(num)
            return
        

        #14
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('robber.png', region=(611,312,55,65), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            robber()
            return

        #15
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('toilet.png', region=(890,270,110,110), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            print('Toilet')
            pyautogui.press('down')
            pyautogui.press('s')
            pyautogui.press('enter')
            time.sleep(1)
            return

        #16
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('rat.png', region=(740,520,100,80), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            print('Rat')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('c')
            pyautogui.press('s')
            pyautogui.press('enter')
            time.sleep(1)
            return

        #17
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('garbage.png', region=(880,540,130,90), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
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

        #18
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('dishes.png', region=(710,280,170,170), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            for idish in range(3):
                pyautogui.press('left')
                pyautogui.press('right')
                pyautogui.press('left')
                pyautogui.press('right')
                pyautogui.press('up')
            time.sleep(1)
            return

        #19
        start = time.time()
        foodType = pyautogui.locateCenterOnScreen('thumb.png', region=(456,814,475,45), grayscale=True)
        runTime.append(time.time() - start)
        if foodType:
            pyautogui.press('t')
            pyautogui.press('enter')
            time.sleep(1)
            return

        print('Failing to find order/task.')
        for i in range(18):
            if runTime[i] > runTime[i+1]:
                worst = i
        print('Worst runtime was ' + str(i) + ' at ' + str(runTime[i]) + ' seconds.')
            
def robber():
    robberimg = None
    while True:
        for robberType in range(9):
            #print(robberType)
            if robberType == 8:
                print('No robber type found.')
                pyautogui.screenshot('robberimg'+str(robberType)+'.png', region=(460,870,1020,80))
                print('New robber saved as robberimg'+str(robberType)+'.png')
                print('Exiting.')
                sys.exit()
            robberimg = pyautogui.locateCenterOnScreen('robberimg' + str(robberType) + '.png', region=(460,870,1020,80), grayscale=True)
            if robberimg:
                break
        
        if robberType == 0:
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
        
        if robberType == 1:
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
        
        if robberType == 2:
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
            
            pyautogui.press('y')
            pyautogui.press('y')
            
            pyautogui.press('e')
            
            pyautogui.press('n')
            pyautogui.press('n')
            
            pyautogui.press('l')
            
            pyautogui.press('f')
            pyautogui.press('f')
            break

        if robberType == 5:
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

        if robberType == 6:
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

        if robberType == 7:
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

    pyautogui.press('enter')
    time.sleep(1)
    return

def corndog():
    print('Corndog found')
    dogType = None

    while True:
        dogType = pyautogui.locateCenterOnScreen('textTheClassicCornDog.png', region=(440,800,900,180), grayscale=True)
        if dogType:
            print('Classic: ketchup, mustard.')
            pyautogui.press('k')
            pyautogui.press('m')
            pyautogui.press('enter')
            return

        dogType = pyautogui.locateCenterOnScreen('textTheYellowDog.png', region=(440,800,900,180), grayscale=True)
        if dogType:
            print('Yellow: mustard.')
            pyautogui.press('m')
            pyautogui.press('enter')
            return

        dogType = pyautogui.locateCenterOnScreen('textTheRedDog.png', region=(440,800,900,180), grayscale=True)
        if dogType:
            print('Red: ketchup.')
            pyautogui.press('k')
            pyautogui.press('enter')
            return

        print('No corndog type found.')


def hamburgerIngredients(num):
    print('Hamburger Step 2')
    global food
    global foodOrder
    global clock
    food[num-1] = None
    clock[num-1] = 0.0

    if foodOrder[num-1] == 'The Original':
        print('The Original: Meat, Lettuce, Bacon, Cheese, Tomatoes')
        pyautogui.press('m')
        pyautogui.press('l')
        pyautogui.press('b')
        pyautogui.press('c')
        pyautogui.press('t')

    elif foodOrder[num-1] == 'The Double':
        print('The Double: Meat (2x), Lettuce, Bacon, Cheese, Tomatoes')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('l')
        pyautogui.press('b')
        pyautogui.press('c')
        pyautogui.press('t')

    elif foodOrder[num-1] == 'The HEARTSTOPPER!':
        print('The HEARTSTOPPER!: Meat (2x), Bacon (2x), Cheese')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('b')
        pyautogui.press('b')
        pyautogui.press('c')

    elif foodOrder[num-1] == 'The Lite Delight':
        print('The Lite Delight: Meat and Lettuce only')
        pyautogui.press('m')
        pyautogui.press('l')

    elif foodOrder[num-1] == 'The Ryan Davis':
        print('The Ryan Davis: Meat, Bacon, Cheese (2x), Tomatoes')
        pyautogui.press('m')
        pyautogui.press('b')
        pyautogui.press('c')
        pyautogui.press('c')
        pyautogui.press('t')

    elif foodOrder[num-1] == 'The Lonely Patty':
        print('The Lonely Patty: Meat only')
        pyautogui.press('m')

    elif foodOrder[num-1] == 'The Triple':
        print('The Triple: Meat (3x) and Cheese')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('c')

    elif foodOrder[num-1] == 'The Triple with Bacon':
        print('The Triple: Meat (3x), Bacon and Cheese')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('m')
        pyautogui.press('b')
        pyautogui.press('c')

    elif foodOrder[num-1] == 'The RED':
        print('The RED: Meat and Tomatoes only')
        pyautogui.press('m')
        pyautogui.press('t')
        
    else:
        print('No order found.')

    
    foodOrder[num-1] = None
    pyautogui.press('enter')
    time.sleep(0.5)
    return


def hamburgerMeat(num):
    print('Hamburger Step 1')
    global food
    global foodOrder
    global clock
    food[num-1] = 'hamburger'

    burgerType = None

    while True:
        burgerimg = None
        for burgerType in range(12):
            #print(burgerType)
            burgerimg = pyautogui.locateCenterOnScreen('burgerimg' + str(burgerType) + '.png', region=(540,815,180,20), grayscale=True)
            if burgerimg:
                break
            if burgerType == 11:
                print('No burger type found')
        
        if burgerType == 0:
            print('The Original: One meat patty')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Original'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 1:
            print('The Double: Two meat patties')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Double'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 2:
            print('BLT: Bacon, lettuce, tomatoe')
            pyautogui.press('b')
            pyautogui.press('l')
            pyautogui.press('t')
            pyautogui.press('enter')
            food[num-1] = None
            time.sleep(0.5)
            return

        elif burgerType == 3:
            print('BLT & C: Bacon, lettuce, tomatoe, cheese')
            pyautogui.press('b')
            pyautogui.press('l')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('enter')
            food[num-1] = None
            time.sleep(0.5)
            return

        elif burgerType == 4:
            print('The HEARTSTOPPER!: Two meat patties')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The HEARTSTOPPER!'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 5:
            print('The Lite Delight: One meat patty')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Lite Delight'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 6:
            print('The Ryan Davis: One meat patty')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Ryan Davis'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 7:
            print('The Tumbleweed: Bacon and cheese')
            pyautogui.press('b')
            pyautogui.press('c')
            pyautogui.press('enter')
            food[num-1] = None
            time.sleep(0.5)
            return

        elif burgerType == 8:
            print('The Lonely Patty: One meat patty')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Lonely Patty'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 9:
            print('The Triple: Three meat patties')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Triple'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 10:
            print('The Triple with Bacon: Three meat patties')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Triple with Bacon'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif burgerType == 11:
            print('The RED: One meat patty')
            pyautogui.press('m')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The RED'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return
    
        print('No burger meat type found.')
    



def soda():
    sodaimg = None
    while True:
        for sodaType in range(42):
            #print(sodaType)
            sodaimg = pyautogui.locateCenterOnScreen('sodaimg' + str(sodaType) + '.png', region=(480,840,710,1), grayscale=True)
            if sodaimg:
                break
            if sodaType == 41:
                print('No soda type found')
                return
        
        if sodaType == 0:
            print('Small Cola')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 1:
            print('Small Grape')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 2:
            print('Small Diet')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 3:
            print('Small Cola (no ice)')
            pyautogui.press('down')
            break

        elif sodaType == 4:
            print('Small Water')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 5:
            print('Small Tea')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 6:
            print('Medium Cola')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 7:
            print('Medium Grape')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 8:
            print('Medium Diet')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 9:
            print('Medium Cola (no ice)')
            pyautogui.press('up')
            pyautogui.press('down')
            break

        elif sodaType == 10:
            print('Medium Water')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 11:
            print('Medium Tea')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 12:
            print('Large Cola')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 13:
            print('Large Grape')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 14:
            print('Large Diet')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 15:
            print('Large Cola (no ice)')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('down')
            break

        elif sodaType == 16:
            print('Large Water')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 17:
            print('Large Tea')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 18:
            print('Jumbo Cola')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 19:
            print('Jumbo Grape')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 20:
            print('Jumbo Diet')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 21:
            print('Jumbo Cola (no ice)')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('down')
            break

        elif sodaType == 22:
            print('Jumbo Water')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 23:
            print('Jumbo Tea')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            break

        elif sodaType == 24:
            print('Jumbo Cola w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 25:
            print('Jumbo Grape w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 26:
            print('Jumbo Diet w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 27:
            print('Jumbo Cola (no ice) w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 28:
            print('Jumbo Water w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 29:
            print('Jumbo Tea w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 30:
            print('Small Cola w/Flavor Blast')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 31:
            print('Small Grape w/Flavor Blast')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 32:
            print('Small Diet w/Flavor Blast')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 33:
            print('Small Cola (no ice) w/Flavor Blast')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 34:
            print('Small Water w/Flavor Blast')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 35:
            print('Small Tea w/Flavor Blast')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 36:
            print('Medium Cola w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 37:
            print('Medium Grape w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 38:
            print('Medium Diet w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 39:
            print('Large Cola w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 40:
            print('Large Grape w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        elif sodaType == 41:
            print('Large Diet w/Flavor Blast')
            pyautogui.press('up')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('i')
            pyautogui.press('down')
            pyautogui.press('f')
            break

        else:
            print('No soda found')


    pyautogui.press('enter')
    return
        
        
def soup(num):
    global food
    global clock
    
    soupimg = None
    for soupType in range(2):
        #print(soupType)
        soupimg = pyautogui.locateCenterOnScreen('soupimg' + str(soupType) + '.png', region=(440,800,100,80), grayscale=True)
        if soupimg:
            break
        if soupType == 1:
            print('No soup type found')
            return

    food[num-1] = 'soup'
    while True:
        
        if soupType == 0:
            pyautogui.press('k')
            pyautogui.press('w')
            pyautogui.press('u')
            pyautogui.press('space')
            pyautogui.press('y')
            for cut in range(3):
                pyautogui.press('down')
                time.sleep(0.15)
            break

        elif soupType == 1:
            pyautogui.press('w')
            pyautogui.press('u')
            pyautogui.press('s')
            pyautogui.press('space')
            pyautogui.press('t')
            for cut in range(3):
                pyautogui.press('down')
                time.sleep(0.15)
            pyautogui.press('a')
            for cut in range(3):
                pyautogui.press('down')
                time.sleep(0.15)
            pyautogui.press('y')
            for cut in range(3):
                pyautogui.press('down')
                time.sleep(0.15)
            break

        else:
            print('No soup found.')

    
    pyautogui.press('enter')
    temp = time.time()
    temp = float(temp)
    clock[num-1] = temp
    return


def lasagna(num):
    global food
    global clock

    lasagnaimg = None
    for lasagnaType in range(2):
        #print(lasagnaType)
        lasagnaimg = pyautogui.locateCenterOnScreen('lasagnaimg' + str(lasagnaType) + '.png', region=(480,840,710,1), grayscale=True)
        if lasagnaimg:
            break
        if lasagnaType == 1:
            print('No lasagna type found')
            return

    food[num-1] = 'lasagna'

    while True:
        
        if lasagnaType == 0:
            for lasindex in range(3):
                pyautogui.press('p')
                pyautogui.press('s')
                pyautogui.press('c')
                pyautogui.press('r')
            break

        if lasagnaType == 1:
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
    
    pyautogui.press('enter')
    temp = time.time()
    temp = float(temp)
    clock[num-1] = temp
    return


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

def fish(num):
    global food
    global clock
    
    food[num-1] = 'fish'

    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('s')
    pyautogui.press('enter')
    temp = time.time()
    temp = float(temp)
    clock[num-1] = temp
    return

def salad():
    saladimg = None
    while True:
        for saladType in range(12):
            #print(saladType)
            saladimg = pyautogui.locateCenterOnScreen('saladimg' + str(saladType) + '.png', region=(565,825,110,20), grayscale=True)
            if saladimg:
                break
            if saladType == 17:
                print('No salad type found')
                return
        
        if saladType == 0:
            print('House Salad')
            pyautogui.press('r')
            pyautogui.press('c')
            pyautogui.press('b')
            break

        elif saladType == 1:
            print('Cheesy Leaves')
            pyautogui.press('r')
            pyautogui.press('c')
            break

        elif saladType == 2:
            print('Pepper Ranch')
            pyautogui.press('r')
            pyautogui.press('c')
            pyautogui.press('o')
            break

        elif saladType == 3:
            print('The Dry Greens')
            pyautogui.press('g')
            break

        elif saladType == 4:
            print('The Dry Deluxe')
            pyautogui.press('m')
            pyautogui.press('g')
            break

        elif saladType == 5:
            print('Kids Delight')
            pyautogui.press('r')
            pyautogui.press('c')
            break

        elif saladType == 6:
            print('The Manhattan')
            pyautogui.press('r')
            pyautogui.press('c')
            pyautogui.press('b')
            pyautogui.press('o')
            pyautogui.press('m')
            pyautogui.press('g')
            break

        elif saladType == 7:
            print('The Mix')
            pyautogui.press('r')
            pyautogui.press('c')
            pyautogui.press('b')
            pyautogui.press('o')
            break

        elif saladType == 8:
            print('Tomato Ranch')
            pyautogui.press('r')
            pyautogui.press('c')
            pyautogui.press('m')
            break

        elif saladType == 9:
            print('The Big Salad')
            pyautogui.press('c')
            pyautogui.press('g')
            break

        elif saladType == 10:
            print('Cheesy Peppers')
            pyautogui.press('c')
            pyautogui.press('o')
            break

        elif saladType == 11:
            print('Salad Verde')
            pyautogui.press('r')
            pyautogui.press('g')
            break

        else:
            print('No salad found')


    pyautogui.press('enter')
    return

def icecream():
    icecreamimg = None
    while True:
        for icecreamType in range(6):
            #print(icecreamType)
            icecreamimg = pyautogui.locateCenterOnScreen('icecreamimg' + str(icecreamType) + '.png', region=(480,840,710,1), grayscale=True)
            if icecreamimg:
                break
            if icecreamType == 5:
                print('No ice cream type found')
                return
        
        if icecreamType == 0:
            print('Plain Vanilla')
            pyautogui.press('v')
            pyautogui.press('v')
            pyautogui.press('v')
            break

        elif icecreamType == 1:
            print('Plain Chocolate')
            pyautogui.press('c')
            pyautogui.press('c')
            pyautogui.press('c')
            break

        elif icecreamType == 2:
            print('Vanilla and Chocolate')
            pyautogui.press('v')
            pyautogui.press('c')
            break

        elif icecreamType == 3:
            print('The Yin and Yang')
            pyautogui.press('v')
            pyautogui.press('c')
            pyautogui.press('h')
            pyautogui.press('p')
            break

        elif icecreamType == 4:
            print('Cherry Vanilla')
            pyautogui.press('v')
            pyautogui.press('v')
            pyautogui.press('c')
            break

        elif icecreamType == 5:
            print('Chocolate Sprinkles')
            pyautogui.press('c')
            pyautogui.press('c')
            pyautogui.press('p')
            break

        else:
            print('No ice cream found')


    pyautogui.press('enter')
    return


def wine():

    wineimg = None
    for wineType in range(3):
        #print(wineType)
        if wineType == 2:
            print('No wine type found.')
            pyautogui.screenshot('wineimg'+str(wineType)+'.png', region=(480,840,400,1))
            print('New wine saved as wineimg'+str(wineType)+'.png')
            print('Exiting.')
            sys.exit()
        wineimg = pyautogui.locateCenterOnScreen('wineimg' + str(wineType) + '.png', region=(480,840,400,1), grayscale=True)
        if wineimg:
            break

    for windex in range(wineType):
        pyautogui.press('w')

    for windex in range(27):
        pyautogui.press('up')
        
    pyautogui.press('enter')
    return


def pizza(num):
    global food
    global clock
    
    pizzaimg = None
    for pizzaType in range(12):
        #print(pizzaType)
        pizzaimg = pyautogui.locateCenterOnScreen('pizzaimg' + str(pizzaType) + '.png', region=(480,840,710,1), grayscale=True)
        if pizzaimg:
            break
        if pizzaType == 11:
            print('No pizza type found')
            return

    food[num-1] = 'pizza'
    while True:
        
        if pizzaType == 0:
            print('Pepperoni Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('p')
            break

        elif pizzaType == 1:
            print('Cheese Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            break

        elif pizzaType == 2:
            print('Meat Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('m')
            break

        elif pizzaType == 3:
            print('P&M Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('p')
            pyautogui.press('m')
            break

        elif pizzaType == 4:
            print('Cheesy Bread')
            pyautogui.press('c')
            break

        elif pizzaType == 5:
            print('Meatlovers Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('p')
            pyautogui.press('m')
            pyautogui.press('b')
            break

        elif pizzaType == 6:
            print('Veggie Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('u')
            pyautogui.press('v')
            pyautogui.press('n')
            break

        elif pizzaType == 7:
            print('Deluxe Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('p')
            pyautogui.press('m')
            pyautogui.press('b')
            pyautogui.press('u')
            pyautogui.press('v')
            pyautogui.press('n')
            break

        elif pizzaType == 8:
            print('Italian Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('m')
            pyautogui.press('u')
            pyautogui.press('v')
            pyautogui.press('n')
            break

        elif pizzaType == 9:
            print('Bacon and Mushroom Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('b')
            pyautogui.press('u')
            break

        elif pizzaType == 10:
            print('Olives and Onions Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('v')
            pyautogui.press('n')
            break

        elif pizzaType == 11:
            print('The PCGB Pizza')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('p')
            pyautogui.press('b')
            pyautogui.press('n')
            break

        else:
            print('No pizza found.')

    
    pyautogui.press('enter')
    temp = time.time()
    temp = float(temp)
    clock[num-1] = temp
    return


def fries():

    friesimg = None
    for friesType in range(5):
        #print(friesType)
        if friesType == 4:
            print('No fries type found.')
            pyautogui.screenshot('friesimg'+str(friesType)+'.png', region=(480,840,400,1))
            print('New fries saved as friesimg'+str(friesType)+'.png')
            print('Exiting.')
            sys.exit()
        friesimg = pyautogui.locateCenterOnScreen('friesimg' + str(friesType) + '.png', region=(480,840,400,1), grayscale=True)
        if friesimg:
            break

    pyautogui.keyDown('down')
    time.sleep(3.05)
    pyautogui.keyUp('down')
    pyautogui.press('p')
    
    while True:
        
        if friesType == 0:
            print('SALT THOSE FRIES BRUH')
            pyautogui.press('a')
            break

        elif friesType == 1:
            print('MY LOVE IS THE SEA')
            pyautogui.press('e')
            break

        elif friesType == 2:
            print('SWEETNSALTY')
            pyautogui.press('a')
            pyautogui.press('s')
            break

        elif friesType == 3:
            print('SUGAR. IN. WATER')
            pyautogui.press('s')
            break

        else:
            print('No fries found.')

    
    pyautogui.press('enter')
    return


def nachosIngredients(num):
    print('Nachos Step 2')
    global food
    global foodOrder
    global clock
    food[num-1] = None
    clock[num-1] = 0.0

    if foodOrder[num-1] == 'Classic Nachos':
        print('Classic Nachos')
        pyautogui.press('q')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'Supreme Nachos':
        print('Supreme Nachos')
        pyautogui.press('q')
        pyautogui.press('c')
        pyautogui.press('j')
        pyautogui.press('t')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'Royal Nachos':
        print('Royal Nachos')
        pyautogui.press('q')
        pyautogui.press('c')
        pyautogui.press('u')
        pyautogui.press('v')
        pyautogui.press('j')
        pyautogui.press('t')
        pyautogui.press('o')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'Italian Style Nachos':
        print('Italian Style Nachos')
        pyautogui.press('q')
        pyautogui.press('v')
        pyautogui.press('o')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'The Chubigans Special':
        print('The Chubigans Special')
        pyautogui.press('q')
        pyautogui.press('b')
        pyautogui.press('r')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'Mexican Siesta':
        print('Mexican Siesta')
        pyautogui.press('q')
        pyautogui.press('u')
        pyautogui.press('b')
        pyautogui.press('r')
        pyautogui.press('g')

    elif foodOrder[num-1] == 'Beef and Beans':
        print('Beef and Beans')
        pyautogui.press('q')
        pyautogui.press('b')
        pyautogui.press('g')
        
    else:
        print('No order found.')

    
    foodOrder[num-1] = None
    pyautogui.press('enter')
    return




def nachosMeat(num):
    print('Nachos Step 1')
    global food
    global foodOrder
    global clock
    food[num-1] = 'nachos'

    nachosType = None

    while True:
        nachosimg = None
        for nachosType in range(18):
            #print(nachosType)
            nachosimg = pyautogui.locateCenterOnScreen('nachosimg' + str(nachosType) + '.png', region=(480,840,420,1), grayscale=True)
            if nachosimg:
                break
            if nachosType == 17:
                print('No nachos type found')
        
        if nachosType == 0:
            print('Classic Nachos')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Classic Nachos'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 1:
            print('Supreme Nachos')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Supreme Nachos'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 2:
            print('Royal Nachos')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Royal Nachos'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 3:
            print('Veggie Nachos')
            pyautogui.press('q')
            pyautogui.press('v')
            pyautogui.press('j')
            pyautogui.press('t')
            pyautogui.press('o')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 4:
            print('Sour Veggie Nachos')
            pyautogui.press('q')
            pyautogui.press('c')
            pyautogui.press('v')
            pyautogui.press('j')
            pyautogui.press('t')
            pyautogui.press('o')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 5:
            print('Guac a Nachos')
            pyautogui.press('q')
            pyautogui.press('u')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 6:
            print('Fiesty Nachos')
            pyautogui.press('q')
            pyautogui.press('c')
            pyautogui.press('u')
            pyautogui.press('j')
            pyautogui.press('o')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 7:
            print('Guac and Chips')
            pyautogui.press('u')
            pyautogui.press('j')
            pyautogui.press('t')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 8:
            print('Jalanacho')
            pyautogui.press('q')
            pyautogui.press('j')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 9:
            print('Bowl of Chips')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 10:
            print('Italian Style Nachos')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Italian Style Nachos'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 11:
            print('Scoops of Plenty')
            pyautogui.press('q')
            pyautogui.press('c')
            pyautogui.press('u')
            pyautogui.press('o')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 12:
            print('The Chubigans Special')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'The Chubigans Special'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 13:
            print('Mexican Siesta')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Mexican Siesta'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 14:
            print('Mexican Fiesta')
            pyautogui.press('q')
            pyautogui.press('c')
            pyautogui.press('v')
            pyautogui.press('j')
            pyautogui.press('t')
            pyautogui.press('o')
            pyautogui.press('b')
            pyautogui.press('r')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 15:
            print('Rice and Beans')
            pyautogui.press('q')
            pyautogui.press('b')
            pyautogui.press('r')
            pyautogui.press('enter')
            food[num-1] = None
            return

        elif nachosType == 16:
            print('Beef and Beans')
            pyautogui.press('g')
            pyautogui.press('enter')
            foodOrder[num-1] = 'Beef and Beans'
            temp = time.time()
            temp = float(temp)
            clock[num-1] = temp
            return

        elif nachosType == 17:
            print('Spicy Rice Special')
            pyautogui.press('q')
            pyautogui.press('c')
            pyautogui.press('j')
            pyautogui.press('t')
            pyautogui.press('o')
            pyautogui.press('r')
            pyautogui.press('enter')
            food[num-1] = None
            return
    
        print('No nachos meat type found.')


######### main ############

clock = [0.0] * MAX_ORDERS
food = [None] * MAX_ORDERS
foodOrder = [None] * MAX_ORDERS


while True:
    print('Awaiting new orders', end="")
    for index in range(MAX_ORDERS):
        if food[index] != None:
            print(', ' + food[index] + ' on ' + str(index+1), end="")
    print('')

    for topIndex in range(MAX_ORDERS):
        number = None
        number = pyautogui.locateCenterOnScreen('on'+str(topIndex+1)+'.png', region=(70,130,80,500), grayscale=True)
        if number:
            if food[topIndex] == None:
                pyautogui.press(str(topIndex+1))
                whichFood(topIndex+1)
            elif food[topIndex] == 'hamburger':
                if float(time.time()) - clock[topIndex] >= 8:
                    pyautogui.press(str(topIndex+1))
                    whichFood(topIndex+1)
            elif food[topIndex] == 'soup':
                if float(time.time()) - clock[topIndex] >= 11:
                    pyautogui.press(str(topIndex+1))
                    food[topIndex] = None
            elif food[topIndex] == 'lasagna':
                if float(time.time()) - clock[topIndex] >= 8:
                    pyautogui.press(str(topIndex+1))
                    food[topIndex] = None
            elif food[topIndex] == 'chicken':
                if float(time.time()) - clock[topIndex] > 15:
                    pyautogui.press(str(topIndex+1))
                    food[topIndex] = None
            elif food[topIndex] == 'fish':
                if float(time.time()) - clock[topIndex] >= 8:
                    pyautogui.press(str(topIndex+1))
                    food[topIndex] = None
            elif food[topIndex] == 'pizza':
                if float(time.time()) - clock[topIndex] >= 8:
                    pyautogui.press(str(topIndex+1))
                    food[topIndex] = None
            elif food[topIndex] == 'nachos':
                if float(time.time()) - clock[topIndex] >= 8:
                    pyautogui.press(str(topIndex+1))
                    whichFood(topIndex+1)
