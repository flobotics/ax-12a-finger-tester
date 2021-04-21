import threading
import time 
from queue import Queue
from queue import Empty
import socket


print_lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_messages = args[0]
        self.id = args[0]
        self.flexiforceSocket = args[1]
        self.addr_ax_moving_speed = 32
        if self.id == 1:
            self.servo_release_speed = 1123
            self.connected_servo_id = 2
        elif self.id == 2:
            self.servo_release_speed = 100
            self.connected_servo_id = 1
        self.releasing = False
        self.connected_servo_moving = False
        self.connected_servo_speed = 0
        

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
                getStr = 'get' + self.id.encode('ascii')
                self.flexiforceSocket.send(getStr) 
                data = self.flexiforceSocket.recv(8)
                print('data %f' % float(data))
                #Notstop
                if float(data) > 0.2:
                    self.releasing = True
                    # Write speed
                    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, self.id, self.addr_ax_moving_speed, self.servo_release_speed)
                    if dxl_comm_result != COMM_SUCCESS:
                        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
                    elif dxl_error != 0:
                        print("%s" % pa_h.getRxPacketError(dxl_error)) 
                elif self.releasing:
                    self.releasing = False
                    # Write speed
                    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, self.id, self.addr_ax_moving_speed, 0)
                    if dxl_comm_result != COMM_SUCCESS:
                        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
                    elif dxl_error != 0:
                        print("%s" % pa_h.getRxPacketError(dxl_error))
                        
#                     ax12_write_moving_speed(packetHandler, portHandler, config['DAX_ID_8'], 0, config)    
                elif self.connected_servo_moving:
                    if float(data) > 0.03:
                        # Write speed
                        dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, self.id, self.addr_ax_moving_speed, self.connected_servo_speed)
                        if dxl_comm_result != COMM_SUCCESS:
                            print("%s" % pa_h.getTxRxResult(dxl_comm_result))
                        elif dxl_error != 0:
                            print("%s" % pa_h.getRxPacketError(dxl_error))

                    
                    
                pass
            else:
                print("msg recv >" + self.flexiforceSocket + "<")
                vals = val.split()
                if int(vals[0]) == self.connected_servo_id:
                    print("servo1")
                    if int(vals[1]) == 0 or int(vals[1]) == 1023:
                        self.connected_servo_moving = False
                        self.releasing = True
                    else:
                        self.connected_servo_moving = True
                        
                    if int(vals[1]) > 1023:
                        self.connected_servo_speed = int(vals[1] - 1023)
                    else:
                        self.connected_servo_speed = int(vals[1] + 1023)
                    
                    
                elif int(vals[0]) == self.id:
                    # Write speed
                    dxl_comm_result, dxl_error = pa_h.write2ByteTxRx(po_h, self.id, self.addr_ax_moving_speed, int(vals[1]))
                    if dxl_comm_result != COMM_SUCCESS:
                        print("%s" % pa_h.getTxRxResult(dxl_comm_result))
                    elif dxl_error != 0:
                        print("%s" % pa_h.getRxPacketError(dxl_error))
                
#                 self.do_thing_with_message(val)

    def do_thing_with_message(self, message):
        if self.receive_messages:
            with print_lock:
                print("id:" + threading.currentThread().getName() + " msg:" + message)

if __name__ == '__main__':
    threads = []
#     tqueues = []

#     s = socket.socket()
#     port = 1500
#     s.bind(('', port))
#     s.listen(5)
#     c, addr = s.accept()
    
    for t in range(2):
        q = Queue()
#         tqueues.append(Queue())
        
#         threads.append(MyThread(q, args=(t % 2 == 0,)))
        threads.append(MyThread(q, args=(t+1, "ff")))
#         threads.append(MyThread(tqueues[t], args=(0 == 0,)))
        threads[t].start()
        time.sleep(0.1)

    for t in threads:
        t.queue.put("1 234")
#         tqueues[t].queue.put("Print this!")

    
        
    print("loop")
    while True:
        inp = input("type")

        for t in threads:
            t.queue.put(inp)

    
    for t in threads:
        t.join()
        
        
        