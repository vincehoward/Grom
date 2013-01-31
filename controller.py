# controller.py

import random


first = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', \
         'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', \
         'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish', \
         'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', \
         'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', \
         'puking', 'puny', 'qualling', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', \
         'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', \
         'villainous', 'warped', 'wayward', 'weedy', 'yeasty', 'cullionly', 'fusty', \
         'caluminous', 'wimpled', 'burly-boned', 'misbegotten', 'odiferous', \
         'poisonous', 'fishified', 'Wart-necked']

second = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', \
          'boil-brained',  'clapper-clawed', 'clay-brained', 'common-kissing', \
          'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', \
          'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', \
          'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', \
          'full-gorged', 'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', \
          'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured', 'knotty-pated', \
          'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', \
          'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', \
          'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', \
          'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', \
          'toad-spotted', 'unchin-snouted', 'weather-bitten', 'whoreson', \
          'malmsey-nosed', 'rampallian', 'lily-livered', 'scurvy-valiant', \
          'brazen-faced', 'unwashed', 'bunch-backed', 'leaden-footed', \
          'muddy-mettled']

third = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', \
         'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', \
         'death-token', 'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', \
         'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', \
         'hugger-mugger', 'joithead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', \
         'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news', \
         'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut', \
         'skainsmate', 'strumpet', 'varlot', 'vassal', 'whey-face', 'wagtail', 'knave', \
         'blind-worm', 'popinjay', 'scullian', 'jolt-head', 'malcontent', 'devil-monk', \
         'toad', 'rascal',  'casket-cockle']


def control(irc, botName, command, cmd, arguments, chan, nick, channel, owner, fantasy, fo):
    mess = 0
    message = [] 
    target = [] 
    if command == 'PRIVMSG':
        if nick == botName or fantasy not in cmd:
            pass
        elif cmd == fantasy + 'barf':
            say(irc, chan, 'Blegh!')
        elif cmd == fantasy + 'insult':
            insult(irc, str(chan), str(arguments))
        elif nick != owner and fantasy  in cmd:
            say(irc, chan, "You don't have the power to do this!")
        elif cmd == fantasy + 'leave':
            quit(irc, chan)
        elif cmd == fantasy + 'part':
            part(irc, chan)
        elif cmd == fantasy + 'op':
            op(irc, chan, arguments)
        elif cmd == fantasy + 'dop':
            dop(irc, chan, arguments)
        elif cmd == fantasy + 'hop':
            hop(irc, chan, arguments)
        elif cmd == fantasy + 'dhop':
            dhop(irc, chan, arguments)
        elif cmd == fantasy + 'ban':
            ban(irc, chan, arguments)
        elif cmd == fantasy + 'unb':
            unban(irc, chan, arguments)
        elif cmd == fantasy + 'kick':
            kick(irc, arguments, chan)
        elif cmd == fantasy + 'fan':
            fantasy = fan(irc, chan, arguments, fantasy)
        elif cmd == fantasy + 'nick':
            botName = nickn(irc, botName, chan, arguments)
        elif cmd == fantasy + 'note':
            target[mess], message[mess], mess = note(chan, arguments, target, message, mess)
    elif command == 'PING' or cmd == 'PING':
        pinged(irc, str(arguments))
        join(irc, str(channel))
    elif command == 'INVITE':
        join(irc, cmd)
    elif command == 'JOIN':
        mess = sending(irc, command, nick, target, message, mess)
    return fantasy, botName


def nickn(irc, botName, chan, args):
    if ' ' in args:
        irc.send("PRIVMSG " + chan + ": Usage: " + fantasy + "nick newnick\r\n")
        return botName
    else:
        irc.send("NICK " + args.strip() + "\r\n")
        return args.strip()


def fan(irc, chan, args, fantasy):
    if ' ' in fantasy:
        irc.send("PRIVMSG " + chan + ": Usage: " + fantasy + "fan <char>\r\n")
        return fantasy
    else:
        irc.send("PRIVMSG " + chan + ": Fantasy character changed to: " + fantasy + "\r\n")
        return args


def sending(irc, command, nick, target, message, mess):
    nick = nick.split('!', 1).pop(0).strip()
    for x in range(0, 9):
        try:
            if nick == target[x]:
                irc.send('PRIVMSG ' + chan + target[x] + ' d0nut told me to tell you: \r\n')
                say(chan, str(message[mess]))
                message[mess] = ''
                target[mess] = ''
        except IndexError:
            pass
    return mess
            

def note(chan, arguments, target, message, mess):
    try:
        target[mess] = str(arguments.split().pop(0).strip())
        message[mess] = str(arguments.strip())
        print 'Arguments: ' + str(arguments) + ' \n'
    except IndexError:
        target.append(str(arguments.split().pop(0).strip()))
        message.append(str(arguments.strip()))
        print 'Arguments: ' + str(arguments) + ' \n'
        print target
        print message
        mess += 1
    return target, message, mess


def op(irc, chan, arguments):
    if arguments != '':
        irc.send('MODE ' + chan + ' +o ' + arguments + ' \r\n')
    else:
        irc.send('MODE ' + chan + ' +o t0rus \r\n')


def hop(irc, chan, arguments):
    if arguments != '':
        irc.send('MODE ' + chan + ' +h ' + arguments + ' \r\n')
    else:
        irc.send('MODE ' + chan + ' +h t0rus \r\n')


def dop(irc, chan, arguments):
    if arguments != '':
        irc.send('MODE ' + chan + ' -o ' + arguments + ' \r\n')
    else:
        irc.send('MODE ' + chan + ' -o t0rus \r\n')


def dhop(irc, chan, arguments):
    if arguments != '':
        irc.send('MODE ' + chan + ' -h ' + arguments + ' \r\n')
    else:
        irc.send('MODE ' + chan + ' -h t0rus \r\n')


def kick(irc, arguments, chan):
    irc.send('KICK ' + chan + ' ' + arguments + ' \r\n')


def unban(irc, chan, arguments):
    irc.send('MODE ' + chan + ' -b *' + arguments + '*!*@*.* \r\n')


def ban(irc, chan, arguments):
    irc.send('MODE ' + chan + ' +b *' + arguments + '*!*@*.* \r\n')
    kick(irc, arguments, chan)


def pinged(irc, response):
    irc.send('PONG ' + response + ' \r\n')


def part(irc, chan):
    say(irc, chan, 'Later.')
    irc.send('PART ' + chan + ' \r\n')


def quit(irc, chan):
    irc.send('QUIT Okay. Bye. \r\n')
    irc.close()


def join(irc, chan):
    irc.send('JOIN ' + chan + ' \r\n')


def say(irc, chan, words):
    irc.send('PRIVMSG ' + chan + ' :' + words + ' \r\n')


def insult(irc, chan, target):
    one = str(first[random.randint(0, 59)])
    two = str(second[random.randint(0, 59)])
    three = str(third[random.randint(0, 59)])
    irc.send('PRIVMSG ' + chan + ' :' + target + '!  Silence, thou ' + one + \
              ' ' + two + ' ' + three + '! \r\n')

