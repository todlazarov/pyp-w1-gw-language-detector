# -​*- coding: utf-8 -*​-

"""This is the entry point of the program."""

from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""

    input_text = text.split() 

    counter_dict = {'spanish': 0, 'german': 0, 'english': 0}

    for language in languages:
        counter = 0
        for word in language['common_words']:
            if word in input_text:
                counter += 1
            counter_dict[language['name']]= counter
    
    return max(counter_dict, key = counter_dict.get)