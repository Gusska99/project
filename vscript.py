import time
import numpy as np
import pyscreenshot as imageGrab
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Python\Scripts\Tesseract-OCR\tesseract.exe'
filename = 'image.png'#посмотреть где фото
x = 1
last_time = time.time()

while (True):
    screen = np.array(imageGrab.grab(bbox=(77, 342, 460, 575)))
    #print('loop took {} seconds'.format(time.time()-last_time))
    last_time=time.time()
   # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, screen)
    #x=x+1
    #print(x)
    img=cv2.imread('image.png')
    text = pytesseract.image_to_string(img,lang="rus")
    print(text)

   
    cv2.destroyAllWindows()      

    
    img = cv2.imread('image.png')
    text = pytesseract.image_to_string(img)
    print(text)