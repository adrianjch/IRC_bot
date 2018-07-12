import random

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
        "Hey guys! {nick} is here!",
        "Welcome, {nick}. I hope you brought pizza.",
        "We were waiting for you {nick}",
        "{nick} it's here, as the prophecy predicted.",
        "It is a bird! It is a plane! Forget it, it's just {nick}",
        "{nick} has arrived. The party is over.",
        "{nick} is here to kick ass and chew gum. And {nick} has no chewing gum left.",
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
