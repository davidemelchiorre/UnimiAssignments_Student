import subprocess
import threading
import socket
import os
comando="Hello World"

host=''
port = 9696
buflen=1024

def start():
    global proc
    print ""
    print "-----------------Start routine-----------------"
    try:
        if proc is None:
            print("Info>> Starting program...")
            proc=subprocess.Popen(["jupyter","notebook"])
            print(proc)
        else:
            print("Info>> Program is already running")
    except NameError:
        print("Info>> Starting program...")
        proc=subprocess.Popen(["jupyter","notebook"])
        print(proc)
    print "-----------------------------------------------"
    print ""
    
def stop():
    global proc
    print ""
    print "-----------------Stop routine------------------"
    try:
        if proc is not None:
            print(proc)
            print("Info>> Stopping program...")
            proc.kill()
            proc=None
        else:
            print("Info>> Program is not running")
    except NameError:
        print("Info>> Program is not running")
    print "-----------------------------------------------"
    print ""

def get():
    print ""
    print "--------------Getting Notebooks----------------"
    print "Cloning into Esercitazioni..."
    subprocess.call('rm -r Esercitazioni', shell=True)
    subprocess.call('git clone https://github.com/davidemelchiorre/UnimiAssignment-Esercitazioni.git Esercitazioni', shell=True)
    subprocess.call('ls -l', shell=True)
    print "cloned into Esercitazioni"
    print "-----------------------------------------------"
    print ""

def quit():
    server.close()
    os.kill(os.getpid(),15)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

def server_function():
    global comando
    while 1:
        client, buf = server.accept()
        #-------------------------
        buf = client.recv(buflen)
        if not buf:break
        comando=buf.decode('utf-8')
        
        if comando!="Hello World":
            print ">",comando
        if comando=="start":
            start()
        if comando=="stop":
            stop()
        if comando=="get":
            get()
        if comando=="quit":
            quit()
            

server_thread=threading.Thread(name='server_thread', target=server_function)
server_thread.start()

print ""
print "Starting Cli Interface..."
print "Type 'quit' to terminate"
#------------------------------------------------------------------------------------
print ""
print "-------------------------Cli Interface-------------------------"
print ""
while 1:
    
    comando = raw_input(">")
    if comando=="start":
        start()
    if comando=="stop":
        stop()
    if comando=="get":
        get()
    if comando=="quit":
        quit()
