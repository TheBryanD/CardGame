import requests

deckreq = requests.get("http://deckofcardsapi.com/api/deck/new")
deck = deckreq.json()

print(str(deck))

pilereq = requests.get("http://deckofcardsapi.com/api/deck/" + deck['deck_id'] + "/pile/discard/add/?cards=AS,2S")
pile = pilereq.json()

pilereq = requests.get("http://deckofcardsapi.com/api/deck/" + deck['deck_id'] + "/pile/discard/add/?cards=AS,2S")

drawRequest = requests.get("http://deckofcardsapi.com/api/deck/" + deck['deck_id'] + "/draw/?count=52")
draw = drawRequest.json()

print(str(draw))

print(str(pile))