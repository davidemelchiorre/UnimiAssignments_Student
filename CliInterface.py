from tornado import httpserver
from tornado import ioloop
from tornado import web
from tornado import websocket
import subprocess
import threading
import os
comando="Hello World"
jupyter=0

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
    tmp="python receive.py "
    for corso in comando.split(" ")[1:]:
        tmp+=corso+" "
    print corso
    #subprocess.call(tmp, shell=True)
    subprocess.call('cd Esercitazioni && ls -l', shell=True)
    print "cloned into Esercitazioni"
    print "-----------------------------------------------"
    print ""

def quit():
    os.kill(os.getpid(),15)

def launch(cmd):
    if comando=="start":
        start()
        jupyter=1
    if comando=="stop":
        stop()
        jupyter=0
    if comando.find("get")>=0:
        get()
    if comando=="quit":
        quit()

class handler(websocket.WebSocketHandler):
    def open(obj):
        print ('Found web graphic interface')
  
    def on_close(obj):
        print ('Web graphic interface closed')
  
    def check_origin(obj, origin):
        return True

    def on_message(obj, received):
        global comando
        print ">",received
        comando=received
        print "remote command launched"

def server_function():
    socket_name="/websocket-server"
    server = httpserver.HTTPServer(web.Application([(socket_name, handler)]))
    server.listen(9595)
    ioloop.IOLoop.instance().start()

def keyboard_function():
    global comando
    while 1:
        try:
            comando = raw_input(">")
        except Error:
            comando="Hello World"
            

server_thread=threading.Thread(name='server_thread', target=server_function)
server_thread.start()
keyboard_thread=threading.Thread(name='keyboard_thread', target=keyboard_function)
keyboard_thread.start()




print ""
print "Starting Cli Interface..."
print "Type 'quit' to terminate"
#------------------------------------------------------------------------------------
print ""
print "-------------------------Cli Interface-------------------------"
print ""
while 1:
    if comando!="Hello World":
        launch(comando)
        comando="Hello World"
