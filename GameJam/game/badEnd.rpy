label badend:
    window hide
    scene bg black
    pause 2
    show maid with dissolve
    window show

    play music "audio/endOST.mp3"

    m "It seems you have shot an innocent person." 
    m "The culprit has gotten away scott free and you have doomed not only your own life but the lives of those around you."
    m "I'm dissatisfied with the results you produced, this is quite the undesirable conclusion."
    m "..."
    m "I expect more from you on your next run."

    hide maid with moveoutbottom

    window hide
    stop music fadeout 5.0
    scene bad end
    with fade
    pause 5