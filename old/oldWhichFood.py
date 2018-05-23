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
