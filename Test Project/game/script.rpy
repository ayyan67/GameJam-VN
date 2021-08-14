# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = "#FF0044")
define d = Character("Aly", color = "#3355FF")


define x = 5



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "How was your day?"

    menu:
        "I had a great day":
            jump GoodDay
        "My day was not good":
            jump BadDay
        
"end of start block"

    #$ x -= 1
    #e "My name is %(x)s"

    

    # This ends the game.

return






label GoodDay:

e "Nice bro good day"


return


label BadDay:

e "Nice bro bad day"

return