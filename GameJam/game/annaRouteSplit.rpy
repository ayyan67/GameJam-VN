
default jDone = False
default aDone = False
default kDone = False

label choices:



menu:
    "Talk to Joffrey" if jDone == False: 

        scene bg door

        j "I can’t believe I’m in this mess! I shouldn't have come to this mansion in the first place! I don’t even need the money but now I’m stuck here! AHHHHRG!" 

        with vpunch
        "You hear the breaking of furniture and glass from the other side of the door."
        

        "{i} “I should just probably just let him cool off” {/i}" 

        $ jDone = True

        jump choices

    
    "Talk to Annabelle" if aDone == False:

        scene bg door

        a "I’m sorry papa. I-I can’t take this anymore, everything is just happening so fast."

        "You hear sobbing from the other side of the door."

        "{i} “I should leave her be. What she needs right now is space, not me interrogating her.” {/i}"


        $ aDone = True

        jump choices
    
    "Talk to Klaus" if kDone == False:

        scene bg cellar

        me"..."

        show klaus angry

        k "You know, I thought I could make a difference. This place, it’s driving me insane. It feels like we’re in some sick game with no escape."

        k "Maybe another drink will clear my mind."

        me "I’ll try to find a way out of here. I swear it."

        "Klaus doesn’t respond, while the empty bottles of wine begin to pile up"

        "What should I do now?"

        $ kDone = True

        menu:
            "Return to the living room":
                scene bg livingroom
                jump choices
            "Go to the basement":
                jump basementScene



        




        jump choices

    "Talk to Cherry":

        jump annaRouteCherry

        

