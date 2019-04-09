import random

def num_vowels(s):
    vowels=0
    for letter in s:
        if letter in [a,e,i,o,u]:
            vowels+=1
    if vowels < 2:
        return False
    else:
        return True
