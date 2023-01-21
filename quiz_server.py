import socket
from threading import Thread
import random

Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5500

Server.bind((ip_address,port))
Server.listen()

listofclients = []
nicknames = []

print('Server has started......')

questions =  [
    " What is the Italian word for PIE? \n a.Mozerella \n b.pasty \n c.patty \n d.torta",
    " Water boils at 212 units at which scale? \n a.Fahrenheit \n b.Celsius \n Rankine \n Kelvin",
    " Which sea creature has three hearts? \n a.Dolphin \n b.Octopus \n c.Walrus \n d.Seal",
    " Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary \n b.Jack \n c.Johnny \n d.Mukesh",
    " How many does an adult human have? \n a.106 \n b.206 \n c.306 \n d.406",
    " How many continents are there in the world? \n a.7 \n b.9 \n c.11 \n d.12",
    " Which is the lightest element? \n a.hydrogen \n b.oxygen \n c.nitrogen \n d.carbon dioxide"
]

answers = ['d','a','b','a','b','a','a']

def clientThread(conn):
    score = 0
    conn.send('Welcome to this quiz game!'.encode('utf-8'))
    conn.send('You will recieve a quiz question.\n \n You have to answer that in a,b,c or d'.encode('utf-8'))
    conn.send('Good Luck!'.encode('utf-8'))

    index, question, answer = get_random_answers(conn)
    while True:
        try:
          message = conn.recv(2048).decode('utf-8')
          if message:
            if message.lower() == answers:
                score += 1
                conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
            else :
                conn.send('Incorrect answer!Better Luck next time!\n\n'.encode('utf-8'))
            remove_question(index)
            index, question, answer = get_random_answers(conn)
          else :
             remove(conn)
        except:
            continue

def get_random_answers(conn):
    random_index = random.randint(0,len(questions) - 1)
    random_questions = questions[random_index]
    random_answers = answers[random_index]
    conn.send(random_questions.encode('utf-8'))
    return random_index,random_questions,random_answers


def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def remove(connection):
    if connection in listofclients:
        listofclients.remove(connection)


while True:
    conn = Server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    nicknames.append(nickname)
    listofclients.append(conn)
    print(nickname + 'connected!')
    new_thread = Thread(target= clientThread,args= (conn,nickname))
    new_thread.start()


