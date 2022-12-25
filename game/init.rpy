# константы
define NOTICE = "это в дальнейшем отразится на сюжете"

# персонажи
define s = Character('Саша', color="#5e9cff", image="sanya")
define t = Character('Екатерина Петровна', color="#eca625", image="teacher")
define d = Character('Дима', color="#0fdcf3", image="dima")
define i = Character('Умный помощник', color="#a8e1ff")
define m = Character('Мама', color="#f95858")
define e = Character('Ева', color="#ecff59")

# переменные
define intellect = 0
define charisma = 0
define bad_point = 0
define funny_jokes = 0
define empty = 0
define task_solved = False
define first_try = True
define school_info = True

# спрайты
image teacher glitched:
    At("teacher", glitch)
    pause 0.2
    At("teacher", chromatic_offset)
    pause 0.2
    At("teacher", glitch)
    pause 0.3
    At("teacher", chromatic_offset)
    pause 0.1
    At("teacher", glitch)
    pause 0.3
    repeat

# положения персонажей
init:
    $ left2 = Position(xalign = 0.05, yalign = 1.0)
    $ right2 = Position(xalign = 0.95, yalign = 1.0)