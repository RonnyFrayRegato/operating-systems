# Programming Assignment 1: Fixing Our Threads

import sys
import threading
import time
import os

def thread_function(name, message):

    # make sure the file exists before attempting to read
    if os.path.exists('names.txt'):
        with open("names.txt", 'r+') as namesfile:
            # print the file before writing a message
            print(namesfile.read())
    else:
        print("The file does not exist.")

    # by appending a file, it is locked & cannot be opened by another thread
    with open('names.txt', 'a') as namesfile, lock:
        namesfile.write(f"Thread name is {name}\t{message}\n")


def sleep_function(name):
    time.sleep(5)
    print(f'{time.strftime("%H:%M:%S", time.localtime())}: Thread {name} is done')


if __name__ == "__main__":
    # basic synchronization using Lock(); not needed due to append locking file
    lock = threading.Lock()

    for n in sys.argv[1:]:
        message = input("Please enter your message: ")
        prth = threading.Thread(target=thread_function, args=(n,message))
        prth.start()

    for n in sys.argv[1:]:
        prth = threading.Thread(target=sleep_function, args=(n,))
        prth.start()
