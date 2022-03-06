import cv2
import numpy as np
from pyzbar.pyzbar import decode
#import Arduino

#img = cv2.imread('Shantonu.png')
cap = cv2.VideoCapture(0)
cap.set(3, 460)
cap.set(4, 480)

with open('my_data.txt') as f:
    myDataList = f.read().splitlines()
# print(myDataList)



while True:
    #Arduino.ServoMotor(0)
    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
            print('Authorized')
            welcome = 'WELCOME SIR'
            index = (240, 420)
            #Arduino.ServoMotor(1)

        else:
            cv2.imshow('Result', img)
            myOutput = 'Un-Authorized'
            welcome = 'YOU DO NOT HAVE PERMISSION SIR'
            myColor = (0, 0, 255)
            index = (50, 450)
            #Arduino.ServoMotor(0)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 4)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
        cv2.putText(img, welcome, index,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, myColor, 2)
    cv2.imshow('Result', img)
    if cv2.waitKey(1) == ord('q'):  # Press 'D' for close the window
        break

cv2.destroyAllWindows()
cap.release()
