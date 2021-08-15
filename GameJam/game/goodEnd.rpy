label goodend:
    window hide
    scene bg black
    pause 2
    show maid with dissolve
    window show

    play music "audio/endOST.mp3"

    m "Congratulations, it seems you have made the correct deduction." 
    m "While what Joffrey did was certainly not acceptable by any means, the life that Annabelle took will never be replaced."
    m "However, I'm still quite dissatisfied with the results you produced; this is not a desirable conclusion."
    m "..."
    m "I expect more from you on your next run."

    hide maid with moveoutbottom


    window hide
    stop music fadeout 5.0
    scene good end
    with fade
    pause 5