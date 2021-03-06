import threading
import time 
from queue import Queue
from queue import Empty
import socket
from dynamixel_sdk import *
import sys
import sys, tty, termios

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

# import sys
# import sys, tty, termios
# from dynamixel_sdk import *                    # Uses Dynamixel SDK library
# from _ast import Or
# import socket
# import time


write_lock = threading.Lock()

class MyThread1(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_messages = args[0]
        self.id = args[0]
        self.flexiforceSocket = args[1]
        self.pa_h = args[2]
        self.po_h = args[3]
        self.addr_ax_moving_speed = 32
        if self.id == 1:
            self.servo_release_speed = 1123
            self.partner_servo_id = 2
        elif self.id == 2:
            self.servo_release_speed = 100
            self.partner_servo_id = 1
        self.stopping = False
        self.partner_servo_moving = False
        self.partner_servo_speed = 0
        
        ##id  flexi-socket  pa po
        

    def run(self):
        while True:
#             print("id:" + threading.currentThread().getName() + " msg:" + str(self.receive_messages))
#             val = self.queue.get_nowait()
            try:
                val = self.queue.get(False)
            except Empty:
                # Handle empty queue here
                # get flexiforce value
                # if value too high -> stop
                # if value absolut too high -> release
                idStr = str(self.id)
                getStr = 'get' + idStr
                with write_lock:
                    self.flexiforceSocket.send(getStr.encode('ascii')) 
                    data = self.flexiforceSocket.recv(8)
#                     print('data %f' % float(data))
#                     print("id:" + threading.currentThread().getName() + " data:" + data.decode('ascii'))
                #Notstop
                if float(data) > 0.5:
                    print('data>0.2 %f' % float(data))
                    self.stopping = True
                    # Write speed
                    with write_lock:
                        dxl_comm_result, dxl_error = self.pa_h.write2ByteTxRx(self.po_h, int(self.id), int(self.addr_ax_moving_speed), int(self.servo_release_speed))
                        if dxl_comm_result != COMM_SUCCESS:
                            print("%s" % self.pa_h.getTxRxResult(dxl_comm_result))
                        elif dxl_error != 0:
                            print("%s" % self.pa_h.getRxPacketError(dxl_error)) 
                elif self.stopping:
                    print('data-stopping %f' % float(data))
                    self.stopping = False
                    # Write speed
                    with write_lock:
                        dxl_comm_result, dxl_error = self.pa_h.write2ByteTxRx(self.po_h, int(self.id), int(self.addr_ax_moving_speed), 0)
                        if dxl_comm_result != COMM_SUCCESS:
                            print("%s" % self.pa_h.getTxRxResult(dxl_comm_result))
                        elif dxl_error != 0:
                            print("%s" % self.pa_h.getRxPacketError(dxl_error))
                        
#                     ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 0, config)    
                elif self.partner_servo_moving:
#                    
                    if float(data) > 0.03: 
                        print('data-partner-moving %f' % float(data))
                        # Write speed
                        with write_lock:
                            dxl_comm_result, dxl_error = self.pa_h.write2ByteTxRx(self.po_h, int(self.id), int(self.addr_ax_moving_speed), int(self.partner_servo_speed))
                            if dxl_comm_result != COMM_SUCCESS:
                                print("%s" % self.pa_h.getTxRxResult(dxl_comm_result))
                            elif dxl_error != 0:
                                print("%s" % self.pa_h.getRxPacketError(dxl_error))

                    
                    
#                 pass
            else:
#                 print("msg recv >" + self.flexiforceSocket + "<")
                vals = val.split()
                if int(vals[0]) == self.partner_servo_id:
#                     print("servo1")
                    if int(vals[1]) == 0 or int(vals[1]) == 1023:
                        self.partner_servo_moving = False
                        self.stopping = True
                    else:
                        self.partner_servo_moving = True
                        
                    if int(vals[1]) > 1023:
                        self.partner_servo_speed = int(vals[1]) - 1023
                    else:
                        self.partner_servo_speed = int(vals[1]) + 1023
                    
                    
                elif int(vals[0]) == int(self.id):
                    # Write speed
                    with write_lock:
                        dxl_comm_result, dxl_error = self.pa_h.write2ByteTxRx(self.po_h, int(self.id), int(self.addr_ax_moving_speed), int(vals[1]))
                        if dxl_comm_result != COMM_SUCCESS:
                            print("%s" % self.pa_h.getTxRxResult(dxl_comm_result))
                        elif dxl_error != 0:
                            print("%s" % self.pa_h.getRxPacketError(dxl_error))
                
#                 self.do_thing_with_message(val)

    def do_thing_with_message(self, message):
        if self.receive_messages:
            with write_lock:
                print("id:" + threading.currentThread().getName() + " msg:" + message)




class MyThread(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
#         self.receive_messages = args[0]
        self.id = args[0]
        self.flexiforceSocket = args[1]
        self.pa_h = args[2]
        self.po_h = args[3]
        self.addr_ax_moving_speed = 32
        if self.id == 1:
            self.servo_release_speed = 100
            self.partner_servo_id = 2
            self.servo_pull_speed = 1123
            self.max_stall_force = 0.6
            self.min_stall_force = 0.5
        elif self.id == 2:
            self.servo_release_speed = 1123
            self.partner_servo_id = 1
            self.servo_pull_speed = 100
            self.max_stall_force = 0.6
            self.min_stall_force = 0.5
        elif self.id == 3:
            self.servo_release_speed = 100
            self.partner_servo_id = 4
            self.servo_pull_speed = 1123
            self.max_stall_force = 0.5
            self.min_stall_force = 0.4
        elif self.id == 4:
            self.servo_release_speed = 1123
            self.partner_servo_id = 3
            self.servo_pull_speed = 100
            self.max_stall_force = 0.5
            self.min_stall_force = 0.4
        elif self.id == 5:
            self.servo_release_speed = 100
            self.partner_servo_id = 6
            self.servo_pull_speed = 1123
            self.max_stall_force = 0.4
            self.min_stall_force = 0.3
        elif self.id == 6:
            self.servo_release_speed = 1123
            self.partner_servo_id = 5
            self.servo_pull_speed = 100
            self.max_stall_force = 0.4
            self.min_stall_force = 0.3
        elif self.id == 7:
            self.servo_release_speed = 100
            self.partner_servo_id = 8
            self.servo_pull_speed = 1123
            self.max_stall_force = 0.3
            self.min_stall_force = 0.2
        elif self.id == 8:
            self.servo_release_speed = 1123
            self.partner_servo_id = 7
            self.servo_pull_speed = 100
            self.max_stall_force = 0.3
            self.min_stall_force = 0.2
            
            
        self.stopping = False
        self.partner_servo_moving = False
        self.partner_servo_speed = 0
        
        self.self_servo_moving = False 
        
#         self.max_stall_force = 0.4
#         self.min_stall_force = 0.1
        self.max_force = 0.8
        
        ##id  flexi-socket  pa po
        

    def run(self):
        while True:
#             print("id:" + threading.currentThread().getName() + " msg:" + str(self.receive_messages))
#             val = self.queue.get_nowait()
            try:
                val = self.queue.get(False)
            except Empty:
                # Handle empty queue here
                # get flexiforce value
                # if value too high -> stop
                # if value absolut too high -> release
                idStr = str(self.id)
                getStr = 'get' + idStr
                with write_lock:
                    self.flexiforceSocket.send(getStr.encode('ascii')) 
                    data = self.flexiforceSocket.recv(8)
#                     print('data %f' % float(data))
#                     print("id:" + threading.currentThread().getName() + " data:" + data.decode('ascii'))
                #Notstop
                if (float(data) > self.max_stall_force) and (not self.self_servo_moving):
#                     print('data>0.2 %f' % float(data))
#                     print("data>0.2 id:" + threading.currentThread().getName() + " data:" + data.decode('ascii'))
                    self.stopping = True
                    
                    self.write_moving_speed(int(self.servo_release_speed) )
                    
                elif float(data) < self.min_stall_force:
                    self.stopping = True
                    
                    self.write_moving_speed(int(self.servo_pull_speed))
                    
                elif self.stopping:
#                     print('data-stopping %f' % float(data))
#                     print("rel id:" + threading.currentThread().getName() + " data:" + data.decode('ascii'))
                    self.stopping = False
                   
                    self.write_moving_speed(0 )
                     
                elif self.partner_servo_moving:
#                    
                    if float(data) > 0.03:
#                         print("part id:" + threading.currentThread().getName() + " data:" + data.decode('ascii'))
#                         print('data-partner-moving %f' % float(data))
                        
                        self.write_moving_speed(int(self.partner_servo_speed) )
                    else:
                        self.write_moving_speed(0 )
                
                elif self.self_servo_moving:
                    
                    if float(data) > self.max_force:
                        self.stopping = True
                        
                        self.write_moving_speed(int(self.servo_release_speed))
                    
                    
#                 pass
            else:
#                 print("msg recv >" + self.flexiforceSocket + "<")
                vals = val.split()
                if int(vals[0]) == self.partner_servo_id:
#                     print("servo1")
                    if int(vals[1]) == 0 or int(vals[1]) == 1023:
                        self.partner_servo_moving = False
                        self.stopping = True
                    else:
                        self.partner_servo_moving = True
                        
#                     if int(vals[1]) > 1023:
#                         self.partner_servo_speed = int(vals[1]) - 1023
#                     else:
#                         self.partner_servo_speed = int(vals[1]) + 1023
                    
                    self.partner_servo_speed = int(vals[1])
                    
                elif int(vals[0]) == int(self.id):
                    self.self_servo_moving = True
                    # Write speed
                    self.write_moving_speed(int(vals[1]) )
                
#                 self.do_thing_with_message(val)

    def write_moving_speed(self, speed):
        with write_lock:
            dxl_comm_result, dxl_error = self.pa_h.write2ByteTxRx(self.po_h, int(self.id), int(self.addr_ax_moving_speed), speed)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % self.pa_h.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % self.pa_h.getRxPacketError(dxl_error))




def ax12_write_ccw_angle_limit(pa_h, po_h, id, limit):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, 8, limit)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Set Torque Limit:%d" % (id, 999))


def ax12_enable_torque(pa_h, po_h, id):
    dxl_comm_result, dxl_error = pa_h.write1ByteTxRx(po_h, id, 24, 1)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("enable-torque %s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Torque:enabled" % (id))
        
def ax12_write_torque_limit(pa_h, po_h, id):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, 34, 400)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("torque-limit %s" % pa_h.getRxPacketError(dxl_error))
    else:
        print("[ID:%03d] Set Torque Limit:%d" % (id, 34))
        
        
def ax12_write_max_torque(pa_h, po_h, id):
    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, id, 14, 1023)
    if dxl_comm_result != COMM_SUCCESS:
        print("write-max-torque res %s" % pa_h.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("write-max-torque err %s" % pa_h.getRxPacketError(dxl_error))
        
        
def getch1():
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
                                
        
if __name__ == '__main__':
    threads = []
#     tqueues = []

    s = socket.socket()
    port = 1500
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    
    portHandler = PortHandler("/dev/ttyUSB0")
    
    if portHandler.openPort():
        print("open port ok")
    else:
        print("open port failed")
        
    packetHandler = PacketHandler(1.0)

    
#     open_port(portHandler)
    
#     set_port_baudrate(portHandler, config)
    portHandler.setBaudRate(1000000)
    
    for i in range(1,9):
        ax12_write_ccw_angle_limit(packetHandler, portHandler, i, 0)
        ax12_enable_torque(packetHandler, portHandler, i)
        ax12_write_torque_limit(packetHandler, portHandler, i)
        ax12_write_max_torque(packetHandler, portHandler, i)
        
        
    
    for t in range(8):
        q = Queue()
#         tqueues.append(Queue())
        
#         threads.append(MyThread(q, args=(t % 2 == 0,)))
        threads.append(MyThread(q, args=(t+1, c, packetHandler ,portHandler )))
#         threads.append(MyThread(tqueues[t], args=(0 == 0,)))
        threads[t].start()
        time.sleep(0.1)

#     for t in threads:
#         t.queue.put("1 234")
#         tqueues[t].queue.put("Print this!")

    while 1:
#         print("Press any key to continue! (or press ESC to quit!)")
    #     if isData():
    #         c = sys.stdin.read(1)
        keychar = getch1()
        if keychar == chr(0x1b):
            break
        elif keychar == 'q':
            inp = "2 100"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'a':
            inp = "2 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'w':
            inp = "1 1123"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 's':
            inp = "1 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'y':
            inp = "1 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "2 100"
            for t in threads:
                t.queue.put(inp)
            inp = "1 0"
            for t in threads:
                t.queue.put(inp)
            inp = "2 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'x':
            inp = "1 100"
            for t in threads:
                t.queue.put(inp)
            inp = "2 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "1 0"
            for t in threads:
                t.queue.put(inp)
            inp = "2 0"
            for t in threads:
                t.queue.put(inp)
                
        elif keychar == 'e':
            inp = "4 100"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'd':
            inp = "4 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'r':
            inp = "3 1123"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'f':
            inp = "3 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'c':
            inp = "3 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "4 100"
            for t in threads:
                t.queue.put(inp)
            inp = "3 0"
            for t in threads:
                t.queue.put(inp)
            inp = "4 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'v':
            inp = "3 100"
            for t in threads:
                t.queue.put(inp)
            inp = "4 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "3 0"
            for t in threads:
                t.queue.put(inp)
            inp = "4 0"
            for t in threads:
                t.queue.put(inp)
                
        elif keychar == 't':
            inp = "6 100"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'g':
            inp = "6 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'z':
            inp = "5 1123"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'h':
            inp = "5 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'b':
            inp = "5 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "6 100"
            for t in threads:
                t.queue.put(inp)
            inp = "5 0"
            for t in threads:
                t.queue.put(inp)
            inp = "6 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'n':
            inp = "5 100"
            for t in threads:
                t.queue.put(inp)
            inp = "6 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "5 0"
            for t in threads:
                t.queue.put(inp)
            inp = "6 0"
            for t in threads:
                t.queue.put(inp)
                
        elif keychar == 'u':
            inp = "8 100"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'j':
            inp = "8 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'i':
            inp = "7 1123"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'k':
            inp = "7 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == 'm':
            inp = "7 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "8 100"
            for t in threads:
                t.queue.put(inp)
            inp = "7 0"
            for t in threads:
                t.queue.put(inp)
            inp = "8 0"
            for t in threads:
                t.queue.put(inp)
        elif keychar == ',':
            inp = "7 100"
            for t in threads:
                t.queue.put(inp)
            inp = "8 1123"
            for t in threads:
                t.queue.put(inp)
            inp = "7 0"
            for t in threads:
                t.queue.put(inp)
            inp = "8 0"
            for t in threads:
                t.queue.put(inp)
            
# 
#     while True:
#         inp = input("type >id speed<")
# 
#         for t in threads:
#             t.queue.put(inp)

    
#     for t in threads:
#         t.join()
        
        
        