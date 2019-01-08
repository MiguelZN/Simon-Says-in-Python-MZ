from tkinter import *
from PIL import ImageTk,Image
import time, random, winsound, functools


class loseMenu(Frame):
    def createNewGame(self):
        singlePlayerGUI.isaLoss=False
        singlePlayerGUI.isPlayerTurn = False
        singlePlayerGUI.score = 0
        singlePlayerGUI.updateLabels()
        self.grid_remove()
        singlePlayerGUI.CPU = CPU(singlePlayerGUI.NumberofCPUTiles)
        singlePlayerGUI.Player = SinglePlayer(0)
        singlePlayerGUI.grid()
        singlePlayerGUI.currentTurn = "cpu"
        singlePlayerGUI.update_idletasks()
        singlePlayerGUI.update()
        singlePlayerGUI.updateLabels()
        self.after(1000)
        singlePlayerGUI.playCPUTURN()
        singlePlayerGUI.update_idletasks()
        singlePlayerGUI.update()
        singlePlayerGUI.updateLabels()

    def __init__(self,root):
        super().__init__(root, width = 500, height = 500)
        self.GameOverLabel = Label(self,text = "Game Over", font = "none 50 bold", fg= "red")
        self.GameOverLabel.grid(row=0,column=1)

        self.NewGameButton = Button(self,text = "New Game", font = "none 20 bold", command = self.createNewGame)
        self.NewGameButton.grid(row=1, column= 1)



class Player():

    #creates a random choice of starter tiles that the computer will select
    def createMoves(self, numberstartertiles):
        listoftiles = []

        for i in range(numberstartertiles):
            listoftiles.append(random.choice(self.LISTOFCOLORS))

        return listoftiles

    def printListofTiles(self):
        print(self.listoftiles)

    def getListofTiles(self):
        return self.listoftiles

    #adds a tile(color) to the CPU's list of colors
    def addTile(self):
        self.listoftiles.append(random.choice(self.LISTOFCOLORS))


    def __init__(self, numberofstartertiles):
        self.LISTOFCOLORS = listofcolors = ["yellow","green","red","blue"]
        self.listoftiles = self.createMoves(numberofstartertiles)

class CPU(Player):

    def __init__(self, numberoftiles):
        super().__init__(numberoftiles)

class SinglePlayer(Player):

    def resetTileList(self):
        self.listoftiles = []

    def addSpecifiedTile(self, color):
        if(color=="green"):
            self.listoftiles.append("green")
        elif(color=="red"):
            self.listoftiles.append("red")
        elif(color=="blue"):
            self.listoftiles.append("blue")
        elif(color=="yellow"):
            self.listoftiles.append("yellow")

    def __init__(self, numberoftiles):
        super().__init__(numberoftiles)


class singlePlayer(Frame):

    def checkIfEqualTiles(self):
        if(len(self.Player.listoftiles)>len(self.CPU.listoftiles)):
            self.isaLoss = True
            return False

        elif(len(self.Player.listoftiles)==len(self.CPU.listoftiles)):
            for i in range(len(self.Player.listoftiles)):
                if(self.Player.listoftiles[i]!=self.CPU.listoftiles[i]):
                    self.isaLoss = True
                    return False
            self.score+=1
            self.CPU.addTile()
            self.currentTurn= "cpu"
            self.isPlayerTurn = False
            self.updateLabels()
            self.update()
            self.updateLabels()
            self.resetTilesBlank()
            self.after(300)
            self.playCPUTURN()

    def resetTilesBlank(self):
        self.topleftgreen.config(image = self.GREENSIMONOFF)
        self.toprightred.config(image = self.REDSIMONOFF)
        self.bottomleftyellow.config(image =self.YELLOWSIMONOFF)
        self.bottomrightblue.config(image = self.BLUESIMONOFF)

    def selectedTile(self, color):
        if(color == "green" ):
            self.topleftgreen.config(image = self.GREENSIMON)
        elif(color == "red" ):
            self.toprightred.config(image=self.REDSIMON)
        elif (color == "blue" ):
            self.bottomrightblue.config(image=self.BLUESIMON)
        elif (color == "yellow" ):
            self.bottomleftyellow.config(image=self.YELLOWSIMON)

        listofsoundspaths = [r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonsound1.wav",
                             r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonsound2.wav"]

        winsound.PlaySound((random.choice(listofsoundspaths)), winsound.SND_ASYNC + winsound.SND_FILENAME)

    def selectedGreen(self):
        if(self.isaLoss==False and self.isgameStarted == True and self.isPlayerTurn == True):
            self.selectedTile("green")
            self.Player.addSpecifiedTile("green")
            singlePlayerGUI.update()
            singlePlayerGUI.update_idletasks()
            self.after(self.gamespeed)
            self.resetTilesBlank()
    def selectedRed(self):
        if(self.isaLoss == False and self.isgameStarted == True and self.isPlayerTurn == True):
            self.selectedTile("red")
            self.Player.addSpecifiedTile("red")
            singlePlayerGUI.update()
            singlePlayerGUI.update_idletasks()
            self.after(self.gamespeed)
            self.resetTilesBlank()
    def selectedBlue(self):
        if(self.isaLoss==False and self.isgameStarted == True and self.isPlayerTurn == True):
            self.selectedTile("blue")
            self.Player.addSpecifiedTile("blue")
            singlePlayerGUI.update()
            singlePlayerGUI.update_idletasks()
            self.after(self.gamespeed)
            self.resetTilesBlank()
    def selectedYellow(self):
        if(self.isaLoss==False and self.isgameStarted == True and self.isPlayerTurn == True):
            self.selectedTile("yellow")
            self.Player.addSpecifiedTile("yellow")
            singlePlayerGUI.update()
            singlePlayerGUI.update_idletasks()
            self.after(self.gamespeed)
            self.resetTilesBlank()

    def updateLabels(self):
        self.scoreLabel.config(text = "Score: "+str(self.score))
        self.currentTurnLabel.config(text = "Current Turn:\n"+self.currentTurn)


    #CPU TURN
    def playCPUTURN(self):
        global whichGUI
        self.after(self.gamespeed*2)

        #prints the current Turn FOR TESTING PURPOSES
        #print(self.currentTurn)

        if(self.currentTurn=="cpu" and whichGUI == "singleMenu" and self.isaLoss == False):
            for i in self.CPU.listoftiles:
                self.selectedTile(i)
                self.after(self.gamespeed)
                self.update_idletasks()
                self.update()
                self.resetTilesBlank()
                self.after(self.gamespeed)
                self.update()
                self.update_idletasks()
                self.after(self.gamespeed)

            self.after(self.gamespeed)
            self.currentTurn = "player"
            self.isPlayerTurn = True
            self.Player.resetTileList()




    def startGame(self):
        self.currentTurn = "cpu"
        self.isgameStarted = True
        self.update()
        self.update_idletasks()
        self.startButton.grid_remove()
        self.playCPUTURN()


    def setGameSpeed(self, gamespeed):
        self.gamespeed = gamespeed



    def __init__(self,root):
        # game attributes
        self.score = 0
        self.NumberofCPUTiles = 2
        self.isaLoss = False
        self.isgameStarted = False
        self.isPlayerTurn = False

        #GAMESPEED
        #50 -> really fast
        #100 -> fast
        #150 -> medium
        #200 -> slow
        #300 -> really slow
        self.gamespeed = 150


        #cpu always goes first
        self.currentTurn = ""

        #CPU
        self.CPU = CPU(self.NumberofCPUTiles)

        #PLAYER
        self.Player  = SinglePlayer(0)

        #GUI
        super().__init__(root)

        # GAME CONSTANTS
        self.green = "GREEN"
        self.blue = "BLUE"
        self.yellow = "YELLOW"
        self.red = "RED"

        imagesize = 250

        YELLOWSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\yellowblink.png")
        YELLOWSIMON.thumbnail((imagesize, imagesize))
        self.YELLOWSIMON = ImageTk.PhotoImage(YELLOWSIMON)

        REDSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\redblink.png")
        REDSIMON.thumbnail((imagesize, imagesize))
        self.REDSIMON = ImageTk.PhotoImage(REDSIMON)

        BLUESIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\blueblink.png")
        BLUESIMON.thumbnail((imagesize, imagesize))
        self.BLUESIMON = ImageTk.PhotoImage(BLUESIMON)

        GREENSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\greenblink.png")
        GREENSIMON.thumbnail((imagesize, imagesize))
        self.GREENSIMON = ImageTk.PhotoImage(GREENSIMON)
#-----------------------------------------------------------------------

        YELLOWSIMONOFF = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\yellowoff.png")
        YELLOWSIMONOFF.thumbnail((imagesize, imagesize))
        self.YELLOWSIMONOFF = ImageTk.PhotoImage(YELLOWSIMONOFF)

        REDSIMONOFF = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\redoff.png")
        REDSIMONOFF.thumbnail((imagesize, imagesize))
        self.REDSIMONOFF = ImageTk.PhotoImage(REDSIMONOFF)

        BLUESIMONOFF = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\blueoff.png")
        BLUESIMONOFF.thumbnail((imagesize, imagesize))
        self.BLUESIMONOFF = ImageTk.PhotoImage(BLUESIMONOFF)

        GREENSIMONOFF = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\greenoff.png")
        GREENSIMONOFF.thumbnail((imagesize, imagesize))
        self.GREENSIMONOFF = ImageTk.PhotoImage(GREENSIMONOFF)

        BLANKSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\offsimon.png")
        BLANKSIMON.thumbnail((imagesize, imagesize))
        self.BLANKSIMON = ImageTk.PhotoImage(BLANKSIMON)


        #SINGLEPLAYER GUI
        self.board = Frame(self)
        self.board.grid(row = 5, column = 5)

        self.topleftgreen = Button(self.board, image = self.GREENSIMONOFF, command = self.selectedGreen)
        self.topleftgreen.grid(row = 0, column = 0)

        self.toprightred = Button(self.board, image = self.REDSIMONOFF,command = self.selectedRed)
        self.toprightred.grid(row = 0, column = 1)

        self.bottomleftyellow = Button(self.board, image = self.YELLOWSIMONOFF,command = self.selectedYellow)
        self.bottomleftyellow.grid(row=1,column=0)

        self.bottomrightblue = Button(self.board, image = self.BLUESIMONOFF,command = self.selectedBlue)
        self.bottomrightblue.grid(row=1,column=1)

        #The INFO side of GUI
        self.infoFrame = Frame(self)
        self.infoFrame.grid(row= 5, column = 6)

        self.startButton = Button(self.infoFrame, text = "Start", command =self.startGame, font = "none 20", bg = "light gray")
        self.startButton.grid(row = 0, column= 0, pady= 20)

        self.scoreLabel = Label(self.infoFrame,text = "Score: "+str(self.score), fg = "black", font = "none 20 bold")
        self.scoreLabel.grid(row=1,column = 0)

        self.currentTurnLabel = Label(self.infoFrame, text = "Current Turn:\n"+self.currentTurn, fg = "black", font = "none 20 bold")
        self.currentTurnLabel.grid(row= 2, column = 0)


class gameMenu(Frame):



    def changeTitleImage(self):
        listofimages = [self.REDSIMON,self.YELLOWSIMON,self.BLUESIMON,self.GREENSIMON,self.BLANKSIMON]

        listofsoundspaths = [r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonsound1.wav",
                             r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonsound2.wav"]

        self.titleimage.config(image =random.choice(listofimages))
        winsound.PlaySound((random.choice(listofsoundspaths)),winsound.SND_ASYNC+winsound.SND_FILENAME)


    def __init__(self, root):
        super().__init__(root)

        imagesize = 500

        YELLOWSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\yellowsimon.png")
        YELLOWSIMON.thumbnail((imagesize, imagesize))
        self.YELLOWSIMON = ImageTk.PhotoImage(YELLOWSIMON)

        REDSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\redsimon.png")
        REDSIMON.thumbnail((imagesize, imagesize))
        self.REDSIMON = ImageTk.PhotoImage(REDSIMON)

        BLUESIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\bluesimon.png")
        BLUESIMON.thumbnail((imagesize, imagesize))
        self.BLUESIMON = ImageTk.PhotoImage(BLUESIMON)

        GREENSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\greensimon.png")
        GREENSIMON.thumbnail((imagesize, imagesize))
        self.GREENSIMON = ImageTk.PhotoImage(GREENSIMON)

        BLANKSIMON = Image.open(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\offsimon.png")
        BLANKSIMON.thumbnail((imagesize, imagesize))
        self.BLANKSIMON = ImageTk.PhotoImage(BLANKSIMON)

        #self.listofsounds = (winsound.PlaySound(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonsound1.wav",winsound.SND_ASYNC+winsound.SND_FILENAME),
        #                winsound.PlaySound(

        self.title= Label(self, text ="SimonSays by Miguel Zavala")
        self.title.grid(row = 4, column = 5)

        self.titleimage = Label(self, image = self.BLANKSIMON)

        self.titleimage.grid(row=5,column=5)

        self.singleplayerButton = Button(self,text = "SinglePlayer", bg = "light gray")

        self.title = Label (self, text = "SimonSays \nby Miguel Zavala")
        self.singleplayerButton.grid(row= 7, column = 5)


#UNIVERSAL MENU
whichGUI = "gameMenu"

root  = Tk()
root.title("SimonSays by Miguel Zavala")
root.iconbitmap(r"C:\Users\Miguel\Desktop\EGGG\CISC108\FinishedProjects\SimonSays\simonicon.ico")


loseMenu1 = loseMenu(root)

whichGUI = "singleMenu"

singlePlayerGUI = singlePlayer(root)
singlePlayerGUI.grid()


#"Options" Menu
OptionsMenu = Menu()
subMenu = Menu()
root.config(menu = OptionsMenu)
OptionsMenu.add_cascade(menu = subMenu, label = "Options")

subMenu.add_cascade(label = "Set Difficulty Below")
subMenu.add_cascade(label = "Very Hard", command = lambda: singlePlayerGUI.setGameSpeed(50))
subMenu.add_cascade(label = "Hard", command = lambda: singlePlayerGUI.setGameSpeed(100))
subMenu.add_cascade(label = "Normal", command = lambda: singlePlayerGUI.setGameSpeed(150))
subMenu.add_cascade(label = "Easy", command = lambda: singlePlayerGUI.setGameSpeed(200))
subMenu.add_cascade(label = "Very Easy", command = lambda: singlePlayerGUI.setGameSpeed(300))
subMenu.add_separator()
subMenu.add_cascade(label = "New Game", command = loseMenu1.createNewGame)



gameMenu1 = gameMenu(root)
root.grid()
#gameMenu1.grid()


def playSingle():
    global whichGUI
    gameMenu1.grid_remove()
    whichGUI = "singleMenu"
    singlePlayerGUI.grid()
gameMenu1.singleplayerButton.config(command = playSingle)

def checkIfLoss():
    if(singlePlayerGUI.isaLoss==True):
        singlePlayerGUI.grid_remove()
        loseMenu1.grid()

ms = 0
s = 1
m = 0
h = 0

while True:
    root.after(100)
    print(singlePlayerGUI.isPlayerTurn)


    #Checks if the player has equal tiles as the CPU and updates labels(who's turn it is, the score)
    if(whichGUI=="singleMenu" and singlePlayerGUI.isaLoss==False):
        singlePlayerGUI.checkIfEqualTiles()
        singlePlayerGUI.updateLabels()

        #PRINTS Player's Listoftiles FOR TESTING PURPOSES ONLY**
        #print(singlePlayerGUI.Player.listoftiles)

    #Checks if the player has lost
    checkIfLoss()

    #game variable tracker (keeps track of the game time in ms)
    ms +=100

    if(ms==1000):
        s+=1
        ms=0

    if(s ==60):
        m+=1


    if(m==60):
        h+=1


    if(s%2==0 and whichGUI =="gameMenu"):
        gameMenu1.changeTitleImage()

    root.update()
    root.update_idletasks()




