import socket
import random
import time
import greetings
import suicide
import pun
# from random import randint

server = 'XXX.XXXXXXXXX.XX'
channel = '#XXXXXX'
nickbot = 'zeugma_bot'
port = XXXX

ircsock = socket.socket()
ircsock.connect((server, port))

handle = ircsock.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')

print('NICK', nickbot, file=handle)
print('USER', nickbot, nickbot, nickbot, ':' + nickbot, file=handle)
print('PASS', 'XXXXXXXX', file=handle)


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
rr_status = 1
greetings_status = 1
pun_status = 1
suicide_status = 0
ops = ["Vield", "adrianjch", "zeugma_bot", "Q"]
with open('actual_streak.txt', 'r') as astreak:
    astreak_contents = astreak.read()
    streak = int(astreak_contents)
max_streak = 5
for line in handle:
    line = time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + line.strip()
    print(line)
    nick_end = line.find("!")
    nick = line[21:nick_end]
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
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :BANANAPHONE!")
            ircsock.send(("PRIVMSG " + channel + " :BANANAPHONE!\n").encode())
# o/ thing
    if channel + " :o/" in line:
        hello_confirm = line[-2:]
        if hello_confirm == "o/":
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :\o")
            ircsock.send(("PRIVMSG " + channel + " :\o\n").encode())
# all joining stuff
    if "JOIN " + channel in line and nick != nickbot:
        if greetings_status == 1:
            message = greetings.random_welcome_message(nick)
            send_message_to_channel(message, channel)
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" + message)
# all leaving stuff
    if "QUIT" in line or "PART" in line:
        if greetings_status == 1:
            message = greetings.random_goodbye_message(nick)
            send_message_to_channel(message, channel)
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" + message)
# all .suicide stuff
    if channel + " :.suicide" in line:
        if suicide_status == 1:
            suicide_confirm = line[-8:]
            if suicide_confirm == ".suicide":
                message = suicide.random_suicide_message(nick, nickbot)
                send_message_to_channel(message, channel)
                print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" + message)
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.suicide is actually disabled. Ask an Op to enable that command.")
            ircsock.send(("PRIVMSG " + channel + " :.suicide is actually disabled. Ask an Op to enable that command.\n").encode())
# all .pun stuff
    if channel + " :.pun" in line:
        if pun_status == 1:
            pun_confirm = line[-4:]
            if pun_confirm == ".pun":
                message = pun.random_pun_message()
                send_message_to_channel(message, channel)
                print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" + message)
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.pun is actually disabled. Ask an Op to enable that command.")
            ircsock.send(("PRIVMSG " + channel + " :.pun is actually disabled. Ask an Op to enable that command.\n").encode())
# all .request stuff
    if channel + " :.request":
        request_confirm = line[-8:]
        if request_confirm == ".request":
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :not yet")
            ircsock.send(("PRIVMSG " + channel + " :not yet\n").encode())

# all .rr stuff
    if channel + " :.rr" in line:
        if rr_status == 1:
            rr_confirm = line[-3:]
            if rr_confirm == ".rr":
                with open('rrstats_pulled.txt', 'w') as write_pulls:
                    write_pulls.write(str(rpulls))
                print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :[rr] " + nick + " slowly pulls the trigger...")
                ircsock.send(("PRIVMSG " + channel + " :[rr] " + nick + " slowly pulls the trigger...\n").encode())
                # print(random.choice(['red', 'blue', 'green', 'yellow', 'brown', 'white']))
                # gun = random.choice(['red', 'blue', 'green', 'yellow', 'brown', 'white'])
                gun = random.randint(1, 6)
                time.sleep(3)
                if gun == 6:
                    with open('rrstats_shots.txt', 'w') as write_shots:
                        write_shots.write(str(rshots))
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :*BANG* you died!")
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
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :[rr] *click* - nothing happens. " + nick + " will live another day. Who's next? Misses since last death: " + str(streak) + ".")
                    ircsock.send(("PRIVMSG " + channel + " :[rr] *click* - nothing happens. " + nick + " will live another day. Who's next? Misses since last death: " + str(streak) + ".\n").encode())
        else:
            ircsock.send(("PRIVMSG " + channel + " :.rr is actually disabled. Ask an Op to enable that command.\n").encode())
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
                        print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:.2%}'.format(percentage_rr)) + ". Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".")
                        ircsock.send(("PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:.2%}'.format(percentage_rr)) + ". Highest streak: " + hstreak_contents + ", broken by " + broker_contents[:1] + "\u000f" + broker_contents[1:] + ".\n").encode())
                        # percentage_rr = int(shots_contents) / int(pulls_contents) * 100
                        # ircsock.send(("PRIVMSG " + channel + " :The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:04.2f}'.format(percentage_rr)) + "%. Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".\n").encode())
# all PM stuff
    if ":adrianjch!uid297864@id-297864.stonehaven.irccloud.com PRIVMSG zeugma_bot :" in line:
        adrianjch = line[75:]
        print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" + adrianjch)
        ircsock.send(("PRIVMSG " + channel + " :" + adrianjch + "\n").encode())
# all raw log stuff
    if time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :" in line:
        print("yes")
        with open('rawlog.txt', 'w') as write_rawlog:
            write_rawlog.write(line)

# all the .command stuff
    if channel + " :.command" in line:
        command_confirm = line[-8:]
        if command_confirm == ".command":
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :use .command <rr/greetings/pun/suicide> <on/off>")
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :It will just work for Ops.")
            ircsock.send(("PRIVMSG " + channel + " :use .command <rr/greetings/pun/suicide> <on/off>\n").encode())
            ircsock.send(("PRIVMSG " + channel + " :It will just work for Ops.\n").encode())

    if channel + " :.command rr off" in line:
        if rr_status == 1:
            rr_off = line[-15:]
            if rr_off == ".command rr off":
                if nick in ops:
                    rr_status = 0
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.rr DISABLED")
                    ircsock.send(("PRIVMSG " + channel + " :.rr DISABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.rr is already disabled.")
            ircsock.send(("PRIVMSG " + channel + " :.rr is already disabled.\n").encode())

    if channel + " :.command rr on" in line:
        if rr_status == 0:
            rr_on = line[-14:]
            if rr_on == ".command rr on":
                if nick in ops:
                    rr_status = 1
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.rr ENABLED.")
                    ircsock.send(("PRIVMSG " + channel + " :.rr ENABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.rr is already enabled.")
            ircsock.send(("PRIVMSG " + channel + " :.rr is already enabled.\n").encode())

    if channel + " :.command greetings off" in line:
        if greetings_status == 1:
            greetings_off = line[-22:]
            if greetings_off == ".command greetings off":
                if nick in ops:
                    greetings_status = 0
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :greetings DISABLED")
                    ircsock.send(("PRIVMSG " + channel + " :greetings DISABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :greetings are already disabled.")
            ircsock.send(("PRIVMSG " + channel + " :greetings are already disabled.\n").encode())

    if channel + " :.command greetings on" in line:
        if greetings_status == 0:
            greetings_on = line[-21:]
            if greetings_on == ".command greetings on":
                if nick in ops:
                    greetings_status = 1
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :greetings ENABLED")
                    ircsock.send(("PRIVMSG " + channel + " :greetings ENABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :greetings are already enabled.")
            ircsock.send(("PRIVMSG " + channel + " :greetings are already enabled.\n").encode())

    if channel + " :.command pun off" in line:
        if pun_status == 1:
            pun_off = line[-16:]
            if pun_off == ".command pun off":
                if nick in ops:
                    pun_status = 0
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.pun DISABLED")
                    ircsock.send(("PRIVMSG " + channel + " :.pun DISABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.pun is already disabled.")
            ircsock.send(("PRIVMSG " + channel + " :.pun is already disabled.\n").encode())

    if channel + " :.command pun on" in line:
        if pun_status == 0:
            pun_on = line[-15:]
            if pun_on == ".command pun on":
                if nick in ops:
                    pun_status = 1
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.pun ENABLED")
                    ircsock.send(("PRIVMSG " + channel + " :.pun ENABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.pun is already enabled.")
            ircsock.send(("PRIVMSG " + channel + " :.pun is already enabled.\n").encode())

    if channel + " :.command suicide off" in line:
        if suicide_status == 1:
            suicide_off = line[-20:]
            if suicide_off == ".command suicide off":
                if nick in ops:
                    suicide_status = 0
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.suicide DISABLED")
                    ircsock.send(("PRIVMSG " + channel + " :.suicide DISABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.suicide is already disabled.")
            ircsock.send(("PRIVMSG " + channel + " :.suicide is already disabled.\n").encode())

    if channel + " :.command suicide on" in line:
        if suicide_status == 0:
            suicide_on = line[-19:]
            if suicide_on == ".command suicide on":
                if nick in ops:
                    suicide_status = 1
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.suicide ENABLED")
                    ircsock.send(("PRIVMSG " + channel + " :.suicide ENABLED\n").encode())
                else:
                    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :Just Ops can do this action.")
                    ircsock.send(("PRIVMSG " + channel + " :Just Ops can do this action.\n").encode())
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime()) + nickbot + " PRIVMSG " + channel + " :.suicide is already enabled.")
            ircsock.send(("PRIVMSG " + channel + " :.suicide is already enabled.\n").encode())
