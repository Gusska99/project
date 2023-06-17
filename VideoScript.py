import numpy as np
import cv2
import imutils
import datetime
  
   
gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)
   
firstFrame = None
gun_exist = False

def pixel(img, b=3):
    (height, widht) = img.shape[:2]
    x = np.linspace(0, widht, b + 1, dtype="int")
    y = np.linspace(0, height, b + 1, dtype="int")
    for i in range(1, len(y)):
        for j in range(1, len(x)):
            X_1 = x[j - 1]
            Y_1 = y[i - 1]
            X_2 = x[j]
            Y_2 = y[i]

            ROI = img[Y_1:Y_2, X_1:X_2]
            (B, G, R) = [int(k) for k in cv2.mean(ROI)[:3]]
            cv2.rectangle(img, (X_1, Y_1), (X_2, Y_2),(B, G, R), -1)
    return img  

while True:
      
    ret, frame = camera.read()
   
    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
    gun = gun_cascade.detectMultiScale(gray,1.3, 5,minSize = (100, 100))
       
    if len(gun) > 0:
        gun_exist = True
           
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame,(x, y),(x + w, y + h),(255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]    
   
    if firstFrame is None:
        firstFrame = gray
        continue
   
    # print(datetime.date())
    # draw the text and timestamp on the frame
    cv2.putText(frame, datetime.datetime.now().strftime("% A % d % B % Y % I:% M:% S % p"),(10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX,0.35, (0, 0, 255), 1)
   
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
      
    if key == ord('q'):
        break
  
    if gun_exist:
        stream = VideoStream(src=0).start()
        method="pixel"
        while True:
            f_stream = stream.read()
            f_stream = imutils.resize(f_stream, width=400)
            (height, widht) = f_stream.shape[:2]
            img_blob = cv2.dnn.blobFromImage(f_stream, 1.0, (300, 300),(104.0, 177.0, 123.0))
            model.setInput(img_blob)
            detect = model.forward()
            print("guns detected")

    else:
        print("guns NOT detected")
  
camera.release()
cv2.destroyAllWindows()