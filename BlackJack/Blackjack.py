#Library Imports
from tkinter.font import Font
import requests
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import io
from urllib.request import urlopen

"""---------------------------------------------------------- Card Class -----------------------------------------------------------------------------------------"""
class Card:
    #Default Constructor
    def __init__(self):
        self.suit = None
        self.value = None
        self.imageUrl = None
        self.code = None
        self.image = None

    #Constructor
    def __init__(self, suit, value, imageUrl, code):
        self.suit = suit
        self.value= None
        self.set_value(value)
        self.imageUrl = imageUrl
        self.code = code
        self.image = self.get_card_image()

    #Set Suit
    def set_suit(self, suit):
        self.suit = suit

    #Set value, if the value is king, queen, or jack =10; ace =11
    def set_value(self, value):
        if isinstance(value, str):
            if value.upper() == 'QUEEN' or value == 'KING' or value == 'JACK':
                self.value = 10
            elif value.upper() == "ACE":
                self.value = 11
            else:
                self.value = int(value)
        else:
            self.value = int(value)

    #set the image Url and get the image associated
    def set_imageUrl(self, url):
        self.imageUrl = url
        self.image = self.get_card_image()

    #set the code
    def set_code(self, code):
        self.code = code        

    #get the card image from the url
    def get_card_image(self):
        #get the image from the API's URL
        imageUrlInfo = requests.get(self.imageUrl)
        #Turn the image into bytes
        image_bytes = io.BytesIO(imageUrlInfo.content)
        #turn it into a usable PhotoImage from TK
        imageToDisplay = ImageTk.PhotoImage(Image.open(image_bytes))
        #Print a str format of the image
        print("\nREQUEST: " + str(imageToDisplay))
        #return the image
        return imageToDisplay

    #display the card given the x, y coords
    def display_card(self, canvas, x, y):
        #if the url is not NULL/None
        if self.imageUrl != None:
            #create card image on given canvas at x,y
            canvas.create_image(x, y, image=self.image)
        else:
            print("No Image to Display")

"""---------------------------------------------------------- /Card Class -----------------------------------------------------------------------------------------"""

"""---------------------------------------------------------- Player Class -----------------------------------------------------------------------------------------"""
class Player:
    def __init__(self):
        self.wins = None
        self.loses = None

    def __init__(self, wins, loses):
        self.wins = int(wins)
        self.loses = int(loses)

    def updateFile(self):
        file = open("W-L", 'w')
        file.write(str(self.wins) + "\n")
        file.write(str(self.loses))
        file.close()
    
    def updateGUI(self):
        winCountLabelStr.set(self.wins)
        loseCountLabelStr.set(self.loses)

"""---------------------------------------------------------- /Player Class -----------------------------------------------------------------------------------------"""


"""---------------------------------------------------------- Functions -----------------------------------------------------------------------------------------"""
"""
Player draws a new card, if they go over 21 they bust, otherwise add the totals together
"""
def hit():
    #draw a card for the player hit
    hitrequest = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=1")
    print(hitrequest)
    print("Drawing card for player's hit....")

    print("Deck: " + str(hitrequest.content))

    #json form of the cards
    hitCard = hitrequest.json()
    print("\n\PLAYERHAND: " + str(hitCard) + "\n\n")
    print("HAND: " + str(hitCard['cards']))

    #convert into Card Obj form
    newCard = Card(hitCard['cards'][0]['suit'], hitCard['cards'][0]['value'], hitCard['cards'][0]['image'], hitCard['cards'][0]['code'])
    #add card to list
    playerCards.append(newCard)

    if len(playerCards) < 6:
        #draw the card
        newCard.display_card(playerCanvas, 230*(len(playerCards)-1)+250 ,300)
    else:
        newCard.display_card(playerCanvas, 230*((len(playerCards)%6))+250 ,350)

    #Get the new total and display it
    newTotal = getTotal(playerCards)
    handTotal.set(newTotal)

    #check if player busted
    if newTotal > 21:
        busted()
        player.loses +=1
        player.updateFile()
        player.updateGUI()
        

"""
Player keeps the hand they have and compares it to the dealer, if they have higher they win
"""
def stay():
    #if the player has not busted
    if bust == False:
        pass
    #Show dealer's first card
    dealerCards[0].display_card(dealerCanvas, 230*0+250, 300)
    #Get total of dealers
    dealersTotal = getTotal(dealerCards)
    if dealersTotal > getTotal(playerCards):
        loseLabel = Label(dealerCanvas, text="You Lose", font=hfont, bg="red")
        loseLabel.place(relheight=0.25, relwidth=0.25, relx=0.5, rely=0.5, anchor="center")
        #Create a button to play again and pass the previous label to destroy, if played again
        playAgainButton = Button(canvasBack, text="Play Again", font=hfont, command= lambda: playagain(loseLabel, playAgainButton))
        #add to loses
        player.loses +=1
        player.updateFile()
        player.updateGUI()
        
    else:
        player.wins +=1
        player.updateFile()
        player.updateGUI()
        winLabel = Label(dealerCanvas, text="You Win", font=hfont, bg="#39e75f")
        winLabel.place(relheight=0.25, relwidth=0.25, relx=0.5, rely=0.5, anchor="center")
        #Create a button to play again and pass the previous label to destroy, if played again
        playAgainButton = Button(canvasBack, text="Play Again", font=hfont, command= lambda: playagain(winLabel, playAgainButton))
    #Disable hit button and stay button
    hitButton.config(state=DISABLED)
    stayButton.config(state=DISABLED)
    #Place the button to play again
    playAgainButton.place(relheight=0.05, relwidth=0.075, relx=0.05, rely=0.9)

def busted():
    bust = True
    #Display Dealer Card
    dealerCards[0].display_card(dealerCanvas, 230*0+250, 300)
    #Create label to say Busted on screen
    bustedLabel = Label(playerCanvas, text="BUSTED", font=hfont, fg="red", bg="#ab23ff")
    bustedLabel.place(relheight=0.25, relwidth=0.25, relx=0.5, rely=0.5, anchor="center")
    #Disable hit button and stay button
    hitButton.config(state=DISABLED)
    stayButton.config(state=DISABLED)
    #Create button to play again
    playAgainButton = Button(canvasBack, text="Play Again", font=hfont, command= lambda: playagain(bustedLabel, playAgainButton))
    playAgainButton.place(relheight=0.05, relwidth=0.075, relx=0.05, rely=0.9)

"""
Gets the total amount that the cards add up to
"""
def getTotal(cards):
    #total init
    total = 0
    #check if cards is a list
    if isinstance(cards, list):
        #loop through cards
        for card in cards:
            #if the cards are Card objects
            if isinstance(card, Card):
                #add the total 
                total += int(card.value)
            #if total > 21 (busted)
            if total > 21:
                #loop through cards to check for aces
                for card in cards:
                    #Ace is found
                    if card.value == 11 and total > 21:
                        #set ace to 1
                        card.set_value(1)
                        #remove 10 from total
                        total -= 10
                        
    else:
        raise Exception("Trying to get total of non-Cards!!!!")

    return total 

"""
Play the game again (reset the game)
:param label: LabelToDelete
:param playAgainButton: Button calling playagain to delete
"""
def playagain(label, playAgainButton):
    #reset busted and delete label and delete button
    label.destroy()
    playAgainButton.destroy()
    bust = False
    #Enable the buttons again
    hitButton.config(state=NORMAL)
    stayButton.config(state=NORMAL)

    #clear cards from board
    playerCanvas.delete("all")
    dealerCanvas.delete("all")

    #reset the deck
    shuffleRequest = requests.get(baseURL + "/api/deck/" + deckJSON['deck_id'] + "/shuffle/")
    print("\n\n\nDEBUG:::::::::::::::::::SHUFFLE COMPLETE\n\n" + str(shuffleRequest.content))

    #reset cardArrays
    playerCards.clear()
    dealerCards.clear()

    print("ALL CARD ARRAYS CLEARED::::::::" + str(playerCards) + " " + str(dealerCards))

    #draw 2 cards from the deck for dealer's cards
    request2 = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=2")
    print(request2)
    print("Drawing dealer's cards...")

    print("Deck: " + str(request2.content))

    #json form of the cards
    dealerHand = request2.json()
    print("\n\DEALERHAND: " + str(dealerHand) + "\n\n")
    print("HAND: " + str(dealerHand['cards']))

    #create a list of cards and add the drawn cards to the list as a Card Object for dealer
    for i in range(len(dealerHand['cards'])):
        newCard = Card(dealerHand['cards'][i]['suit'], dealerHand['cards'][i]['value'], dealerHand['cards'][i]['image'], dealerHand['cards'][i]['code'])
        dealerCards.append(newCard)

    #draw 2 cards from the deck for player's cards
    request2 = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=2")
    print(request2)
    print("Drawing player's cards...")

    print("Deck: " + str(request2.content))

    #json form of the cards
    playerHand = request2.json()
    print("\n\PLAYERHAND: " + str(playerHand) + "\n\n")
    print("HAND: " + str(playerHand['cards']))

    #create a list of cards and add the drawn cards to the list as a Card Object for player
    for i in range(len(playerHand['cards'])):
        newCard = Card(playerHand['cards'][i]['suit'], playerHand['cards'][i]['value'], playerHand['cards'][i]['image'], playerHand['cards'][i]['code'])
        playerCards.append(newCard)

    #Display the cards drawn for the dealer
    for i in range(len(dealerCards)):
        print("I: " + str(i))
        #if it's the first card:
        if i == 0:
            dealerCanvas.create_image((230*i+250, 300), image=deckGraphicImage)
        #otherwise draw it
        else:
            dealerCards[i].display_card(dealerCanvas, 230*i+250, 300)

    #Display the cards drawn for the player
    for i in range(len(playerCards)):
        playerCards[i].display_card(playerCanvas, 230*i+250, 300)

    handTotal.set(getTotal(playerCards))


def initGame():
    pass
"""---------------------------------------------------------- /Functions -----------------------------------------------------------------------------------------"""



"""---------------------------------------------------------- GUI -----------------------------------------------------------------------------------------"""
"""
Create the main window and a frame to put everthing in
"""
#TK main window
rootWindow = tk.Tk()
rootWindow.title("BlackJack")
rootWindow.geometry("1920x1080")

#Create frame for items to go into
frame1 = Frame(rootWindow, bg="green", bd=1, relief=SUNKEN)
#frame1.grid_propagate(False)
frame1.place(relheight=1, relwidth=1)


"""
Create a graphic for the deck at the bottom of the screen and back of cards
"""
#Open graphic for deck back
deckGraphicUrl = urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Card_back_06.svg/1200px-Card_back_06.svg.png")
readURL = deckGraphicUrl.read()
deckGraphicUrl.close()

#Resize deck back image
deckGraphicImageResize = Image.open(io.BytesIO(readURL)).resize([226,316])
#Convert deck back image into tkinter formatting
deckGraphicImage = ImageTk.PhotoImage(deckGraphicImageResize)
#display deck back graphic

"""---------------------------------------------------------- API -----------------------------------------------------------------------------------------"""

#API base url
baseURL = "http://deckofcardsapi.com/"

#Create new deck from API
deck = requests.get(baseURL + "api/deck/new/")
#deck in json format for deck_id and success
deckJSON = deck.json()
print("deckJSON: " + str(deckJSON))

#shuffle the cards
deck = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/shuffle/")
print("\nShuffling...\n")

print("Deck: " + str(deck.content))

#draw 2 cards from the deck for dealer's cards
request2 = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=2")
print(request2)
print("Drawing dealer's cards...")

print("Deck: " + str(request2.content))

#json form of the cards
dealerHand = request2.json()
print("\n\DEALERHAND: " + str(dealerHand) + "\n\n")
print("HAND: " + str(dealerHand['cards']))

#create a list of cards and add the drawn cards to the list as a Card Object for dealer
dealerCards = []
for i in range(len(dealerHand['cards'])):
    newCard = Card(dealerHand['cards'][i]['suit'], dealerHand['cards'][i]['value'], dealerHand['cards'][i]['image'], dealerHand['cards'][i]['code'])
    dealerCards.append(newCard)

#draw 2 cards from the deck for player's cards
request2 = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=2")
print(request2)
print("Drawing player's cards...")

print("Deck: " + str(request2.content))

#json form of the cards
playerHand = request2.json()
print("\n\PLAYERHAND: " + str(playerHand) + "\n\n")
print("HAND: " + str(playerHand['cards']))

#create a list of cards and add the drawn cards to the list as a Card Object for player
playerCards = []
for i in range(len(playerHand['cards'])):
    newCard = Card(playerHand['cards'][i]['suit'], playerHand['cards'][i]['value'], playerHand['cards'][i]['image'], playerHand['cards'][i]['code'])
    playerCards.append(newCard)

"""---------------------------------------------------------- /API -----------------------------------------------------------------------------------------"""

hfont = Font(family="Helvetica", size=18, weight="bold")


"""
Create canvas's and frames for the cards
"""
#Create a canvas for the background
canvasBack = tk.Canvas(frame1, bg="green")
canvasBack.place(relheight=1,relwidth=1)


"""
Create a canvas for the dealer's cards
"""
#Create a frame for the dealer cards
dealerFrame = Frame(frame1, bg="green", bd=1, relief=SUNKEN)
dealerFrame.place(relheight=0.5, relwidth=0.6, rely=0.05, relx=0.5, anchor="n")
#Create a canvas to draw the dealer's cards on
dealerCanvas = Canvas(dealerFrame, bg="green")
dealerCanvas.place(relheight=1, relwidth=1)
Label(dealerCanvas, text="Dealer", bg="green").place(relheight=0.09, relwidth=0.09)


"""
Create a canvas for the player's cards
"""
#Create a frame fro the player cards
playerFrame = Frame(frame1, bg="green", bd=1, relief=SUNKEN)
playerFrame.place(relheight=0.35, relwidth=0.6, rely=0.95, relx=0.5, anchor="s")
#Create a canvas to draw the cards on
playerCanvas = Canvas(playerFrame, bg="green")
playerCanvas.place(relheight=1, relwidth=1)
Label(playerCanvas, text="Your cards", bg="green").place(relheight=0.09, relwidth=0.09)


"""
Create the hit and stay buttons
"""
#Hit button
hitButton = Button(canvasBack, text="Hit", font=hfont, padx=1, pady=1, command=hit)
hitButton.place(relheight=0.05, relwidth=0.075, relx=0.05, rely=0.65)
#Stay Button
stayButton = Button(canvasBack, text="Stay", font=hfont, padx=1, pady=1, command=stay)
stayButton.place(relheight=0.05, relwidth=0.075, relx=0.05, rely=0.725)


"""
Give the player a 'total' amount the cards are worth in their hand
"""
#label for 'Total'
Label(canvasBack, text="Total:", bg="green", font=hfont).place(relx=0.035, rely=0.82)

handTotal = StringVar(canvasBack, '000')
handTotalLabel = Label(canvasBack, textvariable=handTotal, bg="green", font=hfont).place(relx=0.07, rely=0.82)

handTotal.set(str(getTotal(playerCards)))
print("\n\n\n\DEBUG::::::::::" + str(getTotal(playerCards)))

"""
Create a win/lose counter and Labels
"""
#label for "win"
Label(canvasBack, text="Wins:", bg="green", font=hfont).place(relx=0.035, rely=0.15)
#label for "lose"
Label(canvasBack, text="Loses:", bg="green", font=hfont).place(relx=0.035, rely=0.2)

#counters Labels
winCountLabelStr = StringVar()
winCountLabel = Label(canvasBack, textvariable=winCountLabelStr, bg="green", font=hfont)
winCountLabel.place(relx=0.07, rely=0.15)
loseCountLabelStr = StringVar()
loseCountLabel = Label(canvasBack, textvariable=loseCountLabelStr, bg="green", font=hfont)
loseCountLabel.place(relx=0.07, rely=0.2)

#Get the loses and wins from file
file = open("W-L", 'r')
wins = file.readline()
print("WINS:::::" + str(wins))
winCountLabelStr.set(wins)
loseCountLabelStr.set(file.readline())
print("WINS FROM FILE::::::" + str(winCountLabelStr.get()))
print("LOSES FROM FILE::::::" + str(loseCountLabelStr.get()))
file.close()

player = Player(winCountLabelStr.get(), loseCountLabelStr.get())

"""
Display the cards
"""
#Place back of card graphic on the bottom right to be the deck
deckGraphic = canvasBack.create_image((rootWindow.winfo_screenwidth() - 326),(rootWindow.winfo_screenheight() - 416), anchor="center", image=deckGraphicImage, tags=["nonMovable","deck"])


#Display the cards drawn for the dealer
for i in range(len(dealerCards)):
    print("I: " + str(i))
    #if it's the first card:
    if i == 0:
        dealerCanvas.create_image((230*i+250, 300), image=deckGraphicImage)
    #otherwise draw it
    else:
        dealerCards[i].display_card(dealerCanvas, 230*i+250, 300)

#Display the cards drawn for the player
for i in range(len(playerCards)):
    playerCards[i].display_card(playerCanvas, 230*i+250, 300)

bust = False


"""---------------------------------------------------------- /GUI -----------------------------------------------------------------------------------------"""


#Main loop for GUI/Program
rootWindow.mainloop()
