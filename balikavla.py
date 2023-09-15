import time
import cv2
import numpy as np
import mss
import pydirectinput
import random


count=0
max_count=60
prev_x = None
prev_y = None
move_factor = 0.5

def Screen_Shot(left=103, top=127, width=90, height=91):
    stc = mss.mss()
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img

  
def SolucanSecOltaAt():

    random_key = str(random.randint(1, 4))
    pydirectinput.press(random_key)
    time.sleep(0.1)
    pydirectinput.press("f4")
    print("Oltayı attı")
    time.sleep(random.randint(1,3))
               


def FindAndClickFish(duration=random.randint(15,20)):
    prev_x = None
    prev_y = None
    start_time = time.time()
    while time.time() - start_time < duration:
            
        scr = Screen_Shot()  
        hsvframe = cv2.cvtColor(scr, cv2.COLOR_BGR2HSV)

        fish_color_rgb = (56, 91, 124)
        fish_color_hsv = cv2.cvtColor(np.uint8([[fish_color_rgb]]), cv2.COLOR_RGB2HSV)[0][0]

        hue = fish_color_hsv[0]
        saturation = fish_color_hsv[1]
        value = fish_color_hsv[2]

        lower_color = np.array([hue - 10, saturation - 10, value - 10], dtype=np.uint8)
        upper_color = np.array([hue + 10, saturation + 10, value + 10], dtype=np.uint8)
        color_mask = cv2.inRange(hsvframe, lower_color, upper_color)

        fish_color_rgb_on_line = (96,97,120)
        fish_color_hsv2 = cv2.cvtColor(np.uint8([[fish_color_rgb_on_line]]), cv2.COLOR_RGB2HSV)[0][0]

        hue2 = fish_color_hsv2[0]
        saturation2 = fish_color_hsv2[1]
        value2 = fish_color_hsv2[2]

        lower_color2 = np.array([hue2 - 10, saturation2 - 10, value2 - 10], dtype=np.uint8)
        upper_color2 = np.array([hue2 + 10, saturation2 + 10, value2 + 10], dtype=np.uint8)
        color_mask2 = cv2.inRange(hsvframe, lower_color2, upper_color2)

        combined_mask = cv2.bitwise_or(color_mask, color_mask2)

        white_pixels = np.where(combined_mask == 255)


        if white_pixels[0].size > 0 or white_pixels[1].size > 0:
            print("balik goruldu")
                
            x = int(np.mean(white_pixels[1]))
            y = int(np.mean(white_pixels[0]))

            if prev_x is None and prev_y is None:
                prev_x, prev_y = x, y
            else:
                x2 = x + int((x - prev_x) * move_factor)  
                y2 = y + int((y - prev_y) * move_factor) 
                pydirectinput.moveTo(x2+103, y2+127)
                pydirectinput.click()
                prev_x, prev_y = x, y

while True:
   
    count=count+1
    pydirectinput.click(100,10)
    SolucanSecOltaAt()
    FindAndClickFish()
    print("bitti bida calistir")
    print(count)

