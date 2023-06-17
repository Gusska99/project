
import numpy as np
import cv2
from mss import mss
from PIL import Image
import tkinter as tk 
import time
import pyscreenshot as imageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Python\Scripts\Tesseract-OCR\tesseract.exe'

label = tk.Label(text='Text on the screen', font=('Times','30'), fg='black', bg='white')
filename = 'image.png'#посмотреть где фото
x = 1
last_time = time.time()
#bounding_box = {'top': 0, 'left': 0, 'width': 1919, 'height': 1079}
#sct = mss()
stream = VideoStream(src=0).start()
method="pixel"
while True:
    #sct_img = sct.grab(bounding_box)
   # cv2.imshow('screen', np.array(sct_img))

    screen = np.array(imageGrab.grab(bbox=(0, 0, 1919, 1079)))
    last_time=time.time()
    cv2.imwrite(filename, screen)
    x=x+1
    img=cv2.imread('image.png')
    text = pytesseract.image_to_string(img, lang="rus")
    print(text)
    index = text.find('D:\Python\Scripts\librarii\librarii.xlb')
    if index == 1:
        print('не нашел')
        cv2.destroyAllWindows()
        
    else:
        print('нашел')

        while True:
            f_stream = stream.read()
            f_stream = imutils.resize(f_stream, width=400)
            (height, widht) = f_stream.shape[:2]
            img_blob = cv2.dnn.blobFromImage(f_stream, 1.0, (300, 300),(104.0, 177.0, 123.0))
            model.setInput(img_blob)
            detect = model.forward()
            

            #cv2.destroyAllWindows()
            #break

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break