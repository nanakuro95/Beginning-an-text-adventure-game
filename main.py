character = input("Enter a character name: ")
cereal = input("What's your favourite cereal? ")
lives = 3
stamina = ""


def beginning_damaged():
    lives = 3
    stamina = 50
    print(
        "You leave your lovely council abode, prepared for your newest quest already fatigued from the demon toast. Stocked up on healing potions and cheese wheels, you head off for the distant quest marker.")
    quest_list = open("Quest list.txt", "w")
    quest_list = open("Quest list.txt", "a")
    quest_list.write(
        "*Deliver some letters to the old crazy man down the road\n*Bring back the farmers chickens\n*Retrieve stolen items from the local tavern drunk\n*Slay a dragon guarded by other dragons in the great Mountains of Olde\n*Pick up milk on the way home")
    quest_list.close()
    print(
        "Hope you've had a good look at those quests " + character + ". I know they're not difficult and you're more than capable of getting them done, but I heard the weather might not be favourable so might wanna bring a bananna.")
    quests_remaining = 5
def beginning():
    lives = 3
    stamina = 100
    print("You leave your lovely council abode, prepared for your newest quest. Stocked up on healing potions and cheese wheels, you head off for the distant quest marker.")
    quest_list = open("Quest list.txt", "w")
    quest_list = open("Quest list.txt", "a")
    quest_list.write("*Deliver some letters to the old crazy man down the road\n*Bring back the farmers chickens\n*Retrieve stolen items from the local tavern drunk\n*Slay a dragon guarded by other dragons in the great Mountains of Olde\n*Pick up milk on the way home")
    quest_list.close()
    print("Hope you've had a good look at those quests " + character + ". I know they're not difficult and you're more than capable of getting them done, but I heard the weather might not be favourable so might wanna bring a bananna.")
    quests_remaining = 5

def breakfast():
    print(character + " finishes up in the bathroom and heads down for his warriors meal.")
    print("Opening the cupboards a selection of delicious options await you. What will you choose?")
    print("A) A delicious bowl of cereal. B) A plate full of pancakes. Or C) Some awesome toast with delicious melted butter on top.")
    answer = input()
    if "a" in answer:
        print("Absolutely gorgeous bowl of " + cereal + " with a nice glass of orange juice. Your belly is ready for adventure!")
        beginning()
    if "b" in answer:
        print("Your tum tum is nice and full with loads of pancakes. You might be fat rolling it for a while, but you're ready for your journey!")
        beginning()
    else:
        if "c" in answer:
            print("OH NO! THE TOAST WAS AWFUL AND YOUR RESOLVE HAS WEAKENED! Start your journey with reduced stamina.")
            beginning_damaged()


def bathroom():
    print("You get up and head to your remarkably clean bathroom.")
    print("There are several more options in front of you.")
    print("Do you a) Take a shit. b) Brush your teeth. Or c) Have an existential crisis in front of your mirror. It won't judge I promise.")
    answer = input("Make a choice: ")
    if "a" in answer:
        print("Yikes " + character + "! Warn me before ya go at least!")
        breakfast()
    if "b" in answer:
        print("Make sure to get rid of that plaque! Hero's don't have dirty teeth!")
        breakfast()
    else:
        if "c" in answer:
            print("Oof")
            print("Our main character has an extraordinarily large breakdown in front of the mirror, crumbling in front of it and ending up curled up on in ball on the tiled floor. I don't think he'll be saving anyone anytime soon...")
            game_over2()

def phone_browse():
    print(character + "decides he would rather browse the depths of reddit than save the village people or complete his daily quests...")
    print("However, I, using my almighty omniscient powers as the narrator, have decided that although there are some truly cringe-worthy posts to enjoy, " + character + " is going to get his shit together!")
    bathroom()

def game_over2():
    end_game = open("Sad times.txt", "w")
    end_game = open("Sad times.txt", "a")
    end_game.write("Big oof guys. I think we need to give him a hot minute. The orphan research will have to wait another day")
    end_game.close()


def game_over():
    screen = open("You failed ya nugget!.txt", "w")
    screen = open("You failed ya nugget!.txt", "a")
    screen.write("You're really a bad main character ya know that? We'll never be able cure the pandemic of orphans now!")
    screen.close()

def start():
    the_end = False
    print(character + "! You begin your journey by waking up in bed.")
    print("You have three options before you: A) You get right out of bed. B) You check your phone. C) You go back to sleep")
    answer = input("Choose: ")
    if "a" in answer:
        print("Good for you!")
        bathroom()
    if "b" in answer:
        print("Browsing reddit is a dangerous game my friend...you do have a journey to begin ya know...")
        phone_browse()
    else:
        if "c" in answer:
            print("You really gave up that quickly? Wow. Guess I'll tell all the starving villagers to go fuck themselves then.")
            the_end = True
            game_over()

start()

