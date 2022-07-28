#Library Imports
from turtle import screensize
import requests
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import io
from urllib.request import urlopen


"""---------------------------------------------------------- Functions -----------------------------------------------------------------------------------------"""
#Get the api request into a image, passing in the hand and the index of the card in the hand
def cardrequestToImage(hand, i):
    #jsonInfo = request.json()
    #get the image URL from the API
    imageUrl = hand['cards'][i]['image']
    #get the image from the API's URL
    imageUrlInfo = requests.get(imageUrl)
    #Turn the image into bytes
    image_bytes = io.BytesIO(imageUrlInfo.content)
    #turn it into a usable PhotoImage from TK
    imageToDisplay = ImageTk.PhotoImage(Image.open(image_bytes))
    #Print a str format of the image
    print("I: " + str(i) + "\nREQUEST: " + str(imageToDisplay))
    #return the image
    return imageToDisplay

def clickCard(event):
    #removes tags from all cards
    canvasBack.dtag("cardToMove", "cardToMove")

    #if the object is a card (has card tag) then
    if 'card' in canvasBack.gettags("current"):  
        #add "cardToMove" tag to card that object that the mouse clicks on (which has the 'current' tag)
        image = canvasBack.addtag_withtag("cardToMove", "current")
    elif 'deck' in canvasBack.gettags('current'):
        canvasBack.create_image(1000, 200, anchor="center", image=card7, tags="card")

    #Raise card to forground
    canvasBack.tag_raise("cardToMove")

    print("Card TO Move: " + str(canvasBack.gettags("cardToMove")))

def moveCard(event):
    #move card 
    canvasBack.moveto('cardToMove', event.x, event.y)

    print("MOVING: " + str(event.x) + " "  + str(event.y))
"""---------------------------------------------------------- /Functions -----------------------------------------------------------------------------------------"""



"""---------------------------------------------------------- GUI -----------------------------------------------------------------------------------------"""
#TK main window
rootWindow = tk.Tk()
rootWindow.title("")
rootWindow.geometry("800x500")

#Create frame for items to go into
frame1 = Frame(rootWindow, bg="green", bd=1, relief=SUNKEN)
#frame1.grid_propagate(False)
frame1.place(relheight=1, relwidth=1)



"""---------------------------------------------------------- API -----------------------------------------------------------------------------------------"""

#API base url
baseURL = "http://deckofcardsapi.com/"

#Create new deck from API
deck = requests.get(baseURL + "api/deck/new/")
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

#create image of 2 cards from hand 1
card1 = cardrequestToImage(hand=hand1, i=0)
card2 = cardrequestToImage(hand=hand1, i=1)
card3 = cardrequestToImage(hand=hand1, i=2)
card4 = cardrequestToImage(hand=hand1, i=3)
card5 = cardrequestToImage(hand=hand1, i=4)
card6 = cardrequestToImage(hand=hand1, i=5)
card7 = cardrequestToImage(hand=hand1, i=6)

"""---------------------------------------------------------- /API -----------------------------------------------------------------------------------------"""




#Create a canvas for the background
canvasBack = tk.Canvas(frame1, bg="green")
canvasBack.place(relheight=1,relwidth=1)
"""
i = 0
for card in hand1:
    cardIm = cardrequestToImage(hand=hand1, i = i)
    canvasBack.create_image(i*100, i*100, image=cardIm)
    i = i + 1
"""


#Place the images on the canvas
imageObj1 = canvasBack.create_image(200, 200, anchor="center", image=card1, tags="card")
imageObj2 = canvasBack.create_image(500, 200, anchor="center", image=card2, tags="card")
imageObj3 = canvasBack.create_image(600, 200, anchor="center", image=card3, tags="card")
imageObj4 = canvasBack.create_image(700, 200, anchor="center", image=card4, tags="card")
imageObj5 = canvasBack.create_image(800, 200, anchor="center", image=card5, tags="card")
imageObj6 = canvasBack.create_image(900, 200, anchor="center", image=card6, tags="card")
imageObj7 = canvasBack.create_image(1000, 200, anchor="center", image=card7, tags="card")

#Bind mouse click and movement to canvas
canvasBack.bind('<Button-1>', clickCard)
canvasBack.bind('<B1-Motion>', moveCard)


#Open graphic for deck back
deckGraphicUrl = urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Card_back_06.svg/1200px-Card_back_06.svg.png")
readURL = deckGraphicUrl.read()
deckGraphicUrl.close()

#Resize deck back image
deckGraphicImageResize = Image.open(io.BytesIO(readURL)).resize([226,316])
#Convert deck back image into tkinter formatting
deckGraphicImage = ImageTk.PhotoImage(deckGraphicImageResize)
#display deck back graphic
deckGraphic = canvasBack.create_image((rootWindow.winfo_screenwidth() - 326),(rootWindow.winfo_screenheight() - 416), anchor="center", image=deckGraphicImage, tags=["nonMovable","deck"])

heartHole = canvasBack.create_rectangle((rootWindow.winfo_screenwidth() - 100), 150, rootWindow.winfo_screenwidth() - 320, 300, fill="red", tags="nonMovable")
spadeHole = canvasBack.create_rectangle(rootWindow.winfo_x() + 100, 150, 100, 300, fill="black", tags="nonMovable")
diamondHole = canvasBack.create_rectangle(rootWindow.winfo_x() + 100, 150, 100, 300, fill="red", tags="nonMovable")
clubHole = canvasBack.create_rectangle(rootWindow.winfo_x(), 150, 100, 300, fill="black", tags="nonMovable")


"""---------------------------------------------------------- /GUI -----------------------------------------------------------------------------------------"""


#Main loop for GUI/Program
rootWindow.mainloop()
