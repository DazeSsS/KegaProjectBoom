init python:

    def drop1(drop, drags):

        store.place1 = drags[0].drag_name

    def drop2(drop, drags):       

        store.place2 = drags[0].drag_name

    def drop3(drop, drags):       

        store.place3 = drags[0].drag_name

    def drop4(drop, drags):       

        store.place4 = drags[0].drag_name

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

    add "QuestElements/FirstQuest/drop.png":
        xpos 350
        ypos 200

    add "QuestElements/FirstQuest/line1.png":
        xpos 400
        ypos 220

    imagebutton:
        xpos 440
        ypos 880
        auto "QuestElements/FirstQuest/btn_%s.png"
        action [Hide("quest1"), Jump("check_answer")]

    draggroup:
        drag:
            drag_name "place1"
            child "QuestElements/FirstQuest/drop.png"
            xpos 350
            ypos 420
            draggable False
            droppable True
            dropped drop1
        drag:
            drag_name "place2"
            child "QuestElements/FirstQuest/drop.png"
            xpos 350
            ypos 660
            draggable False
            droppable True
            dropped drop2

        drag:
            drag_name "line2"
            child "QuestElements/FirstQuest/line2.png"
            xpos 1150
            ypos 740
            droppable False
            dragged drag2
        drag:
            drag_name "line3"
            child "QuestElements/FirstQuest/line3.png"
            xpos 1150
            ypos 540
            droppable False
            dragged drag3
        drag:
            drag_name "line4"
            child "QuestElements/FirstQuest/line4.png"
            xpos 1150
            ypos 380
            droppable False
            dragged drag4
        drag:
            drag_name "line5"
            child "QuestElements/FirstQuest/line5.png"
            xpos 1150
            ypos 190
            droppable False
            dragged drag5

screen laptop:

    add "QuestElements/SecondQuest/block2.png":
        xpos 100
        ypos 73

    add "QuestElements/SecondQuest/bracket.png":
        xpos 1000
        ypos 80
        zoom 1.5

    text "создание обучающей выборки":
        xpos 1200
        ypos 220
        size 40

    add "QuestElements/SecondQuest/block3.png":
        xpos 100
        ypos 485

    add "QuestElements/SecondQuest/bracket.png":
        xpos 750
        ypos 470

    text "настройка нейронки":
        xpos 900
        ypos 550
        size 40

    add "QuestElements/SecondQuest/block4.png":
        xpos 100
        ypos 705

    add "QuestElements/SecondQuest/bracket.png":
        xpos 1270
        ypos 700
        zoom 0.2

    text "запуск обучения":
        xpos 1350
        ypos 695
        size 40

    add "QuestElements/SecondQuest/block1.png":
        xpos 100
        ypos 765

    add "QuestElements/SecondQuest/bracket.png":
        xpos 750
        ypos 740

    text "шапка нашего кода":
        xpos 900
        ypos 820
        size 40

screen quest2:

    modal True

    textbutton "Запустить" action Jump("check_answer2"):
        xpos 1650
        ypos 50

    draggroup:
        drag:
            drag_name "place1"
            child "QuestElements/SecondQuest/drop.png"
            xpos 100
            ypos 50
            draggable False
            droppable True
            dropped drop1
        drag:
            drag_name "place2"
            child "QuestElements/SecondQuest/drop.png"
            xpos 100
            ypos 280
            draggable False
            droppable True
            dropped drop2
        drag:
            drag_name "place3"
            child "QuestElements/SecondQuest/drop.png"
            xpos 100
            ypos 650
            draggable False
            droppable True
            dropped drop3
        drag:
            drag_name "place4"
            child "QuestElements/SecondQuest/drop.png"
            xpos 100
            ypos 880
            draggable False
            droppable True
            dropped drop4

        drag:
            drag_name "block1"
            child "QuestElements/SecondQuest/block1.png"
            xpos 800
            ypos 800
            droppable False
            dragged drag1
        drag:
            drag_name "block2"
            child "QuestElements/SecondQuest/block2.png"
            xpos 800
            ypos 70
            droppable False
            dragged drag2
        drag:
            drag_name "block3"
            child "QuestElements/SecondQuest/block3.png"
            xpos 800
            ypos 570
            droppable False
            dragged drag3
        drag:
            drag_name "block4"
            child "QuestElements/SecondQuest/block4.png"
            xpos 800
            ypos 500
            droppable False
            dragged drag4

screen epilogue:

    text "ЭПИЛОГ":
        xalign 0.5
        yalign 0.5
        size 50