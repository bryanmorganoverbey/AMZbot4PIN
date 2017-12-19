import pyautogui
import time
# Infinite while loop
image_num = 0
while(True):
    time.sleep(5)
    image_num += 1

    #move mouse to hover over first image in row.
    pyautogui.moveTo(200,250)
    time.sleep(3)
    #for item in current row
    for i in range(4):
        #click on item image

        #pyautogui.click(or whatever)
        # use snipping tool to create and save image
            #scroll down to snipping tool on taskbar
        pyautogui.moveTo(510, 880)
        pyautogui.click()
            #click new snip on snipping tool
        pyautogui.moveTo(334,140)
        pyautogui.click()
            #hover over top left pixel of large image
        pyautogui.moveTo(376,257)
            #click and drag to cover full image
        pyautogui.dragTo(675, 555, button='left')
            #save image
        pyautogui.keyDown('ctrl')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')
            #name image
        pyautogui.typewrite(str(image_num))
        pyautogui.press('enter')
            #minimize snipping tool
        pyautogui.keyDown('windows')
        pyautogui.press('down')
        pyautogui.keyUp('windows')
        #click on large image
        pyautogui.moveRel(-50,-50)
        pyautogui.rightClick()
        pyautogui.moveRel(10,5)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(283,13)

        #Grab affiliate link text
        pyautogui.moveTo(186,90)
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
            #close tab & go to pinterest tab

        pyautogui.keyDown('ctrl')
        pyautogui.press('w')
        pyautogui.keyUp('ctrl')
            #hover over plus sign
        pyautogui.moveTo(1192,90)
            #move to hover over "upload image"
        pyautogui.moveTo(1192, 156, duration=0.5)
        pyautogui.click()
            #hover over "destination url"
        pyautogui.moveTo(500,479)
        pyautogui.click()
            #paste image link
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
            #upload image I just created
        pyautogui.moveTo(876, 369)
        pyautogui.click()
        pyautogui.typewrite(str(image_num) + ".PNG")
        pyautogui.press('enter')

            #post item
        pyautogui.moveTo(891,538)
        pyautogui.press('enter')
            #add caption (optional)
            #choose board
        pyautogui.typewrite('need!')
        pyautogui.moveTo(773,235)
        pyautogui.click()
        pyautogui.moveTo(484,568)
        pyautogui.click()
            #jump back to amazon page
        pyautogui.keyDown('ctrl')
        pyautogui.press('pgdn')
        pyautogui.keyUp('ctrl')
            #close big image of previous item
        pyautogui.press('esc')
            #scroll over to next image in row
        pyautogui.moveRel(250, 0, duration=0)

    #Grab scroll bar and move down a row
    pyautogui.scroll(-318)  # scroll down 318 pixels