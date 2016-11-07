import random
import string


VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'


def gen_word(minlength = 4, maxlength = 20):
    result = '' + random.choice(random.choice([CONSONANTS, VOWELS]))

    if(result[0] in VOWELS):
        odd_letters = VOWELS
        even_letters = CONSONANTS
    else:
        odd_letters = CONSONANTS
        even_letters = VOWELS

    for i in range(random.randint(minlength - 1, maxlength - 1)):
        if i % 2 == 1:
            result += random.choice(odd_letters)
        elif i % 2 == 0:
            result += random.choice(even_letters)

    return result
