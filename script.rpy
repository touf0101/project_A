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
# 여기에서부터 게임이 시작합니다.
label start:
    screen set_name(title, init_name):
        frame:
            xpadding 50
            ypadding 50
            xalign 0.5 yalign 0.5
            vbox:   
                spacing 20
                text title xalign 0.5
                input default init_name xalign 0.5
    $ mn = renpy.call_screen("set_name",title=" 드디어 캐릭터 이름 입력받는다! ", init_name="성호")

    jump day1
    return

label day1:
    "20xx년 8월 19일 오전 6:30"
    "창문 너머로 환한 빛이 드리운다."
    "아침이다."
    "방 안에 알람이 울리기 시작한다."
    n "아잇, 내 소중한 수면시간을..."
    
    
    
    return
