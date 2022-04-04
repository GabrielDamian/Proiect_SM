from threading import RLock
#You can import any required modules here

#This can be anything you want
moduleName = "toggle"

#All of the words must be heard in order for this module to be executed
commandWords = ["toggle"]

is_on = true
lock = RLock()

def execute(command):
    lock.acquire()
    is_on = not is_on
    lock.release()