#DataFlair python ludo - Importing Modules.
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint, choice

class Ludo_Game:
    def __init__(self, root,Dice_side_one, Dice_side_two, Dice_side_three, Dice_side_four, Dice_side_five, Dice_side_six):
        self.window = root
        self.board = 0
        self.make_board = Canvas(self.window, bg="#141414", width=800, height=630)
        self.make_board.pack(fill=BOTH,expand=1)
 
        self.Red_coin = []
        self.Green_coin = []
        self.Yellow_coin = []
        self.Blue_coin = []
 
        self.Red_label = []
        self.Green_label = []
        self.Yellow_label = []
        self.Blue_label = []
 
        self.Predict_BlockValue = []
        self.Total_player = []
        self.Dice_side = [Dice_side_one, Dice_side_two, Dice_side_three, Dice_side_four, Dice_side_five, Dice_side_six]
 
        self.Red_coord = [-1, -1, -1, -1]
        self.Green_coord = [-1, -1, -1, -1]
        self.Yellow_coord = [-1, -1, -1, -1]
        self.Blue_coord = [-1, -1, -1, -1]
 
        self.Position_Red_coin = [0, 1, 2, 3]
        self.Position_Green_coin = [0, 1, 2, 3]
        self.Position_Yellow_coin = [0, 1, 2, 3]
        self.Position_Blue_coin = [0, 1, 2, 3]
 
        for index in range(len(self.Position_Red_coin)):
            self.Position_Red_coin[index] = -1
            self.Position_Green_coin[index] = -1
            self.Position_Yellow_coin[index] = -1
            self.Position_Blue_coin[index] = -1
 
        self.move_Red = 0
        self.move_Green = 0
        self.move_Yellow = 0
        self.move_Blue = 0
 
        self.TakePermission = 0
        self.Six_overlap = 0
 
        self.Active_Red_store = 0
        self.Active_Yellow_store = 0
        self.Active_Green_store = 0
        self.Active_Blue_store = 0
 
        self.Six_Counter = 0
        self.TimeFor = -1
 
        self.Robo = 0
        self.count_RoboStage = 0
        self.Store_Robo = []
 
        self.Board()
 
        self.Instructional_Button_Red()
        self.Instructional_Button_Blue()
        self.Instructional_Button_Yellow()
        self.Instructional_Button_Green()
 
        self.Initial_Control()
def Board(self):
        self.make_board.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")
 
        self.make_board.create_rectangle(100, 15, 100+240, 15+240, width=3, fill="red")
        self.make_board.create_rectangle(100, (15+240)+(40*3), 100+240, (15+240)+(40*3)+(40*6), width=3, fill="blue")
        self.make_board.create_rectangle(340+(40*3), 15, 340+(40*3)+(40*6), 15+240, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3), (15+240)+(40*3), 340+(40*3)+(40*6), (15+240)+(40*3)+(40*6), width=3, fill="yellow")
 
        self.make_board.create_rectangle(100, (15+240), 100+240, (15+240)+40, width=3)
        self.make_board.create_rectangle(100+40, (15 + 240)+40, 100 + 240, (15 + 240) + 40+40, width=3, fill="#F00000")
        self.make_board.create_rectangle(100, (15 + 240)+80, 100 + 240, (15 + 240) + 80+40, width=3)
 
        self.make_board.create_rectangle(100+240, 15, 100 + 240+40, 15 + (40*6), width=3)
        self.make_board.create_rectangle(100+240+40, 15+40, 100+240+80, 15 + (40*6), width=3, fill="green")
        self.make_board.create_rectangle(100+240+80, 15, 100 + 240+80+40, 15 + (40*6), width=3)
 
        self.make_board.create_rectangle(340+(40*3), 15+240, 340+(40*3)+(40*6), 15+240+40, width=3)
        self.make_board.create_rectangle(340+(40*3), 15+240+40, 340+(40*3)+(40*6)-40, 15+240+80, width=3, fill="yellow")
        self.make_board.create_rectangle(340+(40*3), 15+240+80, 340+(40*3)+(40*6), 15+240+120, width=3)
 
        self.make_board.create_rectangle(100, (15 + 240)+(40*3), 100 + 240+40, (15 + 240)+(40*3)+(40*6), width=3)
        self.make_board.create_rectangle(100+240+40, (15 + 240)+(40*3), 100 + 240+40+40, (15 + 240)+(40*3)+(40*6)-40, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 240+40+40, (15 + 240)+(40*3), 100 + 240+40+40+40, (15 + 240)+(40*3)+(40*6), width=3)
 
        X_Start = 100 + 40
        Y_Start = 15 + 240
        X_End = 100 + 40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, end_y, width=2)
            X_Start+=40
            X_End+= 40
 
        X_Start = 100+240+(40*3)+40
        Y_Start = 15 + 240
        X_End = 100+240+(40*3)+40
        Y_End = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, Y_End, width=2)
            X_Start += 40
            X_End += 40
 
        X_Start = 100+240
        Y_Start = 15+40
        X_End = 100+240+(40*3)
        Y_End = 15+40
        for _ in range(5):
            self.make_board.create_line(X_Start,Y_Start, X_End,Y_End, width=2)
            Y_Start += 40
            Y_End += 40
 
        X_Start = 100 + 240
        Y_Start = 15 + (40*6)+(40*3)+40
        X_End = 100 + 240 + (40 * 3)
        Y_End = 15 + (40*6)+(40*3)+40
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, Y_End, width=2)
            Y_Start += 40
            Y_End += 40
 
        self.make_board.create_rectangle(100+20, 15+40-20, 100 + 40 + 60 + 40 +60+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_board.create_rectangle(340+(40*3)+40 - 20, 15 + 40-20, 340+(40*3)+40 + 60 + 40 + 40+20+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_board.create_rectangle(100+20, 340+80-20+15, 100 + 40 + 60 + 40 +60+20, 340+80+60+40+40+20+15, width=3, fill="white")
        self.make_board.create_rectangle(340+(40*3)+40 - 20, 340 + 80 - 20+15, 340+(40*3)+40 + 60 + 40 + 40+20+20, 340 + 80 + 60 + 40 + 40 + 20+15, width=3, fill="white")
 
        self.make_board.create_rectangle(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red")
        self.make_board.create_rectangle(100+40+60+60, 15 + 40, 100+40+60+40+60, 15 + 40 + 40, width=3, fill="red")
        self.make_board.create_rectangle(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3, fill="red")
        self.make_board.create_rectangle(100 + 40 + 60 + 60, 15 + 40+100, 100 + 40 + 60 + 40 +60, 15 + 40 + 40+100, width=3, fill="red")
 
        self.make_board.create_rectangle(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40 + 100, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40 + 100, width=3, fill="green")
 
 
        self.make_board.create_rectangle(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40 + 60 + 40+20, 340+80+60+40+15, 100 + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="blue")
 
        self.make_board.create_rectangle(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+60+40+15,340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="yellow")
 
        self.make_board.create_rectangle(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3)
        
        self.make_board.create_rectangle(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="green", width=3)
 
        self.make_board.create_rectangle(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)
        self.make_board.create_rectangle(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="blue",width=3)
 
        self.make_board.create_polygon(100+240, 15+240, 100+240+60, 15+240+60, 100+240, 15+240+(40*3), width=3,fill="red",outline="black")
        self.make_board.create_polygon(100 + 240+(40*3), 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240+(40*3), 15 + 240 + (40 * 3), width=3, fill="yellow",outline="black")
        self.make_board.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240, width=3, fill="green",outline="black")
        self.make_board.create_polygon(100 + 240, 15 + 240+(40*3), 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240+(40*3), width=3, fill="blue",outline="black")


#<--------------------------------------------------------step 6------------------------------------------------------->

def Prediction_Maker(self,color_indicator):
        try:
            if color_indicator == "red":
                Predict_BlockValue = self.Predict_BlockValue[0]
                if self.Robo and self.count_RoboStage < 3:
                    self.count_RoboStage += 1
                if self.Robo and self.count_RoboStage == 3 and self.Six_Counter < 2:
                    Permanent_Dice_num = self.move_Red = 6
                    self.count_RoboStage += 1
                else:    
                    Permanent_Dice_num = self.move_Red = randint(1, 6)
 
            elif color_indicator == "blue":
                Predict_BlockValue = self.Predict_BlockValue[1]
                Permanent_Dice_num = self.move_Blue = randint(1, 6)
                if self.Robo and Permanent_Dice_num == 6:
                    for coin_loc in self.Position_Red_coin:
                        if coin_loc>=40 and coin_loc<=46:
                            Permanent_Dice_num = self.move_Blue = randint(1, 5)
                            break
                           
            elif color_indicator == "yellow":
                Predict_BlockValue = self.Predict_BlockValue[2]
                Permanent_Dice_num = self.move_Yellow = randint(1, 6)
 
            else:
                Predict_BlockValue = self.Predict_BlockValue[3]
                Permanent_Dice_num = self.move_Green = randint(1, 6)
 
            Predict_BlockValue[1]['state'] = DISABLED
            Temp_Counter = 12
            while Temp_Counter>0:
                move_Temp_Counter = randint(1, 6)
                Predict_BlockValue[0]['image'] = self.Dice_side[move_Temp_Counter - 1]
                self.window.update()
                time.sleep(0.1)
                Temp_Counter-=1
 
            print("Prediction result: ", Permanent_Dice_num)
 
            Predict_BlockValue[0]['image'] = self.Dice_side[Permanent_Dice_num-1]
            if self.Robo == 1 and color_indicator == "red":
                self.window.update()
                time.sleep(0.4)
            self.Instructional_Button(color_indicator,Permanent_Dice_num,Predict_BlockValue)
        except:
            print("Force Stop Error in Prediction")

#<--------------------------------------------------------step 6 ends-------------------------------------------------->

#<--------------------------------------------------------adding contents of step7------------------------------------->

def Instructional_Button(self,color_indicator,Permanent_Dice_num, Predict_BlockValue):
        Robo_Operator = None
        if color_indicator == "red":
            Temp_CoinPosition = self.Position_Red_coin
        elif color_indicator == "green":
            Temp_CoinPosition = self.Position_Green_coin
        elif color_indicator == "yellow":
            Temp_CoinPosition = self.Position_Yellow_coin
        else:
            Temp_CoinPosition = self.Position_Blue_coin
 
        all_in = 1
        for i in range(4):
            if Temp_CoinPosition[i] == -1:
                all_in = 1
            else:
                all_in = 0
                break
 
        if  Permanent_Dice_num == 6:
            self.Six_Counter += 1
        else:
            self.Six_Counter = 0
 
        if ((all_in == 1 and Permanent_Dice_num == 6) or (all_in==0)) and self.Six_Counter<3:
            permission = 1
            if color_indicator == "red":
                temp = self.Red_coord
            elif color_indicator == "green":
                temp = self.Green_coord
            elif color_indicator == "yellow":
                temp = self.Yellow_coord
            else:
                temp = self.Blue_coord
 
            if  Permanent_Dice_num<6:
                if self.Six_overlap == 1:
                    self.time_for-=1
                    self.Six_overlap=0
                for i in range(4):
                    if  temp[i] == -1:
                        permission=0
                    elif temp[i]>100:
                        if  temp[i] + Permanent_Dice_num <=106:
                            permission=1
                            break
                        else:
                            permission=0
                    else:
                        permission=1
                        break
            else:
                for i in range(4):
                    if  temp[i]>100:
                        if  temp[i] + Permanent_Dice_num <= 106:
                            permission = 1
                            break
                        else:
                            permission = 0
                    else:
                        permission = 1
                        break
            if permission == 0:
                self.Command_Maker(None)
            else:
                self.State_controller_Button(Predict_BlockValue[2])
 
                if self.Robo == 1 and Predict_BlockValue == self.Predict_BlockValue[0]:
                    Robo_Operator = "give"
                Predict_BlockValue[1]['state'] = DISABLED# Predict btn deactivation
 
        else:
            Predict_BlockValue[1]['state'] = NORMAL
            if self.Six_overlap == 1:
                self.time_for -= 1
                self.Six_overlap = 0
            self.Command_Maker()
 
        if  Permanent_Dice_num == 6 and self.Six_Counter<3 and Predict_BlockValue[2][0]['state'] == NORMAL:
            self.time_for-=1
        else:
            self.Six_Counter=0
 
        if self.Robo == 1 and Robo_Operator:
            self.Robo_Judge(Robo_Operator)



#<-------------------------------------------------------end of step7-------------------------------------------------->

#<-------------------------------------------------------step 9---------------------------------------------------------->


def Instructional_Button_Red(self):
        Block_Predict_Red = Label(self.make_board,image=self.Dice_side[0])
        Block_Predict_Red.place(x=34,y=15)
        Predict_Red = Button(self.make_board, bg="black", fg="green", relief=RAISED, bd=5, text="Predict", font=("Times new roman", 8, "bold"), command=lambda: self.Prediction_Maker("red"))
        Predict_Red.place(x=25, y=15 + 50)
       
        btn_1 = Button(self.make_board,bg="#262626",fg="#00eb00",text="1",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("red",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=20,y=15+100)
        btn_2 = Button(self.make_board,bg="#262626",fg="#00eb00",text="2",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("red",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=60,y=15+100)
        btn_3 = Button(self.make_board,bg="#262626",fg="#00eb00",text="3",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("red",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=20,y=15+100+40)
        btn_4 = Button(self.make_board,bg="#262626",fg="#00eb00",text="4",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("red",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=60,y=15+100+40)
 
        Label(self.make_board,text="Player 1",bg="#141414",fg="gold",font=("Times new roman",15,"bold")).place(x=15,y=15+140+50)
        self.Instructional_Button_Store(Block_Predict_Red,Predict_Red,[btn_1,btn_2,btn_3,btn_4])
 
    def Instructional_Button_Blue(self):
        Block_Predict_Blue = Label(self.make_board, image=self.Dice_side[0])
        Block_Predict_Blue.place(x=34, y=15+(40*6+40*3)+10)
        Predict_Blue = Button(self.make_board, bg="black", fg="green", relief=RAISED, bd=5, text="Predict",font=("Times new roman", 8, "bold"), command=lambda: self.Prediction_Maker("blue"))
        Predict_Blue.place(x=25, y=15+(40*6+40*3)+40 + 20)
 
        btn_1 = Button(self.make_board,bg="#262626",fg="#00eb00",text="1",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("blue",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=20,y=15+(40*6+40*3)+40 + 70)
        btn_2 = Button(self.make_board,bg="#262626",fg="#00eb00",text="2",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("blue",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=60,y=15+(40*6+40*3)+40 + 70)
        btn_3 = Button(self.make_board,bg="#262626",fg="#00eb00",text="3",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("blue",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=20,y=15+(40*6+40*3)+40 + 70+ 40)
        btn_4 = Button(self.make_board,bg="#262626",fg="#00eb00",text="4",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("blue",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=60,y=15+(40*6+40*3)+40 + 70+ 40)
 
        Label(self.make_board, text="Player 2", bg="#141414", fg="gold", font=("Times new roman", 15, "bold")).place(x=12,y=15+(40*6+40*3)+40 + 110+50)
        self.Instructional_Button_Store(Block_Predict_Blue, Predict_Blue, [btn_1,btn_2,btn_3,btn_4])
 
    def Instructional_Button_Yellow(self):
        Block_Predict_Yellow = Label(self.make_board, image=self.Dice_side[0])
        Block_Predict_Yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 10)+20, y=15 + (40 * 6 + 40 * 3) + 10)
        Predict_Yellow = Button(self.make_board, bg="black", fg="green", relief=RAISED, bd=5, text="Predict",font=("Times new roman", 8, "bold"), command=lambda: self.Prediction_Maker("yellow"))
        Predict_Yellow.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+20, y=15 + (40 * 6 + 40 * 3) + 40 + 20)
       
        btn_1 = Button(self.make_board,bg="#262626",fg="#00eb00",text="1",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("yellow",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_2 = Button(self.make_board,bg="#262626",fg="#00eb00",text="2",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("yellow",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70)
        btn_3 = Button(self.make_board,bg="#262626",fg="#00eb00",text="3",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("yellow",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
        btn_4 = Button(self.make_board,bg="#262626",fg="#00eb00",text="4",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("yellow",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40, y=15 + (40 * 6 + 40 * 3) + 40 + 70+ 40)
       
        Label(self.make_board, text="Player 3", bg="#141414", fg="gold", font=("Times new roman", 15, "bold")).place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 +7),y=15+(40*6+40*3)+40 + 110+50)
        self.Instructional_Button_Store(Block_Predict_Yellow, Predict_Yellow, [btn_1,btn_2,btn_3,btn_4])
 
    def Instructional_Button_Green(self):
        Block_Predict_Green = Label(self.make_board, image=self.Dice_side[0])
        Block_Predict_Green.place(x=100+(40*6+40*3+40*6+10)+20, y=15)
        Predict_Green = Button(self.make_board, bg="black", fg="green", relief=RAISED, bd=5, text="Predict", font=("Times new roman", 8, "bold"), command=lambda: self.Prediction_Maker("green"))
        Predict_Green.place(x=100+(40*6+40*3+40*6+2)+20, y=15 + 50)
       
        btn_1 = Button(self.make_board,bg="#262626",fg="#00eb00",text="1",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("green",'1'), state=DISABLED, disabledforeground="red")
        btn_1.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100)
        btn_2 = Button(self.make_board,bg="#262626",fg="#00eb00",text="2",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("green",'2'), state=DISABLED, disabledforeground="red")
        btn_2.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100)
        btn_3 = Button(self.make_board,bg="#262626",fg="#00eb00",text="3",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("green",'3'), state=DISABLED, disabledforeground="red")
        btn_3.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15,y=15+100+40)
        btn_4 = Button(self.make_board,bg="#262626",fg="#00eb00",text="4",font=("Times new roman",13,"bold","italic"),relief=RAISED,bd=3,command=lambda: self.Main_Controller("green",'4'), state=DISABLED, disabledforeground="red")
        btn_4.place(x=100 + (40 * 6 + 40 * 3 + 40 * 6 + 2)+15 + 40,y=15+100+40)
       
        Label(self.make_board, text="Player 4", bg="#141414", fg="gold", font=("Times new roman", 15, "bold")).place(x=100+(40*6+40*3+40*6+7), y=15+140+50)
        self.Instructional_Button_Store(Block_Predict_Green, Predict_Green, [btn_1,btn_2,btn_3,btn_4])


#<------------------------------------------------------step 9 ends------------------------------------------------------>

#<------------------------------------------------------start of step 11-------------------------------------------------->
            


def Main_Controller(self, Coin_Color, Coin_num):
        Robo_Operator = None
 
        if  Coin_Color == "red":
            self.State_controller_Button(self.Predict_BlockValue[0][2], 0)
 
            if self.move_Red == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")
 
            elif self.Position_Red_coin[int(Coin_num)-1] == -1 and self.move_Red == 6:
                self.Start_position_RedCircle(Coin_num)
                self.Red_coord[int(Coin_num) - 1] = 1
 
            elif self.Position_Red_coin[int(Coin_num)-1] > -1:
                Take_coord = self.make_board.coords(self.Red_coin[int(Coin_num)-1])
                Red_label_X = Take_coord[0] + 10
                Red_label_Y = Take_coord[1] + 5
                self.Red_label[int(Coin_num) - 1].place(x=Red_label_X, y=Red_label_Y)
 
                if self.Position_Red_coin[int(Coin_num)-1]+self.move_Red<=106:
                    self.Position_Red_coin[int(Coin_num)-1] = self.Coin_Motion(self.Position_Red_coin[int(Coin_num) - 1],self.Red_coin[int(Coin_num)-1],self.Red_label[int(Coin_num)-1],Red_label_X,Red_label_Y,"red",self.move_Red)
                    if self.Robo and self.Position_Red_coin[int(Coin_num)-1] == 106 and Coin_Color == "red":
                        self.Store_Robo.remove(int(Coin_num))
                        print("After removing: ", self.Store_Robo)
 
                else:
                    if not self.Robo:
                            Messagebox.showerror("Not possible","Sorry, not permitted")
                    self.State_controller_Button(self.Predict_BlockValue[0][2])
 
                    if self.Robo:
                        Robo_Operator = "give"
                        self.Robo_Judge(Robo_Operator)
                    return
 
                if  self.Position_Red_coin[int(Coin_num)-1]==22 or self.Position_Red_coin[int(Coin_num)-1]==9 or self.Position_Red_coin[int(Coin_num)-1]==48 or self.Position_Red_coin[int(Coin_num)-1]==35 or self.Position_Red_coin[int(Coin_num)-1]==14 or self.Position_Red_coin[int(Coin_num)-1]==27 or self.Position_Red_coin[int(Coin_num)-1]==40 or self.Position_Red_coin[int(Coin_num)-1]==1:
                    pass
                else:
                    if self.Position_Red_coin[int(Coin_num) - 1] < 100:
                        self.coord_overlap(self.Position_Red_coin[int(Coin_num)-1],Coin_Color, self.move_Red)
 
                self.Red_coord[int(Coin_num)-1] = self.Position_Red_coin[int(Coin_num)-1]
 
            else:
                messagebox.showerror("Wrong choice","Sorry, Your coin in not permitted to travel")
                self.State_controller_Button(self.Predict_BlockValue[0][2])
 
                if self.Robo == 1:
                    Robo_Operator = "give"
                    self.Robo_Judge(Robo_Operator)
                return
 
            self.Predict_BlockValue[0][1]['state'] = NORMAL
 
 
        elif Coin_Color == "green":
            self.State_controller_Button(self.Predict_BlockValue[3][2], 0)
 
            if self.move_Green == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")
 
            elif self.Position_Green_coin[int(Coin_num) - 1] == -1 and self.move_Green == 6:
                self.Start_position_GreenCircle(Coin_num)
                self.Green_coord[int(Coin_num) - 1] = 14
 
            elif self.Position_Green_coin[int(Coin_num) - 1] > -1:
                Take_coord = self.make_board.coords(self.Green_coin[int(Coin_num) - 1])
                green_start_label_x = Take_coord[0] + 10
                green_start_label_y = Take_coord[1] + 5
                self.Green_label[int(Coin_num) - 1].place(x=green_start_label_x, y=green_start_label_y)
 
 
                if  self.Position_Green_coin[int(Coin_num) - 1] + self.move_Green <= 106:
                    self.Position_Green_coin[int(Coin_num) - 1] = self.Coin_Motion(self.Position_Green_coin[int(Coin_num) - 1], self.Green_coin[int(Coin_num) - 1], self.Green_label[int(Coin_num) - 1], green_start_label_x, green_start_label_y, "green", self.move_Green)
                else:
                   messagebox.showerror("Not possible","No path available")
                   self.State_controller_Button(self.Predict_BlockValue[3][2])
                   return
 
 
                if  self.Position_Green_coin[int(Coin_num)-1]==22 or self.Position_Green_coin[int(Coin_num)-1]==9 or self.Position_Green_coin[int(Coin_num)-1]==48 or self.Position_Green_coin[int(Coin_num)-1]==35 or self.Position_Green_coin[int(Coin_num)-1]==1 or self.Position_Green_coin[int(Coin_num)-1]==27 or self.Position_Green_coin[int(Coin_num)-1]==40 or self.Position_Green_coin[int(Coin_num)-1]==14:
                    pass
                else:
                    if self.Position_Green_coin[int(Coin_num) - 1] < 100:
                        self.coord_overlap(self.Position_Green_coin[int(Coin_num) - 1],Coin_Color, self.move_Green)
 
                self.Green_coord[int(Coin_num) - 1] = self.Position_Green_coin[int(Coin_num) - 1]
 
            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.State_controller_Button(self.Predict_BlockValue[3][2])
                return
 
            self.Predict_BlockValue[3][1]['state'] = NORMAL
 
        elif Coin_Color == "yellow":
           
            self.State_controller_Button(self.Predict_BlockValue[2][2], 0)
 
            if self.move_Yellow == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")
 
            elif self.Position_Yellow_coin[int(Coin_num) - 1] == -1 and self.move_Yellow == 6:
                self.Start_position_YellowCircle(Coin_num)
                self.Yellow_coord[int(Coin_num) - 1] = 27
 
            elif self.Position_Yellow_coin[int(Coin_num) - 1] > -1:
                Take_coord = self.make_board.coords(self.Yellow_coin[int(Coin_num) - 1])
                yellow_start_label_x = Take_coord[0] + 10
                yellow_start_label_y = Take_coord[1] + 5
                self.Yellow_label[int(Coin_num) - 1].place(x=yellow_start_label_x, y=yellow_start_label_y)
 
                if  self.Position_Yellow_coin[int(Coin_num) - 1] + self.move_Yellow <= 106:
                    self.Position_Yellow_coin[int(Coin_num) - 1] = self.Coin_Motion(self.Position_Yellow_coin[int(Coin_num) - 1], self.Yellow_coin[int(Coin_num) - 1], self.Yellow_label[int(Coin_num) - 1], yellow_start_label_x, yellow_start_label_y, "yellow", self.move_Yellow)
                else:
                   messagebox.showerror("Not possible","No path available")
                   
                   self.State_controller_Button(self.Predict_BlockValue[2][2])
                   return
 
                if  self.Position_Yellow_coin[int(Coin_num)-1]==22 or self.Position_Yellow_coin[int(Coin_num)-1]==9 or self.Position_Yellow_coin[int(Coin_num)-1]==48 or self.Position_Yellow_coin[int(Coin_num)-1]==35 or self.Position_Yellow_coin[int(Coin_num)-1]==1 or self.Position_Yellow_coin[int(Coin_num)-1]==14 or self.Position_Yellow_coin[int(Coin_num)-1]==40 or self.Position_Yellow_coin[int(Coin_num)-1]==27:
                    pass
                else:
                    if self.Position_Yellow_coin[int(Coin_num) - 1] < 100:
                        self.coord_overlap(self.Position_Yellow_coin[int(Coin_num) - 1],Coin_Color, self.move_Yellow)
 
                self.Yellow_coord[int(Coin_num) - 1] = self.Position_Yellow_coin[int(Coin_num) - 1]
 
            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.State_controller_Button(self.Predict_BlockValue[2][2])
                return
 
            self.Predict_BlockValue[2][1]['state'] = NORMAL
 
 
        elif Coin_Color == "blue":
            self.State_controller_Button(self.Predict_BlockValue[1][2], 0)  
 
            if self.move_Red == 106:
                messagebox.showwarning("Destination reached","Reached at the destination")
 
            elif self.Position_Blue_coin[int(Coin_num) - 1] == -1 and self.move_Blue == 6:
                self.Start_position_BlueCircle(Coin_num)
                self.Blue_coord[int(Coin_num) - 1] = 40
 
            elif self.Position_Blue_coin[int(Coin_num) - 1] > -1:
                Take_coord = self.make_board.coords(self.Blue_coin[int(Coin_num) - 1])
                blue_start_label_x = Take_coord[0] + 10
                blue_start_label_y = Take_coord[1] + 5
                self.Blue_label[int(Coin_num) - 1].place(x=blue_start_label_x, y=blue_start_label_y)
 
                if  self.Position_Blue_coin[int(Coin_num) - 1] + self.move_Blue <= 106:
                    self.Position_Blue_coin[int(Coin_num) - 1] = self.Coin_Motion(self.Position_Blue_coin[int(Coin_num) - 1], self.Blue_coin[int(Coin_num) - 1], self.Blue_label[int(Coin_num) - 1], blue_start_label_x, blue_start_label_y, "blue", self.move_Blue)
                else:
                   messagebox.showerror("Not possible","No path available")
                   
                   self.State_controller_Button(self.Predict_BlockValue[1][2])
                   return
 
                if  self.Position_Blue_coin[int(Coin_num)-1]==22 or self.Position_Blue_coin[int(Coin_num)-1]==9 or self.Position_Blue_coin[int(Coin_num)-1]==48 or self.Position_Blue_coin[int(Coin_num)-1]==35 or self.Position_Blue_coin[int(Coin_num)-1]==1 or self.Position_Blue_coin[int(Coin_num)-1]==14 or self.Position_Blue_coin[int(Coin_num)-1]==27 or self.Position_Blue_coin[int(Coin_num)-1]==40:
                    pass
                else:
                    if self.Position_Blue_coin[int(Coin_num) - 1] < 100:
                        self.coord_overlap(self.Position_Blue_coin[int(Coin_num) - 1],Coin_Color, self.move_Blue)
 
                self.Blue_coord[int(Coin_num) - 1] = self.Position_Blue_coin[int(Coin_num) - 1]
 
            else:
                messagebox.showerror("Wrong choice", "Sorry, Your coin in not permitted to travel")
                self.State_controller_Button(self.Predict_BlockValue[1][2])
                return
 
            self.Predict_BlockValue[1][1]['state'] = NORMAL
 
        print(self.Red_coord)
        print(self.Green_coord)
        print(self.Yellow_coord)
        print(self.Blue_coord)
        if self.Robo == 1:
            print("Robo Store is: ", self.Store_Robo)
       
        Permission_Granted = True
 
        if  Coin_Color == "red" and self.Position_Red_coin[int(Coin_num)-1] == 106:
            Permission_Granted = self.Check_Win_Runnerup(Coin_Color)
        elif  Coin_Color == "green" and self.Position_Green_coin[int(Coin_num)-1] == 106:
            Permission_Granted = self.Check_Win_Runnerup(Coin_Color)
        elif  Coin_Color == "yellow" and self.Position_Yellow_coin[int(Coin_num)-1] == 106:
            Permission_Granted = self.Check_Win_Runnerup(Coin_Color)
        elif  Coin_Color == "blue" and self.Position_Blue_coin[int(Coin_num)-1] == 106:
            Permission_Granted = self.Check_Win_Runnerup(Coin_Color)
 
        if Permission_Granted:
            self.Command_Maker(Robo_Operator)



#<----------------------------------------------------end of step 11---------------------------------------->




#<---------------------------------------------------start of step 17------------------------------------------>

if __name__ == '__main__':
    window = Tk()
    window.geometry("800x630")
    window.maxsize(800,630)
    window.minsize(800,630)
    window.title("LUDO Game by DataFlair")
    window.iconbitmap("C:\\Users\\DELL\\Desktop\\DataFlair\\ludo_icon.ico")
    block_six_side = ImageTk.PhotoImage(Image.open("dice1.jpg.webp").resize((33, 33), Image.ANTIALIAS))
    block_five_side = ImageTk.PhotoImage(Image.open("dice2.jpg").resize((33, 33), Image.ANTIALIAS))
    block_four_side = ImageTk.PhotoImage(Image.open("dice3.jpg").resize((33, 33), Image.ANTIALIAS))
    block_three_side = ImageTk.PhotoImage(Image.open("dice4.jpg").resize((33, 33),Image.ANTIALIAS))
    block_two_side = ImageTk.PhotoImage(Image.open("dice5.jpg").resize((33, 33), Image.ANTIALIAS))
    block_one_side = ImageTk.PhotoImage(Image.open("dice6.jpg").resize((33, 33), Image.ANTIALIAS))
    Ludo_Game(window,block_six_side,block_five_side,block_four_side,block_three_side,block_two_side,block_one_side)
    window.mainloop()


#<-------------------------------------------------------end of step 17---------------------------------------->
