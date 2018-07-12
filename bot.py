import socket
import random
import time
import greetings
import suicide
#from random import randint

server = 'xxx.xxxxxxxxxx.xx'
channel = '#xxxxxx'
nickbot = 'zeugma_bot'
port = xxxx

ircsock = socket.socket()
ircsock.connect((server, port))

handle = ircsock.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')

print('NICK', nickbot, file=handle)
print('USER', nickbot, nickbot, nickbot, ':' + nickbot, file=handle)
print('PASS', 'xxxxxxx', file=handle)


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
        message = greetings.random_welcome_message(nick)
        send_message_to_channel(message, channel)
# all leaving stuff
    if "QUIT" in line or "PART" in line:
        message = greetings.random_goodbye_message(nick)
        send_message_to_channel(message, channel)
# all .suicide stuff
    if channel + " :.suicide" in line:
        suicide_confirm = line[-8:]
        if suicide_confirm == ".suicide":
            message = suicide.random_suicide_message(nick, nickbot)
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
                        percentage_rr = int(shots_contents) / int(pulls_contents)
                        ircsock.send(("PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:.2%}'.format(percentage_rr)) + ". Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".\n").encode())
                        # percentage_rr = int(shots_contents) / int(pulls_contents) * 100
                        # ircsock.send(("PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:04.2f}'.format(percentage_rr)) + "%. Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".\n").encode())
# all PM stuff
    if ":adrianjch!uid297864@id-297864.stonehaven.irccloud.com PRIVMSG zeugma_bot :" in line:
        adrianjch = line[75:]
        print(adrianjch)
        ircsock.send(("PRIVMSG " + channel + " : " + adrianjch + "\n").encode())

    #if channel + " :.command rr off" in line:
     #   rr_off = line[-15:]
      #  if rr_off == ".command rr off":
       #     ircsock.send(("NAMES " + channel + "\n").encode())
        #    if "@" + nick in line:
         #       ircsock.send(("PRIVMSG " + channel + " :.rr DISABLED\n").encode())
          #  else:
           #     ircsock.send(("PRIVMSG " + channel + " :Just OPs can do this action.\n").encode())
