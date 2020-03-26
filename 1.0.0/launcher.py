import socket
import threading
import os
import sys
import time
socket.setdefaulttimeout(1)
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect_ex((socket.gethostname(), port))
cl.settimeout(1)

def hb():
    no_exit = True
    # 心跳
    while no_exit:
        # 接收心跳信号
        while no_exit:
            try:
                cmd = cl.recv(1024).decode('UTF-8')
                if cmd == 'hb':
                    break
            except socket.timeout:
                no_exit = False
                break
            else:
                break
        # 发送心跳信号
        while True and no_exit:
            try:
                cl.send(str(key).encode('UTF-8'))
            except Exception:
                no_exit = False
                break
            else:
                break
    cl.close()
    sys.exit(0)


threading.Thread(target=hb,daemon=True).start()

os.system('\npython ' + name + ' 2>%s' % error_file)
cl.close()
sys.exit(0)
