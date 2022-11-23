# game_name : Adventure of Ray Debug(changed)
# game version : 4.8.2
# date : 2022-11-15(PM 04:00)

#Changes
'''
# +appended+ 추가된 것
- background music added(made by Kimdoheum[this game developer with loop pads]) -> line 22~25,616,617
- 2 easter eggs added -> line 253~265
# -deleted- 삭제된 것
- None
# 추가할 것
- ranking_board에 학번 추가하기(dict() 더 써야될듯)
- 스크롤바 선택 후 스크롤링 구현
#  others 기타
- 거의 전체 print함수 주석으로 바꿈(Ctrl+F2 -> Ctrl+/ 으로 해제)
'''

from vars import *
pg.init()           # pygame 초기화

# load music
bgm = pg.mixer.Sound("bgm.ogg")
bgm.set_volume(0.1)
nyan_cat = pg.mixer.Sound("nyan_cat(house).ogg")
nyan_cat.set_volume(0.07)

#### pygame 무한루프 : 게임 본체
def runGame():
    global done,angle,angle_lst,hit,lst_hit_pos
    global score_board,excel_file,score,runtime_sec
    global car,rd,p1
 
   
    screen.blit(rd['road'], (rd['road_x'], rd['road_y']))
    
    delay = 15

    interval = 15

    pg.key.set_repeat(delay, interval)
    while not done:
        clock.tick(60)
        screen.fill(Color)
        p1['x_lim'] = screen_width - p1['x']
        p1['y_lim'] = screen_height - p1['y']
 
        runtime_sec += 1/60 # == second
        score = runtime_sec*10 # 10 per sec
 
        ### 출돌 이벤트 ###
        car['blk2_y'],car['white1_y'],car['skul1_y'],car['yel1_y'],car['pup1_y'] = rd['road_y']-15,rd['road_y']+29,rd['road2_y']+29,rd['road3_y']-15,rd['road4_y']+29
 
        if rd['road_y'] >= screen_height:
            rd['road_y'] = -90
        if rd['road2_y'] >= screen_height:
            rd['road2_y'] = -90
        if rd['road3_y'] >= screen_height:
            rd['road3_y'] = -90
        if rd['road4_y'] >= screen_height:
            rd['road4_y'] = -90
        rd['road_y'] += rd['road_speed']  #도로 움직임(road moving)
        if score > 500:         #score 500이상일때 계속 빨라짐
            rd['road_speed'] += road_speed*0.0005

        if rd['road2_mov'] == True:
            rd['road2_y'] += rd['road_speed']
        if rd['road3_mov'] == True:
            rd['road3_y'] += rd['road_speed']
        if rd['road4_mov'] == True:
            rd['road4_y'] += rd['road_speed']
        cars_moving('car_blk1')
        cars_moving('car_white1')
        cars_moving('car_skul1')
        cars_moving('car_yel1')
        cars_moving('car_pup1')
        p1_moving()

        if rd['road_y'] >= (screen_height-150)*1/4:
            rd['road2_bool'] = True
        if rd['road_y'] >= screen_height*2/4:
            rd['road3_bool'] = True
        if rd['road_y'] >= screen_height*3/4:
            rd['road4_bool'] = True
            ##print('now4')

            ##print('now3')

            ##print('now2')
        else:
            pass
        car_name = ''
        if abs(p1['x'] - car['blk2_x']) < 30 and abs(p1['y'] - car['blk2_y']) < 30:
            #print('hit by car_blk')
            lst_hit_pos.append([car['blk2_x'],round(car['blk2_y'])])  # type: ignore
            
            del lst_hit_pos[0]
            #print(lst_hit_pos)
            #print(lst_hit_pos[0][0],lst_hit_pos[0][1])
            hit = True
            car_name = 'blk1'
            game_over()
        if abs(p1['x'] - car['white1_x']) < 30 and abs(p1['y'] - car['white1_y']) < 30:
            #print('hit by car_white')
            lst_hit_pos.append([car['white1_x'],round(car['white1_y'])])  # type: ignore
 
            del lst_hit_pos[0]
            #print(lst_hit_pos)
            hit = True
            car_name = 'white1'
            game_over()
        if abs(p1['x'] - car['skul1_x']) < 30 and abs(p1['y'] - car['skul1_y']) < 30:
            #print('hit by car_skull')
            lst_hit_pos.append([car['skul1_x'],round(car['skul1_y'])])  # type: ignore
       
            del lst_hit_pos[0]
            #print(lst_hit_pos)
            hit = True
            car_name = 'skul1'
            game_over()

        if abs(p1['x'] - car['yel1_x']) < 30 and abs(p1['y'] - car['yel1_y']) < 30:
            #print('hit by car_yell')
            lst_hit_pos.append([car['yel1_x'],round(car['yel1_y'])])  # type: ignore
       
            del lst_hit_pos[0]
            #print(lst_hit_pos)
            hit = True
            car_name = 'yel1'
            game_over()
        if abs(p1['x'] - car['pup1_x']) < 30 and abs(p1['y'] - car['pup1_y']) < 30:
            #print('hit by car_pupl')
            lst_hit_pos.append([car['pup1_x'],round(car['pup1_y'])])  # type: ignore
       
            del lst_hit_pos[0]
            #print(lst_hit_pos)
            hit = True
            car_name = 'pup1'
            game_over()

        font = pg.font.Font('GodoM.ttf',30)
        score_box = font.render(f'점수 : {str(round(score))}', True, (255,255,255))
        life_box = font.render(f'생명 : {str(p1["life"])}', True, (255,255,255))
        screen.blit(backgorund, (0, 0))
        screen.blit(rd['road'], (rd['road_x'], rd['road_y']))
        road_func(2)
        road_func(3)
        road_func(4)
        screen.blit(p1['p1'], (p1['x'], p1['y']))

        if rd['road4_bool'] == False:  ### 무적효과 ### invincible effect
            p1['ef_time'] += 0.1 # +6/sec
            if p1['ef_time'] < 50:
                if p1['ef_time'] %3 < 0.7:
                    screen.blit(p1['ef1'], (p1['x'], p1['y']))
            if 50 <= p1['ef_time'] < 80:
                if p1['ef_time'] %3 < 1:
                    screen.blit(p1['ef1'], (p1['x'], p1['y']))
            if p1['ef_time'] >= 80 and p1['ef_time'] %3 < 1.2:
                screen.blit(p1['ef2'], (p1['x'], p1['y']))
 
        screen.blit(car['blk2'], (car['blk2_x'], rd['road_y']-15))
        screen.blit(car['white1'], (car['white1_x'], rd['road_y']+29))
        create_effect(car_name)
        screen.blit(score_box, (10,10))
        screen.blit(life_box, (10,50))
        if rd['road2_mov'] == True:
            screen.blit(car['skul1'], (car['skul1_x'], rd['road2_y']+29))
        if rd['road3_mov'] == True:
            screen.blit(car['yel1'], (car['yel1_x'], rd['road3_y']-15))
        if rd['road4_mov'] == True:
            screen.blit(car['pup1'], (car['pup1_x'], rd['road4_y']+29))
       
        pg.display.update()   # 게임 화면 업데이트


def p1_moving():
    global p1,rd,car,pg
    global easter1,score
    spd = 1.5
    if score > 600:
        spd += spd*0.00003
    try:
        for event in pg.event.get():
            
            if event.type == pg.QUIT:   # 게임 화면 종료
                done = True
                game_over()
                #print('score:',score,'t:',round(runtime_sec))
            
            if event.type == pg.KEYDOWN:    #아무키나 눌렀을 때
                p1['key_pressed'] = True

                if event.key == pg.K_w and p1['y_lim'] <= screen_height-15:                ### 더블유 ### 키
                    p1['y'] -= spd
                    angle_lst.append(0)    #angle이 바꼈을때만 동작하게
                    del angle_lst[0] 
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_s and p1['y_lim'] > 60:                ### SSS ### 키
                    p1['y'] += spd
                    angle_lst.append(180) #angle이 바꼈을때만 동작하게
                    del angle_lst[0]
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_d and p1['x_lim'] > 60:                ### DDD ### 키
                    p1['x'] += spd
                    angle_lst.append(270) #angle이 바꼈을때만 동작하게
                    del angle_lst[0]
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_a and p1['x_lim'] <= screen_width-5:                ### AAA ### 키
                    p1['x'] -= spd
                    angle_lst.append(90) #angle이 바꼈을때만 동작하게
                    del angle_lst[0]
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])  
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_u and p1['y_lim'] > 30:  #s키
                    p1['y'] += 100
                    angle_lst.append(180) #angle이 바꼈을때만 동작하게
                    del angle_lst[0]
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])  
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_y and p1['x_lim'] > 60:                ### DDD ### 키
                    p1['x'] += 200
                    angle_lst.append(270) #angle이 바꼈을때만 동작하게
                    del angle_lst[0]
                    p1['p1'] = pg.transform.rotate(p1['p1'], angle_lst[-1] - angle_lst[-2])
                    #print('-'*30)
                    #print('x:',p1['x'],'| y:',p1['y'])
                    #print(angle_lst)
                    #print('SpinValue:',angle_lst[-1] - angle_lst[-2])
                    #print('-'*30+'\n')
                if event.key == pg.K_j:     #easter egg1
                    p1['easter1_time'] += 1
                    print(p1['easter1_time'])
                    if 30 < p1['easter1_time'] < score/5:
                        p1['p1'] = p1['easter1']
                    else:
                        p1['p1'] = player1
                if event.key == pg.K_f:
                    print(round(score))
                    if 400 < score < 800 and p1['music'] != 'nyan_cat':
                        bgm.stop()
                        p1['music'] = 'nyan_cat'
                        nyan_cat.play(-1)
            else:
                p1['key_time'] += 0.1
                if p1['key_time'] > 10:
                    p1['key_time'] = 0
                    p1['key_pressed'] = False  ############
        
    finally:
        # if p1['key_pressed'] == False:
        #     #print('a')
        #     p1_moving()
        # #print()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                #print('aaaa',end = '|')
                break
            else:
                p1_moving()

def cars_moving(car_name):  #rotating and moving cars
    global car
   
    ## blk1 ##
    if car_name == 'car_blk1':  #car_blk1's code
        if car['blk2_rot'] == 'R':
            car['blk2_x'] += car['blk2_spd']
            if car['blk2_x'] > screen_width-90.2:
                car['blk2_rot'] = 'L'
                car['blk2'] = pg.transform.rotate(car['blk2'], 180)
                if car['blk2_spd'] > 25:  #spd limit
                    car['blk2_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('blk',car['blk2_spd'])
                elif car['blk2_spd'] < 3:
                    car['blk2_spd'] += 3
                else:
                    car['blk2_spd'] += randrange(-1,3)
                    #print('blk',car['blk2_spd'])
 
        elif car['blk2_rot'] == 'L':
            car['blk2_x'] -= car['blk2_spd']
            if car['blk2_x'] <0:
                car['blk2_rot'] = 'R'
                car['blk2'] = pg.transform.rotate(car['blk2'], 180)
                if car['blk2_spd'] > 25:  #spd limit
                    car['blk2_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('blk',car['blk2_spd'])
                elif car['blk2_spd'] < 3:
                    car['blk2_spd'] += 3
                else:
                    car['blk2_spd'] += randrange(-1,3)
                    #print('blk',car['blk2_spd'])
             
    ## white1 ##      
    elif car_name == 'car_white1':  
        if car['white1_rot'] == 'R': # direction == >(오른쪽)
            car['white1_x'] += car['white1_spd']
            if car['white1_x'] > screen_width-90.2:
                car['white1_rot'] = 'L'
                car['white1'] = pg.transform.rotate(car['white1'], 180)
                if car['white1_spd'] > 20:  #spd limit
                    car['white1_spd'] -= randrange(4,10)  #높을수록 느려짐
                    #print('흰',car['white1_spd'])
                elif car['white1_spd'] < 3:
                    car['white1_spd'] += 3
                else:
                    car['white1_spd'] += randrange(-1,3)
                    #print('흰',car['white1_spd'])
 
        elif car['white1_rot'] == 'L':
            car['white1_x'] -= car['white1_spd']
            if car['white1_x'] <0:
                car['white1_rot'] = 'R'
                car['white1'] = pg.transform.rotate(car['white1'], 180)
                if car['white1_spd'] > 20:  #spd limit
                    car['white1_spd'] -= randrange(4,10)  #높을수록 느려짐
                    #print('흰',car['white1_spd'])
                elif car['white1_spd'] < 3:
                    car['white1_spd'] += 3
                else:
                    car['white1_spd'] += randrange(-1,3)
                    #print('흰',car['white1_spd'])
 
    ## skul1 ##
    elif car_name == 'car_skul1':  
        if car['skul1_rot'] == 'R': #direction == >
            car['skul1_x'] += car['skul1_spd']
            if car['skul1_x'] > screen_width-90.2:
                car['skul1_rot'] = 'L'
                car['skul1'] = pg.transform.rotate(car['skul1'], 180)
                if car['skul1_spd'] > 33:  #spd limit
                    car['skul1_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('skul',car['skul1_spd'])
                elif car['skul1_spd'] < 3:
                    car['skul1_spd'] += 3
                else:
                    car['skul1_spd'] += randrange(-1,4)
                    #print('skul',car['skul1_spd'])
 
        elif car['skul1_rot'] == 'L':
            car['skul1_x'] -= car['skul1_spd']
            if car['skul1_x'] <0:
                car['skul1_rot'] = 'R'
                car['skul1'] = pg.transform.rotate(car['skul1'], 180)
                if car['skul1_spd'] > 33:  #spd limit
                    car['skul1_spd'] -= randrange(1,10)  #높을수록 느려짐
                    #print('skul',car['skul1_spd'])
                elif car['skul1_spd'] < 3:
                    car['skul1_spd'] += 3
                else:
                    car['skul1_spd'] += randrange(-1,4)
                    #print('skul',car['skul1_spd'])
 
    ### yel1 ###
    
    elif car_name == 'car_yel1':  #car_yel1's code
        if car['yel1_rot'] == 'R':
            car['yel1_x'] += car['yel1_spd']
            if car['yel1_x'] > screen_width-90.2:
                car['yel1_rot'] = 'L'
                car['yel1'] = pg.transform.rotate(car['yel1'], 180)
                if car['yel1_spd'] > 20:  #spd limit
                    car['yel1_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('yel',car['yel1_spd'])
                elif car['yel1_spd'] < 3:
                    car['yel1_spd'] += 3
                else:
                    car['yel1_spd'] += randrange(-1,3)
                    #print('yel',car['yel1_spd'])
 
        elif car['yel1_rot'] == 'L':
            car['yel1_x'] -= car['yel1_spd']
            if car['yel1_x'] <0:
                car['yel1_rot'] = 'R'
                car['yel1'] = pg.transform.rotate(car['yel1'], 180)
                if car['yel1_spd'] > 20:  #spd limit
                    car['yel1_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('yel',car['yel1_spd'])
                elif car['yel1_spd'] < 3:
                    car['yel1_spd'] += 3
                else:
                    car['yel1_spd'] += randrange(-1,3)
                    #print('yel',car['yel1_spd'])
    ### pup1 ###
    
    elif car_name == 'car_pup1':  #car_pup1's code
        if car['pup1_rot'] == 'R':
            car['pup1_x'] += car['pup1_spd']
            if car['pup1_x'] > screen_width-90.2:
                car['pup1_rot'] = 'L'
                car['pup1'] = pg.transform.rotate(car['pup1'], 180)
                if car['pup1_spd'] > 20:  #spd limit
                    car['pup1_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('pup',car['pup1_spd'])
                elif car['pup1_spd'] < 3:
                    car['pup1_spd'] += 3
                else:
                    car['pup1_spd'] += randrange(-1,3)
                    #print('pup',car['pup1_spd'])

        elif car['pup1_rot'] == 'L':
            car['pup1_x'] -= car['pup1_spd']
            if car['pup1_x'] <0:
                car['pup1_rot'] = 'R'
                car['pup1'] = pg.transform.rotate(car['pup1'], 180)
                if car['pup1_spd'] > 20:  #spd limit
                    car['pup1_spd'] -= randrange(3,10)  #높을수록 느려짐
                    #print('pup',car['pup1_spd'])
                elif car['pup1_spd'] < 3:
                    car['pup1_spd'] += 3
                else:
                    car['pup1_spd'] += randrange(-1,3)
                    #print('pup',car['pup1_spd'])

def road_func(num):
    global rd
    if num == 2:
        if rd['road2_bool'] == True:
            rd['road2_mov'] = True
            return screen.blit(rd['road2'], (rd['road2_x'], rd['road2_y']))
           
    elif num == 3:
        if rd['road3_bool'] == True:
            rd['road3_mov'] = True
            return screen.blit(rd['road3'], (rd['road3_x'], rd['road3_y']))
    elif num == 4:
        if rd['road4_bool'] == True:
            rd['road4_mov'] = True
            return screen.blit(rd['road4'], (rd['road4_x'], rd['road4_y']))
 
 
def edit_excel():
    global score, score_board,excel_file,user_name,user_id
    attempt = str(score_board['A2'].value)  # type: ignore
    score = round(score)
    #print(attempt)
    try_score = 'B'+attempt
    try_name = 'C'+attempt
    try_id = 'D'+attempt
    #write score, name and id in excel file
    score_board[try_score].value = (score)  # type: ignore
    score_board[try_name].value = (user_name)  # type: ignore
    score_board[try_id].value = (user_id)  # type: ignore
    score_board['A2'].value += 1  # type: ignore
    excel_file.save("C:/Users/owner/Downloads/score_board.xlsx")
    #다른 사람 점수 보여주는 코드, 함수로 구현해도 괜찮을듯
 
 
def create_effect(a):
    global lst_hit_pos,effect,hit,score,runtime_sec
    global p1
       
    if a != '':
        #print('엄')
        effect_x = (lst_hit_pos[0][0] + p1['x'])/2  # type: ignore
        effect_y = (lst_hit_pos[0][1] + p1['y'])/2 - 10  # type: ignore
        #tkinter실행하는 코드
        # score = round(score)
        # edit_excel(True)
        # #print('score:',score,'t:',round(time_sec))    #tkinter실행시 같이 실행될 코드들
        hit = False
        return screen.blit(effect,(effect_x,effect_y))

####    Game Over Window   ####

def minus_hp():
    global p1,rd
    global screen_height
    p1['x'],p1['y'] = 500,640
    rd['road_x'],rd['road2_x'],rd['road3_x'],rd['road4_x'] = 0,0,0,0
    rd['road_y'],rd['road2_y'],rd['road3_y'],rd['road4_y'] = -90,-90-(screen_height*1/4),-90-(screen_height*2/4),-90-(screen_height*3/4)

def game_over():
    global done, Tk,p1,rd,ranking_board
    if rd['road4_bool'] == True:
        p1['life'] -= 1
        minus_hp()
    else:
        pass
    if p1['life'] == 0:
    #if done == True:
        pg.quit()
        win_end = Tk()
        win_end.geometry('550x400')
        win_end.title('이름입력창(점수 기록용)')
        win_end.option_add('*Font', '맑은고딕 25')
        win_end.config(bg='white') # 백그라운드 색상
        #win_end.resizable(False, False)
        frame1 = tkinter.Frame(win_end,bd=2,relief="solid",width=10)
        frame2 = tkinter.Frame(win_end,bd=2,relief="solid",width=200)
        name = tkinter.Entry(frame1,width=10)
        instruction = tkinter.Label(frame1,font='godoM 10',text='반 번호 이름을 입력해주세요 \n ex) 10101홍길동\n 입력을 다하셨다면 ENTER키를 눌러주세요 ')
        scrollbar=ttk.Scrollbar(frame2)
        ranking_board = tkinter.Text(frame2,yscrollcommand = scrollbar.set,font='godoM 15',bd=2,borderwidth=2)
        scrollbar["command"]=ranking_board.yview
        #ranking_board.config(state='disabled')
        ranking_board.insert(1.0,'==========')
        ranking_board.insert(1.1,'이름\t점수\n')
        ranking_board.insert(1.2,'제발되라고')
        # ,expand=True,fill="both"
        frame1.pack(side='left',expand=True,fill="both")
        frame2.pack(side='right',expand=True,fill="both")
        scrollbar.pack(side="right", fill="y")
        #ranking_board.pack(fill='both',expand=True)
        name.pack(pady=70)
        instruction.pack()
        
        #label_score_board=tkinter.Label(win_end, text='', width=10, height=10, bd=0,relief="solid")
        #label_score_board.pack()
       
        # def scrolling(event):
        #     pass

        def key_event(k):
            global key,user_id,user_name,score_board
            global read_score,read_name,read_id,read_all,read_name_plus_id,ranking_board,sorted_score
            
            key = k.keysym
            if key == 'Return':  #if ENTER key pressed
                try:
                    lst = ['','']
                    for i in name.get(): 
                        if 48 <= ord(str(i)) <= 57:  #numbers
                            lst[0] += (str(i))
                        elif ord(str(i)) == 32:  #blank
                            pass
                        else:  #strings
                            lst[1] += (i)
                    #scrollbar.bind("<B1-Motion>",scrolling)
                    #print(lst)
                    #print(key)
                    user_id = int(lst[0])
                    user_name = lst[1]
                    #print(user_id,user_name,type(user_id))
                    edit_excel()
                    for i in range(2,score_board['A2'].value):  # type: ignore      #2~시도횟수
                        read_score.append(score_board['B'+str(i)])  # type: ignore  #append at cell[Bi](i == 2~시도횟수)
                        read_name.append(score_board['C'+str(i)])  # type: ignore   #append at cell[Ci]
                        read_id.append(score_board['D'+str(i)])  # type: ignore     #append at cell[Di]셀 Di에 추가
                        read_all.append([read_score[i-2].value,read_name[i-2].value,read_id[i-2].value])
                        read_score[i-2] = str(read_score[i-2].value)+'\n'
                        read_name[i-2] = read_name[i-2].value
                        read_id[i-2] = read_id[i-2].value
                        read_name_plus_id.append(str(read_id[i-2])+read_name[i-2])   
                        ranking_board = tkinter.Text(frame2,yscrollcommand = scrollbar.set,height = 5, width = 52,font='godoM 15',bd=2)
                    
                    sorted_score = list()
                    nameNscore = dict()
                    for i in range(len(read_all)):
                        sorted_score.append(read_all[i][0])
                    for i in range(len(read_all)):
                        nameNscore.setdefault(read_all[i][1],read_all[i][0])
                    lst_sorted = sorted(nameNscore.items(), key=itemgetter(1),reverse=True)
                    
                    ### DEBUG ###
                    # print('='*175)
                    # print('read_all:', read_all,'\n')
                    # print('nameNscore:', nameNscore,'\n')
                    # print('lst_sorted:', lst_sorted,'\n')
                    # #print('lst_new:', lst_new)
                    # print('='*175)
                    # print('*'*15)
                    # print('이름','\t','점수')

                    ranking_board.insert('end','이름\t점수\t등수\n')  # type: ignore    # initial value #

                    a = 1
                    for i in lst_sorted:        ## ranking show code ##
                        print(i[0],'\t',i[1])
                        ranking_board.insert('end',f'{i[0]}\t{str(i[1])}\t{a}\n')  # type: ignore
                        
                        a += 1
                    print('*'*15)
                    ranking_board.config(state='disabled')  # type: ignore
                    ranking_board.pack(side='right',fill='both',expand=True)  # type: ignore
                except:
                    #print('잘못된 입력입니다')     ##DEBUG##
                    name.delete(0,END)
                    name.insert(END,'잘못된 입력!')
 
        win_end.bind("<KeyRelease>",key_event)
        win_end.mainloop()

####    Game Start Window   ####

def start_btn_pressed():
    global screen_width,screen_height,screen,backgorund,p1
    win_start.withdraw()
    screen_width,screen_height = 1080,780
    screen = pg.display.set_mode((screen_width,screen_height))
    backgorund = pg.image.load('bg.png')
    backgorund = pg.transform.scale(backgorund,(screen_width,screen_height))
    bgm.play(-1)   #bg_music start
    p1['music'] = 'bgm'
    runGame()

def story_btn_pressed():
    global instruction2,story,story_btn_click,txt
    instruction2.config(state='normal')     # allow editing of text
    ##print(story)        #DEBUG
    if story_btn_click == False:
        instruction2.delete('1.0',END)      #del all text
        instruction2.insert(END,story)      #set text as story
        story_btn_click = True
    else:
        instruction2.delete('1.0',END)      #del all text
        instruction2.insert(END,txt)        #reset text
        story_btn_click = False
    instruction2.config(state='disabled')   # Do not allow editing of text

win_start = Tk()
win_start.geometry('400x300')
win_start.title('Adventure of Ray Debug')
win_start.iconbitmap(r'icon.ico')
win_start.option_add('*Font', 'godoM 15')
win_start.config(bg='white') # 백그라운드 색상
win_start.resizable(False, False)
frame1 = tkinter.Frame(win_start,relief='solid',bd=2)
frame2 = tkinter.Frame(win_start,relief='solid',bd=2)
scrollbar = ttk.Scrollbar(frame1)
instruction2 = tkinter.Text(frame1,yscrollcommand = scrollbar.set,height = 5, width = 52,font='godoM 15',bd=2)
start_btn = tkinter.Button(frame2, text='게임 시작!',command = lambda:start_btn_pressed(),bg='#6390f2',fg='#f2f2f2')
story_btn = tkinter.Button(frame2, text='차 스토리 보기',command = lambda:story_btn_pressed(),bg='#11BB11',fg='#FCFCFC')
scrollbar["command"]=instruction2.yview

um = '\t    ###조작방법###\nWASD를 눌러 캐릭터를 조작 하세요\n\n\t    ###게임방법###\n움직이는 차들을 피해 도로를 건너십시오 차와 부딪히면 생명이 줄어들고, 생명이 모두 소진되면 게임은 끝이 납니다.\n\n\n\t            made by: 김도흠, 황은섭'
 
frame1.pack(side='top', fill='both', expand=True)
frame2.pack(side='bottom')
scrollbar.pack(side="right", fill="y")
instruction2.pack(fill='both',expand=True)
instruction2.insert(END,txt)

instruction2.config(state='disabled')
start_btn.pack(side='left')
story_btn.pack(side='right')

win_start.mainloop()

pg.quit()