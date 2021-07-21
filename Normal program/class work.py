#gram ID: Adventure Game - Part II
#Author: Eric Chen
#Purpose:Create the python program for my game.

from random import randint
#Variables that control the loop program
game_status = 'yes'

while game_status == 'yes':
  #variable initialization
    bag = ['nothing']
    room_status = [0, 0, 0, 0, 0, 0]
    roominfo_list = []
    connections = []
    directions = []
    conlist = []
    dirlist = []
    cholist = []
    anslist = []
    starfish_status = 0
    roomname = ""
    roomnum = 1
    my_live = 1000
  #room function definitions
    def room_1():
        if room_status[0] == 0:
            roomname = "School"
            connections = [2, 3, 4]
            directions = ["n", "e", "w"]
            description = "You saw a map on the school ground and you are very interested in it"
            action = "1.Pick up the map and view the map"
            choice = ['1']
            answer = ["\nThis is a treasure map! ! ! The treasure map points to the secret recipe of a certain food. The treasure map shows that you should first go to the Seaside to the north of the school, then take a boat to the island to the east of the school, then go to the abandoned factory west of the school, and finally enter the basement of the abandoned factory."]
            room_status[0] = 1
            return (roomname, connections, directions, description,action,choice,answer)
        else:
            roomname = "School"
            connections = [2, 3, 4]
            directions = ["n", "e", "w"]
            description = "You returned to school, and a sentence appeared in front of you: Don’t stay here for too long, please go to the location indicated on the treasure map as soon as possible"
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description, action, choice, answer)


    def room_2():
        if room_status[2] == 0:
            roomname = "Seaside"
            connections = [1, 3]
            directions = ["s", "se"]
            description = "You arrive at the Seaside and follow the instructions on the treasure map to find a backpack, you feel something is inside the backpack"
            action = "1.open the backpack"
            choice = ['1']
            answer = ["\nyou open the backpack and found some items:"
                      "treasure map, spatula, lollipop. You put all these things into your backpack."]
            global  bag
            bag = ["lollipop","spatula","treasure map"]
            room_status[2] = 1
            return (roomname, connections, directions, description,action,choice,answer,bag)
        else:
            roomname = "Seaside"
            connections = [1, 3]
            directions = ["s", "se"]
            description = "You returned to Seaside, and a sentence appeared in front of you: Don’t stay here for too long, please go to the location indicated on the treasure map as soon as possible"
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description,action,choice,answer)


    def room_3():
        if room_status[2] == 1:
            roomname = "Island"
            connections = [1, 2]
            directions = ["w", "nw"]
            description = "You arrive on the island by boat, and a huge starfish stops you. You need to find a way to pass him before you can go to the next location."
            action = """You have two options:
            1. Use a spatula to fight with him 
            2. Give a lollipop to the starfish (if you choose to give a lollipop to starfish, it will become your friend and help you) """
            choice = ['1','2']
            answer= [enemy(), "\nYou successfully made friends with Starfish! You got the treasure map he guarded!"]
            room_status[2] = 2
            room_status[3] = 1
            return (roomname, connections, directions, description,action, choice, answer)
        if room_status[2] == 2:
            roomname = "Island"
            connections = [1]
            directions = ["w"]
            description = "You returned to Island, and a sentence appeared in front of you: Don’t stay here for too long, please go to the location indicated on the treasure map as soon as possible"
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description, action, choice, answer)
        else:
            roomname = "Island"
            connections = [1]
            directions = ["w"]
            description = "You are blocked by an invisible force, and a sentence appears in front of you: You currently have no access rights, please go back the same way, and then go to the place indicated by the treasure map."
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description, action, choice, answer)


    def room_4():
        if room_status[3] == 1:
            roomname = "Abandoned Warehouse "
            connections = [1, 5]
            directions = ["e", "s"]
            description = "According to the instructions of the treasure map, when you came to the abandoned factory, a yellow square stopped you, you need to find a way to pass him to go to the next location"
            action = """You have three choices:
            1. Fight with it with a spatula 
            2. Use a lollipop to buy him (if you have a lollipop)
            3. You can to summon its good friend the starfish, When the starfish comes with you,it will not hurt you (provided that you have given the lollipop to the starfish)"""
            choice = ['1','2','3']
            answer = [enemy(),"You successfully made friends with yellow square! The yellow square will no longer be your enemy", "With the help of the starfish, the yellow square will no longer be your enemy"]
            room_status[3] = 2
            room_status[4] = 2
            return (roomname, connections, directions, description,action,choice,answer)
        if room_status[4] == 2:
            roomname = "Abandoned Warehouse "
            connections = [1, 5]
            directions = ["e", "s"]
            description = "You returned to Abandoned Warehouse, and a sentence appeared in front of you: Don’t stay here for too long, please go to the location indicated on the treasure map as soon as possible"
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description, action, choice, answer)
        else:
            roomname = "Abandoned Warehouse "
            connections = [1]
            directions = ["e"]
            description = "You are blocked by an invisible force, and a sentence appears in front of you: You currently have no access rights, please go back the same way, and then go to the place indicated by the treasure map."
            action = "1.check your bag"
            choice = ['1']
            answer = [bag]
            return (roomname, connections, directions, description, action, choice, answer)


    def room_5():
        description = "According to the instructions of the treasure map, you find the entrance to the basement behind the abandoned factory. You see a treasure chest in the middle of the basement. When you walk over, a huge crab suddenly appears. You must fight it to get the treasure chest"
        connections = [1]
        directions = ["game ending"]
        action = """you only have one choices: 
        1.Fight for wealth! ! ! ! ! ! ! !！！！！！！！！！"""
        choice = ['1']
        answer = [enemy()]
        return (roomname, connections, directions, description, action, choice, answer)


    def enemy():
        global my_live
        n = 0
        m = 0
        enemy_live = 3
        while True:
            enemy_attack = randint(1,3)
            my_attack = randint(1,3)
            if my_attack < enemy_attack:
                my_live = my_live - 1
                n = n + 1
            if my_attack > enemy_attack:
                enemy_live = enemy_live - 1
                m = m + 1
                if enemy_live == 0:
                    return "you win! You hit the enemy ", m, "times and kill him. Enemy hit you",n,"times and you have",my_live," lives left"
            if my_attack == enemy_attack:
                my_live = my_live - 1
                enemy_live = enemy_live -1
                n = n + 1
                m = m + 1
                if enemy_live == 0:
                    return "you win! You hit the enemy ", m, "times and kill him. Enemy hit you",n,"times and you have",my_live," lives left"

    print("Welcome to the word game: Looking for the legendary treasure. !!!!\n")
  #main game play loop
    while True:
      #room selection if statments
        if roomnum == 1:
            roominfo_list = room_1()

        if roomnum == 2:
            roominfo_list = room_2()

        if roomnum == 3:
            roominfo_list = room_3()

        if roomnum == 4:
            roominfo_list = room_4()

        if roomnum == 5:
            roominfo_list = room_5()

        print(roominfo_list[0])
        print()
        print(roominfo_list[3])
        print()

        print("you can do: ", roominfo_list[4])
        cholist = roominfo_list[5]
        anslist = roominfo_list[6]

        action = input("\nwhat is your choose? (just enter the number of the option): ")
        if action == '2':
            if bag[0] != 'lollipop':
                print("You cheated, you don't have a lollipop anymore, because you cheated and the game is over.")
                print()
                game_status = input("\nyesDo you want to play againt? (yes or no): ")
                break
        if action == '2':
            bag.pop(0)
        if action == '3':
            if bag[0] == 'lollipop':
                print("You cheated, you didn't give the starfish lollipop at all but you killed it, because you cheated, the game is over.")
                print()
                game_status = input("\nDo you want to play againt? (yes or no): ")
                break

        index = cholist.index(action)
        print(anslist[index])

        print("\nyou can go: ", roominfo_list[2])
        conlist = roominfo_list[1]
        dirlist = roominfo_list[2]

        where = input("\nwhich way you want to go? ")
        print()
        if where == 'game ending':
            print("You got the secret recipe of Crab Fort that SpongeBob SquarePants and Crab Boss will guard for life. According to the method taught by the secret recipe of the crab castle, you set up the king crab castle on the earth and obtained a huge amount of wealth.")
            game_status = input("\nDo you want to play againt? (yes or no): ")
            break
        index = dirlist.index(where)
        roomnum = conlist[index]

print("Thank you for playing the game I wrote, have a good day!")