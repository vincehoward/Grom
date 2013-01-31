
#!/usr/bin/env python
# Grom v2.0
# Written by Vince Howard (d0nut)

import socket
import time
import os
from gromJuice import parser
from controller import control

fo = open("grom.log","a")
botName = 'Grom'
port = 6667
network = ' '
channel = ''
fantasy = '^'
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#owner = ''
owner = ''

irc.connect((network, port))
irc.recv(1024)
irc.send('NICK Grom \r\n')
irc.send('USER Grom n n : Grom \r\n')

while True: 
    data = irc.recv (4096) 
    #fo.write(str(data)) #Print the Data to the console(For debug purposes)
    print data
    parsed = parser(data)
    command = parsed['command']
    cmd = parsed['cmd']
    arguments = parsed['arg']
    chan = str(parsed['chan'])
    nick = parsed['nick']
    """  Logging; Uncomment to enable.
    fo.write("Server Command: " + command + "\n")
    fo.write("String Command: " + cmd + "\n")
    fo.write("Arguments: " + arguments + "\n")
    fo.write("Chan: " + chan + "\n")
    fo.write("Nick: " + nick + "\n")
   """
    print 'command ' + command + ' \n'
    print 'cmd ' + cmd + ' \n'
    print 'arguments ' + arguments + ' \n'
    print 'chan ' + chan + ' \n'
    print 'nick ' + nick + ' \n'

    fantasy, botName = control(irc, botName, command, cmd, arguments, \
                               chan, nick, channel, owner, fantasy, fo)

fo.close()
