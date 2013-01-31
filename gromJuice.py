
# gromJuice.py

import random
import socket
import os


def parser(rawData):
    """Breaks a message from an IRC server into its prefix, command, and arguments.
    """
    prefix = ''
    send = ''
    chan = ''
    command = ''
    command1 = ''
    arg = []
    trailing = []
    
    if not rawData:
        return {'nick':'', 'command':'', 'arg':'', 'chan':'', \
                'send':'', 'cmd':''}
    data = rawData.split(' ')
    
    if data[0] == "PING":
        command1 = "PING"
        arg = data[1]
    else:
       if rawData[0] == ':':
          prefix, rawData = rawData[1:].split(' ', 1)
          if rawData.find(' :') != -1:
            rawData, trailing = rawData.split(' :', 1)
            arg = rawData.split()
            arg.append(trailing)
       else:
          arg = rawData.split()

       try:
           command = arg.pop(0)
           chan = arg.pop(0)
       except IndexError:
           pass

       if len(arg) == 0:
          command1 = ""
          arg = ""
       elif len(arg[0].split(' ', 1)) > 1:
          command1, arg = arg[0].split(' ', 1)
       elif len(arg) > 0:
          command1 = arg.pop(0)
          arg = ""
    
    command1 = command1.strip()
    chan = chan.strip()
    arg = arg.strip()

    return {'nick':prefix, 'command':command, 'arg':arg, 'chan':chan, \
            'send':send, 'cmd':command1}

