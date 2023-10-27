# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image bg room = "bga/he_room.bmp"
image bg school_twi = "bga/school_fun_twi.bmp"
image bg school_shoes = "bga/school_sho_day.bmp"
image bg street_t = "bga/street_t.bmp"
image bg street_flows = "bga/street_flo.bmp"
image bg school_front = "bga/school_fro.bmp"
image bg home_front = "bga/home_fro.bmp"
image bg home_in = "bga/home_in.bmp"
image bg conbini = "bga/conbini.bmp"
image bg twilight = "bga/twilight.bmp"
image bg past_school = "bga/past_school.bmp"
image bg school_artroom = "bga/school_art.bmp"
image bg school_hall = "bga/school_hall.bmp"
image bg school_library = "bga/school_lib.bmp"
image bg school_healthroom = "bga/school_heal.bmp"
image bg school_classroom = "bga/school_room.bmp"
image bg school_stairs = "bga/school_sta.bmp"
image bg school_roof_twi = "bga/school_top.bmp"
image bg school_roof_twi_2 = "bga/school_top_2.bmp"
image bg school_roof_door = "bga/school_top_door.bmp"
image bg street_tt = "bga/street_tt.bmp"
image bg school_room_front = "bga/school_room_2.bmp"
image bg black = "bga/black.png"
image bg school_pri = "bga/school_pri.bmp"
image bg school_market = "bga/school_mar.bmp"
image bg school_com = "bga/school_com.bmp"


image char_a = im.FactorScale("char/a.png", 0.33)
image char_b = im.FactorScale("char/b.png", 0.33)
image char_c = im.FactorScale("char/c.png", 0.33)
image char_d = im.FactorScale("char/d.png", 0.33)


define audio.alarm = "effect/alarm_clock.mp3"
define audio.heart_beat = "effect/heart_beat.mp3"
define audio.school_bell = "effect/school_bell.mp3"
define audio.chair = "effect/slide_chair.mp3"
define audio.door_close = "effect/slide_door_close.mp3"
define audio.door_open = "effect/slide_door_open.mp3"


define audio.bgm_1 = "bgm/After Merienda.mp3"
define audio.bgm_2 = "bgm/Coffee Shop in Yume.mp3"
define audio.bgm_3 = "bgm/Our home.mp3"
define audio.bgm_4 = "bgm/Rainy day Traumerei.mp3"
define audio.bgm_5 = "bgm/Snow hertz.mp3"
define audio.bgm_6 = "bgm/Tea time in the sunshine.mp3"
define audio.bgm_7 = "bgm/Toroime Diary.mp3"
define audio.bgm_8 = "bgm/Welcome to Traume.mp3"
define audio.bgm_9 = "bgm/YU.ME.NO!.mp3"
define audio.bgm_10 = "bgm/Yuno Atelier.mp3"


# 게임에서 사용할 캐릭터를 정의합니다.
define n = Character("mn", dynamic = True, color="#ffffff")
define a = Character('유이', color="#fa7e7e")
define b = Character('이솔', color="#2f6be2")
define c = Character('가온', color="#fa6dee")
define d = Character('모람', color="#f0ff1d")
define narrator = Character(None, what_color="#00ddff")
define t = Character('선생님', color="#999999")
define m = Character(None, what_color="#ff0000")

# 여기에서부터 게임이 시작합니다.
label start:
    stop music fadeout 1.0


    screen set_name(question_name, hero_name):
        frame:
            xpadding 50
            ypadding 50
            xalign 0.5 yalign 0.5

            vbox:   
                spacing 20
                text question_name xalign 0.5
                input default hero_name xalign 0.5

    $ mn = renpy.call_screen("set_name", question_name="당신의 이름은?", hero_name="성호")

    
    with Dissolve(.5)
    
    jump day1_1

    return

