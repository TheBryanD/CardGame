import requests
import tkinter as tk
from tkinter import Image
from PIL import ImageTk, Image
from io import StringIO
from requests.api import request
import urllib3 as ur
import io
import os

#Tk init
rootWindow = tk.Tk()
rootWindow.title("")
rootWindow.geometry("800x500")

#Frame to build in
frame1 = tk.Frame(rootWindow).grid()

#Base URL for API
baseURL = "http://deckofcardsapi.com/"

#Create new deck of cards
deck = requests.get(baseURL + "api/deck/new/")
cards = deck.json()


print("::" + str(cards['deck_id']))
print("Cards" + str(cards))

#pick card from deck
request2 = requests.get(baseURL + "api/deck/" + cards['deck_id'] + "/draw/?count=1")
request3 = requests.get(baseURL + "api/deck/" + cards['deck_id'] + "/draw/?count=1")
#Turn request into json format
Player1Cards = request2.json()
print(Player1Cards['cards'][0]['image'])


#get the url from the json text returned
imgURL = Player1Cards['cards'][0]['image']

#get the request of the url of the image
img_Info = requests.get(Player1Cards['cards'][0]['image'])

#get the bytes form of the image
image_bytes = io.BytesIO(img_Info.content)
#get a variable of the image
img = Image.open(image_bytes)
#create a variable of the image as ImageTk
imageToDisplay = ImageTk.PhotoImage(Image.open(image_bytes))
#make image a label and display the image
ImageLabel = tk.Label(frame1, image=imageToDisplay)
ImageLabel.grid()

print("PlayerCards: " + str(Player1Cards))


#main loop for gui
rootWindow.mainloop()
