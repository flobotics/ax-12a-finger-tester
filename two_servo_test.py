import sys
import sys, tty, termios
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from _ast import Or

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)



def getch():
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getch1():
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    print('finger controller')
    
    i = 0
    
    while 1:
#         print("Press any key to continue! (or press ESC to quit!)")
    #     if isData():
    #         c = sys.stdin.read(1)
        keychar = getch1()
        if keychar == chr(0x1b):
            break
        elif keychar == 'q' or keychar == 'e' or keychar == 't' or keychar == 'u':
            print('found q----------servo1-up  servo2-down %d' % i)
            i += 10
        elif keychar == 'w' or keychar == 'r' or keychar == 'z' or keychar == 'i':
            print('found q----------servo1-up  servo2-down %d' % i)
            i -= 10
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    