

import threading
import time
import socketio

sio = socketio.Client()

class Manager_connect(threading.Thread):

  def __init__(self):  
    threading.Thread.__init__(self)  
    
  @sio.on("connect")
  def otr(msg_text = "hola"):
    print('connection established')
    sio.emit('mensaje', msg_text)

  @sio.event
  def data(*args):
    print('message received with ', args)

  def send_msg():
    print ('se envio')
    sio.emit('mensaje', 'fdsfdsfdsfd')

  def run(self):
    sio.connect('http://localhost:5000')
    sio.wait()





      
