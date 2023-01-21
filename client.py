from tkinter import *
import socket
from threading import Thread

#nickname = input('Enter your nickname here')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5500

client.connect((ip_address,port))

class GUI:
    def __init__(self):
       self.Window = Tk()
       self.Window.withdraw()

       self.login = Toplevel()
       self.login.title('Login')
       self.login.resizable(width= False,height= False)
       self.login.configure(width= 400,height= 400,bg='grey')

       self.label = Label(self.login,text='Please login to continue',fg='black',font=('Helvetica 30',20))
       self.label.place(relx= 0.5,rely= 0.1)
       
       self.name_label= Label(self.login,text="NAME : ")
       self.name_label.placep(relx=0.35,rely=0.3)

       self.entry_name= Entry(self.login,text=' ',font=('Calibri',10))
       self.entry_name.place(relx=0.65,rely=0.3)

       self.go = Button(self.login,text='CONTINUE',font="Helvetica 14 bold",command= lambda: goAhead(self.entry_name.get())) 
       self.go.place(relx=0.7,rely= 0.8)

g = GUI()

def goAhead(self,name):
  self.login.destroy()
  self.name = name
  rcv = Thread(target= self.receive)
  rcv.start()



def recieve(self):
    while True:
        try:
          message = client.recv(2048).decode('utf-8')
          if message == 'NICKNAME':
                client.send(self.name.encode('utf-8'))
          else :
             print(message)
        except:
            print('Sorry! an eror has occured')
            client.close()
            break

#def write():
 #   while True:
  #      message = '{} : {}'.format(nickname,input(' '))
  #      client.send(message.encode('utf-8'))

#recieve_Thread = Thread(target= recieve)
#recieve_Thread.start()

#write_Thread = Thread(target= write)
#write_Thread.start()
