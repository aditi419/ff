import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET. socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind(ip_address, port)
server.listen()

questions = [
    "What is the Italian word for PIE? /n a. Mozarella /n b. Pasty /n c. Patty /n d. Pizza",
    "Water boils at 212 Units at which scale? /n a. Fahrenheit /n b. Celsius /n c. Rankine /n d. Kevlin",
    "Which sea creature has 3 hearts? /n a. Dolphin /n b. Octopus /n c. Walrus /n d. Seal",
    "What element does not exist? /n a. Xr /n b. Re /n c. Si /n d. Pa",
    "How many players are on the field in baseball? /n a. 6 /n b. 7 /n c. 9 /n d. 8",
    "Who is Loki? a. God of Thunder /n b. God of Dwarfs /n c. God of Mischeif /n d. God of Gods",
    "Which planet is closest to the sun? /n a. Mercury /n b. Pluto /n c. Earth /n d. Venus"
]

answers = [
    'd', 'a', 'b', 'a', 'c', 'a', 'a'
]

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions) - 1)
    random_question - questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode("utf-8"))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode("utf-8"))
    conn.send("You will recieve a question. The answer to that question should be one of a, b, c, or d.")
    conn.send("Good Luck!/n/n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your score is {score}/n/n".encode('utf-8'))
                else: 
                    conn.send("Incorrect answer! Better luck next time!/n/n".encde('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue