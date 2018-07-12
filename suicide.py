import random


def random_suicide_message(nick, nickbot):
    suicide_messages = [
        "{nick} slipped in the bathroom and choked on the shower curtain.",
        "{nick} trips over his own shoe laces and dies.",
        "{nick} died from a high salt intake.",
        "{nick} slips on a banana peel and falls down the stairs.",
        "{nick} dies from watching the emoji movie and enjoying it.",
        "{nick} tried to outrun a train, the train won.",
        "{nick} dies from severe dislike of sand. It's coarse and rough and irritating it gets everywhere.",
        "{nick} dies from dabbing too hard.",
        "{nick} can't be killed because it's a ghost.",
        "{nickbot} shoots {nick} in the head.",
        "{nickbot} turns on Goosebumps(2015 film) on the TV. {nick} being a scaredy-cat, dies of an heart attack.",
        "{nick} vocally opposed the Clintons and then suddenly disappeared.",
        "{nick} ate a piece of exotic butter. It was so amazing that it killed him.",
        "{nick} was eaten alive by ants.",
        "{nick} ripped its own heart out to show their love for {nickbot}.",
        "{nickbot} shot {nick} using the Starkiller Base!",
        "{nickbot} gets {nick} to watch anime with it. {nick} couldn't handle it.",
        "{nickbot} hugs {nick} too hard..",
        "{nick} ate too many laxatives and drowned in its own shit. Ew.",
        "{nick} was murdered by {nickbot} and everyone knows it, but there is no proof.",
        "{nick} chokes in a trash can.",
        "The bullet missed Harambe and hit {nick} instead. Yay for Harambe!",
        "{nickbot} was so swag that {nick} died due to it. #Swag",
        "{nick} decided it was a good idea to fight a tiger while smelling like meat. It did not end well.",
        "{nick} was so dumb that it choked on oxygen.",
        "{nick} was killed by their own stupidity.",
        "Our lord and savior Gaben strikes {nick} with a lighting bolt.",
        "{nick} dies of dysentery.",
        "{nick} eats too much copypasta and explodes.",
        "{nick} died from a tragic amount of bad succ.",
        "{nick} fires a supersonic frozen turkey at {nick}, killing it instantly.",
        "{nickbot} pushes {nick} into the cold vacuum of space.",
    ]
    return random.choice(suicide_messages).format(nick=nick, nickbot=nickbot)
