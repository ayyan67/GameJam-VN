
image dinosaur = "dino.jpg"
default hasKey = False


label basementScene:
    
    scene bg basement
    with fade

    "You walk out of the wine cellar and make your way to the basement. 
    Unlike the rest of the mansion, it has an old and decrepit vibe."


    "In the middle of the room stands a table with 4 drawers. A feeling of being watched settles over nerves. 
    You want to leave, but the drawers draw your attention. You only have time to open one, choose wisely."

    menu:
        "Open the bottom-left drawer":
            "You find nothing but old papers and a strange drawing of a dinosaur"

            show dinosaur

            me"{i}huh, maybe the master had a strange obsession with Albertan archeology{/i}"
            me"{i}This won't help me though{/i}"

            hide dinosaur
            

            me"Okay, I better head back"
            jump choices

        "Open the upper-left drawer":
            "You find a key with a note attached"

            "{i}It says this is the key to the Security room, this might be useful for later.{/i}"

            me"Okay, I better head back"

            $ hasKey = True

            jump choices

        "Open the bottom-right drawer":
            "You find a strange magazine with the title ‘Back to the Future’, featuring a young kid next to a futuristic car"
            "{i}Useless{/i}"
            me"Okay, I better head back"
            jump choices

        "Open the upper-right drawer":

            "You find a roadside picture of metal balls forming a dome."
            "{i} Useless.{/i}"
            me"Okay, I better head back"

            jump choices

            
