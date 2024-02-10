#This program implements the Hangman game. Game play: A solution word is randomly selected from a list of 213 words 
#stored in the 'hangman_words.py' file. It prompts the player to guess letters that might be in the solution
#word. If the letter is not in the word, a graphic of a stickman on a gallows stored in the 'hangman_art.py' file
#displays in progressively more complete stages. If enough (6) letters not in the solution word are guessed,
#the picture of the man on the gallows completes and the player loses the game. If a letter is guessed that is 
#present in the solution word, the letter is removed from the word. When all letters of the word are guessed and
#its length is (0), the player wins the game. The game handles multiple occurrences of a letter in solution word. 
#For example, one guess at 't' would remove both ocurrances in 'little'. The game also handles letters that have 
#been previously guessed. The remove_letter() function is invoked when the player's guess is found to be 
#present in the solution word. It iterates the solution word to identify the indexes of the string where it 
#finds the guessed letter. It uses the index to remove the letter by concatinating the slice before it and the 
#slice following it into the remains of the solution word in which the same letter, in a subsequent guess
#cannot be found again. Since it is possible for a word to have multiple occurances of the same letter, 
#it adjusts the index on-the-fly after each letter is removed to account for the shorter word length.

import hangman_words
import hangman_art
from random import randint
import os
os.system('cls')
print(hangman_art.logo)

def remove_letter(word, letter_guess):
    print('removing: ', letter_guess)
    index = 0
    for letter in word:
        print(letter)
        if letter == letter_guess:
            print(f'found {letter_guess} at index {index}, removing..')
            word = word[:index]+word[index+1:]
            index-=1
        index+=1
    return(word)

r = randint(1, 214)
solution_word = hangman_words.word_list[r]
word = solution_word
stages_index = 6
print(f'Psst.. the word is: {word}')
word_length = len(word)
print(f'word_length: {word_length} \n')
letters_used = ''

while (stages_index > 0):
    letter_guess = input('Guess a letter: ')
    letter_guess = letter_guess.lower()
    if letter_guess in letters_used:
        print(f'The letter {letter_guess}, has alread been used.')
        print('letters_used: ', letters_used)
        print('word: ', word)
        print(f'word_length: {word_length} \n')
        continue

    elif letter_guess in word:
        print(f'The letter {letter_guess} is present in the word.')
        letters_used = letters_used + letter_guess
        print('letters_used: ', letters_used)
        word = remove_letter(word, letter_guess)
        print('returned word: ', word)
        word_length = len(word)
        print(f'word_length: {word_length} \n')
        if word_length == 0:
            print(f'Congrats! you win. The word was: {solution_word}')
            break

    else:
        print(f'The letter {letter_guess} is not present in the word.')
        letters_used = letters_used + letter_guess
        print('letters_used: ', letters_used)
        print('word: ', word)
        print(f'word_length: {word_length} \n')
        print(hangman_art.stages[stages_index-1])
        stages_index -= 1
        if stages_index == 0:
            print(f'Sorry, you lost. The word was: {solution_word}')