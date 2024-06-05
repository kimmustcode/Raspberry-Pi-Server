from socket import * 
import subprocess
import sys
import signal 
from socket import *
import os 
import time 

HOST = "0.0.0.0"
PORT = 42069

prev = ""
liveProcs = [] 

cmd = 'python myprograms/Raspberry-Pi-Server/For-Device/imageFrame.py https://www.kimcodes.lol/static/dakota4.png'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fns=os.setsid)

c1 = p.pid 
liveProcs.append(c1)
c2 = p.pid + 1 
liveProcs.append(c2)

with socket(AF_INET, SOCK_STREAM) as s: 
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if data and data != prev: 
            cmd = ['python myprograms/Raspberry-Pi-Server/For-Device/imageFrame.py' + str(data.decode('utf-8'))]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setid)
            c1 = p.pid 
            c2 = p.pid +1 
            time.sleep()

            removed = []
            for proc in liveProcs:
                os.system("kill - 9" + str(proc))
                removed.append(proc)

            for proc in removed:
                liveProcs.remove(proc)

            removed = []

            liveProcs.append(c1)
            liveProcs.append(c2)

            prev = data
