# 1- importing random module
import random

# 2- creating subjects
subjects = [
    "Hania Aamir",
    "Saba Qamar",
    "Fawad Khan", 
    "Bilal Abbas Khan",
    "A Group of Monkeys",
    "Prime Minister Imran Khan",
    "Auto Rickshaw Driver from Pakistan"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Pakistan Local Train",
    "a plate of Samosa",
    "inside Parliament",
    "at Tarbela Dam",
    "during IPL Match",
    "at Wagah Border"
]

# 3- starting headline generation using loop
while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n", headline)

    while True:
        user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

        if user_input == "yes":
            break

        elif user_input == "no":
            print("\nThanks for using Fake News Headline Generator.")
            exit()

        else:
            print("Invalid input! Please enter yes or no.")