# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
       if char not in letters_guessed:
         return False
    return True

    
    
            



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE
    guessed_word = ''
    for char in secret_word:
        if char not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += char
    return guessed_word

                
    
        
                
                
        



        
             
               
               
   


    



def get_available_letters(letters_guessed):
    temp=""
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    z="abcdefghijklmnopqrstuvwxyz"
    for char in z:
        if char not in letters_guessed:
            temp+=char
    return temp

    
    

def hangman(secret_word):
    letters_guessed=""
    guess=""
    n=6
    warning=3
    v=["a","e","i","o","u"]     
    z=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    '''
    secret_word: apple, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word=choose_word(wordlist)
    print("Welcome to the game hangman")
    print("I am thinking of a word that is "+ str(len(secret_word)) +"  words long")
    while n>0 and warning>0:
     print("You have " + str(n) + " guesses left")
     Input_guess=input("Please enter a letter:  ")
     is_letter_already_guessed = Input_guess in letters_guessed
     letters_guessed+=Input_guess
     guess=get_guessed_word(secret_word, letters_guessed)
     if  is_letter_already_guessed and Input_guess!="*":
        print("You have already guess this word")
        warning=warning-1
        print("You have " + str(warning) + " warning remaining")
        if warning < n:
           n=n-1
     elif Input_guess=="*":
         print("The possible outcome are:"+ show_possible_matches(guess) )
     else:                                          
         if Input_guess not in secret_word and Input_guess in z:
            n=n-1
            print("You have "+ str(n) + " guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Opps!That letter is not in my word:"+guess)
         elif Input_guess not in secret_word and Input_guess in v:
            n=n-2
            print("You have "+ str(n) + " guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Opps!That letter is not in my word:"+guess)
        
         elif Input_guess  in secret_word and Input_guess in z:
            print("You have "+ str(n) + "guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Good Guess:" + guess)
         elif Input_guess  in secret_word and Input_guess in v:
            print("You have "+ str(n) + "guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Good Guess:" + guess)
        
         elif Input_guess not in z and Input_guess not in v:
            print("You can only type in alphabet")
            warning=warning-1
            print("You have " + str(warning) + " warning remaining")
            if warning < n:
               n=n-1
     x=is_word_guessed(secret_word, letters_guessed)      
     if n==0 or n==-1 or warning==0:
           print("You have lost")
           print("The word was " + secret_word)           
     elif x is True:   
        print("Congratulation You won")
        print("Your total score for this game is: " + str(n*len(secret_word)) )
        break    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (
                my_word[i] != other_word[i] \
                or my_word.count(my_word[i]) != other_word.count(my_word[i]) \
            ):
                return False
        return True
    
    
        
   
       



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words_list = open(WORDLIST_FILENAME, 'r').readline().split()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
    return(' '.join(possible_matches))
                             



def hangman_with_hints(secret_word):
    letters_guessed=""
    guess=""
    n=6
    warning=3
    v=["a","e","i","o","u"]     
    z=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word=choose_word(wordlist)
    print("Welcome to the game hangman")
    print("I am thinking of a word that is "+ str(len(secret_word)) +"  words long")
    while n>0 and warning>0:
     print("You have " + str(n) + " guesses left")
     Input_guess=input("Please enter a letter:  ")
     is_letter_already_guessed = Input_guess in letters_guessed
     letters_guessed+=Input_guess
     if  is_letter_already_guessed:
        print("You have already guess this word")
        warning=warning-1
        print("You have " + str(warning) + " warning remaining")
        if warning < n:
           n=n-1
     elif Input_guess=="*":
         print("The possible outcome are:"+ show_possible_matches(guess) )
     else:
                                               
         if Input_guess not in secret_word and Input_guess in z:
            n=n-1
            print("You have "+ str(n) + " guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Opps!That letter is not in my word:"+guess)
         elif Input_guess not in secret_word and Input_guess in v:
            n=n-2
            print("You have "+ str(n) + " guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Opps!That letter is not in my word:"+guess)
        
         elif Input_guess  in secret_word and Input_guess in z:
            print("You have "+ str(n) + "guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Good Guess:" + guess)
         elif Input_guess  in secret_word and Input_guess in v:
            print("You have "+ str(n) + "guesses left")
            print("Available letters:" + get_available_letters(letters_guessed))
            print("Good Guess:" + guess)
        
         elif Input_guess not in z and Input_guess not in v:
            print("You can only type in alphabet")
            warning=warning-1
            print("You have " + str(warning) + " warning remaining")
            if warning < n:
               n=n-1
     x=is_word_guessed(secret_word, letters_guessed)      
     if n==0 or n==-1 or warning==0:
           print("You have lost")
           print("The word was " + secret_word)           
     elif x is True:   
        print("Congratulation You won")
        print("Your total score for this game is: " + str(n*len(secret_word)) )
        break    
    
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
#    secret_word = choose_word(wordlist)
#    hangman_with_hints(secret_word)
