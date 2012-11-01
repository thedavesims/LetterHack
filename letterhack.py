#!/usr/bin/python
from copy import copy
import sys


def find_words(letter_string):
    #Convert letters to lowercase and split it into a list
    letters = list(letter_string.lower())
    #list to hold our words loaded from our text file
    words=[]
    found_words=[]
    partial_words=[]
    #load words from dictionary file
    with open("enable.txt") as f:
        words = [line.strip() for line in f.readlines()]
    #for each word in the list
    for word in words: 
        word_as_list = list(word)
        any_missing = False
        for letter in letters:
            if letter in word_as_list:
                word_as_list.remove(letter)
            else:
                any_missing = True
        if len(word_as_list) == 0:
            found_words.append(word)
        if not any_missing:
            partial_words.append(word)
    found_words.sort(key=len)        
    partial_words.sort(key=len)
    print "Top 5 Words by length: "
    for word in found_words[-5:]:
        print word
    print "Top 5 Words by that are supersets: "
    for word in partial_words[:10]:
        print word        


if __name__ == '__main__':
    #The list of letters that appear on your letterpress screen
    letter_string = 'WCVOUBISHROZORELDANCLZYVG'
    if len(sys.argv) > 1:
        letter_string = sys.argv[1]
    find_words(letter_string)