# This is where we define the transformations

# This transform sizes the character properly at the given X position.
transform tcommon(x=975, z=0.95):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

# These transforms have the characters stand still at a given position given
# how many characters are on screen and which character number they are.
transform t41:
    tcommon(535)
transform t42:
    tcommon(828)
transform t43:
    tcommon(1121)
transform t44:
    tcommon(1415)
transform t31:
    tcommon(575)
transform t32:
    tcommon(975)
transform t33:
    tcommon(1375)
transform t21:
    tcommon(735)
transform t22:
    tcommon(1215)
transform t11:
    tcommon(975)