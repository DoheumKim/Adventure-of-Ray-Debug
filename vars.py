# filename : vars.py
# module version : 4.8.1~4.8.2
# date : 2022-11-15(AM 12:00)
 
#Changes
'''
# +appended+ 추가된 것
- easter egg added -> line 102~104
- codes in main >> background music added(made by Kimdoheum[this game developer with looppad])
# -deleted- 삭제된 것
None
#  others 기타
- organized variables using 
'''
import pygame as pg  
from random import randrange   #차 속도 랜덤하게 바꾸려고
from openpyxl import *  # type: ignore   #엑셀파일 불러오고 쓰고 다하는거
import tkinter
from tkinter import ttk    #시작창, 종료창 만드는 거
from tkinter import *  # type: ignore
from time import sleep  #안씀
from operator import itemgetter  #스코어 표시할때 쓸 거
if __name__ == '__main__':   #모듈을 실행했다고 알려주는 거
    print('\n!This is module!\n')
    pg.quit()
# BackGround Settings
pg.display.set_caption('Adventure of Ray Debug')  #제목 설정
pg.display.set_icon(pg.image.load('icon.png'))    #외부 파일 불러와서 아이콘으로 설정
#Color: tuple = (255, 255, 255)  # 하얀색(White)
screen_width:int = 1080   #창 크기
screen_height:int = 780   #창 크기
screen = pg.display.set_mode((screen_width,screen_height))
done: bool = False
clock = pg.time.Clock()
backgorund = pg.image.load('bg.png')   #외부 파일 불러와서 변수에 저장
backgorund = pg.transform.scale(backgorund,(screen_width,screen_height))   #background변수를 배경으로 설정
score,runtime_sec,road_speed = 0, 0, 0.7    #점수, 실행시간, 도로속도
excel_file = load_workbook("C:/Users/owner/Downloads/score_board.xlsx",data_only=True)   #엑셀 파일 불러오기(나중에 수정도 함)
score_board = excel_file['Sheet1']   #불러온 엑셀파일의 시트(Sheet1)
hit:bool = False    #캐릭터가 차랑 부딪혔는지 확인하기 위한 변수
cur_music = ''   #현재 재생중인 배경음악
 
# Objects' Settings
    ## Roads' ##
road2_bool,road3_bool,road4_bool = False,False,False    # 도로 나타나는 시간 설정(예시: road2_bool == True면 road2 나타남)
road2_mov,road3_mov,road4_mov = False,False,False
road_x,road2_x,road3_x,road4_x = 0,0,0,0
road_y,road2_y,road3_y,road4_y = -90,-90,-90,-90   ## Pos value 
road_scale:tuple = (1080,100)    #도로 크기 정의
road1,road2,road3,road4 =\
pg.image.load('road.png'),\
pg.image.load('road2.png'),\
pg.image.load('road3.png'),\
pg.image.load('road4.png')
# 사진파일 불러와서 변수에 저장
road1,road2,road3,road4 =\
pg.transform.scale(road1,road_scale),\
pg.transform.scale(road2,road_scale),\
pg.transform.scale(road3,road_scale),\
pg.transform.scale(road4,road_scale)
#road1,road2등의 변수로 오브젝트 생성
    ## Cars' ##
car_blk2,car_white1,car_skul1,car_yel1,car_pup1 =\
pg.image.load('car_blk2.png'),\
pg.image.load('car_white1.png'),\
pg.image.load('car_skul1.png'),\
pg.image.load('car_yel1.png'),\
pg.image.load('car_pup1.png')
# 외부 파일 불러와서 변수에 저장
car_blk2,car_white1,car_skul1,car_yel1,car_pup1 =\
pg.transform.rotate(car_blk2, -45),\
pg.transform.rotate(car_white1, 135),\
pg.transform.rotate(car_skul1, 135),\
pg.transform.rotate(car_yel1, -45),\
pg.transform.rotate(car_pup1, 45)
 # 자동차 오브젝트의 방향 설정
car_blk2,car_white1,car_skul1,car_yel1,car_pup1 =\
pg.transform.scale(car_blk2,(105,85)),\
pg.transform.scale(car_white1,(105,85)),\
pg.transform.scale(car_skul1,(105,85)),\
pg.transform.scale(car_yel1,(105,85)),\
pg.transform.scale(car_pup1,(105,85))
# 자동차 오브젝트(.png파일임)의 크기 설정
car_blk2_x,car_white1_x,car_skul1_x,car_yel1_x,car_pup1_x = 0,1080,0,0,0   ### 좌표값(position value)
car_blk2_rot,car_white1_rot,car_skul1_rot,car_yel1_rot,car_pup1_rot = 'R','L','L','R','L'  ### 회전값(rotation value)
spd = randrange(3,5)  
blk2_spd,white1_spd,skul1_spd,yel1_spd,pup1_spd = spd,spd,spd,spd+1,spd+1    ### Speed  #자동차들의 스피드 초기값 정의
    # Player's
player1 = pg.image.load('modang.png')  #이미지 불러와서 변수에 저장(실제 움직이는 캐릭터임)
player1 = pg.transform.scale(player1,(50,50)) #사진크기 조정
mu_juck_efct1 = pg.image.load('mu_juck_efct1.png')#이미지 불러와서 변수에 저장 -> 무적 효과 표현을 위함
mu_juck_efct1 = pg.transform.scale(mu_juck_efct1,(50,50))
mu_juck_efct2 = pg.image.load('mu_juck_efct2.png')#이미지 불러와서 변수에 저장 -> 무적 효과 표현을 위함
mu_juck_efct2 = pg.transform.scale(mu_juck_efct2,(50,50))
playe1_x,player1_y = 500,640  #Pos value
    # EasterEgg
easter1 = pg.image.load('easter.png')
easter1 = pg.transform.scale(easter1,(50,50))   #이스터에그
easter1_time:int = 0
# Objects
effect = pg.image.load('spark.png')    #충돌 이펙트
effect = pg.transform.scale(effect,(40,40))
lst_hit_pos = [0]   #충돌위치
angle = 0   #플레이어의 방향
angle_lst = [0,0]
p1 =\
{'p1':player1,'x':playe1_x,'y':player1_y,'life':3,'music':cur_music,
'ef_time':0,'ef1':mu_juck_efct1,'ef2':mu_juck_efct2,'key_time':0,
'x_lim':0,'y_lim':0,'key_pressed':False,'easter1':easter1,'easter1_time':easter1_time}
#플레이어 및 이스터에그 관련
car =\
{'blk2':car_blk2,'white1':car_white1,'skul1':car_skul1,'yel1':car_yel1,'pup1':car_pup1,
'blk2_x':0,'white1_x':screen_width,'skul1_x':0,'yel1_x':0,'pup1_x':0,
'blk2_rot':car_blk2_rot,'white1_rot':car_white1_rot,'skul1_rot':car_skul1_rot,'yel1_rot':car_yel1_rot,'pup1_rot':car_pup1_rot,
'blk2_spd':blk2_spd,'white1_spd':white1_spd,'skul1_spd':skul1_spd,'yel1_spd':yel1_spd,'pup1_spd':pup1_spd}
#자동차 관련
rd =\
{'road':road1,'road2':road2,'road3':road3,'road4':road4,
'road_x':road_x,'road2_x':road2_x,'road3_x':road3_x,'road4_x':road4_x,
'road_y':road_y,'road2_y':road2_y,'road3_y':road3_y,'road4_y':road4_y,
'road2_bool':road2_bool,'road3_bool':road3_bool,'road4_bool':road4_bool,
'road2_mov':road2_mov,'road3_mov':road3_mov,'road4_mov':road4_mov,
'road_speed':road_speed,'road_scale':road_scale}
#도로 관련
 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
'''                                                                                        Game Start & Over Window                                                                                         '''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
 
#Changes
'''
# +appended+ 추가된 것
- um,um2,txt,dev_names,story
- story_btn_pressed
- read_.
- ranking_board
# -deleted- 삭제된 것
- None
#  others 기타
-
'''
key = 0  #누른 키
user_id = int() 
user_name = ''
story_btn_click = False
um = '\t    ###조작방법###\nWASD를 눌러 캐릭터를 조작 하세요\
\n\n\t    ###게임방법###\n움직이는 차들을 피해 도로를 건너십시오 차와 부딪히면 생명이 줄어들고, 생명이 모두 소진되면 게임은 끝이 납니다.\n\n'
um2 = '게임시작 후 4번째 도로가 나타날 때까지 무적효과가 적용됩니다. 노란색 이펙트로 확인할 수 있습니다.\n\n'
dev_names = '\t            made by: 김도흠, 황은섭'
txt = um+um2+dev_names #게임 시작창에서 나오는 텍스트
story = '\t###자동차 스토리###\n\
흰차 : 편돌이가 영끌해서 산 중고 K5입니다. 많이 타서 그런지 느려 터졌습니다!\n\n\
검은차 : 7년차 직장인 아저씨가 큰맘 먹고 산 신형 sm6입니다. 새거라 그런지 빠르네요!\n\n\
빨간차 : 극한의 컨셉충이 해골을 차 보닛에다 박았어요! 폭주족 컨셉인가요?\n\n\
노란차 : 람보르기니 아벤타도르입니다! 연비를 버리고 속도를 얻었죠!\n\n\
보라색 차 : 보라색 맛 났어! 뭔 일이 날지 모르는 차입니다! 조심하세요!'
# 스토리 버튼 누르면 나오는 텍스트
read_score = list()  #엑셀파일에서 점수가져와서 저장
read_name = list()  #엑셀파일에서 이름가져와서 저장
read_id = list()  #엑셀파일에서 학번가져와서 저장
read_all = list()  #엑셀파일에서 가져온거 다 저장
read_name_plus_id = list()     #엑셀파일에서 가져온 점수, 학번저장
ranking_board = 0