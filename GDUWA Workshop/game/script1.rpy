label vn_start:
    scene bg build with fade

    play music c1 fadein 1.0

    show miki smile at t22
    show aiko smile at t21

    p "Hey, you girls doing okay, you've been looking at me for a long time."

    show miki o_smile_c_blush at t22

    mi "Everything is fine, don't worry. Right, Aiko?"

    "She said as she nudges the girl next to her"

    $ ai_name = "Aiko"

    show aiko o_smile_blush at t21
    show miki smile_c_blush at t22

    ai "Ah, right... Yeah, nothing wrong."

    show aiko smile_blush at t21

    p "Ummmm, alright then."

    p "Oh yeah, Miki. You girls hungry?"

    show miki o_smile at t22

    $ mi_name = "Miki"

    mi "I know I am."

    show miki smile at t22
    show aiko o_smile_c at t21

    ai "I am too."

    show aiko smile_c at t21

    p "Then, let's go in."

    hide miki
    hide aiko

    stop music fadeout 1.0

    scene bg black with fade

    play sound co volume 1.0
    
    queue sound cc volume 1.0

    scene bg restraunt with fade

    play music c2 fadein 1.0

    "We entered the restaunt, ready to order food."

    return

label order:

    show miki o_smile at t11

    mi "What do you plan to order, [p_name]?"

    show miki smile at t11

    menu:
        p "I think I'll have a..."
        "Coffee":
            p "Coffee."
        "Sandwich":
            p "Sandwich."
        "Chips":
            p "Chips"

    show miki smile at t21
    show aiko o_smile at t22

    ai "Not a bad choice, I'd say."

    return