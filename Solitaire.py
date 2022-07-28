"""
TODO
Create piles for:
    each hole
    discard
Fix printing card images
Make game rules
Add stacking mechanic
Fix All Bugs
Fix window size/ resizing
Figure out how to turn and unturn initial cards around
Find way to match card GUI to slot or card attributes
"""

#Library Imports
import requests
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import io
from urllib.request import urlopen

#Cards Master Lists for checking
masterCardListSpade = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS']
masterCardListClub = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC']
masterCardListHeart = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH']
masterCardListDiamond = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD']
masterCardEmptyListHeart = []
masterCardEmptyListSpade = []
masterCardEmptyListClub = []
masterCardEmptyListDiamond = []

#Arrays for each card playing slot
slot0 = []
slot1 = []
slot2 = []
slot3 = []
slot4 = []
slot5 = []
slot6 = []

#Slot GUI areas
#slot0GUI = [(rootWindow.winfo_screenwidth() - 100), 50, (rootWindow.winfo_screenwidth() - 320), 362]

"""---------------------------------------------------------- Functions -----------------------------------------------------------------------------------------"""

def updateSlots():
    global slot0card0, slot1card0, slot2card0, slot3card0, slot4card0, slot5card0, slot6card0
    global slot1card1, slot2card1, slot3card1, slot4card1, slot5card1, slot6card1
    global slot2card2, slot3card2, slot4card2, slot5card2, slot6card2
    global slot3card3, slot4card3, slot5card3, slot6card3
    global slot4card4, slot5card4, slot6card4
    global slot5card5, slot6card5
    global slot6card6
    slot0card0 = slotCardToImage(slot0[0])
    canvasBack.create_image(32, 32, anchor="nw", image=slot0card0, tags=["card", slot0[0]['code']])
    slot1card0 = slotCardToImage(slot1[0])
    canvasBack.create_image(282, 32, anchor="nw", image=slot1card0, tags=["card", slot1[0]['code']])
    slot2card0 = slotCardToImage(slot2[0])
    canvasBack.create_image(532, 32, anchor="nw", image=slot2card0, tags=["card", slot2[0]['code']])
    slot3card0 = slotCardToImage(slot3[0])
    canvasBack.create_image(782, 32, anchor="nw", image=slot3card0, tags=["card", slot3[0]['code']])
    slot4card0 = slotCardToImage(slot4[0])
    canvasBack.create_image(1032, 32, anchor="nw", image=slot4card0, tags=["card", slot4[0]['code']])
    slot5card0 = slotCardToImage(slot5[0])
    canvasBack.create_image(1282, 32, anchor="nw", image=slot5card0, tags=["card", slot5[0]['code']])
    slot6card0 = slotCardToImage(slot6[0])
    canvasBack.create_image(1532, 32, anchor="nw", image=slot6card0, tags=["card", slot6[0]['code']])

    slot1card1 = slotCardToImage(slot1[1])
    canvasBack.create_image(282, 102, anchor='nw', image=slot1card1, tags=["card", slot1[1]['code']])
    slot2card1 = slotCardToImage(slot2[1])
    canvasBack.create_image(532, 102, anchor='nw', image=slot1card1, tags=["card", slot2[1]['code']])
    slot3card1 = slotCardToImage(slot3[1])
    canvasBack.create_image(782, 102, anchor="nw", image=slot3card1, tags=["card", slot3[1]['code']])
    slot4card1 = slotCardToImage(slot4[1])
    canvasBack.create_image(1032, 102, anchor="nw", image=slot4card1, tags=["card", slot4[1]['code']])
    slot5card1 = slotCardToImage(slot5[1])
    canvasBack.create_image(1282, 102, anchor="nw", image=slot5card1, tags=["card", slot5[1]['code']])
    slot6card1 = slotCardToImage(slot6[1])
    canvasBack.create_image(1532, 102, anchor="nw", image=slot6card1, tags=["card", slot6[1]['code']])

    slot2card2 = slotCardToImage(slot2[2])
    canvasBack.create_image(532, 172, anchor='nw', image=slot2card2, tags=["card", slot2[2]['code']])
    slot3card2 = slotCardToImage(slot3[2])
    canvasBack.create_image(782, 172, anchor='nw', image=slot3card2, tags=["card", slot3[2]['code']])
    slot4card2 = slotCardToImage(slot4[2])
    canvasBack.create_image(1032, 172, anchor="nw", image=slot4card2, tags=["card", slot4[2]['code']])
    slot5card2 = slotCardToImage(slot5[2])
    canvasBack.create_image(1282, 172, anchor="nw", image=slot5card2, tags=["card", slot5[2]['code']])
    slot6card2 = slotCardToImage(slot6[2])
    canvasBack.create_image(1532, 172, anchor="nw", image=slot6card2, tags=["card", slot6[2]['code']])

    slot2card2 = slotCardToImage(slot2[2])
    canvasBack.create_image(532, 242, anchor='nw', image=slot2card2, tags=["card", slot2[2]['code']])
    slot3card2 = slotCardToImage(slot3[2])
    canvasBack.create_image(782, 242, anchor='nw', image=slot3card2, tags=["card", slot3[2]['code']])
    slot4card2 = slotCardToImage(slot4[2])
    canvasBack.create_image(1032, 242, anchor="nw", image=slot4card2, tags=["card", slot4[2]['code']])
    slot5card2 = slotCardToImage(slot5[2])
    canvasBack.create_image(1282, 242, anchor="nw", image=slot5card2, tags=["card", slot5[2]['code']])
    slot6card2 = slotCardToImage(slot6[2])
    canvasBack.create_image(1532, 242, anchor="nw", image=slot6card2, tags=["card", slot6[2]['code']])

    slot3card3 = slotCardToImage(slot3[3])
    canvasBack.create_image(782, 312, anchor='nw', image=slot3card3, tags=["card", slot3[3]['code']])
    slot4card3 = slotCardToImage(slot4[3])
    canvasBack.create_image(1032, 312, anchor="nw", image=slot4card3, tags=["card", slot4[3]['code']])
    slot5card3 = slotCardToImage(slot5[3])
    canvasBack.create_image(1282, 312, anchor="nw", image=slot5card3, tags=["card", slot5[3]['code']])
    slot6card3 = slotCardToImage(slot6[3])
    canvasBack.create_image(1532, 312, anchor="nw", image=slot6card3, tags=["card", slot6[3]['code']])

    slot4card4 = slotCardToImage(slot4[4])
    canvasBack.create_image(1032, 382, anchor="nw", image=slot4card4, tags=["card", slot4[4]['code']])
    slot5card4 = slotCardToImage(slot5[4])
    canvasBack.create_image(1282, 382, anchor="nw", image=slot5card4, tags=["card", slot5[4]['code']])
    slot6card4 = slotCardToImage(slot6[4])
    canvasBack.create_image(1532, 382, anchor="nw", image=slot6card4, tags=["card", slot6[4]['code']])

    slot5card5 = slotCardToImage(slot5[5])
    canvasBack.create_image(1282, 452, anchor="nw", image=slot5card5, tags=["card", slot5[5]['code']])
    slot6card5 = slotCardToImage(slot6[5])
    canvasBack.create_image(1532, 452, anchor="nw", image=slot6card5, tags=["card", slot6[5]['code']])

    slot6card6 = slotCardToImage(slot6[6])
    canvasBack.create_image(1532, 522, anchor="nw", image=slot6card6, tags=["card", slot6[6]['code']])

def startingCards():
    #draw the initial cards
    first28Cards = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=28")
    first28CardsJSON = first28Cards.json()
    #save them in slots
    #slot0
    slot0.append(first28CardsJSON['cards'][0])
    print("\n\n DEBUG:::::::::: "+ str(slot0[0]))
    #slot1
    for i in range(2):
        slot1.append(first28CardsJSON['cards'][i+1])
    print("\n\n DEBUG:::::::::: "+ str(slot1[0]))
    print("\n\n DEBUG:::::::::: "+ str(slot1[1]))
    #slot2
    for i in range(3):
        slot2.append(first28CardsJSON['cards'][i+3])
    print("\n\n DEBUG:::::::::: "+ str(slot2[0]))
    print("\n\n DEBUG:::::::::: "+ str(slot2[1]))
    print("\n\n DEBUG:::::::::: "+ str(slot2[2]))
    #slot3
    for i in range(4):
        slot3.append(first28CardsJSON['cards'][i+6])
    #slot4
    for i in range(5):
        slot4.append(first28CardsJSON['cards'][i+10])
    #slot5
    for i in range(6):
        slot5.append(first28CardsJSON['cards'][i+15])
    #slot6
    for i in range(7):
        slot6.append(first28CardsJSON['cards'][i+21])

    #place them
    
    
def slotCardToImage(cardFromSlot):
    imageUrl = cardFromSlot['images']['png']
    imageURLInfo = requests.get(imageUrl)
    image_bytes = io.BytesIO(imageURLInfo.content)
    imageToDisplay = ImageTk.PhotoImage(Image.open(image_bytes))
    return imageToDisplay


#Get the api request into a image, passing in the hand and the index of the card in the hand
def cardrequestToImage(hand, i):
    #jsonInfo = request.json()
    print("DEBUG: hand" + str(hand) + ", i: " + str(i))
    #get the image URL from the API
    imageUrl = hand['cards'][i]['image']
    print("DEBUG: imageUrl: " + str(imageUrl))
    #get the image from the API's URL
    imageUrlInfo = requests.get(imageUrl)
    print("DEBUG: imageUrlInfo: " + str(imageUrlInfo))
    #Turn the image into bytes
    image_bytes = io.BytesIO(imageUrlInfo.content)
    print("DEBUG: image_bytes: " + str(image_bytes))
    #turn it into a usable PhotoImage from TK
    imageToDisplay = ImageTk.PhotoImage(Image.open(image_bytes))
    print("DEBUG: imageToDisplay: " + str(imageToDisplay))
    #Print a str format of the image
    print("I: " + str(i) + "\nREQUEST: " + str(imageToDisplay))
    #return the image
    return imageToDisplay

def clickCard(event):
    #removes tags from all cards
    canvasBack.dtag("cardToMove", "cardToMove")

    #if the object is a card (has card tag) then
    if 'card' in canvasBack.gettags("current"):
        if canvasBack.gettags("current")[1] in masterCardEmptyListHeart:
            masterCardEmptyListHeart.remove(canvasBack.gettags("current")[1])
        print("\n\nCURRENT::::::::::::::::::\n\n" + str(canvasBack.gettags("current")) + "\n\nPILE::::::::" + str(masterCardEmptyListHeart))
        #add "cardToMove" tag to card that object that the mouse clicks on (which has the 'current' tag)
        image = canvasBack.addtag_withtag("cardToMove", "current")
    elif 'deck' in canvasBack.gettags('current'):
        drawThree()

    #Raise card to forground
    canvasBack.tag_raise("cardToMove")

    print("Card TO Move: " + str(canvasBack.gettags("cardToMove")))

def moveCard(event):
    #move card 
    canvasBack.moveto('cardToMove', event.x, event.y)

    print("MOVING: " + str(event.x) + " "  + str(event.y))

def clickRelease(event):
    #get coordinates of each hole for cards
    heartHoleCoords = canvasBack.coords(heartHole)
    diamondHoleCoords = canvasBack.coords(diamondHole)
    clubHoleCoords = canvasBack.coords(clubHole)
    spadeHoleCoords = canvasBack.coords(spadeHole)

    print("\n\nDEBUG ::: Heart Hole coords: " + str(heartHoleCoords))
    #if cursor releases card inside box
    if (event.x > heartHoleCoords[0] and event.x < heartHoleCoords[2] and event.y > heartHoleCoords[1] and event.y < heartHoleCoords[3]):
        print("\n\nDEBUG:::::: IN HEART HOLE!!!")
        if len(masterCardEmptyListHeart) == 0:
            print(str(canvasBack.gettags('cardToMove')))
            if 'AH' in (canvasBack.gettags('cardToMove')):
                addToPile('heartHole', canvasBack.gettags('current')[1])
                canvasBack.moveto(canvasBack.find_withtag("AH"), heartHoleCoords[0], heartHoleCoords[1])

        #And the card is correct
        if(canvasBack.gettags("current")):
            masterCardEmptyListHeart.append(canvasBack.gettags("current"))
    if (event.x > diamondHoleCoords[0] and event.x < diamondHoleCoords[2] and event.y > diamondHoleCoords[1] and event.y < diamondHoleCoords[3]):
        print("\n\nDEBUG:::::: IN DIAMOND HOLE!!!")
    if (event.x > clubHoleCoords[0] and event.x < clubHoleCoords[2] and event.y > clubHoleCoords[1] and event.y < clubHoleCoords[3]):
        print("\n\nDEBUG:::::: IN CLUB HOLE!!!")
    if (event.x > spadeHoleCoords[0] and event.x < spadeHoleCoords[2] and event.y > spadeHoleCoords[1] and event.y < spadeHoleCoords[3]):
        print("\n\nDEBUG:::::: IN SPADE HOLE!!!")

global c1, c2, c3
def drawThree():
    #vars
    global c1, c2, c3
    cardsOut = []

    #First Check to see if deck has enough cards
    threeCardsReqCheck = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'])
    #turn the check into a JSON format to look at ['remaining']
    threeCardsReqJSONCheck = threeCardsReqCheck.json()
    
    print("3CardsREQJSONcheck:::::::::::::::::::::::::::::::::::::::::" + str(threeCardsReqJSONCheck))
    #compare ['remaining'] cards to 2 in order to see if there are at least 3 cards
    if threeCardsReqJSONCheck['remaining'] > 2:
        #draw 3 more cards
        threeCardsReq = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=3")
        #convert to JSON
        threeCardsReqJSON = threeCardsReq.json()
        print(str(threeCardsReqJSON))

        #print the cards
        c1 = cardrequestToImage(threeCardsReqJSON, 0)
        c2 = cardrequestToImage(threeCardsReqJSON, 1)
        c3 = cardrequestToImage(threeCardsReqJSON, 2)

        #Draw the images on the canvas of each card
        canvasBack.create_image((rootWindow.winfo_screenwidth() - 326),(rootWindow.winfo_screenheight() - 850), anchor="center", image=c1, tags=["card", threeCardsReqJSON['cards'][0]['code']])
        canvasBack.create_image((rootWindow.winfo_screenwidth() - 426),(rootWindow.winfo_screenheight() - 850), anchor="center", image=c2, tags=["card", threeCardsReqJSON['cards'][1]['code']])
        canvasBack.create_image((rootWindow.winfo_screenwidth() - 526),(rootWindow.winfo_screenheight() - 850), anchor="center", image=c3, tags=["card", threeCardsReqJSON['cards'][2]['code']])

        #put last cards in discard pile
        for i in range(3):
            cardsOut.append(threeCardsReqJSON['cards'][i]['code'])
        print("DEBUG::: CARDS OUT " + str(cardsOut))
        for i in range(3):
            addToPile('discard', cardsOut[i])
        cardsOut.clear()


    #if remaining cards are 2 or less:
    elif threeCardsReqJSONCheck['remaining'] > 0:
        ###Show remaining cards in pile
        #Get amount of cards left
        numCards = threeCardsReqJSONCheck['remaining']
        #draw that many
        lessThanThreeCardsReq = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=" + str(numCards))
        lessThanThreeCardsReqJSON = lessThanThreeCardsReq.json()
        print(str(lessThanThreeCardsReqJSON))

        #print the cards
        c1 = cardrequestToImage(lessThanThreeCardsReqJSON, 0)
        c2 = cardrequestToImage(lessThanThreeCardsReqJSON, 1)

        #draw cards
        canvasBack.create_image(500, 500, anchor="center", image=c1, tags="card")
        canvasBack.create_image(600, 600, anchor="center", image=c2, tags="card")

        #put last cards in discard pile
        for i in range(threeCardsReqJSONCheck['remaining']):
            cardsOut.append(lessThanThreeCardsReqJSON['cards'][i]['code'])
        print("\nDEBUG::: CARDS OUT " + str(cardsOut))
        for i in range(threeCardsReqJSONCheck['remaining']):
            addToPile('discard', cardsOut[i])
        cardsOut.clear()

        #maybe put "shuffle" on the deck

    else:

        #shuffle cards from discard pile back into deck
        """BUG: Doesn't have anything in discard pile, throws exception"""
        emptyDeckReq = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "pile/discard/return/")
        #emptyDeckReqJSON = emptyDeckReq.json()
        #print(str(emptyDeckReqJSON['remaining']))


    print(str(threeCardsReqJSONCheck))


#Creates a pile of cards to use for dynamic card placement with API given a [string] name
def CreatePile(pileName):
    #get a new pile named <pileName>
    req = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/pile/" + pileName + "/add/?cards=")
    print("\nPILE: " + str(req.json()))
    #get a list of the cards in '<pileName>'
    req = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/pile/" + pileName + "/list/")
    print("\nPILE LIST: " + str(req.json()))

def addToPile(pileName, card):
    #add card to pile
    req = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/pile/" + pileName + "/add/?cards=" + card)
    #get a list of the cards in '<pileName>'
    #req = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/pile/" + pileName + "/list/")
    print("\nPILE LIST: " + str(req.json()))
"""---------------------------------------------------------- /Functions -----------------------------------------------------------------------------------------"""



"""---------------------------------------------------------- GUI -----------------------------------------------------------------------------------------"""
#TK main window
rootWindow = tk.Tk()
rootWindow.title("Solitaire")
rootWindow.geometry(str(rootWindow.winfo_screenwidth()) + 'x' + str(rootWindow.winfo_screenheight()))

#Create frame for items to go into
frame1 = Frame(rootWindow, bg="green", bd=1, relief=SUNKEN)
#frame1.grid_propagate(False)
frame1.place(relheight=1, relwidth=1)



"""---------------------------------------------------------- API -----------------------------------------------------------------------------------------"""

#API base url
baseURL = "http://deckofcardsapi.com/"

#check connection to API
try:
    #Create new deck from API
    deck = requests.get(baseURL + "api/deck/new/")
except:
    #Error and quit if cannot connect
    print("ERROR, CANNOT CONNECT TO API, EXITING")
    quit()
#deck in json format
deckJSON = deck.json()

print("deckJSON: " + str(deckJSON))

#shuffle the cards
deck = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/shuffle/")
print("Shuffling...")


print("Deck: " + str(deck.content))

#draw 7 cards from the deck
request2 = requests.get(baseURL + "api/deck/" + deckJSON['deck_id'] + "/draw/?count=7")
print(request2)
print("Drawing 7 cards...")

print("Deck: " + str(request2.content))

#json form of the cards drawn
hand1 = request2.json()
print("\n\nHAND1: " + str(hand1) + "\n\n")
print("HAND: " + str(hand1['cards']))
"""
#create image of cards from hand1
card1 = cardrequestToImage(hand=hand1, i=0)
card2 = cardrequestToImage(hand=hand1, i=1)
card3 = cardrequestToImage(hand=hand1, i=2)
card4 = cardrequestToImage(hand=hand1, i=3)
card5 = cardrequestToImage(hand=hand1, i=4)
card6 = cardrequestToImage(hand=hand1, i=5)
card7 = cardrequestToImage(hand=hand1, i=6)
"""
#Create a pile for discards, and each hole
CreatePile('discard')
CreatePile('heartHole')
CreatePile('diamondHole')
CreatePile('clubHole')
CreatePile('spadeHole')
"""---------------------------------------------------------- /API -----------------------------------------------------------------------------------------"""


#Create a canvas for the background
canvasBack = tk.Canvas(frame1, bg="green")
canvasBack.place(relheight=1,relwidth=1)
"""
#Place the images on the canvas
imageObj1 = canvasBack.create_image(200, 200, anchor="center", image=card1, tags="card")
imageObj2 = canvasBack.create_image(500, 200, anchor="center", image=card2, tags="card")
imageObj3 = canvasBack.create_image(600, 200, anchor="center", image=card3, tags="card")
imageObj4 = canvasBack.create_image(700, 200, anchor="center", image=card4, tags="card")
imageObj5 = canvasBack.create_image(800, 200, anchor="center", image=card5, tags="card")
imageObj6 = canvasBack.create_image(900, 200, anchor="center", image=card6, tags="card")
imageObj7 = canvasBack.create_image(1000, 200, anchor="center", image=card7, tags="card")
"""
#Bind mouse click and movement to canvas
canvasBack.bind('<Button-1>', clickCard)
canvasBack.bind('<B1-Motion>', moveCard)
canvasBack.bind('<B1-ButtonRelease>', clickRelease)


#Open graphic for deck back
deckGraphicUrl = urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Card_back_06.svg/1200px-Card_back_06.svg.png")
readURL = deckGraphicUrl.read()
deckGraphicUrl.close()

#Resize deck back image
deckGraphicImageResize = Image.open(io.BytesIO(readURL)).resize([226,316])
#Convert deck back image into tkinter formatting
deckGraphicImage = ImageTk.PhotoImage(deckGraphicImageResize)
#display deck back graphic
deckGraphic = canvasBack.create_image((rootWindow.winfo_screenwidth() - 326),(rootWindow.winfo_screenheight() - 1200), anchor="center", image=deckGraphicImage, tags=["nonMovable","deck"])

#Creates and draws the holes for the whole deck of each suite
heartHoleLabel = Label(canvasBack, text="Hearts", fg="Red", bg="#2B5526").place(x=(rootWindow.winfo_screenwidth() - 250), y=1306)
heartHole = canvasBack.create_rectangle((rootWindow.winfo_screenwidth() - 100), 1150, (rootWindow.winfo_screenwidth() - 320), 1462, fill="#2B5526", tags="nonMovable")
spadeHoleLabel = Label(canvasBack, text="Spades", fg="black", bg="#2B5526").place(x=(rootWindow.winfo_screenwidth() - 500), y=1306)
spadeHole = canvasBack.create_rectangle((rootWindow.winfo_screenwidth() - 350), 1150, (rootWindow.winfo_screenwidth() - 570), 1462, fill="#2B5526", tags="nonMovable")
diamondHoleLabel = Label(canvasBack, text="Diamonds", fg="Red", bg="#2B5526").place(x=(rootWindow.winfo_screenwidth() - 750), y=1306)
diamondHole = canvasBack.create_rectangle((rootWindow.winfo_screenwidth() - 600), 1150, (rootWindow.winfo_screenwidth() - 820), 1462, fill="#2B5526", tags="nonMovable")
clubHoleLabel = Label(canvasBack, text="Clubs", fg="black", bg="#2B5526").place(x=(rootWindow.winfo_screenwidth() - 1000), y=1306)
clubHole = canvasBack.create_rectangle((rootWindow.winfo_screenwidth() - 850), 1150, (rootWindow.winfo_screenwidth() - 1070), 1462, fill="#2B5526", tags="nonMovable")
"""---------------------------------------------------------- /GUI -----------------------------------------------------------------------------------------"""
startingCards()
updateSlots()

#Main loop for GUI/Program
rootWindow.mainloop()
