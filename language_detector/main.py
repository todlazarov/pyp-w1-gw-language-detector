# -​*- coding: utf-8 -*​-

"""This is the entry point of the program."""

from languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    input_text = []
    input_text = text.split(' ') 

    spanish_counter = 0 
    german_counter = 0
    
    for word in languages[0]['common_words']:
        if word in input_text:
            spanish_counter += 1
    for word in languages[1]['common_words']:
        if word in input_text:
            german_counter += 1
    
    if spanish_counter > german_counter:
        return 'spanish'
    elif german_counter > spanish_counter:
        return 'german'
    else:
        return 'equal'