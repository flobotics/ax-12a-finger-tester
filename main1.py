import sys
import sys, tty, termios
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

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
    config['DAX_ID_1_TORQUE_LIMIT']= 1
    config['DAX_ID_2_TORQUE_LIMIT']= 2
    config['DAX_ID_3_TORQUE_LIMIT']= 3
    config['DAX_ID_4_TORQUE_LIMIT']= 4
    config['DAX_ID_5_TORQUE_LIMIT']= 5
    config['DAX_ID_6_TORQUE_LIMIT']= 6
    config['DAX_ID_7_TORQUE_LIMIT']= 7
    config['DAX_ID_8_TORQUE_LIMIT']= 8
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
        print("%d" % config['DAX_ID_' + str(i) + '_GOAL'])
    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
    
    