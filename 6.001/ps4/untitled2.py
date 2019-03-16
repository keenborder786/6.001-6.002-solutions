# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:08:22 2018

@author: MMOHTASHIM
"""
import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        file_name="words.txt"
        
        self.message_text=text
        self.valid_words=load_words(file_name)
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy=self.valid_words.copy()
        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0<=int(shift)<=26, "Please enter a valid shift value"
        i=0
        a=0
        dic_word={b:a for a,b in enumerate(string.ascii_lowercase[:26])}
        dic_word_2={b:a for a,b in enumerate(string.ascii_uppercase[:26])}
        for char in dic_word:
           dic_word[char]+=shift
           if dic_word[char] >=26:
               dic_word[char]=a
               a+=1
        for char in dic_word_2:
           dic_word_2[char]+=shift
           if dic_word_2[char] >=26:
               dic_word_2[char]=i
               i+=1
        dic_word.update(dic_word_2)
        return dic_word
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dic_word=self.build_shift_dict(shift)
        alpha_lower=string.ascii_lowercase
        alpha_higher=string.ascii_uppercase
        encrypted_message_text=""
        for char in  self.message_text:
            if char in alpha_lower:
               index=dic_word[char]
               new_word=alpha_lower[index]
               encrypted_message_text+=new_word
            elif char in alpha_higher:
               index_2=dic_word[char]
               new_word_2=alpha_higher[index_2]
               encrypted_message_text+=new_word_2
            else:
               encrypted_message_text+=char
        return encrypted_message_text   
message=Message("Hello, World!")    
#print(message.get_message_text())
#print(message.get_valid_words())
print(message.apply_shift(4))
