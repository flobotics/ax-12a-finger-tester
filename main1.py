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


def get_config_dict():
    config = dict();
    config['ADDR_AX_MODEL_NUMBER']= 0
    config['ADDR_AX_FIRMWARE_VERSION']= 2
    config['ADDR_AX_ID']= 3
    config['ADDR_AX_BAUDRATE_BUS']= 4
    config['ADDR_AX_RETURN_DELAY_TIME']= 5
    config['ADDR_AX_CW_ANGLE_LIMIT']= 6
    config['ADDR_AX_CCW_ANGLE_LIMIT']= 8
    config['ADDR_AX_TEMPERATURE_LIMIT']= 11
    config['ADDR_AX_MIN_VOLTAGE_LIMIT']= 12
    config['ADDR_AX_MAX_VOLTAGE_LIMIT']= 13
    config['ADDR_AX_MAX_TORQUE']= 14
    config['ADDR_AX_STATUS_RETURN_LEVEL']= 16
    config['ADDR_AX_ALARM_LED']= 17
    config['ADDR_AX_SHUTDOWN']= 18
    config['ADDR_AX_TORQUE_ENABLE']= 24
    config['ADDR_AX_LED']= 25
    config['ADDR_AX_CW_COMPLIANCE_MARGIN']= 26
    config['ADDR_AX_CCW_COMPLIANCE_MARGIN']= 27
    config['ADDR_AX_CW_COMPLIANCE_SLOPE']= 28
    config['ADDR_AX_CCW_COMPLIANCE_MARGIN']= 29
    config['ADDR_AX_GOAL_POSITION']= 30
    config['ADDR_AX_MOVING_SPEED']= 32
    config['ADDR_AX_TORQUE_LIMIT']= 34
    config['ADDR_AX_PRESENT_POSITION']= 36
    config['ADDR_AX_PRESENT_SPEED']= 38
    config['ADDR_AX_PRESENT_LOAD']= 40
    config['ADDR_AX_PRESENT_INPUT_VOLTAGE']= 42
    config['ADDR_AX_PRESENT_TEMPERATURE']= 43
    config['ADDR_AX_REGISTERED']= 44
    config['ADDR_AX_MOVING']= 46
    config['ADDR_AX_LOCK']= 47
    config['ADDR_AX_PUNCH']= 48
    
    
#     config['ADDR_AX_TORQUE_ENABLE']= 24
#     config['ADDR_AX_GOAL_POSITION']= 30
#     config['ADDR_AX_PRESENT_POSITION']= 36
#     config['ADDR_AX_LED']= 25
#     config['ADDR_AX_MOVING_SPEED']= 32
#     config['ADDR_AX_TORQUE_LIMIT']= 34
#     config['ADDR_AX_PRESENT_LOAD']= 40
    
    
    config['PROTOCOL_VERSION']= 1.0
    config['BAUDRATE']= 1000000
    config['DEVICENAME']= '/dev/ttyUSB0'
    config['DAX_ID_1']= 1
    config['DAX_ID_2']= 2
    config['DAX_ID_3']= 3
    config['DAX_ID_4']= 4
    config['DAX_ID_5']= 5
    config['DAX_ID_6']= 6
    config['DAX_ID_7']= 7
    config['DAX_ID_8']= 8
    config['DAX_ID_1_GOAL']= 0
    config['DAX_ID_2_GOAL']= 0
    config['DAX_ID_3_GOAL']= 0
    config['DAX_ID_4_GOAL']= 0
    config['DAX_ID_5_GOAL']= 0
    config['DAX_ID_6_GOAL']= 0
    config['DAX_ID_7_GOAL']= 0
    config['DAX_ID_8_GOAL']= 0
    
    config['DAX_ID_1_GOAL_MIN']= 0
    config['DAX_ID_2_GOAL_MIN']= 0
    config['DAX_ID_3_GOAL_MIN']= 0
    config['DAX_ID_4_GOAL_MIN']= 0
    config['DAX_ID_5_GOAL_MIN']= 0
    config['DAX_ID_6_GOAL_MIN']= 0
    config['DAX_ID_7_GOAL_MIN']= 0
    config['DAX_ID_8_GOAL_MIN']= 0
    
    config['DAX_ID_1_GOAL_MAX']= 1023
    config['DAX_ID_2_GOAL_MAX']= 1023
    config['DAX_ID_3_GOAL_MAX']= 1023
    config['DAX_ID_4_GOAL_MAX']= 1023
    config['DAX_ID_5_GOAL_MAX']= 1023
    config['DAX_ID_6_GOAL_MAX']= 1023
    config['DAX_ID_7_GOAL_MAX']= 1023
    config['DAX_ID_8_GOAL_MAX']= 1023
    
    config['DAX_ID_1_2_SPEED'] = 200
    config['DAX_ID_3_4_SPEED'] = 200
    config['DAX_ID_5_6_SPEED'] = 200
    config['DAX_ID_7_8_SPEED'] = 200
    
    config['DAX_ID_1_TORQUE_LIMIT']= 300
    config['DAX_ID_2_TORQUE_LIMIT']= 300
    config['DAX_ID_3_TORQUE_LIMIT']= 300
    config['DAX_ID_4_TORQUE_LIMIT']= 300
    config['DAX_ID_5_TORQUE_LIMIT']= 300
    config['DAX_ID_6_TORQUE_LIMIT']= 300
    config['DAX_ID_7_TORQUE_LIMIT']= 300
    config['DAX_ID_8_TORQUE_LIMIT']= 300
    config['DAX_ID_1_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_2_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_3_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_4_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_5_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_6_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_7_MOVING_TORQUE_LIMIT']= 300
    config['DAX_ID_8_MOVING_TORQUE_LIMIT']= 300
    
    config['TORQUE_ENABLE']= 1
    config['TORQUE_DISABLE']= 0
    
    return config

def open_port(ph):
    if ph.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()
        
def set_port_baudrate(ph, config):
    if ph.setBaudRate(config['BAUDRATE']):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()
        
def ax12_enable_torque(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write1ByteTxRx(po_h, id, config['ADDR_AX_TORQUE_ENABLE'], config['TORQUE_ENABLE'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Torque:enabled" % (id))
        
        
def ax12_read_present_position(pa_h, po_h, id, config):
    dxl_present_position, dxl_comm_result, dxl_error = pa_h.read2ByteTxRx(po_h, id, config['ADDR_AX_PRESENT_POSITION'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    
    print("[ID:%03d] PresentPos:%03d" % (id, dxl_present_position))
    config['DAX_ID_' + str(id) + '_GOAL'] = dxl_present_position
    

def ax12_write_torque_limit(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_TORQUE_LIMIT'], config['DAX_ID_' + str(id) + '_TORQUE_LIMIT'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Set Torque Limit:%d" % (id, config['ADDR_AX_TORQUE_LIMIT']))
        
        
def ax12_write_goal_position(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_GOAL_POSITION'], config['DAX_ID_' + str(id) + '_GOAL'])
    if dxl_comm_result != COMM_SUCCESS:
        print("id %s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("id %s" % pa_h.getRxPacketError(dxl_error))
        
        
def ax12_write_moving_speed(pa_h, po_h, id, config):
    if id == 1 or id == 2:
        DXA_ID_SPEED = config['DAX_ID_1_2_SPEED']
    if id == 3 or id == 4:
        DXA_ID_SPEED = config['DAX_ID_3_4_SPEED']
    if id == 5 or id == 6:
        DXA_ID_SPEED = config['DAX_ID_5_6_SPEED']
    if id == 7 or id == 8:
        DXA_ID_SPEED = config['DAX_ID_7_8_SPEED']
        
    # Write speed
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, config['DAX_ID_' + str(id)], config['ADDR_AX_MOVING_SPEED'], DXA_ID_SPEED)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
        
        
        
###    newwww
def check_moving_limits(left_servo_used, stepsize, left_id, right_id, LEFT_ID_GOAL, RIGHT_ID_GOAL, config):
    if left_servo_used:
        if ((LEFT_ID_GOAL + stepsize) <= config['DAX_ID_' + str(left_id) + '_GOAL_MAX']) and ((RIGHT_ID_GOAL + stepsize) <= config['DAX_ID_' + str(right_id) + '_GOAL_MAX']):
            return True
        else:
            return False
    else:
        if ((LEFT_ID_GOAL - stepsize) >= config['DAX_ID_' + str(left_id) + '_GOAL_MIN']) and ((RIGHT_ID_GOAL - stepsize) >= config['DAX_ID_' + str(right_id) + '_GOAL_MIN']):
            return True
        else:
            return False
    
    
def check_torque_limit(id, DXL_ID_GOAL, turn_cw, pa_h, po_h, config):
    do_work = True
    
    while do_work:
        # Read present position
        dxl_present_torque, dxl_comm_result, dxl_error = pa_h.read2ByteTxRx(po_h, id, config['ADDR_AX_PRESENT_LOAD'])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % pa_h.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % pa_h.getRxPacketError(dxl_error))
        
#         print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, dxl_goal_position[index], dxl_present_torque))
#         DXL_ID_PRESENT_TORQUE = dxl_present_torque
        print("[ID:%03d] PresPos:%s" % (id, dxl_present_torque))
        print("[ID:%03d] Torque-limit:%d" % (id, config['DAX_ID_' + str(id) + '_MOVING_TORQUE_LIMIT']))
       
        
        if dxl_present_torque > config['DAX_ID_' + str(id) + '_MOVING_TORQUE_LIMIT']:
            ### if cw=clock-wise
            if turn_cw:
               config['DAX_ID_' + str(id) + '_GOAL'] = config['DAX_ID_' + str(id) + '_GOAL'] - 2
            else:
                config['DAX_ID_' + str(id) + '_GOAL'] = config['DAX_ID_' + str(id) + '_GOAL'] + 2
                
            # Write goal position
            dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_GOAL_POSITION'], config['DAX_ID_' + str(id) + '_GOAL'])
            if dxl_comm_result != COMM_SUCCESS:
                print("id %s" % pa_h.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("id %s" % pa_h.getRxPacketError(dxl_error))
                
        else:
            do_work = False
        
        
def check_all_torque_limits(dont_check, pa_h, po_h, config):
    if dont_check is not 1:
        check_torque_limit(config['DAX_ID_1'] , config['DAX_ID_1_GOAL'], False, pa_h, po_h, config)
    if dont_check is not 2:
        check_torque_limit(config['DAX_ID_2'], config['DAX_ID_2_GOAL'], True, pa_h, po_h, config)
    if dont_check is not 3:
        check_torque_limit(config['DAX_ID_3'], config['DAX_ID_3_GOAL'], False, pa_h, po_h, config)
    if dont_check is not 4:
        check_torque_limit(config['DAX_ID_4'], config['DAX_ID_4_GOAL'], True, pa_h, po_h, config)
    if dont_check is not 5:
        check_torque_limit(config['DAX_ID_5'], config['DAX_ID_5_GOAL'], False, pa_h, po_h, config)
    if dont_check is not 6:
        check_torque_limit(config['DAX_ID_6'], config['DAX_ID_6_GOAL'], True, pa_h, po_h, config)
    if dont_check is not 7:
        check_torque_limit(config['DAX_ID_7'], config['DAX_ID_7_GOAL'], False, pa_h, po_h, config)
    if dont_check is not 8:
        check_torque_limit(config['DAX_ID_8'], config['DAX_ID_8_GOAL'], True, pa_h, po_h, config)         


    
        
def main():
    print('finger controller')
    
    config = get_config_dict()    
    print(config)
    
    portHandler = PortHandler(config['DEVICENAME'])
    packetHandler = PacketHandler(config['PROTOCOL_VERSION'])
    
    open_port(portHandler)
    set_port_baudrate(portHandler, config)
    
    for i in range(1,9):
        ax12_enable_torque(packetHandler, portHandler, i, config)
        ax12_write_torque_limit(packetHandler, portHandler, i, config, )
        ax12_read_present_position(packetHandler, portHandler, i, config)
        ax12_write_moving_speed(packetHandler, portHandler, i, config)
        print("%d" % config['DAX_ID_' + str(i) + '_GOAL'])
        
        
    while 1:
        print("Press any key to continue! (or press ESC to quit!)")
    #     if isData():
    #         c = sys.stdin.read(1)
        keychar = getch()
        if keychar == chr(0x1b):
            break
        elif keychar == 'q' or keychar == 'e' or keychar == 't' or keychar == 'u':
            print('found q----------servo1-up  servo2-down')
            print(keychar)
            
            if keychar == 'q':
                r_id = 1
                l_id = 2
            elif keychar == 'e':
                r_id = 3
                l_id = 4
            elif keychar == 't':
                r_id = 5
                l_id = 6
            elif keychar == 'u':
                r_id = 7
                l_id = 8
            
            if check_moving_limits(True, 
                                   10, 
                                   config['DAX_ID_' + str(l_id)], 
                                   config['DAX_ID_' + str(r_id)],
                                   config['DAX_ID_' + str(r_id) + '_GOAL'], 
                                   config['DAX_ID_' + str(l_id) + '_GOAL'], 
                                   config):
                config['DAX_ID_' + str(r_id) + '_GOAL'] = config['DAX_ID_' + str(r_id) + '_GOAL'] + 10
                config['DAX_ID_' + str(l_id) + '_GOAL'] = config['DAX_ID_' + str(l_id) + '_GOAL'] + 10
            print("%s" % config['DAX_ID_' + str(r_id) + '_GOAL'])
            print("%s" % config['DAX_ID_' + str(l_id) + '_GOAL'])
            
            # Write goal position
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(r_id)], config)
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(l_id)], config)
                
            check_all_torque_limits(config['DAX_ID_' + str(l_id)], packetHandler, portHandler, config)
            
            
        elif keychar == 'w' or keychar == 'r' or keychar == 'z' or keychar == 'i':
            print('found w----------servo1-down  servo2-up')
            
            if keychar == 'w':
                r_id = 1
                l_id = 2
            elif keychar == 'r':
                r_id = 3
                l_id = 4
            elif keychar == 'z':
                r_id = 5
                l_id = 6
            elif keychar == 'i':
                r_id = 7
                l_id = 8
            
            if check_moving_limits(False, 
                                   10,
                                   config['DAX_ID_' + str(l_id)], 
                                   config['DAX_ID_' + str(r_id)],  
                                   config['DAX_ID_' + str(l_id) + '_GOAL'], 
                                   config['DAX_ID_' + str(r_id) + '_GOAL'], 
                                   config):
                config['DAX_ID_' + str(r_id) + '_GOAL'] = config['DAX_ID_' + str(r_id) + '_GOAL'] - 10
                config['DAX_ID_' + str(l_id) + '_GOAL'] = config['DAX_ID_' + str(l_id) + '_GOAL'] - 10
            print("%s" % config['DAX_ID_' + str(r_id) + '_GOAL'])
            print("%s" % config['DAX_ID_' + str(l_id) + '_GOAL'])
            
            # Write goal position
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(r_id)], config)
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(l_id)], config)
            
            
            check_all_torque_limits(config['DAX_ID_' + str(r_id)], packetHandler, portHandler, config)
            
            
            
            
            
            
            
        elif keychar == 'a' or keychar == 'd' or keychar == 'g' or keychar == 'j':
            print('found a----------servo1-2 up')
            
            if keychar == 'a':
                r_id = 1
                l_id = 2
            elif keychar == 'd':
                r_id = 3
                l_id = 4
            elif keychar == 'g':
                r_id = 5
                l_id = 6
            elif keychar == 'j':
                r_id = 7
                l_id = 8
            
            if check_moving_limits(True, 
                                   10, 
                                   config['DAX_ID_' + str(l_id)], 
                                   config['DAX_ID_' + str(r_id)],
                                   config['DAX_ID_' + str(r_id) + '_GOAL'], 
                                   config['DAX_ID_' + str(l_id) + '_GOAL'], 
                                   config):
            
#             if check_moving_limits(keychar, 10, DXL_ID_1_GOAL, DXL_ID_2_GOAL):
                config['DAX_ID_' + str(r_id) + '_GOAL'] = config['DAX_ID_' + str(r_id) + '_GOAL'] + 10
                config['DAX_ID_' + str(l_id) + '_GOAL'] = config['DAX_ID_' + str(l_id) + '_GOAL'] - 10
            print("%s" % config['DAX_ID_' + str(r_id) + '_GOAL'])
            print("%s" % config['DAX_ID_' + str(l_id) + '_GOAL'])
            
            
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(r_id)], config)
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(l_id)], config)
            
            
        elif keychar == 's' or keychar == 'f' or keychar == 'h' or keychar == 'k':
            print('found s----------servo1-2 down')
            
            if keychar == 's':
                r_id = 1
                l_id = 2
            elif keychar == 'f':
                r_id = 3
                l_id = 4
            elif keychar == 'h':
                r_id = 5
                l_id = 6
            elif keychar == 'k':
                r_id = 7
                l_id = 8
            
            if check_moving_limits(False, 
                                   10,
                                   config['DAX_ID_' + str(l_id)], 
                                   config['DAX_ID_' + str(r_id)],  
                                   config['DAX_ID_' + str(l_id) + '_GOAL'], 
                                   config['DAX_ID_' + str(r_id) + '_GOAL'], 
                                   config):
                config['DAX_ID_' + str(r_id) + '_GOAL'] = config['DAX_ID_' + str(r_id) + '_GOAL'] - 10
                config['DAX_ID_' + str(l_id) + '_GOAL'] = config['DAX_ID_' + str(l_id) + '_GOAL'] + 10
            print("%s" % config['DAX_ID_' + str(r_id) + '_GOAL'])
            print("%s" % config['DAX_ID_' + str(l_id) + '_GOAL'])
            
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(r_id)], config)
            ax12_write_goal_position(packetHandler, portHandler, config['DAX_ID_' + str(l_id)], config)
            

        elif keychar == 'y' or keychar == 'c' or keychar == 'b' or keychar == 'm':
            print('found y----------servo1-2  speed up') 
            
            if keychar == 'y':
                config['DAX_ID_1_2_SPEED'] = config['DAX_ID_1_2_SPEED'] + 10
                DXA_ID_SPEED = config['DAX_ID_1_2_SPEED']
                r_id = 1
                l_id = 2
            elif keychar == 'c':
                config['DAX_ID_3_4_SPEED'] = config['DAX_ID_3_4_SPEED'] + 10
                DXA_ID_SPEED = config['DAX_ID_3_4_SPEED']
                r_id = 3
                l_id = 4
            elif keychar == 'b':
                config['DAX_ID_5_6_SPEED'] = config['DAX_ID_5_6_SPEED'] + 10
                DXA_ID_SPEED = config['DAX_ID_5_6_SPEED']
                r_id = 5
                l_id = 6
            elif keychar == 'm':
                config['DAX_ID_7_8_SPEED'] = config['DAX_ID_7_8_SPEED'] + 10
                DXA_ID_SPEED = config['DAX_ID_7_8_SPEED']
                r_id = 7
                l_id = 8
            
             
            print("%s" % DXA_ID_SPEED)
            
            # Write speed
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, config['DAX_ID_' + str(l_id)], config['ADDR_AX_MOVING_SPEED'], DXA_ID_SPEED)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
                
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, config['DAX_ID_' + str(r_id)], config['ADDR_AX_MOVING_SPEED'], DXA_ID_SPEED)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            
        elif keychar == 'x' or keychar == 'v' or keychar == 'n' or keychar == ',':
            print('found y----------servo1-2  speed down') 
            
            if keychar == 'x':
                config['DAX_ID_1_2_SPEED'] = config['DAX_ID_1_2_SPEED'] - 10
                DXA_ID_SPEED = config['DAX_ID_1_2_SPEED']
                r_id = 1
                l_id = 2
            elif keychar == 'v':
                config['DAX_ID_3_4_SPEED'] = config['DAX_ID_3_4_SPEED'] - 10
                DXA_ID_SPEED = config['DAX_ID_3_4_SPEED']
                r_id = 3
                l_id = 4
            elif keychar == 'n':
                config['DAX_ID_5_6_SPEED'] = config['DAX_ID_5_6_SPEED'] - 10
                DXA_ID_SPEED = config['DAX_ID_5_6_SPEED']
                r_id = 5
                l_id = 6
            elif keychar == ',':
                config['DAX_ID_7_8_SPEED'] = config['DAX_ID_7_8_SPEED'] - 10
                DXA_ID_SPEED = config['DAX_ID_7_8_SPEED']
                r_id = 7
                l_id = 8
            
            print("%s" % DXA_ID_SPEED)
            
            # Write speed
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, config['DAX_ID_' + str(r_id)], config['ADDR_AX_MOVING_SPEED'], DXA_ID_SPEED)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
                
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, config['DAX_ID_' + str(l_id)], config['ADDR_AX_MOVING_SPEED'], DXA_ID_SPEED)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))      
        

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
    
    