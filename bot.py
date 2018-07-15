import socket
import random
import time
import greetings
import funnykill
import pun
import food
# from random import randint

server = 'euroserv.fr.quakenet.org'
channel = '#XXXXXX'
nickbot = 'Zeugma'
port = XXXX

ircsock = socket.socket()
ircsock.connect((server, port))

handle = ircsock.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')

print('NICK', nickbot, file=handle)
print('USER', nickbot, nickbot, nickbot, ':' + nickbot, file=handle)


streak = 0
ops = ["Vield", "adrianjch", "Zeugma", "Q"]
users = ["Vield", "adrianjch", "Zeugma", "Q", "muliro", "Filipa", "NeatNit", "GhostsDaddy", "zeugm_bot", "fishbot", "WOLFI3654atNU", "Vary_", "Vary"]
with open('actual_streak.txt', 'r') as astreak:
    astreak_contents = astreak.read()
    streak = int(astreak_contents)
max_streak = 5
# configuration status
with open('commands_config.txt', 'r') as config:
    config_contents = config.read()
    if "rr_status = 1" in config_contents:
        rr_status = 1
    else:
        rr_status = 0
    if "greetings_status = 1" in config_contents:
        greetings_status = 1
    else:
        greetings_status = 0
    if "pun_status = 1" in config_contents:
        pun_status = 1
    else:
        pun_status = 0
    if "funnykill_status = 1" in config_contents:
        funnykill_status = 1
    else:
        funnykill_status = 0
    if "pizza_status = 1" in config_contents:
        pizza_status = 1
    else:
        pizza_status = 0

for line in handle:
    line = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + line.strip()
    print(line)
    day = line.split(' ')[0]
    hour = line.split(' ')[1]
    nick = line[21:line.find("!")]
    command = line.split(' ')[3]
    channel_msg = line[line.find(command) + len(command) + 1:]
    message = line[line.find(channel) + len(channel) + 2:]
    printer = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + nickbot + " PRIVMSG " + channel + " :"
    sender = "PRIVMSG " + channel + " :"
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

# join to channel
    if "End of /MOTD command" in line:
        ircsock.send(('JOIN ' + channel + '\n').encode())

# PING response to avoid getting disconnect
    if "PING" in line:
        print("PONG :" + line.split(':')[3], file=handle)

# all raw log stuff
    if time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) in line:
        with open('rawlog.txt', 'a') as write_rawlog:
            write_rawlog.write(line + '\n')


    if command == "PRIVMSG":
# all .pizza thing
        if message == ".pizza":
            if pizza_status == 1:
                message = food.random_pizza_message(nick)
                print(printer + message)
                ircsock.send((sender + message + "\n").encode())
            else:
                print(printer + ".pizza is actually disabled. Ask an Op to enable that command.")
                ircsock.send((sender + ".pizza is actually disabled. Ask an Op to enable that command.\n").encode())

        if message.startswith(".pizza "):
            if pizza_status == 1:
                if message[7:] in users:
                    message = food.random_pizza_message(message[7:])
                    print(printer + message)
                    ircsock.send((sender + message + "\n").encode())
            else:
                print(printer + ".pizza is actually disabled. Ask an Op to enable that command.")
                ircsock.send((sender + ".pizza is actually disabled. Ask an Op to enable that command.\n").encode())
# bananaphone thing
        if message == "ringringringringringringring":
            # print("PRIVMSG " + channel + " BANANAPHONE!", file=handle)
            print(printer + "BANANAPHONE!")
            ircsock.send((sender + "BANANAPHONE!\n").encode())
# o/ thing
        if message == "o/":
            print(printer + "\o")
            ircsock.send((sender + "\o\n").encode())
# all .funnykill stuff
        if message == ".funnykill":
            if funnykill_status == 1:
                message = funnykill.random_funnykill_message(nick, nickbot)
                print(printer + message)
                ircsock.send((sender + message + "\n").encode())
            else:
                print(printer + ".funnykill is actually disabled. Ask an Op to enable that command.")
                ircsock.send((sender + ".funnykill is actually disabled. Ask an Op to enable that command.\n").encode())
# all .pun stuff
        if message == ".pun":
            if pun_status == 1:
                message = pun.random_pun_message()
                print(printer + message)
                ircsock.send((sender + message + "\n").encode())
            else:
                print(printer + ".pun is actually disabled. Ask an Op to enable that command.")
                ircsock.send((sender + ".pun is actually disabled. Ask an Op to enable that command.\n").encode())
# all .rr stuff
        if message == ".rr":
            if rr_status == 1:
                with open('rrstats_pulled.txt', 'w') as write_pulls:
                    write_pulls.write(str(rpulls))
                print(printer + "[rr] " + nick + " slowly pulls the trigger...")
                ircsock.send((sender + "[rr] " + nick + " slowly pulls the trigger...\n").encode())
                gun = random.randint(1, 6)
                time.sleep(3)
                if gun == 6:
                    with open('rrstats_shots.txt', 'w') as write_shots:
                        write_shots.write(str(rshots))
                    print(printer + "*BANG* you died!")
                    ircsock.send((sender + "*BANG* you died!\n").encode())
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
                    print(printer + "[rr] *click* - nothing happens. " + nick + " will live another day. Who's next? Misses since last death: " + str(streak) + ".")
                    ircsock.send((sender + "[rr] *click* - nothing happens. " + nick + " will live another day. Who's next? Misses since last death: " + str(streak) + ".\n").encode())
            else:
                ircsock.send((sender + ".rr is actually disabled. Ask an Op to enable that command.\n").encode())
# all .rrstats stuff
        if message == ".rrstats":
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
                            print(printer + "The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:.2%}'.format(percentage_rr)) + ". Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".")
                            ircsock.send((sender + "The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:.2%}'.format(percentage_rr)) + ". Highest streak: " + hstreak_contents + ", broken by " + broker_contents[:1] + "\u000f" + broker_contents[1:] + ".\n").encode())
                            # percentage_rr = int(shots_contents) / int(pulls_contents) * 100
                            # ircsock.send((sender + "The trigger was pulled " + pulls_contents + " times, " + shots_contents + " shots were fired. That's " + str('{:04.2f}'.format(percentage_rr)) + "%. Highest streak: " + hstreak_contents + ", broken by " + broker_contents + ".\n").encode())
# all the .command stuff
        if message == ".command":
            print(printer + "use .command <rr/greetings/pun/suicide/pizza> <on/off>")
            print(printer + "It will just work for Ops.")
            ircsock.send((sender + "use .command <rr/greetings/pun/suicide/pizza> <on/off>\n").encode())
            ircsock.send((sender + "It will just work for Ops.\n").encode())

        if message == ".command rr off":
            if rr_status == 1:
                if nick in ops:
                    # with open('commands_config.txt', 'w') as wconfig:
                       # wconfig.write( .replace("rr_status = 1", "rr_status = 0"))
                    rr_status = 0
                    print(printer + ".rr DISABLED")
                    ircsock.send((sender + ".rr DISABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".rr is already disabled.")
                ircsock.send((sender + ".rr is already disabled.\n").encode())

        if message == ".command rr on":
            if rr_status == 0:
                if nick in ops:
                    rr_status = 1
                    print(printer + ".rr ENABLED.")
                    ircsock.send((sender + ".rr ENABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".rr is already enabled.")
                ircsock.send((sender + ".rr is already enabled.\n").encode())

        if message == ".command greetings off":
            if greetings_status == 1:
                if nick in ops:
                    greetings_status = 0
                    print(printer + "greetings DISABLED")
                    ircsock.send((sender + "greetings DISABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + "greetings are already disabled.")
                ircsock.send((sender + "greetings are already disabled.\n").encode())

        if message == ".command greetings on":
            if greetings_status == 0:
                if nick in ops:
                    greetings_status = 1
                    print(printer + "greetings ENABLED")
                    ircsock.send((sender + "greetings ENABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + "greetings are already enabled.")
                ircsock.send((sender + "greetings are already enabled.\n").encode())

        if message == ".command pun off":
            if pun_status == 1:
                if nick in ops:
                    pun_status = 0
                    print(printer + ".pun DISABLED")
                    ircsock.send((sender + ".pun DISABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".pun is already disabled.")
                ircsock.send((sender + ".pun is already disabled.\n").encode())

        if message == ".command pun on":
            if pun_status == 0:
                if nick in ops:
                    pun_status = 1
                    print(printer + ".pun ENABLED")
                    ircsock.send((sender + ".pun ENABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".pun is already enabled.")
                ircsock.send((sender + ".pun is already enabled.\n").encode())

        if message == ".command funnykill off":
            if funnykill_status == 1:
                if nick in ops:
                    funnykill_status = 0
                    print(printer + ".funnykill DISABLED")
                    ircsock.send((sender + ".funnykill DISABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".funnykill is already disabled.")
                ircsock.send((sender + ".funnykill is already disabled.\n").encode())

        if message == ".command funnykill on":
            if funnykill_status == 0:
                if nick in ops:
                    funnykill_status = 1
                    print(printer + ".funnykill ENABLED")
                    ircsock.send((sender + ".funnykill ENABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".funnykill is already enabled.")
                ircsock.send((sender + ".funnykill is already enabled.\n").encode())

        if message == ".command pizza off":
            if pizza_status == 1:
                if nick in ops:
                    pizza_status = 0
                    print(printer + ".pizza DISABLED")
                    ircsock.send((sender + ".pizza DISABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".pizza is already disabled.")
                ircsock.send((sender + ".pizza is already disabled.\n").encode())

        if message == ".command pizza on":
            if pizza_status == 0:
                if nick in ops:
                    pizza_status = 1
                    print(printer + ".pizza ENSABLED")
                    ircsock.send((sender + ".pizza ENABLED\n").encode())
                else:
                    print(printer + "Just Ops can do this action.")
                    ircsock.send((sender + "Just Ops can do this action.\n").encode())
            else:
                print(printer + ".pizza is already enabled.")
                ircsock.send((sender + ".pizza is already enabled.\n").encode())

# all joining stuff
    if " JOIN " + channel in line and nick != nickbot:
        if greetings_status == 1:
            message = greetings.random_welcome_message(nick)
            print(printer + message)
            ircsock.send((sender + message + "\n").encode())

# all leaving stuff
    if " QUIT :" in line or " PART " + channel in line:
        if greetings_status == 1:
            message = greetings.random_goodbye_message(nick)
            print(printer + message)
            ircsock.send((sender + message + "\n").encode())

# if bot gets kicked, joins again
    if command == "KICK" and message.startswith("eugma "):
        ircsock.send(('JOIN ' + channel + '\n').encode())
        ircsock.send((sender + "I'm sorry, you can't kick me. ¯\_(ツ)_/¯\n").encode())

# all PM stuff
    if channel_msg.startswith(nickbot + " :") and nick == "adrianjch":
        adrianjch_message = line[91:]
        print(printer + adrianjch_message)
        ircsock.send((sender + adrianjch_message + "\n").encode())

    # if channel_msg.startswith("Zeugma :") and nick != "adrianjch":
     #   print(printer + nickbot + " just works in " + channel)
      #  ircsock.send((sender + nickbot + " just works in " + channel + "\n").encode())
