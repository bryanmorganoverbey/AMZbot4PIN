import pyautogui
import time
# Infinite while loop
image_num = 0
while(True):
    image_num += 1
    #Grab scroll bar and move down a row
    pyautogui.scroll(-318)  # scroll down 318 pixels
    #move mouse to hover over first image in row.
    pyautogui.moveTo(200,250)
    time.sleep(3)
    #for item in current row
    for i in range(4):
        #click on item image
        pyautogui.moveRel(250,0, duration = 0)
        time.sleep(3)
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
        #click on large image



            #Grab affiliate link text

            # Go to pinterest tab

            #press create new post

            #upload image I just created

            #paste in link text

            #post item

            #add caption (optional)

