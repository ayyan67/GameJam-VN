label cherryChoose:

    "{i}You run out of the gaming room and into the main hall. At the top of your lungs you shout.{/i}"

    window hide
    scene bg hallway
    with fade
    scene bg mansion # replace with room scene
    with fade
    window show

    me "{b}EVERYONE GET TO THE MAIN HALL. I KNOW WHO KILLED JOFFREY. I HAVE A GUN. IF THE MURDERER DOESN'T COME TO THE MAIN HALL RIGHT NOW, I'LL GO AND KILL THEM IN WHATEVER ROOM THEY'RE IN.{/b}" 

    "{i} Cherry and Anabelle appear on top of the stairs, frightened. Their lips were quivering.{/i}" 
    "{i}Klaus stumbles out of the hallway from the wine cellar, looking irritated. Chef comes out of the kitchen with a stern look on his face.{/i}" 
    "{i}The Maid does not show up but you are confident in her innocence. {/i}"

    me "The maid did not kill Joffrey. I can voich for that. The murderer must be one of you four." 

    show klaus angry
    with dissolve

    k " I deed not kill Joffree... I'm innacenn..."

    "Klaus attempts to profess his innocence through his drunken haze."

    hide klaus angry
    show cherry scared
    with dissolve

    c "I swear I didn't kill him! I couldn't have! I was in my room past 11!"

    hide cherry scared
    show chef
    with dissolve

    ch "I was in my kitchen all night!" 

    hide chef
    show annabelle smile
    with dissolve

    a "I won't even bother making an excuse. You don't trust me, plain and simple. Anything I say is a lie in your ears." 

    

    me "You got that right."
    hide annabelle smile
    show annabelle
    with dissolve

    a "What is this supposed to be a public execution? Do you want to save us all? How full of yourself can you get?"

    me "Shut up. This bullet will save us all."

    hide annabelle

    me "The murderer is-" 

    
    menu:
        "Head Chef":
            me "The murderer is Chef! Joffrey showed him no respect and shat on his food! He had full reason to kill him!" 

            show chef

            ch "What do you think you're doin-"

            play sound "audio/gun.mp3"
            with vpunch
            "You fire the gun."

            jump badend

        "Klaus":

            me "The murderer is Klaus! He was sick of Joffrey's shit and wanted to get rid of him so we could enjoy these 3 days together!"
            show klaus angry
            k "N-n-nuhh.... I'mm innacen-"

            play sound "audio/gun.mp3"
            with vpunch

            "You fire the gun."
            jump badend
        "Cherry":
            me "The murderer is Cherry! She was sick of Joffrey's rudeness and harassment so she had to get rid of him!" 
            show cherry sad
            c "N-no! I swear I'm innoce-"

            play sound "audio/gun.mp3"
            with vpunch

            "You fire the gun."

            jump badend

        "Annabelle":
            me "The murderer is Annabelle." 
            show annabelle smile
            
            "{i} Annabelle smirks, she struts down the stairs {/i}"
            show annabelle smile at right
            with move
            show cherry scared at left
            
            c "No... Annabelle! That can't be true!"

            show klaus angry at center

            k "A-Annabarr...?!"

            hide klaus angry
            show chef

            ch "Oh my god."

            hide cherry scared
            hide chef
            show annabelle smile at center with move

            a "You'd be pretty goddamn stupid if you couldn't figure out it was me. You know Joffrey was outside at some point before he died. Who was the only one that was outside? ME." 

            "{i}... {/i}" 

            "Annabelle reaches the bottom of the stairs and walks towards you."

            a "What, not going to shoot me?" 

            "{i} You furrow your brows. You are furious. {/i}" 

            "{i} There is nothing you can say that justifies taking another person's life. {/i}" 

            me "Why did you kill Joffrey?"

            "You tighten your grip on the revolver." 

            a "..."

            me "Was it because he was an ass?!" 

            hide annabelle smile
            show annabelle

            a "He tried to assault me." 

            me "Huh?"

            a "While I was by the pool, Joffrey came onto me and I kicked him to the ground. I ran into the living room."
            a "He was so pissed. He wanted to kill me. Had I not beat and stabbed him with the lamp, I would probably be the corpse in the living room right now." 

            me "..."

            a "Well? Satisfied? Still want to shoot me?" 

            me "I... uh..." 

            a "Shoot me. Or I will kill you and everyone else in this room." 

            "{i}Your palms are sweaty, your grip on the revolver tightens{/i}" 

            a "If I'm the only one alive, I leave with $100,000. That's 100 months worth of rent. A year's worth of salary."
            a "I cannot fathom how someone can throw away that much money so easily. But I won't miss this opportunity. This is for me and my dad."

            show annabelle smile at right
            with move
            show cherry scared at left

            c "Annabelle why! I thought we became friends" 

            a "Cherry, you were the first person I told about my family and our situation. So you should know full well how much I need the money for my dad's operation." 
            a "If come out of this trip with no cash, my Dad will be euthanized."

            c "But-"

            a "I would snuff the life out of you, I don't care." 

            hide cherry scared
            show annabelle smile at center with move

            "Cherry falls to her knees and starts sobbing in horror. Annabelle turns to you." 

            hide annabelle smile
            show annabelle
            with dissolve
            a "My Dad is on his last breath, and unless I make it there with the money for the operation, they're going to euthanize him."
            "Don't you understand? Me going home empty-handed would be the same as killing him" 
            a "I love my dad. He's the entire world to me. So if he dies. I'm better off dead as well"

            "Your eyes are filled with terror. You're shaking. But Annabelle's gaze does not waver." 

            a "So shoot me. It's me or the rest of you."            

            me "Annabelle please..."

            "{i}Why am I in this situation, I can't do this to her!{/i}"

            show annabelle :
                yalign 0.1
                ease 0.1 zoom 2
            pause 0.4
            show annabelle:
                ease 0.2 zoom 1
           
            "Before you can react, Annabelle rushes towards you and grabs the pistol, pointing it back towards you."

            a "Don't you dare move." 

            "Annabelle cracks open the revolver and glances at the chamber. She looks surprised for a moment before letting out a sign of resignation." 

            a "Fate's really cruel, huh." 

            "Annabelle puts the gun to her head." 

            hide annabelle
            show annabelle smile

            a "I'll see you later dad."

            me "{b}ANNABELLE STOP-{/b}" 
            play sound "audio/gun.mp3"
            with vpunch
            jump goodend