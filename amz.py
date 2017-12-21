import pyautogui
import time
import win32clipboard as clip

def check_if_slot_is_link():
    #move cursor to /shop/ in address bar
    pyautogui.moveTo(386,47,duration=1)
    pyautogui.dragTo(416,47, duration = 1)
    #copy those four letters
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    clip.OpenClipboard()
    copied = clip.GetClipboardData()
    clip.CloseClipboard()
    if(copied == 'shop'):
        return True
    else:
        return False

def run_algorithm():
    # use snipping tool to create and save image '''this should be its own function'''
    # scroll down to snipping tool on taskbar
    pyautogui.moveTo(510, 880, duration=1)
    pyautogui.doubleClick()
    time.sleep(3)
    # click new snip on snipping tool
    pyautogui.moveTo(795, 128, duration=1)
    pyautogui.click()
    time.sleep(3)
    # hover over top left pixel of large image
    pyautogui.moveTo(376, 257, duration=1)
    # click and drag to cover full image
    pyautogui.dragTo(675, 555, button='left', duration=1)
    # save image
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    # name image
    pyautogui.typewrite(str(image_num))
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    # close snipping tool
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    time.sleep(3)

    # click on large image
    pyautogui.moveRel(-150, -250, duration=1)
    pyautogui.rightClick()
    pyautogui.moveRel(10, 5, duration=1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(283, 13, duration=1)
    pyautogui.click()
    # Grab affiliate link text
    pyautogui.moveTo(186, 90, duration=2)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    # close tab & go to pinterest tab

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    pyautogui.moveTo(283, 13, duration=1)
    pyautogui.click()
    # hover over plus sign
    pyautogui.moveTo(1192, 90)
    # move to hover over "upload image"
    pyautogui.moveTo(1192, 156, duration=0.5)

    pyautogui.click()
    # hover over "destination url"
    pyautogui.moveTo(500, 479, duration=1)
    pyautogui.click()
    # paste image link
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

    # upload image I just created
    pyautogui.moveTo(876, 369)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite(str(image_num) + ".PNG")
    pyautogui.press('enter')
    time.sleep(2)
    # post item
    pyautogui.moveTo(891, 538, duration=1)
    pyautogui.click()
    time.sleep(2)
    # add caption (optional)
    # choose board
    pyautogui.typewrite('need!')
    time.sleep(2)
    pyautogui.moveTo(773, 235, duration=1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(484, 568, duration=1)
    pyautogui.click()
    time.sleep(3)
    # jump back to amazon page
    pyautogui.keyDown('ctrl')
    pyautogui.press('pgup')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    # close big image of previous item
    pyautogui.press('esc')
    pyautogui.moveTo(773, 235, duration=1)

time.sleep(10)
image_num = 1
while True:
    slot = 1
    while slot<=5:
        pyautogui.moveTo(150+ (slot-1)*255, 250, duration=1)
        #click image corresponding to this slot.
        pyautogui.doubleClick()
        if check_if_slot_is_link():
            slot +=1
            #go back to prev page (navagate back from link page)
            pyautogui.moveTo(17, 44, duration = 1)
            pyautogui.click()
            pyautogui.moveTo(773, 235, duration=1)
        else:
            run_algorithm()
        slot +=1
        image_num +=1
    #Grab scroll bar and move down a row
    pyautogui.scroll(-318)  # scroll down 318 pixels


