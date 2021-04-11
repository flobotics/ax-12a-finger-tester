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
    elif keychar == 'e':
        if ((DXL_ID_3_GOAL + stepsize) <= DXL_ID_3_GOAL_MAX) and ((DXL_ID_4_GOAL + stepsize) <= DXL_ID_4_GOAL_MAX):
            return True
#                 DXL_ID_1_GOAL = DXL_ID_1_GOAL + 10
#                 DXL_ID_2_GOAL = DXL_ID_2_GOAL + 10
        else:
            return False
    elif keychar == 'r':
        if ((DXL_ID_3_GOAL - stepsize) >= DXL_ID_3_GOAL_MIN) and ((DXL_ID_4_GOAL - stepsize) >= DXL_ID_4_GOAL_MIN):
            return True
        else:
            return False



# Control table address
ADDR_AX_TORQUE_ENABLE       = 24                          # Control table address is different in Dynamixel model
ADDR_AX_GOAL_POSITION       = 30
ADDR_AX_PRESENT_POSITION    = 36
ADDR_AX_LED                 = 25  #1byte
ADDR_MOVING_SPEED           = 32   #2byte   0->1023    0=full,  1=very-very-slow  ,100=faster 1023=fastest
ADDR_TORQUE_LIMIT          = 34    #2byte  0->1023

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID_1                      = 7                 # Dynamixel ID : 1
DXL_ID_2                      = 8                 # Dynamixel ID : 1
DXL_ID_3                      = 5                 # Dynamixel ID : 1
DXL_ID_4                      = 6                 # Dynamixel ID : 1
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

DXL_ID_1_TORQUE_LIMIT       = 1023

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

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_1, dxl_goal_position[index], dxl_present_position))
DXL_ID_3_GOAL = dxl_present_position

dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID_4, ADDR_AX_PRESENT_POSITION)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID_2, dxl_goal_position[index], dxl_present_position))
DXL_ID_4_GOAL = dxl_present_position
# DXL_ID_2_GOAL = 1023 - DXL_ID_1_GOAL


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
        
        
    elif keychar == 'a':
        print('found a----------servo1-2 up')
        
        if (DXL_ID_1_GOAL + 10) <= 1023:
            DXL_ID_1_GOAL = DXL_ID_1_GOAL + 10
            DXL_ID_2_GOAL = 1023 - DXL_ID_1_GOAL
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
        
        if (DXL_ID_1_GOAL - 10) >= 0:
            DXL_ID_1_GOAL = DXL_ID_1_GOAL - 10
            DXL_ID_2_GOAL = 1023 - DXL_ID_1_GOAL
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