def count_quests():
    quests = [
        ["Deliver some letters to the old crazy man down the road"],
        ["Bring back the farmers chickens"],
        ["Retrieve stolen items from the local tavern drunk"],
        ["Slay a dragon guarded by other dragons in the great Mountains of Olde"],
        ["Pick up milk on the way home"],
    ]
    for quest in quests:
        for number in quest:
            print(str(quest) + "/" + str(len(quests)))

#this nested for loop and and 2D lists need work on. trying to figure out how I can count items within the list to see how many items inside are left but failed. need more knowledge! :3


count_quests()