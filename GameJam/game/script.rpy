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
    scene bg black
    

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

    "Friday 10 PM, you are browsing the internet on your phone when you get an email notification with an invitation."
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
    The Household of Umair"

    me "No shotthis is real, it has to be a scam."
   
    "You look up on your laptop if there are scams similar to the email you just received, but there seems to be no relevant results"

    me "Although if this ends up being real, I don't have to worry about my income or tuition for a bit."

    "You search up if there are similar scams to the email you just received, but there are no results"
    "Upon futher research into the address provided in the email, you discover a lavish manor located in the outskirts of the city."

    me "It's close enough to bus to, so I guess the worst case is a wasted trip."
    

    scene day1
    with fade
    pause 2
    scene bg mansionentrance # replace with mansion scene
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

    hide annabelle

    show maid
    with moveinleft
    "A cold breeze blew past us as the gates of the mansion swung wide open. 
    A tall woman in a Victorian maid dress steps out. 
    Her face was expressionless as she bows and welcomes us to the mansion."

    m "Welcome to the esteemed Umair mansion. 
    I will be your guide for your stay. 
    Please, let me carry your luggage."

    show maid at left
    with move
    show joffrey at right


    j "Damn girl, you ain't so bad-looking!"

    "He dumps his bags on the maid and strolls past her."
    hide joffrey
    show cherry mad at right
    hide cherry mad
    c "What an ass..."
    
    show klaus mad at right
    k "Hey, these bags look pretty heavy. I can help carry them if you like."
    
    m "I appreciate the kind words but please spare your concern for me. 
    You are our valued guest and we will accommodate you fully over these next three days."

    hide maid
    hide klaus mad

    scene bg mansion
    with fade

    "All five of us and the maid walk through the gates and head into the mansion. Upon entering the large
    wooden front door, you are greeted with a red velvet carpet and sparkling chandelier. 
    "
    "Between two massive spiral staircases stands a tall buff man with a perm. 
    He wears an intense, irritated expression."

    show chef
    with moveinbottom

    ch "I'm the Head Chef around here, which is the name you MUST refer to me as. 
    Breakfast is at 8. Lunch is at 2. Dinner at 8. If you miss it, tough luck. 
    Go starve for all I care, damn freeloaders. Understood?"

    "Eveyone around me except for Joffrey nods"

    ch "{b}I can't hear you, is that a yes?!{/b}"

    show chef at left
    with move
    show joffrey at right

    j "Piss off! I'm your guest and someone like me deserves all kinds of respect around here."

    show chef at center
    with move
    show maid at left
    with move


    "The chef approaches Joffrey with a tightened fist, but he is promptly stopped by the maid. 
    The Chef sighs and furrows his brows. He looks even more irritated than before. "

    hide chef
    with moveoutleft
    hide joffrey
    show joffrey smile at right

    "After some exchanged glances between the two, The Chef struts away, and Joffrey smiles smugly."

    hide maid
    with moveoutleft
    show klaus mad at left
    with moveinleft

    k "Yo, Joffrey, chill man. Don't go picking fights with people. We're all here for the same reason."

    hide klaus mad
    hide joffrey smile
    show maid

    "The maid clears her throat and continues."

    m "The Master will wholeheartedly welcome his guests after he returns from his business trip. 
    Please make yourself at home for the time being."


    hide maid

    "The group dissipates after hearing her words and everyone looks for their own corner of the
    mansion to go to. You head up the stairs and find an empty guest room. "

    scene bg room2
    with fade

    "You lay your bags down
    by the side of the bed and flop onto it. The sudden motion of the matress expelled an antique
    smell that quickly filled the room."

    me "{i}I guess it wasn't a scam after all, huh? This place looks like the real deal.{/i}"
    me "{i}Despite the scene Joffrey made, it doesn't concern me. 
    I'm going to take my sweet time and enjoy my time in this mansion. {/i}"

    # knock sound effect
    scene bg black
    with fade
    "{i}As you begin to doze off, you hear a loud knock at your door. You open it and are greeted by an enthusiastic Klaus.{/i}"
    scene bg room2
    with fade
    show klaus
    k "Hey homie! We're meeting up in the living room to chill and get to know each other. Wanna come?"

    me "Huh? Ummm yeah sure, I guess I'll head down in a bit."
    hide klaus

    scene bg hallway
    with fade
    "{i}Begrudgingly, you bring myself out of your room.
    Before you and Klaus head into the main lobby, 
    we hear Joffrey's loud ramblings echo through the halls{/i}"

    scene bg lobby
    with fade
    show joffrey smile

    j "Yeah, I don't go to university cause it's a total waste of time y'know. 
    9-5 jobs are for sheep that can't think for themselves. 
    "
    "Think about it, Anna, drop out and become my secretary. 
    I'm raking it in, you can make a shit ton of money too."

    me "{i}What is he going on about?{/i}"

    hide joffrey smile
    show annabelle

    a "I... Uh don't plan on dropping out..."

    hide annabelle
    show joffrey

    j "C'mon... Don't be dumb. You know who Elon Musk is, right? R
    He said Dogecoin is gonna hit a dollar. I swear I know my shi-"

    show joffrey at left
    with move
    show cherry mad at right

    c "She said she doesn't want to join your stupid joke of a business."

    j "Shut up, no one's talking to you tubby."

    me "{i}...{/i}"

    c "I may enjoy food, but at least I'm not a stingy rat."

    show joffrey at center
    with move
    show klaus mad at left
    with moveinleft

    k "Hey, hey, hey! Guys, let's settle down! 
    Joffrey man, what'd I say about chilling out, yo?"

    j "She called my business stupid. She had it coming..."

    c "This guy won't stop bothering Annabelle with his annoying bullshit and keeps talking over her. 
    Why wouldn't I step in?"
    
    hide joffrey
    show annabelle at center

    a "It's.. it's fine..."

    k "Hey Joffrey man, I'm sure you're a great entrepreneur, and other people 
    would be more willing to join your business, but sometimes it's just not for everyone. 
    Annabelle's gotta have some stuff she wants to do after school too right?"

    a "I think want to be a nurse."

    hide cherry mad
    show cherry at right

    c "Oh my god! That's so cool! I'm trying to be a veterinarian! How about you [me]?"

    me "I don't really know what I'm going to be in the future, 
    so I'm in open studies right now. Business does seem pretty interesting, though."

    hide annabelle
    show joffrey smile at center

    j "Attaboy, I always thought you were a wuss in high school, but now you have the alpha male mindset."

    me "{i}...{/i}"

    k "I'm trying to be a personal trainer, so I'm learning Kinesiology. But Joffrey, y'see what I mean? Everyone's got something they wanna do."

    j "Yeah, yeah, fine. I get it. Success isn't meant for everyone."

    c "I still think whatever you're doing is dumb, but hey, to each to their own."

    hide joffrey smile
    show joffrey

    me "You know, let's all get along. We're lucky to be here, so we should try to at least make the most of it."

    hide joffrey
    show annabelle at center

    a "I... I think I passed by a game room e-earlier. There was a ping pong table and stuff..."

    hide klaus
    show klaus at left

    k "Hell yeah, I was a ping pong god in middle school! My nickname? The flaming paddler."

    me "That's great, let's head on over then."

    hide joffrey
    hide annabelle
    hide cherry

    scene bg hallway
    with fade

    "{i}You and the group go back into the hallway and head left. As you pass by the kitchen, the Chef notices the group walking by and shoots a nasty glare, 
    but only you seemed to notice. You approach a red door that Annabelle points.{/i}"

    scene bg arcade
    with fade

    "{i}Upon entering, you are greeted by a colourful, dimly lit room. 
    There's a huge pool table in the center of the room with a ping pong table next to ir. The walls are lined with arcade cabinets and there
    are various brightly lit and flashing machines scattered in the room.{/i}"

    show klaus
    with moveinbottom

    k "{b}YO, THIS IS GREAT!{/b} I haven't played pool in ages. Damn! They have this old arcade game too!"

    show klaus at left
    with move

    show annabelle

    a "This is my first time seeing a pool table..."

    show cherry at right

    c "Hey, I've played pool before I can teach you!"

    a "Thanks..."

    hide annabelle
    hide cherry
    show joffrey at right
    with moveinright

    j "Hmph, all this is child's play unless you guys want to bet some real money."

    hide joffrey
    with moveoutright
    show klaus at center
    with move

    k "Wanna play homie? You seem full of potential."

    me "I haven't played in years, but sure I can take you on."

    k "{b}LET'S DO THIS!!{/b}"

init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "Klaus"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "bg pong field"

    add pong

    text _("You"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text _("klaus"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text _("Click to Begin"):
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

    show klaus

    if _return == "Klaus":

        
        me "Holy crap, Klaus is insane! He destroyed me!"

    else:

        me "Holy crap, Klaus is insane! I barely won by the skin of my teeth!" 

    
    k "Man, that was fun! I sure worked up a sweat!"

    hide klaus
    show cherry at left
    show annabelle at right

    c "Annabelle! Are you sure this is your first time?!"
    a "I tend to pick up things pretty fast..."

    show joffrey at center
    with moveinleft

    j "You boors done yet? I think it's time for dinner now."

    hide cherry
    hide annabelle
    show joffrey at left
    with move
    show klaus at right

    k "Yeah, I'm starving! Let's get to the dining room before Chef gets mad!"

    hide joffrey
    hide klaus

    scene bg kitchen
    "The group gets seated in five grandiose dining chairs surrounding the large dinner table. 
    The maid follows you out of the hallway carrying a jug of water, five glasses and five sets of cutlery, setting it all up in front of us."

    show chef
    with moveinleft
    hide chef
    with moveoutright

    "The head chef comes out balancing five plates like a performer and lays them out in front of you flawlessly. 
    The aroma that filled the table was enchanting, leaving all our mouths salivating, Cherry especially. 
    She begins wolfing down the steak while Joffrey pokes at his food"

    show joffrey

    j "I don't eat non-organic food because the carcinogens rot your brain and that's not a good long-term investment."

    show joffrey at left
    with move
    show cherry at right
    
    c "Just enjoy the food pea brain."

    show klaus

    k "Holy moly! This steak's so tender, hey Chef how many grams is this?! I need to know how much protein to drink later!"

    "{i}The chef ignores him and walks away. You could've sworn you saw him snear a little while he was leaving but that thought quickly leaves your head.{/i}"

    scene 3hrs
    with fade
    pause 2
    scene bg room2 # replace with room scene
    with fade

    me "{i}After eating, we all headed up to our rooms. 
    Joffrey was rambling about doubling profits from his business to Annabelle but she politely shooed him away and closed her door. 
    Joffrey sighs, scoffs and enters the room next to Annabelle's.{/i}"
    me "{i}Cherry ended up napping in the living room. I assume she asked Chef for thirds and probably passed out from a food-coma. 
    I think Klaus got his hands into the wine cellar and started drinking whatever liquid he could find. He's probably passed out there as well. 
    It's only 10 PM and I'm not sleeping anytime soon, I think I'll just head out, explore the mansion and see if I can talk to anybody.{/i}"

    scene bg hallway
    with fade

    "You exit your room and hear splashing outside. 
    You go to the end of the hallway and see Annabelle sitting by the pool."
    
    "You jump up and head downstairs to the living room and see Cherry on the floor groaning."

    scene bg lobby
    show cherry sad
    
    me "Hey, you alright?"

    c "Yeah... Yeah... I'm fine..."

    me "I don't know about that, it looked like you hit your head pretty hard."

    hide cherry sad
    show cherry
    c "Nah! I'm built like a potato!"

    me "{i}Potato?!{/1}"

    c "I'm pretty famished though."

    me "{i}She's famished?!{/1}"

    menu:
        "test"

        "Help cherry find some food":

            # Choice 1: Help Cherry find food.

            jump day2cherry

        "Hang out with Annabelle at the pool":

            # Choice 2: Talk to Annabelle

            jump day2anna

    label after_menu:
        "After having my drink, I got on with my morning."


label day2cherry:

    "HERE IS DAY 2 CHERRY ROUTE"

    return


label day2anna:

    "HERE IS DAY 2 ANNA ROUTE"

    return