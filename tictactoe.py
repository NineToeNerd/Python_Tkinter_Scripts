'''
Tic-Tac-Toe Game

implements gameplay of classic tic-tac-toegame with Tkinter
Author: Tracy Lynn Wesley
'''

from Tkinter import *

class TicTacToe(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Tic-Tac-Toe *** Try to get three in a row! ***")
        self.grid()

        frame1 = Frame(self)
        frame1.grid()

        self.canvas = Canvas(frame1, width = 500, height = 500, bg ="white")
        self.canvas.grid(columnspan = 2)
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.create)

        self.canvas.create_line(185, 100, 185, 400, width = 5)
        self.canvas.create_line(315, 100, 315, 400, width = 5)
        self.canvas.create_line(75, 200, 425, 200, width = 5)
        self.canvas.create_line(75, 300, 425, 300, width = 5)

        playGame = Button(frame1, text = "New Game", command = self.__init__)
        playGame.grid(row = 1, column = 0, sticky = E)

        self.player = Label(frame1, text = "Player 1 Turn")
        self.player.grid(row = 1, column = 1)

        self.player1b = False
        self.player2b = False
        
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0
        self.val4 = 0
        self.val5 = 0
        self.val6 = 0
        self.val7 = 0
        self.val8 = 0
        self.val9 = 0

    def create(self, event):
        if self.player["text"] == "Player 1 Turn":
            if 75 < event.x < 185:
                if 100 < event.y < 200:
                    if self.val1 == 0:
                        self.createX1()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val4 == 0:
                        self.createX4()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val7 == 0:
                        self.createX7()
                        self.turn()
            elif 185 < event.x < 315:
                if 100 < event.y < 200:
                    if self.val2 == 0:
                        self.createX2()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val5 == 0:
                        self.createX5()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val8 == 0:
                        self.createX8()
                        self.turn()
            elif 315 < event.x < 425:
                if 100 < event.y < 200:
                    if self.val3 == 0:
                        self.createX3()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val6 == 0:
                        self.createX6()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val9 == 0:
                        self.createX9()
                        self.turn()
        else:
            if 75 < event.x < 185:
                if 100 < event.y < 200:
                    if self.val1 == 0:
                        self.createO1()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val4 == 0:
                        self.createO4()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val7 == 0:
                        self.createO7()
                        self.turn()
            elif 185 < event.x < 315:
                if 100 < event.y < 200:
                    if self.val2 == 0:
                        self.createO2()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val5 == 0:
                        self.createO5()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val8 == 0:
                        self.createO8()
                        self.turn()
            elif 315 < event.x < 425:
                if 100 < event.y < 200:
                    if self.val3 == 0:
                        self.createO3()
                        self.turn()
                elif 200 < event.y < 300:
                    if self.val6 == 0:
                        self.createO6()
                        self.turn()
                elif 300 < event.y < 400:
                    if self.val9 == 0:
                        self.createO9()
                        self.turn()
        self.testWin()
            
    def turn(self):
        if self.player["text"] == "Player 1 Turn":
            self.player["text"] = "Player 2 Turn"
        else:
            self.player["text"] = "Player 1 Turn"

    def createX1(self):
        x1 = 100
        y1 = 125
        x2 = 150
        y2 = 175
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x1")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x2")
        self.val1 = 1

    def createO1(self):
        x1 = 100
        y1 = 125
        x2 = 150
        y2 = 175
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o1")
        self.val1 = 2

    def createX2(self):
        x1 = 225
        y1 = 125
        x2 = 275
        y2 = 175
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x3")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x4")
        self.val2 = 1

    def createO2(self):
        x1 = 225
        y1 = 125
        x2 = 275
        y2 = 175
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o2")
        self.val2 = 2

    def createX3(self):
        x1 = 350
        y1 = 125
        x2 = 400
        y2 = 175
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x5")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x6")
        self.val3 = 1
        
    def createO3(self):
        x1 = 350
        y1 = 125
        x2 = 400
        y2 = 175
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o3")
        self.val3 = 2

    def createX4(self):
        x1 = 100
        y1 = 225
        x2 = 150
        y2 = 275
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x7")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x8")
        self.val4 = 1

    def createO4(self):
        x1 = 100
        y1 = 225
        x2 = 150
        y2 = 275
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o4")
        self.val4 = 2
        
    def createX5(self):
        x1 = 225
        y1 = 225
        x2 = 275
        y2 = 275
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x9")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x10")
        self.val5 = 1
        
    def createO5(self):
        x1 = 225
        y1 = 225
        x2 = 275
        y2 = 275
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o5")
        self.val5 = 2
        
    def createX6(self):
        x1 = 350
        y1 = 225
        x2 = 400
        y2 = 275
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x11")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x12")
        self.val6 = 1
        
    def createO6(self):
        x1 = 350
        y1 = 225
        x2 = 400
        y2 = 275
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o6")
        self.val6 = 2
        
    def createX7(self):
        x1 = 100
        y1 = 325
        x2 = 150
        y2 = 375
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x13")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x14")
        self.val7 = 1
        
    def createO7(self):
        x1 = 100
        y1 = 325
        x2 = 150
        y2 = 375
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o7")
        self.val7 = 2
        
    def createX8(self):
        x1 = 225
        y1 = 325
        x2 = 275
        y2 = 375
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x15")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x16")
        self.val8 = 1
        
    def createO8(self):
        x1 = 225
        y1 = 325
        x2 = 275
        y2 = 375
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o8")
        self.val8 = 2
        
    def createX9(self):
        x1 = 350
        y1 = 325
        x2 = 400
        y2 = 375
        self.canvas.create_line(x1, y1, x2, y2, width = 4, tags = "x17")
        self.canvas.create_line(x2, y1, x1, y2, width = 4, tags = "x18")
        self.val9 = 1
        
    def createO9(self):
        x1 = 350
        y1 = 325
        x2 = 400
        y2 = 375
        self.canvas.create_oval(x1, y1, x2, y2, width = 4, tags = "o9")
        self.val9 = 2

    def testWin(self):
        if self.val1 == self.val2 == self.val3:
            if self.val1 == 1:
                self.canvas.create_line(75, 150, 425, 150, width = 2, tags = "line")
                self.player1()
            elif self.val1 == 2:
                self.canvas.create_line(75, 150, 425, 150, width = 2, tags = "line")
                self.player2()
        if self.val1 == self.val5 == self.val9:
            if self.val1 == 1:
                self.canvas.create_line(75, 100, 425, 400, width = 2, tags = "line")
                self.player1()
            elif self.val1 == 2:
                self.canvas.create_line(75, 100, 425, 400, width = 2, tags = "line")
                self.player2()
        if self.val1 == self.val4 == self.val7:
            if self.val1 == 1:
                self.canvas.create_line(125, 100, 125, 400, width = 2, tags = "line")
                self.player1()
            elif self.val1 == 2:
                self.canvas.create_line(125, 100, 125, 400, width = 2, tags = "line")
                self.player2()
        if self.val2 == self.val5 == self.val8:
            if self.val2 == 1:
                self.canvas.create_line(250, 100, 250, 400, width = 2, tags = "line")
                self.player1()
            elif self.val2 == 2:
                self.canvas.create_line(250, 100, 250, 400, width = 2, tags = "line")
                self.player2()
        if self.val3 == self.val6 == self.val9:
            if self.val3 == 1:
                self.canvas.create_line(375, 100, 375, 400, width = 2, tags = "line")
                self.player1()
            elif self.val3 == 2:
                self.canvas.create_line(375, 100, 375, 400, width = 2, tags = "line")
                self.player2()
        if self.val3 == self.val5 == self.val7:
            if self.val3 == 1:
                self.canvas.create_line(425, 100, 75, 400, width = 2, tags = "line")
                self.player1()
            elif self.val3 == 2:
                self.canvas.create_line(425, 100, 75, 400, width = 2, tags = "line")
                self.player2()
        if self.val4 == self.val5 == self.val6:
            if self.val4 == 1:
                self.canvas.create_line(75, 250, 425, 250, width = 2, tags = "line")
                self.player1()
            elif self.val4 == 2:
                self.canvas.create_line(75, 250, 425, 250, width = 2, tags = "line")
                self.player2()
        if self.val7 == self.val8 == self.val9:
            if self.val7 == 1:
                self.canvas.create_line(75, 350, 425, 350, width = 2, tags = "line")
                self.player1()
            elif self.val7 == 2:
                self.canvas.create_line(75, 350, 425, 350, width = 2, tags = "line")
                self.player2()
        if self.val1 != 0 and self.val2 != 0 and self.val3 != 0 and self.val4 != 0 and\
           self.val5 != 0 and self.val6 != 0 and self.val7 != 0 and self.val8 != 0 and\
           self.val9 != 0 and self.player1b == False and self.player2b == False:
            self.cat()

    def player1(self):
        self.canvas.create_text(200, 50, text = "Player 1 Wins!", tags = "text")
        self.player1b = True
        self.canvas.bind("<Button-1>", self.nothing)

    def player2(self):
        self.canvas.create_text(200, 50, text = "Player 2 Wins!", tags = "text")
        self.player2b = True
        self.canvas.bind("<Button-1>", self.nothing)

    def cat(self):
        self.canvas.create_text(200, 50, text = "It's a tie!", tags = "text")

    def nothing(self, event):
        pass
        


TicTacToe().mainloop()
