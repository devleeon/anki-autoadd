
from wiktionaryparser import WiktionaryParser
from tkinter import *
import re


class WikLoader():
    root = Tk()
    root.geometry("200x150")
    pattern = r'/[^,>]+/'
    repattern = re.compile(pattern)

    parser = WiktionaryParser()
    parser.set_default_language('english')
    parser.include_relation('alternative forms')

    wordInput = 'lovely'

    words = parser.fetch(wordInput)
    origin = ""
    definitions = []
    poSpeechs = ""
    pronunciations = ""
    for word in words:
        origin += word['etymology']
        pronunciations = repattern.match(word['pronunciations']['text'][0])
        definitions = word['definitions']
        for definition in definitions:
            poSpeechs += ('\n' + definition['partOfSpeech'])

    print(origin)
    print(poSpeechs)
    print(pronunciations)
