import random
import time
import os
import configparser
from user import User

#----------------------CONFIG----------------------#
config = configparser.ConfigParser()
config.read('config.ini')
#--------------------------------------------------#

sessionExp = 0
def placeEmptyChars(msg):
    emptyChar = '‎'
    return ''.join('%s%s' % (x, emptyChar if random.randint(0, 1) else '') for x in msg)

def sendMsg(msg):
    if config.getboolean('Messages', 'useEmptyChars') and config.getboolean('Messages', 'useMessagePasting'):
        msg = placeEmptyChars(msg)
    user.send(msg)
    global sessionExp
    sessionExp += 1
    tick(msg, sessionExp)
    
def updateMessages():
    msgFile = open(file=config.get('Messages', 'filePath'), encoding="utf8", mode='r')
    content = msgFile.read()
    msgList = content.splitlines()
    msgFile.close()
    return msgList

def tick(msg, xp):
    if config.getboolean('Config', 'updateConfigOnCycle'):
        config.read('config.ini')
    seconds = config.getint('Timer', 'timerSeconds')
    if(config.getboolean('Timer', 'useRandomTime')):
        seconds += random.randint(-config.getint('Timer', 'randomTimeMargin'), config.getint('Timer', 'randomTimeMargin'))
    for i in range(seconds):
        consoleMessage = "session xp: {0} | {1} | last msg: {2}".format(xp, seconds-i, msg)
        os.system('cls')
        print("█▀▀ ▄▀█ █▀█ █▀▄▀█ █▄▄ █▀█ ▀█▀ █▀█ █▀█ █▀█ █▀█\n█▀░ █▀█ █▀▄ █░▀░█ █▄█ █▄█ ░█░ ▀▀█ █▄█ █▄█ █▄█\n")
        print(consoleMessage, end='\r')
        i+=1
        time.sleep(1)

user = User(config)

input('press enter in this window once you are logged in and the channel message box is selected')

msgList = updateMessages()
while True:
    if config.getboolean('Messages', 'useRandomMessage'):
        msg = random.choice(msgList)
        sendMsg(msg)
    else:
        for i in range(len(msgList)):
            msg = msgList[i]
            sendMsg(msg)
    if config.getboolean('Messages', 'updateMessagesOnCycle'):
            msgList = updateMessages()