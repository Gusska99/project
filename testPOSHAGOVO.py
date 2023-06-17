# Import OpenCV module 
import cv2 
import numpy as np
from mss import mss
from PIL import Image
import pyscreenshot as imageGrab
from matplotlib import pyplot as pltd 

filename = 'image.png'
screen = np.array(imageGrab.grab(bbox=(0, 0, 1919, 1079)))
cv2.imwrite(filename, screen)
img=cv2.imread('image.png') 

imaging_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
imaging_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

xml_data = cv2.CascadeClassifier('XML-data.xml') 
detecting = xml_data.detectMultiScale(imaging_gray, minSize =(30, 30)) 

amountDetecting = len(detecting) 

if amountDetecting != 0: 
    for(a, b, width, height) in detecting: 
        cv2.rectangle(imaging_rgb,(a, b), (a + height, b + width), (0, 275, 0), 9) 
pltd.subplot(1, 1, 1) 
pltd.imshow(imaging_rgb) 
pltd.show() 
