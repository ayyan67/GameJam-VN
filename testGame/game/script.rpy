# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# At the start of script.rpy, add this code:
init python:
    import os

define a = Character("Aly")


define affection = 2

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aly

    # These display lines of dialogue.
    a "save here"
    a "what anime do you like?"

menu:  
    
    # q1
    "steins gate":
        jump q2

    "sword art online":
        $ affection -= 1
        jump q2

label q2:
    a "who is ur fav woman?"

    menu:
        "rias gremory":
            $ affection -= 1
            jump cont

        "illyasviel von einzbern":
            jump cont

label cont:
    if affection == 0:
        jump badend
    elif affection == 1:
        jump nend
    else:
        jump goodend



label badend:
    a "ur an imposter"
    a "i never want to see you again im deleting the save file"
    a "dont try to reset"
    python:
        os.remove('Desktop/Test/game/saves/1-1-LT1.save')
        # Specify the file path as well
    jump quit


label nend:
    a "i think you'll like welcome to the nhk"   
    a "i recomment fate carnival phantasm"
    a "reload the save if you want to check out my loli collection"
    jump quit

label goodend:
    a "you can become the animation to my ping pong"
    a "come check out my loli figure collection"
    jump quit




label quit:
# game end
    return
