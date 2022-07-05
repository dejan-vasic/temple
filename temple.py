import os
import re
import sys
import time
import threading

class task:

    def __init__(self, name, time):
        self.name = name
        self.time = time

class temple:

    __list = []

    def add(task):
        f = open("temple.txt", 'a')
        f.write(f"{task.name}, {task.time}\n")
        f.close()

    def __read():
        f = open("temple.txt", 'r')
        for line in f.readlines():
            word = line.split(", ")
            temple.__list.append(task(word[0], word[1].strip("\n")))

    def clear():
        f = open("temple.txt", 'w')
        f.write('')

    def list():
        temple.__read()
        os.system('clear')
        for task in temple.__list:
            print(f"{task.name}, {task.time}")

    def note():
        pass
    
    def start_timer():
        temple.__read()
        for i in range(len(temple.__list)):
            os.system("clear")
            task = temple.__list[i]
            print(f"{task.name.upper()}...")
            x = threading.Thread(target=temple.note)
            x.start()
            form = re.search("\D..", task.time)
            if form.group() == "min":
                time.sleep(int(re.sub("\D..", '', task.time)) * 60)
            elif form.group() == "sec":
                time.sleep(int(re.sub("\D..", '', task.time)))
            x.join()
            if i < len(temple.__list) - 1:
                next_task = temple.__list[i + 1]
                os.system("termux-notification")
                os.system("termux-media-player play ../storage/downloads/my_baby.mp3")
                print(f"pause, now {next_task.name.upper()}!")
                cont  = 'n'
                while cont == 'n':
                    print("Are you ready? [Y/n]")
                    cont = input()
                    
        print("end circle")

argv = sys.argv[1:]

if argv[0] == "-a":
    temple.add(task(argv[1], argv[2]))

if argv[0] == "-s":
    temple.start_timer()

if argv[0] == "-l":                                     
    temple.list()

if argv[0] == "-c":
    temple.clear()
