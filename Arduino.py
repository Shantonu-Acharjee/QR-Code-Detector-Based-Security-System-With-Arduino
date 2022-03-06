import pyfirmata
from pyfirmata import Arduino, SERVO
import time
port = 'COM6'
board = Arduino(port)


try:
    
    a = 0
    Motor = board.get_pin('d:9:s')
    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    
    def ServoMotor(val = 0):
        print('your val :.....>',val)
        global a
        if val == 1 and a == 0:
            a = 1
            Motor.write(0)
            time.sleep(2)
            Motor.write(75)
            a = 0
        
        """if val != 1 and a == 1:
            Motor.write(75)
            a = 0"""

           
        
except:
    print('Arduino File Error')







