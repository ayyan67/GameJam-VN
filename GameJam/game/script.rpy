# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    python:
        import os

        user = os.environ.get('username')

    "Hello there, [user]."


    # get player name
    $ player_name = renpy.input("Before we begin, what is your name?")    
    $ player_name = player_name.strip()

    # default player name
    if player_name == "":
        $ player_name="Shuji"



    scene bg room
   

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
