import pytesseract
import pyautogui
import time
import os
from PIL import Image
#------------------------------------

# make sure you have your monkeytype browser in full screen 
# when you are using this app and open the browser after you have 
# started the program 

#------------------------------------
PATH = os.getcwd()
print(PATH)
time.sleep(2)

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'      # ENTER PATH TO TESSERACT EXECUTABLE  

ss = pyautogui.screenshot(f"{PATH}/monkeyhack/reader.png", region=(310, 310, 1500, 500))
time.sleep(1.5)
img = Image.open(f'{PATH}/monkeyhack/reader.png')
text = pytesseract.image_to_string(img)
a = text.replace('\n', ' ')
#for char in a.split():
#    pyautogui.typewrite(char)
#    pyautogui.typewrite(" ")
pyautogui.typewrite(a)
print(a)
#os.remove(f'{PATH}/monkeyhack/reader.png')