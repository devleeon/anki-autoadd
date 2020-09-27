import genanki
import sys
from anki import decks

from anki import Collection
from anki.utils import intTime
import time

collection_path = 'C:/Users/leeon/AppData/Roaming/Anki2/leeon/collection.anki2'
col = Collection(collection_path)
today = intTime()  # anki function returns current integer time
nextTwenty = today + 60*60  # integer time in 20 minutes

query = "select count(id) from cards where queue = 1 and due < %s" % nextTwenty
learnAheadCards = col.db.scalar(query)
deck = decks.DeckManager

print("You have %s learning cards due in Anki" % learnAheadCards)
print(col.db.all(query))
col.close()
