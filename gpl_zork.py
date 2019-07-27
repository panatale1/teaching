# Introduction narration of game

keep_going = True
loop = 4
print("---------------------------------------------------------")
print("Welcome to Greenburgh Zork - The Unofficial Python Version.")
print("INSTRUCTIONS:")
print("Tell the game what you want to do. Use phrases like 'open box', 'go left', or 'look at desk'.")
_ = raw_input("Hit Enter when ready.")

while keep_going:
    # First Input Loop
    while loop == 4:
        if loop == 4:
            print("---------------------------------------------------------")
            print("You are standing in the Children's Room. Ahead is the Desk and the Storytime Room.")
            print("Behind you is the door to Teenburgh.")
            print("There is a Small Box on the desk.")
            second = raw_input("What do you do? ")

        if second.lower() == ("take box"):
            print("---------------------------------------------------------")
            print("It is securely anchored.")
        elif second.lower() == ("open box"):
            print("---------------------------------------------------------")
            print("Opening the small box reveals a leaflet.")
        elif second.lower() == ("go to storytime"):
            print("---------------------------------------------------------")
            print("The door is locked, but there is a lockbox on the door.")
        elif second.lower() == ("open lockbox"):
            print("---------------------------------------------------------")
            print("You guess the combination is 0000 and get a key.")
        elif second.lower() == ("go to teenburgh"):
            print("---------------------------------------------------------")
            print("The door is securly locked.")
        elif second.lower() in ("look at room", "look around"):
            print("---------------------------------------------------------")
            print(
            "The room has lots of bookshelves and table. There are doors to the Storytime Room and Teenburgh.")
        elif second.lower() == ("use key"):
            print("---------------------------------------------------------")
            print("You unlock the door and go through")
            loop = 8
        elif second.lower() == ("read leaflet"):
            print("---------------------------------------------------------")
            print(
            "Welcome to the Unofficial Greenburgh Version of Zork. Your mission is to escape the library.")
        else:
            print("---------------------------------------------------------")


    # Used Key from Lockbox
    while loop == 8:
        if loop == 8:
            print("---------------------------------------------------------")
            print(
            "This is Teenburgh. Through the glass doors ahead of you, there appears to be light. To your left is the Teen Desk")
            teenburgh_input = raw_input("What do you do? ")

        if teenburgh_input.lower() == ("open glass doors "):
            print("---------------------------------------------------------")
            print("You would need a key to get through the doors.")
        elif teenburgh_input.lower() == ("go left"):
            print("---------------------------------------------------------")
            print("The desk is clear, but there are two drawers in the desk.")
        elif teenburgh_input.lower() == ("open drawers"):
            print("---------------------------------------------------------")
            print("The bottom drawer is locked, but you find a key in the top drawer.")
        elif teenburgh_input.lower() == ("use key"):
            loop = 9
        else:
            print("---------------------------------------------------------")


    # Used key from desk drawer
    while loop == 9:
        if loop == 9:
            print("---------------------------------------------------------")
            print(
            "You unlock the glass doors and now are in the Adult Room. There is a door to your left, tables are in front of you, and there are bookshelves to the right.")
            adult_input = raw_input("What do you do? ")

        if adult_input.lower() == ("go left"):
            print("---------------------------------------------------------")
            print("The door is locked.")
        elif adult_input.lower() == ("open door"):
            print("---------------------------------------------------------")
            print("The door is locked.")
        elif adult_input.lower() == ("look at tables"):
            print("---------------------------------------------------------")
            print("The tables have this weeks newspapers on it")
        elif adult_input.lower() in ["read papers", "read newspapers"]:
            print("---------------------------------------------------------")
            print("There's nothing interesting in the papers")
        elif adult_input.lower() in ["go right", "look at shelves", "look at bookshelves"]:
            print("---------------------------------------------------------")
            print("Among the bookshelves is a glass room")
        elif adult_input.lower() in ["enter room", "go room", "enter glass room", "go glass room"]:
            print("--------------------------------------------------------")
            print("On the table is a key.")
        elif adult_input.lower() == "use key":
            print("---------------------------------------------------------")
            print("You return to the main area and unlock the door. There are stairs on the other side.")
        elif adult_input.lower() in ["go down stairs", "go downstairs"]:
            loop = 10
        else:
            print("---------------------------------------------------------")


    # Main Lobby loop
    while loop == 10:
        if loop == 10:
            print("---------------------------------------------------------")
            print("You are in the main lobby. In front of you is the Circulation Desk.")
            print("To the left is the main entrance, to the right is a hallway.")
            lobby_input = raw_input("What do you do? ")

        if lobby_input.lower() in ["go left", "exit building"]:
            print("---------------------------------------------------------")
            print("There is a sign on the front doors and they are locked.")
        elif lobby_input.lower() == ("read sign"):
            print("---------------------------------------------------------")
            print("The sign says the doors are out of order")
        elif lobby_input.lower() == ("look at desk"):
            print("---------------------------------------------------------")
            print("There is a golden statue on the desk.")
        elif lobby_input.lower() == ("take statue"):
            print("---------------------------------------------------------")
            print("You take the statue. Why not, it's a free statue.")
        elif lobby_input.lower() == ("look at statue"):
            print("---------------------------------------------------------")
            print("It's a golden statue of Dr. Martin Luther King, Jr.")
            print("You shake it, and something rattles inside it.")
        elif lobby_input.lower() == ("open statue"):
            print("---------------------------------------------------------")
            print("You've found a glass cutter.")
        elif lobby_input.lower() in ["go right", "go hallway"]:
            loop = 11
        else:
            print("---------------------------------------------------------")


    # End of game
    while loop == 11:
        if loop == 11:
            print("---------------------------------------------------------")
            print("You reach the end of the hall. There is a glass door in front of you that is locked from the inside.")
            print("There is a sign on the door.")
            hallway_input = raw_input("What do you do? ")

        if hallway_input.lower() == ("read sign"):
            print("---------------------------------------------------------")
            print("The sign says 'To exit, cut through the door. Dr. King can help.'")
        elif hallway_input.lower() in ["go back", "return", "go to desk"]:
            loop = 10
        elif hallway_input.lower() in ["use glass cutter", "use glasscutter", "use cutter", "cut glass"]:
            print("---------------------------------------------------------")
            print("You use the glass cutter to remove a piece of glass.")
            print("You reach through, unlock the door, and escape the library!")
            loop = 12
        else:
            print("---------------------------------------------------------")

    while loop == 12:
        # Exit loop at the end of game
        exit_input = raw_input("Do you want to continue? Y/N ")
        if exit_input.lower()[0] == ("n"):
            keep_going = False
            break
        elif exit_input.lower()[0] == ("y"):
            print("---------------------------------------------------------")
            print("Everything around you goes hazy as you fall asleep on the loading dock.")
            print("A short time later, you awaken and stand up.")
            loop = 4
