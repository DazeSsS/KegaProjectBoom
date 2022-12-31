# константы
define NOTICE = "это в дальнейшем отразится на сюжете"

# персонажи
define s = Character('Саша', color="#5e9cff", image="sanya")
define t = Character('Екатерина Петровна', color="#eca625", image="teacher")
define d = Character('Дима', color="#0fdcf3", image="dima")
define i = Character('Умный помощник', color="#7efd7a")
define m = Character('Мама', color="#f95858")
define e0 = Character('Ассистентка', color="#ecff59")
define e = Character('Ева', color="#ecff59")
define ml = Character('$!&^%*@#?', color="#ff0000")
define k1 = Character('@^#$%*&', color="#c291fd")
define k2 = Character('%!#$@&', color="#b2f9db")
define v = Character('Влад', color="#ffe47a")
define c = Character('Посетитель', color="#ff3636")
define c1 = Character('Денис Нечипоренко', color="#ff3636")

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
image dima glitched:
    At("dima", glitch)
    pause 0.8
    At("dima", chromatic_offset)
    pause 0.5
    At("dima", glitch)
    pause 0.3
    At("dima", chromatic_offset)
    pause 0.2
    repeat

image man glitched:
    At("man", glitch)
    pause 0.8
    At("man", chromatic_offset)
    pause 0.5
    At("man", glitch)
    pause 0.3
    At("man", chromatic_offset)
    pause 0.2
    repeat

image woman glitched:
    At("woman", glitch)
    pause 0.6
    At("woman", chromatic_offset)
    pause 0.7
    At("woman", glitch)
    pause 0.4
    At("woman", chromatic_offset)
    pause 0.2
    repeat

# положения персонажей
init:
    $ left2 = Position(xalign = 0.15, yalign = 1.0)
    $ right2 = Position(xalign = 0.85, yalign = 1.0)
    $ right3 = Position(xalign = 1.0, yalign = 1.0)