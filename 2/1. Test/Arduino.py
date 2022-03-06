from ast import While
from pyfirmata import Arduino, SERVO
import time
import keyboard
port = 'COM7'
board = Arduino(port)



Motor = board.get_pin('d:9:s')
Motor.write(0)

def ServoMotor(val):
    if val == 1:
        Motor.write(90)
        time.sleep(.3)
       
    else:
        Motor.write(0)
      
        


def QrState(valu):
    if valu == 1:
        board.digital[13].write(1)
        

    if valu != 1:
        board.digital[13].write(0)



