def start():
    print('''
        Beyond the Castle
               +~~
               |~~
               |
        +---------------+
        |               |
    +-----------------------+
    |         +--+          |
    |         |  |          |
    +-----------------------+
    ''')
    print("You find an abandoned castle in the woods.")
    print("Seeking your fortune, you decide to investigate.")
    print("As you enter the castle, a tree falls, blocking your exit.")
    print("When the dust settles, you see that you are an empty stone room.")
    print("There is a door on the left and a door on the right.")
    print("Choose a door, left or right?")
    
    while True:
        choice = input('> ')
        
        if "left" in choice.lower():
            print("You go through the left door.")
            ogre_room()
        elif "right" in choice.lower():
            print("You go through the right door.")
            choice_room()
        else:
            print("You can only choose 'left' or 'right'")

def ogre_room():
    print('ogre room')
    exit(0)

def choice_room():
    print('choice room')
    exit(0)

def dead(explaination):
    print(explaination)
    exit(0)
    
start()
