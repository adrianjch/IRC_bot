import random

INGREDIENTS = (
    'bacon',
    'bbq sauce',
    'black olives',
    'brie',
    'chilli oil',
    'double cheese',
    'fresh onion',
    'garlic',
    'green olives',
    'ham',
    'jalapenos',
    'mozzarella',
    'pepperoni',
    'pork',
    'roasted chicken',
    'salami',
    'salsa',
    'sweetcorn',
    'tabasco',
    'tomato',
)

VEGAN_INGREDIENTS = (
    "smoked tofu",
    "cashew nuts",
    "tomato",
    "black olives",
    "green olives",
    "caramelized onion",
    "chilli oil",
    "garlic",
    "vegan cheese",
)


def random_pizza_message(nick):
    MODE = [
        "NORMAL",
        "REPEATED",
        "MESSED_UP",
        "NEED_MORE_MONEY",
        "NO_FLOUR",
        "PIZZA_IMAGE",
        "LATE_PIZZA",
        "INFINITE_INGREDIENTS",
    ]

    MODE_WEIGHTS = [
        855,
        10,
        30,
        30,
        30,
        10,
        30,
        5,
    ]

    pizza_images = [
        "https://i.imgur.com/Kr3jeFE.jpg",
        "https://i.imgur.com/x8A9kva.png",
        "https://i.imgur.com/7D6OiqK.jpg",
        "https://i.imgur.com/0SNvRwr.jpg",
        "https://i.imgur.com/yJy0xxo.jpg",
        "https://i.imgur.com/E561XOP.jpg",
        "https://i.imgur.com/BG39k1J.jpg",
        "https://i.imgur.com/Oh5R2UN.jpg",
        "https://i.imgur.com/lMfVxOg.jpg",
    ]

    delivery_mode = random.choices(MODE, MODE_WEIGHTS)
    is_vegan = (nick == "Vield")
    if delivery_mode == ['REPEATED']:
        toppings_choices = VEGAN_INGREDIENTS if is_vegan else INGREDIENTS
        ingredients = random.choice(toppings_choices)
        return "ACTION serves to " + nick + " a pizza with {}, {} and {}.".format(ingredients, ingredients, ingredients)
    elif delivery_mode == ['MESSED_UP']:
        toppings_choices = VEGAN_INGREDIENTS if is_vegan else INGREDIENTS
        ingredients = random.sample(toppings_choices, 2)
        return "ACTION serves to " + nick + " a little burnt pizza with {} and {}.".format(*ingredients)
    elif delivery_mode == ['NEED_MORE_MONEY']:
        return "Okay, that will be 15.50 please."
    elif delivery_mode == ['NO_FLOUR']:
        return "So sorry, we're out of flour!"
    elif delivery_mode == ['INFINITE_INGREDIENTS']:
        toppings_choices = INGREDIENTS
        ingredients = random.sample(toppings_choices, 20)
        return "ACTION serves to " + nick + " a pizza with {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, and {}.".format(*ingredients)
    elif delivery_mode == ['PIZZA_IMAGE']:
        return random.choice(pizza_images)
    elif delivery_mode == ['LATE_PIZZA']:
        toppings_choices = VEGAN_INGREDIENTS if is_vegan else INGREDIENTS
        ingredients = random.sample(toppings_choices, 3)
        time.sleep(10)
        return "Your pizza will arrive in 15 minutes."
        return "ACTION serves to " + nick + " a pizza with {}, {} and {}.".format(*ingredients)
    else:
        toppings_choices = VEGAN_INGREDIENTS if is_vegan else INGREDIENTS
        ingredients = random.sample(toppings_choices, 3)
        return "ACTION serves to " + nick + " a pizza with {}, {} and {}.".format(*ingredients)
