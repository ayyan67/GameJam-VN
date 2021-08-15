

label annaRouteCherry:

 "{i}Cherry seems to be acting awfully suspicious. I should definetly ask her some questions?{/i}"

 me"{i}She was heading to the kitchen if I recall correctly{/i}"
 

 scene bg hallway
 with fade
 scene bg kitchen
 with fade

 show cherry scared
  
 me"What are you doing here?"

 c "SHHHHHH! come over, I have something to say."

 "You and Cherry secretly move to the corner of the kitchen."

 c "Please just believe me. I was just looking for food when..."

 c "I saw something in the pantry and then chef was yelling and threatening me with his knife. I didn’t mean to kill him"

 me"Calm down, what do you mean by you didn’t mean to kill?"

 c "It’s an accident I swear I killed chef while acting in self-defence. There was a dead body in the pantry so chef must be a killer."

 me"There was a WHAT in the pantry?"

 c "It was pitch black but I definitely saw a body inside the pantry…"

 me"A DEAD BODY!? That’s impossible! We are the only ones in the mansion!"

 c "SHHHHHH! I swear it was in the pantry, I can prove it."

 "Walking towards the pantry, you and Cherry slowly slide open the pantry door anticipating the horror that might be behind it. But-"

 me"It’s empty. There’s no dead body, Cherry."

 c "I swear I saw it! There’s no way!"

 me"I’m trying to believe your story, but can you just tell me the truth. Why did you kill chef?"

 hide cherry scared

 show cherry mad 
 with hpunch

 c "GODDAMMIT I TOLD YOU SAW A DEAD BODY! BUT IT’S GONE AND I DON’T KNOW WHY!"
 
 me"cherry-"

 c "You JUST don’t get it! Out of everyone in the group, I thought you and Klaus were half-decent people. But apparently, you were not the person I thought you were."

 hide cherry mad
 with moveoutright

 "Cherry storms out of the kitchen, heading down towards the wine cellar." 
 
 scene bg hallway
 with fade

 show cherry mad at left
 with moveinleft

 show maid

 "As you try to catch up to her, you swiftly pass by the Maid as you head towards the wine cellar."
 

 hide cherry mad
 with moveoutright

 hide maid 
 scene bg cellar
 with fade

 

 "Entering the wine cellar, you hear a fierce guttural scream from behind the wine cabinets." 
 
 show cherry scared

 "Cherry stops in her tracks and looks toward the location of the scream."

 hide cherry scared

 show cherry sad 
 hide cherry sad
 with moveoutbottom
 
 "In a blink of an eye, Cherry’s body is obliterated by a hulking mass of muscles - her innards splattering a cross you and into the hallway. A towering monster covered in blood stands before you."
 
 me"Klaus… is that you?"

 show klaus angry
 with dis

 "Clouds of steam escape from his nostrils. Your eyes make contact. His mouth slowly forms an unnatural grin, inhuman almost."

 
 with hpunch
 k "GRRRRRAAAAHHHHHH!!!"

 "You make a run for it"

 scene bg hallway
 with fade

 "{i}Klaus is right behind me what do I do?!?{/i}"
 
 menu: 
     "Go into the basement":

         scene bg basement
         with fade

         
         "You hide in the basement for what seems like an eternity"
         
         show klaus
         with moveinbottom

         "Klaus eventually finds you"

         with vpunch
         "You are torn limb from limb"
         with vpunch

         scene bad end
         pause 2

     "Hide in your room":
         scene bg door
         with fade

         
         "Klaus catches up to you right outside your door." 
         
         show klaus
         with moveinleft

         with vpunch
         "He grabs you by your head and pulls your spine out from your body"
         with vpunch

         scene bad end
         pause 2

     "Go into the kitchen":
         jump routePantry

     "Go into the Games Room":

         scene bg arcade
         with fade

         "You manage to outmaneuver Klaus and escape to the Games Room"
         "You can hear Klaus charging towards you. You look for an escape route and notice a gap in one of the shelves, revealing a door"

         "{i} Surveillance Room {/i}"

         me"This may be my only chance at living, I've gotta get in here"

         if hasKey:

             me"This is the only key I have"
             "You cross your fingers and insert the key into the door"
             jump annaRouteSurveillance
            
         "Despite your desperate attempts to force it open, the door doesn't budge"

        

         show klaus
         with moveinright

         with vpunch
         "Klaus catches up to you and crushes your skull between his thunder thighs"
         with vpunch

         scene bad end
         pause 2

        
     


         
        
        



        

 




