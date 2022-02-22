from pyfirmata import ArduinoMega
import time
import keyboard
port = 'COM3'
board = ArduinoMega(port)





def QrState(valu):
    if valu == 1:
        board.digital[13].write(1)
        

    if valu != 1:
        board.digital[13].write(0)



