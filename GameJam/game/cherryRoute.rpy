label day2cherry:
    show cherry

    me "I can help you find some food. I doubt Chef would be too pleased with us asking for food at this hour. 
    He seems pretty strict about his cooking schedule."

    c "That's great! Let's head on to the kitchen. It definitely has a pantry full of snacks!"

    me "I have some snacks from before I arrived. I got some potato chips and sour gummies."

    c "Ooooh, I love sour gummies!"

    me "Great, give me a sec. I'll get the snacks from my room."

    window hide
    scene 2mins
    with fade
    pause 2
    scene bg lobby
    with fade
    window show

    show cherry

    me "Here's all my snacks."

    c "Thank you! It feels like forever since I've had these types of snacks so I've been craving them." 

    me "No problem, I'm happy to help."

    c "I'm glad you were around though. I've had a condition ever since I was young where I'd go on feeding frenzies whenever I get extremely hungry."

    me "I see... Have you gone to any doctors about it, this seems kinda serious."

    hide cherry
    show cherry sad

    c "Yeah I've visited a couple of gastroenterologists around the city and they tole me it's genetic. Nothing I can do about it..."

    me "Huh...that sucks."

    hide cherry sad
    show cherry

    c "Well anyways, I'm glad I didn't have to go into a feeding frenzy here. Wouldn't want to embarrass myself in front of you guys." 

    me "Yeah no problem, let me know if you have any other problems."

    c "Yeah, thanks! Well I'll get going now, night night!" 

    me "Good night, I'll see you tomorrow."

    stop music fadeout 1.0

    hide cherry
    with moveoutright

    scene bg hallway night
    me "{i}I head back to my room, leaving Cherry in the living room with all my snacks. 
    As I pass by the glass doors leading to the outdoor pool in the back yard, I catch a glimpse of someone still swimming in the pool."
    me "{i}I still have some energy left in me so I guess I'll look around the mansion.{/i}"

    "You leave the living room and take a left and then a right. Across the hallway, it's a dead-end, but you notice a staircase leading down below."

    scene bg hallway night
    with fade
    "You head down the stairs and see an open door to the wine cellar. Surrounded by bottles, Klaus is passed out drunk."
    
    scene bg hallway night
    with fade
    "You take a left and see the basement under a smaller set of stairs. On the basement door, you see a map of the first and ground floors of the mansion."

    show mansion map at center
    with dissolve

    me "{i}This seems pretty handy, I guess I'll keep it on me{/i}"

    hide mansion map
    with dissolve

    scene bg room2 night

    "You enter your room and flop onto the soft bed. Your exhaustion causes you to fall asleep almost instantly, leaving the lights on in the room."

    window hide
    scene 3hrs
    with fade
    pause 2
    scene bg room2 night
    with fade
    window show


    scene bg black

    "The lights suddenly flicker off, leaving the room shrouded in a blanket of darkness, waking you up."

    me "{i}It's pitch black and I can't see an inch in front of me.{/i}"

    "However, despite the sudden occurrence, you couldn't be bothered to think more about it and you quickly drift off back to sleep."

    window hide
    scene day2
    with fade
    pause 2
    scene bg room2
    with fade
    window show

    play sound "audio/alarm.mp3"
    # phone alarm sfx

    "You awaken to the sound of your phone alarm which was originally set for seven. You drowsily put it to snooze and fall back asleep."
    stop sound 


    unknown "[me]... Ple... Ke... Up..." 

    unknown "Wa... up..." 

    me "I don't care about breakfast just let me sleep for five more minutes..."

    show maid
    with moveinbottom

    m "Please wake up. There has been a murder in the mansion."

    play music "audio/spookyOST.mp3"

    "The maid's words linger in your mind as oyu try to process them. You suddenly sit up alarmed."

    "{i}What did she just say? God I hope I'm hearing things.{/i}"

    m "The Head Chef has made breakfast. However, given the state that the living room is now in, no one is really eager to have breakfast."

    "{i}This has got to be a prank.{/i}"

    "As the reality of the Maid's revelation sets into your head, you feel goosebumps begin to form all over your body"

    "{i}A murder? This can't be real, theres no way. I gotta get out of here. 
    Paying for my rent just isn't worth my life, theres too much I still need to do. I can't die, i need to get the fuck out...{/i}"

    "You begin to grab your belongings and pack your bags ,but the maid stops you in your tracks."

    m "I'm afraid you cannot just leave in this situation." 

    m "We have informed my master adn the authorities regarding the murder that has occurred on his estate. 
    Therefore we has initiated a security lockdown to prevent any murder suspects from leaving the scene."

    me "You can't be serious, let me speak to the guy!"

    m "I'm afraid I cannot allow that to happen at the moment. The neccessary procedures are put in place for a situation like this
    so that no one, including the staff, can leave the property, no matter the reason."

    "Before you can retort, a piecing shriek from downstairs interupts your train of thought."

    m "Annabelle?!"
    
    window hide
    scene bg hallway
    with fade
    scene bg livingroom
    with fade
    window show

    "You rush downstairs and see Klaus, Annabelle and Cherry standing right outside the living room. 
    Klaus's face is pale and his lips are trembling. He notices you and stares at you hopelessly."
    "Annabelle, covering her face, is on her knees sobbing. Cherry is trying to comfort her but she too looks terrified."

    me "{i}...{/i}"

    "A you approach where the group is, you are met by a gruesome scene."
    window hide
    scene deathcg2 day
    with vpunch
    pause 1
    window show
    "Joffrey's lifeless body lies face down in a pool of blood."

    me "{i}Ugh...{/i}"

    "You recall the taste of last night's dinner in your throat as you suppress the urge to vomit."

    scene bg livingroom
    with fade
    show chef
    with moveinleft
    "The Head Chef walks in calmly, his usually tense face replaced with that of someone much softer."

    ch "I called the police but the line didn't go through."

    "Annabelle starts sobbing even harder." 

    show chef at left
    with move
    show klaus angry at right

    k "So are we just stuck here? With a dead body for god-knows how long!"

    hide chef
    show maid at left

    m "I'm afraid that is the current situation."

    k "{b}Man SHIT!{/b}"
    hide maid
    hide klaus angry with moveoutright

    "Klaus punches the nearest wall"

    m "Klaus, we gotta stay calm bro. Everyone here's distressed we gotta work through this together."

    "You try to reach out to him but he slaps your hand away."

    show klaus angry with moveinright

    k "{b}FUCK OFF! DON'T TOUCH ME!{/b}"

    "The room pauses for a brief moment from his sudden out-of-character voice raise."

    k "{b}DON'T YOU GET IT?! WE ARE THE ONLY ONES HERE! JOFFREY WAS JUST MURDERED! ONE OF US HAD TO HAVE DONE IT.{/b}"

    me "Listen Klaus, if we work together to establish our alibis maybe we can rule this out as an accident. 
    We have to stick together in these types of situations."

    k "Nah man. I'm done. I'm fucking done playing nice with all of you-"

    me "Klaus!"

    k "{b}STOP RIGHT THERE. I CAN'T TRUST ANY OF YOU. TAKE ONE STEP CLOSER AND I'LL BEAT THE SHIT OUT OF YOU.{/b}"

    hide klaus angry with moveoutright

    "You halt your movements as Klaus angrily rushes down the hallway away from the group."

    "{i}He's definitely going to end up drinking himself dead drunk in the wine cellar. I guess that's one way to deal with this shitty reality{/i}"

    me "Does anyone know what happened? Cherry? Annabelle?"

    show cherry scared at left
    show annabelle cry at right
    
    c "[me], I don't think you can talk to Annabelle in her current state. I'll take her up to her room and stay with her."

    me "How are you feeling about this?"

    c "To be honest, I'm really scared... I don't want to be like Klaus and instantly jump to the conclusion that one of us here is a murderer but..."

    me "It's okay I can't blame you for thinking that way."

    c "I'm sure you're safe because I saw you go up to your room and never leave it. 
    I don't where Annabelle was, but given her extreme reaction to Joffrey's corpse, there's no way she could commit murder."

    c "That just leaves Klaus, the Head Chef and the maid, but I don't want to suspect any of them."

    "Cherry shoots a worried glance at Maid and Chef. Chef is noticeably perturbed while Maid's expression does not change."

    c "Sorry I can't stick around here any longer, I'm going to bring Anna to her room."

    me "You sure you ok? You haven't had breakfast yet right?"

    c "No, I still have your snacks from last night so I think I'll be good. They should probably last me until tonight."

    me "Well, you and Annabelle take care. I'll stick by the scene to see if I find any leads as to what happened."    

    hide cherry scared
    hide annabelle cry

    show chef with moveinright

    ch "Just so you know I was a hundred percent by myself in the kitchen past 12 AM preparing the ingredients for you people."

    me "Thank you, Head Chef."

    ch "You not gonna eat my food?"

    me "Sorry I don't have much of an appetite right now."

    hide chef with moveoutright

    "Chef walks back into the kitchen, mumbling under his breath." 

    "You turn your attention to the remaining person left in the living room."

    show maid

    me "Do you happen to know about anything that happened?"

    m "After you, Joffrey and Annabelle went upstairs after dinner, Klaus went to the wine cellar and Cherry remained in the dining room asking for more food. 
    During this time, I washed the dishes and cleaned the entire first floor until about quarter to 10."
    m "I returned to my bedroom, took a bath at 10 PM and went to sleep at 10:30 PM. 
    During the time I was leaving to my bedroom, Cherry was passed out on the couch and Annabelle was by the pool."

    me "I see. That's basically what I know as well."

    m "Would you like to investigate Joffrey's body?"

    "{i}I am curious but I'd leave my fingerprints on the scene. I'd rather wait for the cops to arrive and th-{/i}"

    m "I can handle the body if you would prefer to not touch it."

    me "..."
    me "Thanks."

    show deathcg2 day
    with fade

    "You and maid head over to Joffrey's corpse. The Maid grabs Joffrey's head by his hair and lifts his head up from the pool of blood."

    me "{i}How is she so emotionless doing that?{/i}"

    m "The tips of his hair are stained in his own blood, the source being a large gash on the top of his head. 
    It seems that the wound is still open which would explain why the blood around that area is still liquid."

    "You catch a glimpse of some reflections in his head as the light hits his disheveled hair."

    me "There's something in the wound."

    m "It's glass."

    "Joffrey's entire left face looks like it was mauled by a bear. A chunk of his cheek is scraped off and his right eye sockets is destroyed."

    m "There are some bruises and scratches covering his entire body." 

    "The maid lifts up his shirt and reveals a deep gash around his hip. As you eyes scan down Joffrey's body, you notice his muddy jeans."

    me "Why would there be mud on him?"

    m "Ah. That likely means at one point last night, he was outside in the backyard, dead or alive."

    me"{i}The lack of blood outside the glass sliding doors probably means that he was killed indoors. So then why is there mud? 
    Given how the lamp in the living room is knocked over, I think that's probably what ended up killing him. {/i}"

    m "So what do you think?"

    me "Huh?"

    m "Was it premeditated?"

    me "{i}A lamp is a pretty terrible murder weapon.{/i}"
    me "{i}If you really wanted to kill someone, you would grab a knife and stab them, strangle them or even just drown them in a pool.{/i}"
    me "{i}Using a lamp to stab someone, especially with how difficult it is to hold, it would make sense if it was used in the heat of the moment.{/i}"

    me "I don't think it was premeditated."

    m "..."
    me "..."

    scene bg livingroom
    show maid

    me "I think I've seen enough here. Are you sure you're okay with all this?"
    m "Please do not worry about me, it is all part of the job."
    
    me "Alright,  I'll go check up on Cherry and Annabelle."

    scene bg hallway
    with fade

    "As you leave the room, you turn to glance at the maid, and the same emotionless expression remains on her face."
    me "{i}I still don't know how she can do things like that without batting an eye.{/i}"
    me "{i}You've gotta be inhuman to show that little emotion in this type of scenario. 
    Maybe she has a dark past so she's desensitized to these types of things.{/i}"
    
    stop music fadeout 1.0

    scene bg door
    with fade

    play sound "audio/knock.mp3"

    "You go upstairs and knock on Annabelle's door"

    me "Hey are you guys alright in there?"

    "The door opens and you are greeted by an exhausted looking Cherry."

    show cherry scared
    with moveinbottom

    c "Annabelle is just in her bed right now resting. She's been through a lot. I think she's okay for now." 

    me "It's good she's calmed down." 

    c "So did you figure anything out?"

    c "For one, I'm pretty sure someone used the lamp to kill Joffrey. 
    Also, he died in the living room but his pants were muddy. There may have been a struggle as well." 

    c "..."
    c "I know he was an absolute ass this entire time but murder is just too much. No one can justify killing another human being."
    c "..."
    c "Are they...?"

    me "If you're talking about the Chef and the Maid, I doubt its them since they both have alibis." 

    c "Are you sure we can trust them?" 

    me "I don't know about the Chef but the Maid was a great help during the investigation so I think I can trust her. "

    c  "That's good. I think you're one of the few people I can trust here." 

    me "..."

    c "This whole taking care of Annabelle is stressing me out. I'm starving."

    me "Lunch is in an hour."

    c "Yeah, but what if I get hungry after dinner again? I finished all the snacks you gave me!"

    menu:
        "Help Cherry find some food":

            # Choice 1: Help Cherry find food.

            jump day2cherrycherry

        "Watch over Annabelle and tell Cherry to talk to the chef":

            # Choice 2: Talk to Annabelle

            jump day2cherryanna


return