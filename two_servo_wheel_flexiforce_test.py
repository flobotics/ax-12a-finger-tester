import sys
import sys, tty, termios
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from _ast import Or
import socket
import time

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

def ax12_enable_torque(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write1ByteTxRx(po_h, id, config['ADDR_AX_TORQUE_ENABLE'], config['TORQUE_ENABLE'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Torque:enabled" % (id))
        
def ax12_disable_torque(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write1ByteTxRx(po_h, id, config['ADDR_AX_TORQUE_ENABLE'], config['TORQUE_DISABLE'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Torque:enabled" % (id))
        
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
    
    
    config['VALUE_AX_MAX_TORQUE_1']= 1023
    config['VALUE_AX_MAX_TORQUE_2']= 1023
    config['VALUE_AX_MAX_TORQUE_3']= 1023
    config['VALUE_AX_MAX_TORQUE_4']= 1023
    config['VALUE_AX_MAX_TORQUE_5']= 1023
    config['VALUE_AX_MAX_TORQUE_6']= 1023
    config['VALUE_AX_MAX_TORQUE_7']= 1023
    config['VALUE_AX_MAX_TORQUE_8']= 1023
    

    
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
    
    config['DAX_ID_1_TORQUE_LIMIT']= 400
    config['DAX_ID_2_TORQUE_LIMIT']= 400
    config['DAX_ID_3_TORQUE_LIMIT']= 400
    config['DAX_ID_4_TORQUE_LIMIT']= 400
    config['DAX_ID_5_TORQUE_LIMIT']= 400
    config['DAX_ID_6_TORQUE_LIMIT']= 400
    config['DAX_ID_7_TORQUE_LIMIT']= 400
    config['DAX_ID_8_TORQUE_LIMIT']= 400
    config['DAX_ID_1_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_2_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_3_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_4_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_5_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_6_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_7_MOVING_TORQUE_LIMIT']= 600
    config['DAX_ID_8_MOVING_TORQUE_LIMIT']= 600
    
    config['TORQUE_ENABLE']= 1
    config['TORQUE_DISABLE']= 0
    config['WHEEL_MODE'] = 0
    config['JOINT_MODE'] = 1023
    
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
        
        
def ax12_read_present_position(pa_h, po_h, id, config):
    dxl_present_position, dxl_comm_result, dxl_error = pa_h.read2ByteTxRx(po_h, id, config['ADDR_AX_PRESENT_POSITION'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    
    print("[ID:%03d] PresentPos:%03d" % (id, dxl_present_position))
    config['DAX_ID_' + str(id) + '_GOAL'] = dxl_present_position


def ax12_read_present_load(pa_h, po_h, id, config):
    dxl_present_torque, dxl_comm_result, dxl_error = pa_h.read2ByteTxRx(po_h, id, config['ADDR_AX_PRESENT_LOAD'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    
#         print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, dxl_goal_position[index], dxl_present_torque))
#         DXL_ID_PRESENT_TORQUE = dxl_present_torque
    print("[ID:%03d] PresLoad:%d" % (id, dxl_present_torque))
    
    return dxl_present_torque

            
def ax12_write_goal_position(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_GOAL_POSITION'], config['DAX_ID_' + str(id) + '_GOAL'])
    if dxl_comm_result != COMM_SUCCESS:
        print("id %s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("id %s" % pa_h.getRxPacketError(dxl_error))
        
def ax12_write_max_torque(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_MAX_TORQUE'], config['VALUE_AX_MAX_TORQUE_' + str(id)])
    if dxl_comm_result != COMM_SUCCESS:
        print("id %s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("id %s" % pa_h.getRxPacketError(dxl_error))
        
def ax12_write_moving_speed(pa_h, po_h, id, speed, config):
        
    # Write speed
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_MOVING_SPEED'], speed)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
        
def ax12_write_torque_limit(pa_h, po_h, id, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_TORQUE_LIMIT'], config['DAX_ID_' + str(id) + '_TORQUE_LIMIT'])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Set Torque Limit:%d" % (id, config['ADDR_AX_TORQUE_LIMIT']))
        
def ax12_write_ccw_angle_limit(pa_h, po_h, id, mode, config):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, config['ADDR_AX_CCW_ANGLE_LIMIT'], mode)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Set Torque Limit:%d" % (id, config['ADDR_AX_TORQUE_LIMIT']))
        
                                                
def main():
    print('finger controller')
    
    s = socket.socket()
    port = 1500
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    print ('Got connection from', addr )
    
    config = get_config_dict()    
    print(config)
    
    portHandler = PortHandler(config['DEVICENAME'])
    packetHandler = PacketHandler(config['PROTOCOL_VERSION'])
    
    open_port(portHandler)
    set_port_baudrate(portHandler, config)
    
    
    
    for i in range(7,9):
        ax12_write_ccw_angle_limit(packetHandler, portHandler, i, config['WHEEL_MODE'], config)
        ax12_enable_torque(packetHandler, portHandler, i, config)
        ax12_write_torque_limit(packetHandler, portHandler, i, config)
        ax12_write_max_torque(packetHandler, portHandler, i, config)

    
    while 1:
#         print("Press any key to continue! (or press ESC to quit!)")
    #     if isData():
    #         c = sys.stdin.read(1)
        keychar = getch1()
        if keychar == chr(0x1b):
            break
        elif keychar == 'o':
            print('found o----------servo7-8 setup %d' % i)
            
            ctrl7 = True
            ctrl8 = True
            while (ctrl7 or ctrl8):
                print('c7 %d' % ctrl7)
                print('c8 %d' % ctrl8)
               
                
                c.send(b'get7') 
                data = c.recv(8)
                print('data7 %f' % float(data))
                if(float(data) > 0.010000):
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 0, config)
                    ctrl7 = False
                else:
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 100, config)

                c.send(b'get8') 
                data = c.recv(8)
                print('data8 %f' % float(data))
                if(float(data) > 0.010000):
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 1024, config)
                    ctrl8 = False
                else:
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 1123, config)
                    
                
                    
                time.sleep(0.1)
                
            print('end o');
            
        elif keychar == 'q' or keychar == 'e' or keychar == 't' or keychar == 'u':
            #send speed  e.g. 5 to servo-thread-7
            #wait 0.1 second
            #send speed 0 to servo-thread-7
            
            ctrl8 = True
                
            c.send(b'get7') 
            data = c.recv(8)
            print('data7 %f' % float(data))
            ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 200, config)
            time.sleep(0.1)
            ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 0, config)
           
            while (ctrl8):
                c.send(b'get8') 
                data = c.recv(8)
                print('data8 %f' % float(data))
                if(float(data) > 0.03):
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 200, config)
                    print('a')
                else:
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 0, config)    
                    ctrl8 = False
                    print('b')
                        
                
                    
                
                
            print('end q');
        elif keychar == 'w' or keychar == 'r' or keychar == 'z' or keychar == 'i':
            print('found w----------servo1-up  servo2-down %d' % i)
            
            ctrl7 = True
                
            c.send(b'get8') 
            data = c.recv(8)
            print('data8 %f' % float(data))
            ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 1223, config)
            time.sleep(0.1)
            ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 0, config)
           
            while (ctrl7):
                c.send(b'get7') 
                data = c.recv(8)
                print('data7 %f' % float(data))
                if(float(data) > 0.030000):
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 1223, config)
                else:
                    ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_7'], 0, config)    
                    ctrl7 = False
                        
                
                    
                
                
            print('end w');

    c.close() 
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    