# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Klaus", who_color = "#79c27b")
define j = Character("Joffrey", who_color = "#747acc")
define c = Character("Cherry", who_color = "#e6bb5e")
define a = Character("Annabelle", who_color = "#ca6e7d")
define ch = Character("Chef", who_color = "#885d53")
define m = Character("Maid", who_color = "#e5ba5d")
define unknown = Character("???")

define me = Character("[player_name]")

#The defined character below will show the nvl window, which is a textbox overlaying the screen
define fullscreen = Character(None, kind=nvl, what_text_align=0.5, what_xalign=0.5, what_minwidth=700)
# The game starts here.

label start:

    # grabs user PC name
    scene bg room
    
    # get player n
    python:
        player_name = renpy.input("What is your name?")
        player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"


    "Pleased to meet you, [player_name]!"
    


    scene prologue
    with fade
    pause 2
    scene bg room # replace with room scene
    with fade
    
    # PROLOGUE

    "Friday 10 PM, you are browsing the internet when you get an email notification with an invitation."
    fullscreen "Dear invited guests \n 
    As we are celebrating the hundredth anniversary of our establishment, you are one of five candidates chosen to 
    stay at the esteemed Umair mansion for 3 days and nights! As a part of this event, 
    one person out of all the candidates will receive a cash prize of $100,000. 
    You are free to decline however; know that this is an exceptionally rare opportunity. 
    More detailed information will be provided at the event. If you have any further questions, 
    please contact: XXX - XXXX - XXXX. 
    We look forward to your presence at our mansion.”\n
    Address: XXXX XXXXXX XXXXXX\n
    \n
    Sincerely, 
    The Household of Umair
    "

    me "No shotthis is real, it has to be a scam."
   
    "You search up if there are similar scams to the email you just received, but there are no results"

    me "Although if this ends up being real, I don't have to worry about my income or tuition for a bit."

    "You search up if there are similar scams to the email you just received, but there are no results"
    "Upon futher research into the address provided in the email, you discover a lavish manor located in the outskirts of the city."

    me "It's close enough to bus to, so I guess the worst case is a wasted trip."
    

    scene day1
    with fade
    pause 2
    scene bg room # replace with mansion scene
    with fade

    "It's a sunny day, and you arrive at the mansion by Bus and a short walk. 
    Needing to travel a whole hour from your apartment in the scorching heat has already left you irritated. "
    "The thought that the email was actually a scam is about to set you off until you see other people gathered waiting in front of a gate. 
    Out of the four, a tall, muscular man waves you over to the group."

    show klaus
    
    unknown "Hey you must be the fifth, I'm Klaus"

    
    me "Hey, nice to meet you, same with you guys. I'm [me]. I think we were in the same lecture before, right? 
    I didn't think I'd see someone from my university here."
    hide klaus  

    show joffrey
    unknown "Yo, I recognize you from highschool. You were the loser who sat in the back of the class."

    me "..."

    me "{i}I don't know where he goes now, but he was a total druggie back in high school. 
    I think his name was Joffrey or something. He pissed off all the teachers and slept around too. 
    Right now, he dresses a bit better, but his personality is as shitty as it was back in school{/i}"
    hide joffrey  
    
    show cherry

    c "Cherry: Hey my name's Cherry. 
    I went to Southside high school so this is probably my first time seeing all of you."
    c"Did you guys come for the food as well?
    I bet a mansion this big has a chef or something so it seemed like a pretty worthy gamble to come here!"

    "She says this all while excitedly mowing down a double big mac."
    hide cherry

    show annabelle
    unknown "Hi... I'm Annabelle..."

    me "{i}I could barely make out what she said from behind her thick round glasses. 
    Despite her appearance, her timid nature seemed discrepant.{/i}"

    "A cold breeze blew past us as the gates of the mansion swung wide open. 
    A tall woman in a Victorian maid dress steps out. 
    Her face was expressionless as she bows and welcomes us to the mansion."

    m "Welcome to the esteemed Umair mansion. 
    I will be your guide for your stay. 
    Please, let me carry your luggage."

    j "Damn girl, you ain't so bad-looking!"

    "He dumps his bags on the maid and strolls past her."

    c "What an ass..."

    k "Hey, these bags look pretty heavy. I can help carry them if you like."

    m "I appreciate the kind words but please spare your concern for me. 
    You are our valued guest and we will accommodate you fully over these next three days."

    "All five of us and the maid walk through the gates and head into the mansion. Upon entering the large
    wooden front door, you are greeted with a red velvet carpet and sparkling chandelier. 
    "
    "Between two massive spiral staircases stands a tall buff man with a perm. 
    He wears an intense, irritated expression."

    ch "I'm the Head Chef around here, which is the name you MUST refer to me as. 
    Breakfast is at 8. Lunch is at 2. Dinner at 8. If you miss it, tough luck. 
    Go starve for all I care, damn freeloaders. Understood?"

    "Eveyone around me except for Joffrey nods"

    ch "{b}I can't hear you, is that a yes?!{/b}"

    j "Piss off! I'm your guest and someone like me deserves all kinds of respect around here."

    "The chef approaches Joffrey with a tightened fist, but he is promptly stopped by the maid. 
    The Chef sighs and furrows his brows. He looks even more irritated than before. 
    After some exchanged betweent he two, The Chef struts away, and Joffrey smiles smugly."

    k "Yo, Joffrey, chill man. Don't go picking fights with people. We're all here for the same reason."

    "The maid clears her throat and continues."

    m "The Master will wholeheartedly welcome his guests after he returns from his business trip. 
    Please make yourself at home for the time being."

    "The group dissipates after hearing her words and everyone looks for their own corner of the
    mansion to go to. You head up the stairs and find an empty guest room. "
    "You lay your bags down
    by the side of the bed and flop onto it. The sudden motion of the matress expelled an antique
    smell that quickly filled the room."

    me "{i}I guess it wasn't a scam after all, huh? This place looks like the real deal.{/i}"
    me "{i}Despite the scene Joffrey made, it doesn't concern me. 
    I'm going to take my sweet time and enjoy my time in this mansion. {/i}"

    "{i}As you begin to doze off, you hear a loud knock at your door.{/i}"

    k "Hey homie! We're meeting up in the living room to chill and get to know each other. Wanna come?"

    me "Huh? Ummm yeah sure, I guess I'll head down in a bit."

    me"{i}Begrudgingly, I bring myself out of my room.
    Before me and Klaus head into the room, 
    we hear Joffrey's loud ramblings through the halls{/i}"

    j "Yeah, I don't go to university cause it's a total waste of time y'know. 
    9-5 jobs are for sheep that can't think for themselves. 
    "
    "Think about it, Anna, drop out and become my secretary. 
    I'm raking it in, you can make a shit ton of money too."

    me "{i}What is he going on about?{/i}"

    a "I... Uh don't plan on dropping out..."

    j "C'mon... Don't be dumb. You know who Elon Musk is, right? 
    He said Dogecoin is gonna hit a dollar. I swear I know my shi-"

    c "She said she doesn’t want to join your stupid joke of a business."

    j "Shut up, no one's talking to you tubby."

    me "{i}...{/i}"

    c "I may enjoy food, but at least I’m not a stingy rat."

    k "Hey, hey, hey! Guys, let's settle down! 
    Joffrey man, what’d I say about chilling out, yo?"

    j "She called my business stupid. She had it coming..."

    c "This guy won’t stop bothering Annabelle with his annoying bullshit and keeps talking over her. 
    Why wouldn’t I step in?"

    a "It’s.. it’s fine..."

    k "Hey Joffrey man, I’m sure you’re a great entrepreneur, and other people 
    would be more willing to join your business, but sometimes it's just not for everyone. 
    Annabelle’s gotta have some stuff she wants to do after school too right?"

    a "I think want to be a nurse."

    c "Oh my god! That’s so cool! I’m trying to be a veterinarian! How about you [me]?"

    me "I don’t really know what I’m going to be in the future, 
    so I’m in open studies right now. Business does seem pretty interesting, though."


    return
 