define e = Character("Eileen", color="#c8ffc8")
default points = 0

label start:

    scene bg room with dissolve
    show eileen happy

    
    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"



    menu:

        "Go outside.":
            jump outside

        "Stay in this room.":
            jump stay

label outside:

    scene bg whitehouse with dissolve
    show eileen concerned

    e "It's freezing out here!"
    e "What should I do now??"

    menu:

        "Go back inside.":
            e "Thank goodness!"

        "Venture the outside world.":
            e "I don't know if I'm ready for that yet."
    return


label stay:

    show eileen happy
    $ points += 1
    e "Much better. It's warm in here."
    if points >= 1:
        e "You've stayed in this room a lot. Maybe you should go outside."
    return