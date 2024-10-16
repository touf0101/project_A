init python:
    health=0
    humor=0
    charisma=0
    wisdom=0
    mental=0

    money=0
    tired=0

init:
    screen imagemap_test:
        imagemap:
            auto 'imagemap_%s.png'
            hotspot (166, 153, 354, 202) action Show('detail_rest')
            hotspot (182, 459, 356, 203) action Show('detail_study')
            hotspot (761, 147, 356, 203) action Show('detail_store')
            hotspot (785, 462, 357, 206) action Show('detail_talk')
            hotspot (1330, 313, 357, 202) action Show('detail_play')

    screen detail_rest:
        frame:
            align (0.5,0.5)
            vbox:
                textbutton '숏폼보기' action [Hide('detail_rest'), Return('shot')]
                textbutton '잠자기' action  [Hide('detail_rest'), Return('rest')]
    screen detail_store:
        frame:
            align (0.5,0.5)
            vbox:
                textbutton '야끼소바빵' action  [Hide('detail_store'), Return('bread')]
                textbutton '녹차마루' action [Hide('detail_store'), Return('ice')]
    screen detail_study:
        frame:
            align (0.5,0.5)
            vbox:
                textbutton '복습' action  [Hide('detail_study'), Return('studied')]
                textbutton '예습' action [Hide('detail_study'), Return('studying')]
    screen detail_talk:
        frame:
            align (0.5,0.5)
            vbox:
                textbutton '망상하기' action  [Hide('detail_talk'), Return('self')]
                textbutton '친구와 대화하기' action [Hide('detail_talk'), Return('friend')]
    screen detail_play:
        frame:
            align (0.5,0.5)
            vbox:
                textbutton '축구' action  [Hide('detail_play'), Return('soccer')]
                textbutton '판치기' action [Hide('detail_play'), Return('game')]
    screen check:
        frame:
            align (0.5, 0.5)
            vbox:
                text '스탯이 올랐습니다.'
                textbutton '확인' action Return()

label imagemap:
    $ task=0
    while task<2:
        call screen imagemap_test
        
        if _return is 'rest':
            '쉬었다'
            $ task+=1
        elif _return is 'store':
            '먹었다'
            $ task+=1
        elif _return is 'study':
            '복습했다'
            $ task+=1
        elif _return is 'talk':
            '망상했다'
            $ task+=1
        elif _return is 'paly':
            '게임했다'
            $ task+=1
    call screen check
    return

