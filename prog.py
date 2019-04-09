import random #idk why
import json #idk why

def num_vowels(s): #return vowels
    vowels=0 #initialize
    for letter in s: #iterate
        if letter in [a,e,i,o,u]: #if letter is vowel (list of vowels)
            vowels+=1 #add one
    if vowels < 2: #if less than 2 vowel
        return False #false
    else: #otherwise
        return True #true

