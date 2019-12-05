# -*- coding: utf-8 -*-
import json

with open('vocab.json', 'r') as f:
    words_dict = json.load(f)

for word in words_dict:
    print("INSERT INTO \"dictionary_translateword\" VALUES (\"{}\",\"{}\", {})".format(word['word'],\
                                                                                       word['translate'],\
                                                                                       word['frequency']))