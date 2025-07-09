print(r'''
                             _____
                          .-" .-. "-.
                        _/ '=(0.0)=' \_
                      /`   .='|m|'=.   `\
                      \________________ /
                  .--.__///`'-,__~\\\\~`
                 / /6|__\// a (__)-\\\\
                 \ \/--`((   ._\   ,)))
                 /  \\  ))\  -==-  (O)(
                /    )\((((\   .  /)))))
               /  _.' /  __(`~~~~`)__
              //"\\,-'-"`   `~~~~\\~~`"-.
             //  /`"              `      `\
            //
''')
print("Welcome to Treasure Island ye Old One-Eyed Fool.")
print("Your mission is to find the treasure, take that eye patch off so you can think better.")
#a backslash is an escape symbol, so it escapes the code.
direction_crossroad = input('You\'re at a cross road, Where do you want to go?\n '
                            'Type "Left" or "Right"\n').lower()
if direction_crossroad == "left":
    print("Phew, made it to the river, looks like you need to get across.")
    action_choice = input('Would you like to "Swim" or "Wait for the boat"?\n').lower()
    if action_choice == "wait for the boat" or action_choice == "wait":
        print(r'''Some magical pirate boat appeared out of nowhere and you crossed the terrorizing river to Treasure Island
            __/\__
         ~~~\____/~~~~~~
           ~  ~~~   ~.    ''')
        print("You see three treasure chests, only one contains the treasure\n"
              "If you choose the wrong chest, oly Merlin can save you, choose correctly and you can hopefully buy a new eye")
        chest_color = input('Which chest do you choose? "Red", "Yellow" or "Blue"\n').lower()
        if chest_color == "red":
            print("You got burned by Hell's Fire. Game over.")
        elif chest_color == "blue":
            print("Full of seawater, might as well stick your head in it and drown. Game over.")
        elif chest_color == "yellow":
            print(r'''Well blow me down, Ye struck gold! Go forth and celebrate
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            ******************************************************************************* ''')
        else:
            print("You really don't want to find that treasure huh?")
    else:
        print("You forgot you can't swim matey.Game over")
else:
    print("You got lost and drank your sorrows away. Game over")