import numpy as np
from tkinter import *
from PIL import ImageTk, Image, ImageOps
import math

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        self.deck = []

    def populate(self):
        for suit in ["Diamonds", "Clubs", "Hearts", "Spades"]:
            for number in range(1, 14):
                self.deck.append(Card(suit, number))

    def shuffle(self):
        np.random.shuffle(self.deck)

    def deal(self):
        self.deck.pop(0)
        self.deck.pop(1)
        self.deck.pop(2)
        return [self.deck[0], self.deck[1], self.deck[2]]

def show(sumen, psum, label, e1, e2, e3, eh, ec1, ec2, ec3):

    global pot, playerpts, playerptslabel, potlabel, eptslabel, epts, nextroundbtn, turn

    if (turn == 0):

        io1 = Image.open("./sprites/" + str(eh[0].suit) + ".png")
        pi1 = ImageTk.PhotoImage(ImageOps.flip(io1))
        io2 = Image.open("./sprites/" + str(eh[1].suit) + ".png")
        pi2 = ImageTk.PhotoImage(ImageOps.flip(io2))
        io3 = Image.open("./sprites/" + str(eh[2].suit) + ".png")
        pi3 = ImageTk.PhotoImage(ImageOps.flip(io3))

        ec1.configure(image=pi1)
        ec1.image=pi1
        ec2.configure(image=pi2)
        ec2.image=pi2
        ec3.configure(image=pi3)
        ec3.image=pi3

        e1["text"] = eh[0].number
        e2["text"] = eh[1].number
        e3["text"] = eh[2].number

        if abs(21 - psum) < abs(21 - sumen): 
            label["text"] = "You win!"
            playerpts = playerpts + pot
            pot = 10
            playerptslabel["text"]="Balance: " + str(int(playerpts))
            potlabel["text"] = "Pot: " + str(int(pot))
            nxtroundbtn.place(height=50, width=150, x=600, y=510)
            
        if abs(21 - psum) > abs(21 - sumen): 
            label["text"] = "You lose!"
            epts = epts + pot
            pot = 10
            eptslabel["text"] = "Enemy Balance: " + str(int(epts))
            playerptslabel["text"]="Balance: " + str(int(playerpts))
            potlabel["text"] = "Pot: " + str(int(pot))
            nxtroundbtn.place(height=50, width=150, x=600, y=510)

        if abs(21 - psum) == abs(21 - sumen):
            label["text"] = "It's a tie!"
            playerpts = playerpts + math.floor(pot/2)
            epts = epts + math.floor(pot/2)
            pot = 10
            nxtroundbtn.place(height=50, width=150, x=600, y=510)
        turn = 2
    else:
        return

def fold():
    global viclabel, nxtroundbtn, pot, playerpts, playerptslabel, potlabel, eptslabel, epts
    viclabel["text"]="You Lose!"
    epts = epts + pot
    pot = 10
    nxtroundbtn.place(height=50, width=150, x=600, y=510)

def raisepot():
    global pot
    global playerpts
    global playerptslabel
    global potlabel
    global turn

    reduce = math.floor(pot/2)

    if (reduce > playerpts):
        return
    
    else:
        if (turn == 0):
            playerpts = playerpts - reduce
            playerptslabel["text"] = "Balance: " + str(playerpts)
            pot = pot + reduce
            potlabel["text"]=("Pot: " + str(pot))
            swapturn()
        else:
            return

def swapturn():
    
    global turn
    print(turn)
    if turn == 0: 
        turn = 1
        evaluate()
    else:
        turn = 0

def eraise():
    global pot
    global epts
    global eptslabel
    global potlabel
    global turn

    reduce = math.floor(pot/2)

    if (reduce > epts):
        return
    
    else:
        if (turn == 1):
            epts = epts - reduce
            eptslabel["text"] = "Enemy Balance: " + str(epts)
            pot = pot + reduce
            potlabel["text"]=("Pot: " + str(pot))
            swapturn()
        else:
            return

def efold():
    global viclabel, nxtroundbtn, pot, playerpts, playerptslabel, potlabel, eptslabel, epts
    viclabel["text"]="You Win!"
    playerpts = playerpts + pot
    pot = 10
    nxtroundbtn.place(height=50, width=150, x=600, y=510)

def evaluate():
    global enemysum, handsum, viclabel, ecard1, ecard2, ecard3, enemyhand, ecard1imglabel, ecard2imglabel, ecard3imglabel

    if (turn == 1):
        if (enemysum >= 16 and enemysum <= 26 and pot <= 30):
            #raise
            eraise()
            return
        elif (enemysum >= 18 and enemysum <= 24 and pot <= 60):
            #raise
            eraise()
            return
        elif (enemysum >= 19 and enemysum <= 23 and pot <= 80):
            #raise
            eraise()
            return
        elif (enemysum >= 16 and enemysum <= 26 and pot > 30):
            eshow(enemysum, handsum, viclabel, ecard1, ecard2, ecard3, enemyhand, ecard1imglabel, ecard2imglabel, ecard3imglabel)
            return
        elif (enemysum >= 18 and enemysum <= 24 and pot > 60):
            eshow(enemysum, handsum, viclabel, ecard1, ecard2, ecard3, enemyhand, ecard1imglabel, ecard2imglabel, ecard3imglabel)
            return
        elif (enemysum >= 19 and enemysum <= 23 and pot > 80):
            eshow(enemysum, handsum, viclabel, ecard1, ecard2, ecard3, enemyhand, ecard1imglabel, ecard2imglabel, ecard3imglabel)
            return
        elif (enemysum == 21):
            #raise
            eraise()
            return
        elif (enemysum > 26):
            #fold
            efold()
            return
        elif (enemysum < 16):
            #fold
            efold()
            return

def eshow(sumen, psum, label, e1, e2, e3, eh, ec1, ec2, ec3):

    global pot, playerpts, playerptslabel, potlabel, eptslabel, epts, nxtroundbtn, turn

    if (turn == 1):

        io1 = Image.open("./sprites/" + str(eh[0].suit) + ".png")
        pi1 = ImageTk.PhotoImage(ImageOps.flip(io1))
        io2 = Image.open("./sprites/" + str(eh[1].suit) + ".png")
        pi2 = ImageTk.PhotoImage(ImageOps.flip(io2))
        io3 = Image.open("./sprites/" + str(eh[2].suit) + ".png")
        pi3 = ImageTk.PhotoImage(ImageOps.flip(io3))

        ec1.configure(image=pi1)
        ec1.image=pi1
        ec2.configure(image=pi2)
        ec2.image=pi2
        ec3.configure(image=pi3)
        ec3.image=pi3

        e1["text"] = eh[0].number
        e2["text"] = eh[1].number
        e3["text"] = eh[2].number

        if abs(21 - psum) < abs(21 - sumen): 
            label["text"] = "You win!"
            playerpts = playerpts + pot
            pot = 10
            playerptslabel["text"]="Balance: " + str(int(playerpts))
            potlabel["text"] = "Pot: " + str(int(pot))
            nxtroundbtn.place(height=50, width=150, x=600, y=510)
            
        if abs(21 - psum) > abs(21 - sumen): 
            label["text"] = "You lose!"
            epts = epts + pot
            pot = 10
            eptslabel["text"] = "Enemy Balance: " + str(int(epts))
            playerptslabel["text"]="Balance: " + str(int(playerpts))
            potlabel["text"] = "Pot: " + str(int(pot))
            nxtroundbtn.place(height=50, width=150, x=600, y=510)

        if abs(21 - psum) == abs(21 - sumen):
            label["text"] = "It's a tie!"
            playerpts = playerpts + math.floor(pot/2)
            epts = epts + math.floor(pot/2)
            pot = 10
            nxtroundbtn.place(height=50, width=150, x=600, y=510)
        turn = 2
    else:
        return
    
def nextround():
    global Deck, turn, pot, hand, enemyhand, handsum, enemysum, nextroundbtn, viclabel, ecard1imglabel, ecard2imglabel, ecard3imglabel, ecard1imgtk, ecard2imgtk
    global ecard3imgtk, ecard1, ecard2, ecard3, card1, card2, card3, card1imglabel, card2imglabel, card3imglabel, card1imgtk, card2imgtk, card3imgtk, card1img
    global card2img, card3img, potlabel, playerptslabel, eptslabel
    Deck.deck = []
    Deck.populate()
    Deck.shuffle()
    hand = Deck.deal()
    enemyhand = Deck.deal()
    viclabel["text"] = ""
    turn = 0
    ecard1imglabel["image"] = ecard1imgtk
    ecard2imglabel["image"] = ecard2imgtk
    ecard3imglabel["image"] = ecard3imgtk
    ecard1["text"] = ""
    ecard2["text"] = ""
    ecard3["text"] = ""
    potlabel["text"] = "Pot: " + str(pot)
    playerptslabel["text"] = "Balance: " + str(int(playerpts))
    eptslabel["text"] = "Enemy Balance: " + str(int(epts)) 
    card1["text"] = str(hand[0].number)
    card2["text"] = str(hand[1].number)
    card3["text"] = str(hand[2].number)
    card1img = Image.open("./sprites/" + str(hand[0].suit) + ".png")
    card2img = Image.open("./sprites/" + str(hand[1].suit) + ".png")
    card3img = Image.open("./sprites/" + str(hand[2].suit) + ".png")
    card1imgtk = ImageTk.PhotoImage(card1img)
    card2imgtk = ImageTk.PhotoImage(card2img)
    card3imgtk = ImageTk.PhotoImage(card3img)
    card1imglabel.image = card1imgtk
    card2imglabel.image = card2imgtk
    card3imglabel.image = card3imgtk
    card1imglabel.configure(image=card1imgtk)
    card2imglabel.configure(image=card2imgtk)
    card3imglabel.configure(image=card3imgtk)
    handsum = hand[0].number + hand[1].number + hand[2].number
    enemysum = enemyhand[0].number + enemyhand[1].number + enemyhand[2].number
    nxtroundbtn.place_forget()


Deck = Deck()
Deck.populate()
Deck.shuffle()
hand = Deck.deal()
enemyhand = Deck.deal()
pot = 10

# 0 = player's turn, 1 = cpu's turn
turn = 0

playerpts = 100
epts = 100

root = Tk()
root.geometry("800x800")
root.title("Blackjack")
root.configure(bg="green")
card1 = Label(root, text=str(hand[0].number), bg="green")
card2 = Label(root, text=str(hand[1].number), bg="green")
card3 = Label(root, text=str(hand[2].number), bg="green")
viclabel = Label(root, bg="green")
card1img = Image.open("./sprites/" + str(hand[0].suit) + ".png")
card2img = Image.open("./sprites/" + str(hand[1].suit) + ".png")
card3img = Image.open("./sprites/" + str(hand[2].suit) + ".png")
card1imgtk = ImageTk.PhotoImage(card1img)
card2imgtk = ImageTk.PhotoImage(card2img)
card3imgtk = ImageTk.PhotoImage(card3img)
card1imglabel = Label(image=card1imgtk)
card2imglabel = Label(image=card2imgtk)
card3imglabel = Label(image=card3imgtk)

potlabel = Label(root, text="Pot: " + str(pot), bg="green")
playerptslabel = Label(root, text="Balance: " + str(int(playerpts)), bg="green")
eptslabel = Label(root, text="Enemy Balance: " + str(int(epts)), bg="green")

ecard1img = Image.open("./sprites/Back.png")
ecard2img = Image.open("./sprites/Back.png")
ecard3img = Image.open("./sprites/Back.png")
ecard1imgtk = ImageTk.PhotoImage(ecard1img)
ecard2imgtk = ImageTk.PhotoImage(ecard2img)
ecard3imgtk = ImageTk.PhotoImage(ecard3img)
ecard1imglabel = Label(image=ecard1imgtk)
ecard2imglabel = Label(image=ecard2imgtk)
ecard3imglabel = Label(image=ecard3imgtk)
ecard1 = Label(root, bg="green")
ecard2 = Label(root, bg="green")
ecard3 = Label(root, bg="green")

handsum = hand[0].number + hand[1].number + hand[2].number
enemysum = enemyhand[0].number + enemyhand[1].number + enemyhand[2].number

showbtn = Button(root, text="Show!", command= lambda: show(enemysum, handsum, viclabel, ecard1, ecard2, ecard3, enemyhand, ecard1imglabel, ecard2imglabel, ecard3imglabel))
foldbtn = Button(root, text="Fold!", command= fold)
raisebtn = Button(root, text="Raise!", command = raisepot)
nxtroundbtn = Button(root, text="Next Round!", command = nextround)


# for card in hand:
#     print(str(card.number) + " of " + card.suit)

# for card in enemyhand:
#     print(str(card.number) + " of " + card.suit)

# card1.place(x=150, y=665)
# card2.place(x=300, y=665)
# card3.place(x=450, y=665)
showbtn.place(height=50, width=150, x=600, y=600)
foldbtn.place(height=50, width=150, x=600, y=700)
viclabel.place(x=650,y=580)
card1.place(x=175, y=600)
card2.place(x=325, y=600)
card3.place(x=475, y=600)
card1imglabel.place(x=150, y=620)
card2imglabel.place(x=300, y=620)
card3imglabel.place(x=450, y=620)
ecard1imglabel.place(x=150, y=120)
ecard2imglabel.place(x=300, y=120)
ecard3imglabel.place(x=450, y=120)
ecard1.place(x=175, y=255)
ecard2.place(x=325, y=255)
ecard3.place(x=475, y=255)
potlabel.place(x=650, y=400)
playerptslabel.place(x=30, y=450)
eptslabel.place(x=30, y=350)
raisebtn.place(height=50, width=150, x=600, y=420)
# nxtroundbtn.place(height=50, width=150, x=600, y=510)
# nxtroundbtn.place_forget()




root.mainloop()

# cmd = input("What do you want to do? ")
# if (cmd == "fold"):
#     exit()
# if (cmd == "show"):
#     if abs(21 - handsum) < abs(21 - enemysum): 
#         print("You win!")
#     if abs(21 - handsum) > abs(21 - enemysum): 
#         print("You lose!")
#     if abs(21 - handsum) == abs(21 - enemysum):
#         print("It's a tie!")


