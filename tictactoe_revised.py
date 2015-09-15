'''
Tic-Tac-Toe-Game
(using python 2.7)

implements gameplay of classic tic-tac-toe
game with Tkinter
Author: Tracy Lynn Wesley
'''

from Tkinter import *

WIDTH = 500
HEIGHT = 500

WINNING_COMBOS = [[0, 1, 2, "h"], [3, 4, 5, "h"], [6, 7, 8, "h"],
                  [0, 3, 6, "v"], [1, 4, 7, "v"], [2, 5, 8, "v"],
                  [0, 4, 8, "d"], [2, 4, 6, "d"]]

class TicTacToe(Frame):
    '''
    The classic Tic-Tac-Toe game implemented as a Tkinter frame.

    First, initialize the game, then respond to mouse clicks by writing an X
    or an O in the spot clicked. The X or O written is determined by who the
    current player is (switches every turn starting with player 1 - X).
    After each mouse click, check to see if there are three X's or O's in a
    row somewhere. If so, there is a winner. If all spots are taken and there
    is no winner, there is a tie.
    '''

    def __init__(self):
        '''
        Initialize the tic-tac-toe game - a canvas, a grid, and a play button
        and bind the mouse-click event to the onClick function
        '''
        Frame.__init__(self)
        self.master.title("Tic-Tac-Toe *** Try to get three in a row! ***")
        self.grid()
        gameFrame = Frame(self)
        gameFrame.grid()
        self.canvas = Canvas(gameFrame, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.grid(columnspan=2)
        self.canvas.focus_set()
        
        self.canvas.bind("<Button-1>", self.onClick)
        
        self.gridSquares = self.createGameboard(WIDTH, HEIGHT, 5)
        
        playButton = Button(gameFrame, text="New Game", command=self.__init__)
        playButton.grid(row=1, column=0, sticky=E)

        self.player = 1
        self.playerText = Label(gameFrame, text="Player 1 Turn")
        self.playerText.grid(row=1, column=1)

    def createGameboard(self, width, height, thickness = 1):
        '''
        Create 4 lines based on the current height and width
        '''
        hUnit = height/5
        wUnit = width/5
        
        self.canvas.create_line(wUnit*2, hUnit, wUnit*2, hUnit*4,
                                width = thickness)
        self.canvas.create_line(wUnit*3, hUnit, wUnit*3, hUnit*4,
                                width = thickness)
        self.canvas.create_line(wUnit, hUnit*2, wUnit*4, hUnit*2,
                                width = thickness)
        self.canvas.create_line(wUnit, hUnit*3, wUnit*4, hUnit*3,
                                width = thickness)
        '''top row'''
        gs1 = GridSquare(wUnit, wUnit*2, hUnit, hUnit*2)
        gs2 = GridSquare(wUnit*2, wUnit*3, hUnit, hUnit*2)
        gs3 = GridSquare(wUnit*3, wUnit*4, hUnit, hUnit*2)

        '''middle row'''
        gs4 = GridSquare(wUnit, wUnit*2, hUnit*2, hUnit*3)
        gs5 = GridSquare(wUnit*2, wUnit*3, hUnit*2, hUnit*3)
        gs6 = GridSquare(wUnit*3, wUnit*4, hUnit*2, hUnit*3)

        '''bottom row'''
        gs7 = GridSquare(wUnit, wUnit*2, hUnit*3, hUnit*4)
        gs8 = GridSquare(wUnit*2, wUnit*3, hUnit*3, hUnit*4)
        gs9 = GridSquare(wUnit*3, wUnit*4, hUnit*3, hUnit*4)

        gridSquares = list()
        gridSquares.append(gs1)
        gridSquares.append(gs2)
        gridSquares.append(gs3)
        gridSquares.append(gs4)
        gridSquares.append(gs5)
        gridSquares.append(gs6)
        gridSquares.append(gs7)
        gridSquares.append(gs8)
        gridSquares.append(gs9)

        return gridSquares

    def onClick(self, event):
        '''
        Called when the mouse left button is clicked.
        Depending on the player, location of the click, and if there is an X or
        O in that spot, an X or O may be placed in the location clicked.
        Afterward, check to see if there is a winner.
        '''
        for i in range(len(self.gridSquares)):
            current = self.gridSquares[i]
            if current.xMin < event.x < current.xMax and current.yMin <\
                    event.y < current.yMax and current.value == "":
                if self.player == 1:
                    self.drawShape(current, "X")
                    self.player = 2
                else:
                    self.drawShape(current, "O")
                    self.player = 1
                self.playerText["text"] = "Player " + str(self.player) + " Turn"
                self.testForWin(i)

    def drawShape(self, gs, shape):
        '''
        Draw a shape in the current grid square. Shape will be either an X or
        an O.
        '''
        padding = (gs.xMax - gs.xMin)/10
        x1 = gs.xMin + padding
        y1 = gs.yMin + padding
        x2 = gs.xMax - padding
        y2 = gs.yMax - padding
        if shape == "X":
            self.canvas.create_line(x1, y1, x2, y2, width=4)
            self.canvas.create_line(x2, y1, x1, y2, width=4)
            gs.value = "X"
        elif shape == "O":
            self.canvas.create_oval(x1, y1, x2, y2, width=4)
            gs.value = "O"

    def testForWin(self, gsNum):
        '''
        Check to see if the player has won after clicking on the current grid
        square, and if not, check to see if there was a tie
        '''
        gsList = self.gridSquares
        winningCombo = [-1 for x in range(3)]
        winType = ""
        
        for j in range(len(WINNING_COMBOS)):
            combo = WINNING_COMBOS[j]
            if gsNum in combo and gsList[combo[0]].value ==\
                    gsList[combo[1]].value == gsList[combo[2]].value:
                winningCombo = combo
                winType = combo[3]

        allDone = True
        for gs in gsList:
            if gs.value == "":
                allDone = False

        w = WIDTH / 2
        offset = WIDTH / 10


        if winningCombo[0] != -1:
            firstIndex = winningCombo[0]
            first = gsList[winningCombo[0]]
            last = gsList[winningCombo[2]]
            if winType == "h":
                y = first.yMin + (first.yMax - first.yMin)/2
                self.canvas.create_line(first.xMin, y, last.xMax, y)
            elif winType == "v":
                x = first.xMin + (first.xMax - first.xMin)/2
                self.canvas.create_line(x, first.yMin, x, last.yMax)
            elif firstIndex == 0:
                self.canvas.create_line(first.xMin, first.yMin,
                                        last.xMax, last.yMax)
            else:
                self.canvas.create_line(first.xMax, first.yMin,
                                        last.xMin, last.yMax)
            winningText = "Player " + str(self.player) + " Wins!"
            self.canvas.create_text(w - offset, offset, text=winningText)
            self.canvas.unbind("<Button-1>")
        elif allDone:
            self.canvas.create_text(w - offset, offset, text="It's a tie!")
            self.canvas.unbind("<Button-1>")



class GridSquare:
    '''
    Represents a square on the TicTacToe gameboard.
   
    Each grid square has a label and an xMin, xMax, yMin, and yMax.
    '''
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xMin = xmin
        self.xMax = xmax
        self.yMin = ymin
        self.yMax = ymax
        self.value = ""

TicTacToe().mainloop()
