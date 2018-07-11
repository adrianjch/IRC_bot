import socket
import random
import time
#from random import randint

server = 'dyn.thomas-windt.me'
channel = '#notfun'
nickbot = 'zeugma_bot'
port = 5905

ircsock = socket.socket()
ircsock.connect((server, port))

handle = ircsock.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')

print('NICK', nickbot, file=handle)
print('USER', nickbot, nickbot, nickbot, ':' + nickbot, file=handle)
print('PASS', 'efkebdnn', file=handle)


def send_message_to_channel(message, channel):
    """Sends the given message to the given channel.

    Args:
      message : unicode
        E.g. "Hello, world!"
        A message to send to the channel. Note that there is a maximum
        length for messages on IRC.
      channel : unicode
        E.g. "#notfun".
    """
    ircsock.send(("PRIVMSG " + channel + " :" + message + "\n").encode())


def random_welcome_message(nick):
    """Returns a random greeting for a person who has joined the channel.

    Args:
      nick : unicode
        E.g. "adrianjch".
        A nickname, or a name to be filled into the greeting.

    Returns:
      A randomised greeting, like "Hi, adrianjch!"
    """
    welcome_messages = [
        "{nick} has joined!",
        "Welcome, {nick}!",
        "Is this {nick}? The real one? :O",
        "I don't know who you are, but I suppose you can join. ¯\_(ツ)_/¯",
        "Be careful! {nick} has joined!",
        "A mysterious {nick} has arrived!",
        "{nick}!!! I missed you!",
    ]
    return random.choice(welcome_messages).format(nick=nick)


def random_goodbye_message(nick):
    goodbye_messages = [
        "Have a nice day!",
        "{nick} left.",
        "I hope to see you soon!",
        "See you later aligator! \o",
        "Please come again, don't do like my daddy :(",
    ]
    return random.choice(goodbye_messages).format(nick=nick)


streak = 0
with open('actual_streak.txt', 'r') as astreak:
    astreak_contents = astreak.read()
    streak = int(astreak_contents)
max_streak = 5
for line in handle:
    line = line.strip()
    print(line)
    nick_end = line.find("!")
    nick = line[1:nick_end]
    with open('rrstats_pulled.txt', 'r') as pulls:
        with open('rrstats_shots.txt', 'r') as shots:
            with open('rrstats_streak.txt', 'r') as hstreak:
                pulls_contents = pulls.read()
                shots_contents = shots.read()
                hstreak_contents = hstreak.read()
                rpulls = int(pulls_contents) + 1
                rshots = int(shots_contents) + 1
    if streak > max_streak:
        max_streak = streak
    if max_streak > int(hstreak_contents):
        with open('rrstats_streak.txt', 'w') as write_hstreak:
            write_hstreak.write(str(max_streak))
    if "End of /MOTD command" in line:
        ircsock.send(('JOIN ' + channel + '\n').encode())
    # if "End of /NAMES list" in line:
    # ircsock.send(("PRIVMSG " + channel + " :Yes, hello.\n").encode())
# bananaphone thing
    if channel + " :ringringringringringringring" in line:
        ringringringringringringring_confirm = line[-28:]
        if ringringringringringringring_confirm == "ringringringringringringring":
            ircsock.send(("PRIVMSG " + channel + " :BANANAPHONE!\n").encode())
# o/ thing
    if channel + " :o/" in line:
        hello_confirm = line[-2:]
        if hello_confirm == "o/":
            ircsock.send(("PRIVMSG " + channel + " :\o\n").encode())
# all joining stuff
    if "JOIN " + channel in line and nick != nickbot:
        message = random_welcome_message(nick)
        send_message_to_channel(message, channel)
# all leaving stuff
    if "QUIT" in line or "PART" in line:
        message = random_goodbye_message(nick)
        send_message_to_channel(message, channel)
# all .rr stuff
    if channel + " :.rr" in line:
        rr_confirm = line[-3:]
        if rr_confirm == ".rr":
            with open('rrstats_pulled.txt', 'w') as write_pulls:
                write_pulls.write(str(rpulls))
            ircsock.send(("PRIVMSG " + channel + " :[rr] " + nick + " slowly pulls the trigger...\n").encode())
            # print(random.choice(['red', 'blue', 'green', 'yellow', 'brown', 'white']))
            # gun = random.choice(['red', 'blue', 'green', 'yellow', 'brown', 'white'])
            gun = random.randint(1, 6)
            print(gun)
            time.sleep(3)
            if gun == 6:
                with open('rrstats_shots.txt', 'w') as write_shots:
                    write_shots.write(str(rshots))
                ircsock.send(("PRIVMSG " + channel + " :*BANG* you died!\n").encode())
                ircsock.send(("KICK " + channel + " " + nick + " :*BANG*\n").encode())
                with open('rrstats_streak.txt', 'r') as hstreak:
                    hstreak_contents = hstreak.read()
                    if streak > int(hstreak_contents):
                        with open('rrstats_broker.txt', 'w') as write_broker:
                            write_broker.write(str(nick))
                streak = 0
                with open('actual_streak.txt', 'w') as write_streak:
                    write_streak.write(str(0))
            else:
                streak = streak + 1
                with open('actual_streak.txt', 'w') as write_streak:
                    write_streak.write(str(streak))
                print(streak)
                ircsock.send(("PRIVMSG " + channel + " :[rr] *click* - nothing happens. " + nick + " will live another day. Who's next? Misses since last death: " + str(streak) + ".\n").encode())
# all .rrstats stuff
    if channel + " :.rrstats" in line:
        with open('rrstats_pulled.txt', 'r') as pulls:
            with open('rrstats_shots.txt', 'r') as shots:
                with open('rrstats_streak.txt', 'r') as hstreak:
                    with open('rrstats_broker.txt', 'r') as broker:
                        pulls_contents = pulls.read()
                        shots_contents = shots.read()
                        hstreak_contents = hstreak.read()
                        broker_contents = broker.read()
                        rpulls = int(pulls_contents) + 1
                        rshots = int(shots_contents) + 1
                        percentage_rr = int(shots_contents) / int(pulls_contents) * 100
                        ircsock.send(("PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str(percentage_rr) + "%. Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".\n").encode())
# all PM stuff
    if ":adrianjch!uid297864@id-297864.stonehaven.irccloud.com PRIVMSG zeugma_bot :" in line:
        adrianjch = line[75:]
        print(adrianjch)
        ircsock.send(("PRIVMSG " + channel + " : " + adrianjch + "\n").encode())
