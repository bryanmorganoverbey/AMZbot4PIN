import pyautogui
import time
# Infinite while loop
while(True):
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
        pyautogui.moveTo(850,1000)
        #click on large image



            #Grab affiliate link text

            # Go to pinterest tab

            #press create new post

            #upload image I just created

            #paste in link text

            #post item

            #add caption (optional)

