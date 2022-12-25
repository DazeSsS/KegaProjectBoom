init python:

    def drop1(drop, drags):

        store.place1 = drags[0].drag_name

    def drop2(drop, drags):       

        store.place2 = drags[0].drag_name

    def drop3(drop, drags):

        store.place3 = drags[0].drag_name

    def drag1(drags, drop):

        if not drop:
            return

        drags[0].snap(drop.x + 50, drop.y + 20)

    def drag2(drags, drop):

        if not drop:
            return

        drags[0].snap(drop.x + 50, drop.y - 20)

    def drag3(drags, drop):

        if not drop:
            return

        drags[0].snap(drop.x + 50, drop.y + 15)

    def drag4(drags, drop):

        if not drop:
            return

        drags[0].snap(drop.x + 50, drop.y + 25)

    def drag5(drags, drop):

        if not drop:
            return

        drags[0].snap(drop.x + 50, drop.y + 35)

screen quest1:
    modal True

    python:
        store.pos1 = ""
        store.pos2 = ""
        store.pos3 = ""
        store.pos4 = ""
        store.pos5 = ""
        store.place1 = ""
        store.place2 = ""
        store.place3 = ""

    imagebutton:
        xpos 450
        ypos 780
        auto "QuestElements/FirstQuest/btn_%s.png"
        action [Hide("quest1"), Jump("check_answer")]

    draggroup:
        drag:
            drag_name "place1"
            child "QuestElements/FirstQuest/drop.png"
            xpos 400
            ypos 200
            draggable False
            droppable True
            dropped drop1
        drag:
            drag_name "place2"
            child "QuestElements/FirstQuest/drop.png"
            xpos 400
            ypos 400
            draggable False
            droppable True
            dropped drop2
        drag:
            drag_name "place3"
            child "QuestElements/FirstQuest/drop.png"
            xpos 400
            ypos 600
            draggable False
            droppable True
            dropped drop3

        drag:
            drag_name "line1"
            child "QuestElements/FirstQuest/line1.png"
            xpos 1200
            ypos 100
            droppable False
            dragged drag1
        drag:
            drag_name "line2"
            child "QuestElements/FirstQuest/line2.png"
            xpos 1200
            ypos 680
            droppable False
            dragged drag2
        drag:
            drag_name "line3"
            child "QuestElements/FirstQuest/line3.png"
            xpos 1200
            ypos 520
            droppable False
            dragged drag3
        drag:
            drag_name "line4"
            child "QuestElements/FirstQuest/line4.png"
            xpos 1200
            ypos 400
            droppable False
            dragged drag4
        drag:
            drag_name "line5"
            child "QuestElements/FirstQuest/line5.png"
            xpos 1200
            ypos 240
            droppable False
            dragged drag5