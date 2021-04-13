#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL AX-12a, and an USB2DYNAMIXEL
# Be sure that DXL AX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
#
import sys
import select
import tty
import termios

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                    # Uses Dynamixel SDK library

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def check_moving_limits(key, stepsize, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
    if keychar == 'q':
        if ((DXL_ID_1_GOAL + stepsize) <= DXL_ID_1_GOAL_MAX) and ((DXL_ID_2_GOAL + stepsize) <= DXL_ID_2_GOAL_MAX):
            return True
#                 DXL_ID_1_GOAL = DXL_ID_1_GOAL + 10
#                 DXL_ID_2_GOAL = DXL_ID_2_GOAL + 10
        else:
            return False
    elif keychar == 'w':
        if ((DXL_ID_1_GOAL - stepsize) >= DXL_ID_1_GOAL_MIN) and ((DXL_ID_2_GOAL - stepsize) >= DXL_ID_2_GOAL_MIN):
            return True
        else:
            return False
#             DXL_ID_1_GOAL = DXL_ID_1_GOAL - 10
#             DXL_ID_2_GOAL = DXL_ID_2_GOAL - 10
    elif keychar == 'a':
        if ((DXL_ID_1_GOAL + stepsize) <= DXL_ID_1_GOAL_MAX) and ((DXL_ID_2_GOAL - stepsize) >= DXL_ID_2_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 's':
        if ((DXL_ID_1_GOAL - stepsize) >= DXL_ID_1_GOAL_MIN) and ((DXL_ID_2_GOAL + stepsize) <= DXL_ID_2_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'd':
        if ((DXL_ID_3_GOAL + stepsize) <= DXL_ID_3_GOAL_MAX) and ((DXL_ID_4_GOAL - stepsize) >= DXL_ID_4_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 'f':
        if ((DXL_ID_3_GOAL - stepsize) >= DXL_ID_3_GOAL_MIN) and ((DXL_ID_4_GOAL + stepsize) <= DXL_ID_4_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'g':
        if ((DXL_ID_5_GOAL + stepsize) <= DXL_ID_5_GOAL_MAX) and ((DXL_ID_6_GOAL - stepsize) >= DXL_ID_6_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 'h':
        if ((DXL_ID_5_GOAL - stepsize) >= DXL_ID_5_GOAL_MIN) and ((DXL_ID_6_GOAL + stepsize) <= DXL_ID_6_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'j':
        if ((DXL_ID_7_GOAL + stepsize) <= DXL_ID_7_GOAL_MAX) and ((DXL_ID_8_GOAL - stepsize) >= DXL_ID_8_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 'k':
        if ((DXL_ID_7_GOAL - stepsize) >= DXL_ID_7_GOAL_MIN) and ((DXL_ID_8_GOAL + stepsize) <= DXL_ID_8_GOAL_MAX):
            return True
        else:
            return False
    
    elif keychar == 'e':
        if ((DXL_ID_3_GOAL + stepsize) <= DXL_ID_3_GOAL_MAX) and ((DXL_ID_4_GOAL + stepsize) <= DXL_ID_4_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'r':
        if ((DXL_ID_3_GOAL - stepsize) >= DXL_ID_3_GOAL_MIN) and ((DXL_ID_4_GOAL - stepsize) >= DXL_ID_4_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 't':
        if ((DXL_ID_5_GOAL + stepsize) <= DXL_ID_5_GOAL_MAX) and ((DXL_ID_6_GOAL + stepsize) <= DXL_ID_6_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'z':
        if ((DXL_ID_5_GOAL - stepsize) >= DXL_ID_5_GOAL_MIN) and ((DXL_ID_6_GOAL - stepsize) >= DXL_ID_6_GOAL_MIN):
            return True
        else:
            return False
        
    elif keychar == 'u':
        if ((DXL_ID_7_GOAL + stepsize) <= DXL_ID_7_GOAL_MAX) and ((DXL_ID_8_GOAL + stepsize) <= DXL_ID_8_GOAL_MAX):
            return True
        else:
            return False
        
    elif keychar == 'i':
        if ((DXL_ID_7_GOAL - stepsize) >= DXL_ID_7_GOAL_MIN) and ((DXL_ID_8_GOAL - stepsize) >= DXL_ID_8_GOAL_MIN):
            return True
        else:
            return False



def check_torque_limit(DXL_ID, DXL_ID_MOVING_TORQUE_LIMIT, DXL_ID_GOAL, turn_cw):
    do_work = True
    
    print("idddd")
    print(DXL_ID)
    
    while do_work:
        # Read present position
        dxl_present_torque, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_LOAD)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, dxl_goal_position[index], dxl_present_torque))
        DXL_ID_PRESENT_TORQUE = dxl_present_torque
       
        
        if DXL_ID_PRESENT_TORQUE > DXL_ID_MOVING_TORQUE_LIMIT:
            ### if cw=clock-wise
            if turn_cw:
                DXL_ID_GOAL = DXL_ID_GOAL - 2
            else:
                DXL_ID_GOAL = DXL_ID_GOAL + 2
            # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_AX_GOAL_POSITION, DXL_ID_GOAL)
            if dxl_comm_result != COMM_SUCCESS:
                print("id1 %s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("id1 %s" % packetHandler.getRxPacketError(dxl_error))
                
        else:
            do_work = False
    
    
def check_all_torque_limits(dont_check):
    if dont_check is not DXL_ID_1:
        check_torque_limit(DXL_ID_1, DXL_ID_1_MOVING_TORQUE_LIMIT, DXL_ID_1_GOAL, False)
    if dont_check is not DXL_ID_2:
        check_torque_limit(DXL_ID_2, DXL_ID_2_MOVING_TORQUE_LIMIT, DXL_ID_2_GOAL, True)
    if dont_check != DXL_ID_3:
        check_torque_limit(DXL_ID_3, DXL_ID_3_MOVING_TORQUE_LIMIT, DXL_ID_3_GOAL, False)
    if dont_check != DXL_ID_4:
        check_torque_limit(DXL_ID_4, DXL_ID_4_MOVING_TORQUE_LIMIT, DXL_ID_4_GOAL, True)
    if dont_check != DXL_ID_5:
        check_torque_limit(DXL_ID_5, DXL_ID_5_MOVING_TORQUE_LIMIT, DXL_ID_5_GOAL, False)
    if dont_check != DXL_ID_6:
        check_torque_limit(DXL_ID_6, DXL_ID_6_MOVING_TORQUE_LIMIT, DXL_ID_6_GOAL, True)
#     if dont_check != DXL_ID_7:
#         check_torque_limit(DXL_ID_7, DXL_ID_7_MOVING_TORQUE_LIMIT, DXL_ID_7_GOAL, False)
    if dont_check != DXL_ID_8:
        check_torque_limit(DXL_ID_8, DXL_ID_8_MOVING_TORQUE_LIMIT, DXL_ID_8_GOAL, True)
    

# Control table address
ADDR_AX_TORQUE_ENABLE       = 24                          # Control table address is different in Dynamixel model
ADDR_AX_GOAL_POSITION       = 30
ADDR_AX_PRESENT_POSITION    = 36
ADDR_AX_LED                 = 25  #1byte
ADDR_MOVING_SPEED           = 32   #2byte   0->1023    0=full,  1=very-very-slow  ,100=faster 1023=fastest
ADDR_TORQUE_LIMIT          = 34    #2byte  0->1023
ADDR_PRESENT_LOAD           = 40

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID_1                      = 7                 # Dynamixel ID : 1
DXL_ID_2                      = 8                 # Dynamixel ID : 1
DXL_ID_3                      = 5                 # Dynamixel ID : 1
DXL_ID_4                      = 6                 # Dynamixel ID : 1
DXL_ID_5                      = 3                 # Dynamixel ID : 1
DXL_ID_6                      = 4                 # Dynamixel ID : 1
DXL_ID_7                      = 1                 # Dynamixel ID : 1
DXL_ID_8                      = 2                 # Dynamixel ID : 1
BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 0           # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 1023            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold

DXL_ID_1_GOAL               = 0
DXL_ID_1_GOAL_MIN           = 0  #248
DXL_ID_1_GOAL_MAX           = 1023
DXL_ID_2_GOAL               = 1023
DXL_ID_2_GOAL_MIN           = 0
DXL_ID_2_GOAL_MAX           = 1023  #775

DXL_ID_3_GOAL               = 0
DXL_ID_3_GOAL_MIN           = 0  #248
DXL_ID_3_GOAL_MAX           = 1023
DXL_ID_4_GOAL               = 1023
DXL_ID_4_GOAL_MIN           = 0
DXL_ID_4_GOAL_MAX           = 1023  #775
DXL_ID_3_4_SPEED            = 0

DXL_ID_5_GOAL               = 0
DXL_ID_5_GOAL_MIN           = 0  #248
DXL_ID_5_GOAL_MAX           = 1023
DXL_ID_6_GOAL               = 1023
DXL_ID_6_GOAL_MIN           = 0
DXL_ID_6_GOAL_MAX           = 1023  #775
DXL_ID_5_6_SPEED            = 0

DXL_ID_7_GOAL               = 0
DXL_ID_7_GOAL_MIN           = 0  #248
DXL_ID_7_GOAL_MAX           = 1023
DXL_ID_8_GOAL               = 1023
DXL_ID_8_GOAL_MIN           = 0
DXL_ID_8_GOAL_MAX           = 1023  #775
DXL_ID_7_8_SPEED            = 0

DXL_ID_1_TORQUE_LIMIT       = 1023

DXL_ID_1_MOVING_TORQUE_LIMIT       = 300
DXL_ID_2_MOVING_TORQUE_LIMIT       = 300
DXL_ID_3_MOVING_TORQUE_LIMIT       = 300
DXL_ID_4_MOVING_TORQUE_LIMIT       = 300
DXL_ID_5_MOVING_TORQUE_LIMIT       = 300
DXL_ID_6_MOVING_TORQUE_LIMIT       = 300
DXL_ID_7_MOVING_TORQUE_LIMIT       = 300
DXL_ID_8_MOVING_TORQUE_LIMIT       = 300

DXL_ID_1_2_SPEED    = 30

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")
    
    
# Read present position
dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_1, dxl_goal_position[index], dxl_present_position))
DXL_ID_1_GOAL = dxl_present_position

dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_2, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_2, dxl_goal_position[index], dxl_present_position))
DXL_ID_2_GOAL = dxl_present_position
# DXL_ID_2_GOAL = 1023 - DXL_ID_1_GOAL


##servo-5-6
# Read present position
dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_3, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_3, dxl_goal_position[index], dxl_present_position))
DXL_ID_3_GOAL = dxl_present_position

dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_4, dxl_goal_position[index], dxl_present_position))
DXL_ID_4_GOAL = dxl_present_position
# DXL_ID_2_GOAL = 1023 - DXL_ID_1_GOAL

# Read present position
dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_5, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_5, dxl_goal_position[index], dxl_present_position))
DXL_ID_5_GOAL = dxl_present_position

dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_6, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_6, dxl_goal_position[index], dxl_present_position))
DXL_ID_6_GOAL = dxl_present_position


# Read present position
dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_7, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_7, dxl_goal_position[index], dxl_present_position))
DXL_ID_7_GOAL = dxl_present_position

dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_8, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_8, dxl_goal_position[index], dxl_present_position))
DXL_ID_8_GOAL = dxl_present_position




# Write torque limit
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_TORQUE_LIMIT, DXL_ID_1_TORQUE_LIMIT)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
    
# Write torque limit
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_TORQUE_LIMIT, DXL_ID_1_TORQUE_LIMIT)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
            
            
            

while 1:
    print("Press any key to continue! (or press ESC to quit!)")
#     if isData():
#         c = sys.stdin.read(1)
    keychar = getch()
    if keychar == chr(0x1b):
        break
    elif keychar == 'q':
        print('found q----------servo1-up  servo2-down')
        
        if check_moving_limits(keychar, 10, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
            DXL_ID_1_GOAL = DXL_ID_1_GOAL + 10
            DXL_ID_2_GOAL = DXL_ID_2_GOAL + 10
        print("%s" % DXL_ID_1_GOAL)
        print("%s" % DXL_ID_2_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_GOAL_POSITION, DXL_ID_1_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id1 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id1 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_AX_GOAL_POSITION, DXL_ID_2_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id2 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id2 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_2)
            
            
    elif keychar == 'w':
        print('found w----------servo1-down  servo2-up')
        
        if check_moving_limits(keychar, 10, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
            DXL_ID_1_GOAL = DXL_ID_1_GOAL - 10
            DXL_ID_2_GOAL = DXL_ID_2_GOAL - 10
        print("%s" % DXL_ID_1_GOAL)
        print("%s" % DXL_ID_2_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_GOAL_POSITION, DXL_ID_1_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_AX_GOAL_POSITION, DXL_ID_2_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_1)
        
        
    elif keychar == 'a':
        print('found a----------servo1-2 up')
        
        if check_moving_limits(keychar, 10, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
            DXL_ID_1_GOAL = DXL_ID_1_GOAL + 10
            DXL_ID_2_GOAL = DXL_ID_2_GOAL - 10
        print("%s" % DXL_ID_1_GOAL)
        print("%s" % DXL_ID_2_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_GOAL_POSITION, DXL_ID_1_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_AX_GOAL_POSITION, DXL_ID_2_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 's':
        print('found s----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
            DXL_ID_1_GOAL = DXL_ID_1_GOAL - 10
            DXL_ID_2_GOAL = DXL_ID_2_GOAL + 10
        print("%s" % DXL_ID_1_GOAL)
        print("%s" % DXL_ID_2_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_GOAL_POSITION, DXL_ID_1_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_AX_GOAL_POSITION, DXL_ID_2_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 'y':
        print('found y----------servo1-2  speed up')  
        DXL_ID_1_2_SPEED = DXL_ID_1_2_SPEED +10
        print("%s" % DXL_ID_1_2_SPEED)
        
        # Write speed
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_MOVING_SPEED, DXL_ID_1_2_SPEED)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_MOVING_SPEED, DXL_ID_1_2_SPEED)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 'x':
        print('found y----------servo1-2  speed down') 
        
        DXL_ID_1_2_SPEED = DXL_ID_1_2_SPEED - 10
        print("%s" % DXL_ID_1_2_SPEED)
        # Write speed
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_MOVING_SPEED, DXL_ID_1_2_SPEED)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_2, ADDR_MOVING_SPEED, DXL_ID_1_2_SPEED)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))  
        

    elif keychar == 'e':
        print('found e----------servo1-up  servo2-down')
        
        if check_moving_limits(keychar, 10, DXL_ID_3_GOAL, DXL_ID_4_GOAL):
            DXL_ID_3_GOAL = DXL_ID_3_GOAL + 10
            DXL_ID_4_GOAL = DXL_ID_4_GOAL + 10
        print("goal3 %s" % DXL_ID_3_GOAL)
        print("goal4 %s" % DXL_ID_4_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_3, ADDR_AX_GOAL_POSITION, DXL_ID_3_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id3 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id3 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_GOAL_POSITION, DXL_ID_4_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id4 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id4 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_4)
            
            
    elif keychar == 'r':
        print('found r----------servo1-down  servo2-up')
        
        if check_moving_limits(keychar, 10, DXL_ID_3_GOAL, DXL_ID_4_GOAL):
            DXL_ID_3_GOAL = DXL_ID_3_GOAL - 10
            DXL_ID_4_GOAL = DXL_ID_4_GOAL - 10
        print("goal3 %s" % DXL_ID_3_GOAL)
        print("goal4 %s" % DXL_ID_4_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_3, ADDR_AX_GOAL_POSITION, DXL_ID_3_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id3 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id3 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_GOAL_POSITION, DXL_ID_4_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id4 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id4 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_3)

    elif keychar == 'd':
        print('found d----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_3_GOAL, DXL_ID_4_GOAL):
            DXL_ID_3_GOAL = DXL_ID_3_GOAL + 10
            DXL_ID_4_GOAL = DXL_ID_4_GOAL - 10
        print("%s" % DXL_ID_3_GOAL)
        print("%s" % DXL_ID_4_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_3, ADDR_AX_GOAL_POSITION, DXL_ID_3_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_GOAL_POSITION, DXL_ID_4_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 'f':
        print('found f----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_3_GOAL, DXL_ID_4_GOAL):
            DXL_ID_3_GOAL = DXL_ID_3_GOAL - 10
            DXL_ID_4_GOAL = DXL_ID_4_GOAL + 10
        print("%s" % DXL_ID_3_GOAL)
        print("%s" % DXL_ID_4_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_3, ADDR_AX_GOAL_POSITION, DXL_ID_3_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_GOAL_POSITION, DXL_ID_4_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))


    elif keychar == 't':
        print('found t----------servo1-up  servo2-down')
        
        if check_moving_limits(keychar, 10, DXL_ID_5_GOAL, DXL_ID_6_GOAL):
            DXL_ID_5_GOAL = DXL_ID_5_GOAL + 10
            DXL_ID_6_GOAL = DXL_ID_6_GOAL + 10
        print("goal5 %s" % DXL_ID_5_GOAL)
        print("goal6 %s" % DXL_ID_6_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_5, ADDR_AX_GOAL_POSITION, DXL_ID_5_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id5 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id5 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_6, ADDR_AX_GOAL_POSITION, DXL_ID_6_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id6 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id6 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_6)
            
            
    elif keychar == 'z':
        print('found z----------servo1-down  servo2-up')
        
        if check_moving_limits(keychar, 10, DXL_ID_5_GOAL, DXL_ID_6_GOAL):
            DXL_ID_5_GOAL = DXL_ID_5_GOAL - 10
            DXL_ID_6_GOAL = DXL_ID_6_GOAL - 10
        print("goal5 %s" % DXL_ID_5_GOAL)
        print("goal6 %s" % DXL_ID_6_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_5, ADDR_AX_GOAL_POSITION, DXL_ID_5_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id5 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id5 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_6, ADDR_AX_GOAL_POSITION, DXL_ID_6_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id6 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id6 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_5)
            
    elif keychar == 'g':
        print('found g----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_5_GOAL, DXL_ID_6_GOAL):
            DXL_ID_5_GOAL = DXL_ID_5_GOAL + 10
            DXL_ID_6_GOAL = DXL_ID_6_GOAL - 10
        print("%s" % DXL_ID_5_GOAL)
        print("%s" % DXL_ID_6_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_5, ADDR_AX_GOAL_POSITION, DXL_ID_5_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_6, ADDR_AX_GOAL_POSITION, DXL_ID_6_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 'h':
        print('found h----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_5_GOAL, DXL_ID_6_GOAL):
            DXL_ID_5_GOAL = DXL_ID_5_GOAL - 10
            DXL_ID_6_GOAL = DXL_ID_6_GOAL + 10
        print("%s" % DXL_ID_5_GOAL)
        print("%s" % DXL_ID_6_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_5, ADDR_AX_GOAL_POSITION, DXL_ID_5_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_6, ADDR_AX_GOAL_POSITION, DXL_ID_6_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))        
            
            
    elif keychar == 'u':
        print('found u----------servo1-up  servo2-down')
        
        if check_moving_limits(keychar, 10, DXL_ID_7_GOAL, DXL_ID_8_GOAL):
            DXL_ID_7_GOAL = DXL_ID_7_GOAL + 10
            DXL_ID_8_GOAL = DXL_ID_8_GOAL + 10
        print("goal7 %s" % DXL_ID_7_GOAL)
        print("goal8 %s" % DXL_ID_8_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_7, ADDR_AX_GOAL_POSITION, DXL_ID_7_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id7 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id7 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_8, ADDR_AX_GOAL_POSITION, DXL_ID_8_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id8 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id8 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_8)
            
            
    elif keychar == 'i':
        print('found i----------servo1-down  servo2-up')
        
        if check_moving_limits(keychar, 10, DXL_ID_7_GOAL, DXL_ID_8_GOAL):
            DXL_ID_7_GOAL = DXL_ID_7_GOAL - 10
            DXL_ID_8_GOAL = DXL_ID_8_GOAL - 10
        print("goal7 %s" % DXL_ID_7_GOAL)
        print("goal8 %s" % DXL_ID_8_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_7, ADDR_AX_GOAL_POSITION, DXL_ID_7_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id7 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id7 %s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_8, ADDR_AX_GOAL_POSITION, DXL_ID_8_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("id8 %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("id8 %s" % packetHandler.getRxPacketError(dxl_error))
            
        check_all_torque_limits(DXL_ID_7)
            
    elif keychar == 'j':
        print('found j----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_7_GOAL, DXL_ID_8_GOAL):
            DXL_ID_7_GOAL = DXL_ID_7_GOAL + 10
            DXL_ID_8_GOAL = DXL_ID_8_GOAL - 10
        print("%s" % DXL_ID_7_GOAL)
        print("%s" % DXL_ID_8_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_7, ADDR_AX_GOAL_POSITION, DXL_ID_7_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_8, ADDR_AX_GOAL_POSITION, DXL_ID_8_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        
    elif keychar == 'k':
        print('found k----------servo1-2 down')
        
        if check_moving_limits(keychar, 10, DXL_ID_7_GOAL, DXL_ID_8_GOAL):
            DXL_ID_7_GOAL = DXL_ID_7_GOAL - 10
            DXL_ID_8_GOAL = DXL_ID_8_GOAL + 10
        print("%s" % DXL_ID_7_GOAL)
        print("%s" % DXL_ID_8_GOAL)
        
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_7, ADDR_AX_GOAL_POSITION, DXL_ID_7_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_8, ADDR_AX_GOAL_POSITION, DXL_ID_8_GOAL)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))      

#     # Write goal position
#     dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_GOAL_POSITION, dxl_goal_position[index])
#     if dxl_comm_result != COMM_SUCCESS:
#         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
#     elif dxl_error != 0:
#         print("%s" % packetHandler.getRxPacketError(dxl_error))
# 
#     while 1:
#         # Read present position
#         dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_PRESENT_POSITION)
#         if dxl_comm_result != COMM_SUCCESS:
#             print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
#         elif dxl_error != 0:
#             print("%s" % packetHandler.getRxPacketError(dxl_error))
# 
#         print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_1, dxl_goal_position[index], dxl_present_position))
# 
#         if not abs(dxl_goal_position[index] - dxl_present_position) > DXL_MOVING_STATUS_THRESHOLD:
#             break
# 
#     # Change goal position
#     if index == 0:
#         index = 1
#     else:
#         index = 0


# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID_1, ADDR_AX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()