# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define a = Character('소꿉친구', color="#b83939")
define b = Character('전학생', color="#ffffff")
define c = Character('선배', color="#793ac1")
define d = Character('후배', color="#f0ff1d")
define n = Character(None)
define narrator = Character(None, what_color="#00ddff")
define t = Character('선생님', color="#404040ff")

# 여기에서부터 게임이 시작합니다.
label start:
    screen set_name(question_name, hero_name):
        frame:
            xpadding 50
            ypadding 50
            xalign 0.5 yalign 0.5
            vbox:   
                spacing 20
                text question_name xalign 0.5
                input default hero_name xalign 0.5
    $ mn = renpy.call_screen("set_name",question_name=" 드디어 캐릭터 이름 입력받는다! ", hero_name="성호")

    jump day1_1
    return

