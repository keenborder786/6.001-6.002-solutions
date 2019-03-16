# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
    
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"
        '''
        i=0
        a=0
        b=0
        dic_lower={}
        dic_upper={}
        lower=string.ascii_lowercase
        upper=string.ascii_uppercase
        for char in vowels_permutation:
            if char in lower:
               new_index=VOWELS_LOWER[i]
               dic_lower[char]=new_index
               dic_lower[new_index]=char
               dic_upper[VOWELS_UPPER[i]]=VOWELS_UPPER[i]
            if char in upper:
               new_index_2=VOWELS_UPPER[i]
               dic_upper[char]=new_index_2
               dic_upper[new_index_2]=char
               dic_lower[VOWELS_LOWER[i]]=VOWELS_LOWER[i]
               
            i+=1
        for char in CONSONANTS_LOWER:
            dic_lower[char]=CONSONANTS_LOWER[a]
            a+=1
        for char in CONSONANTS_UPPER:
             dic_lower[char]=CONSONANTS_UPPER[b]
             b+=1
        if dic_lower.update(dic_upper)!=None:
            return dic_lower.update(dic_upper)
        elif dic_lower==None:
            return dic_upper
        else:
            return dic_lower
         

            
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message=""
        dic=transpose_dict
        text=self.message_text
        for char in text:
            if char in string.ascii_lowercase:
                new_word=dic[char]
                encrypted_message+=new_word
            elif char in string.ascii_uppercase:
                new_word=dic[char]
                encrypted_message+=new_word
            else:
                encrypted_message+=char
        return encrypted_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text=text
        SubMessage.__init__(self,text)
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encry
        pted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        encrypted_message=self.text
        vowel_lower_permutations=get_permutations("aeiou")
        vowel_upper_permutations=get_permutations("AEIOU")
        imax=0
        i=0
        i_2=0
        imax_2=0
        for vowel in vowel_lower_permutations:
            dic=self.build_transpose_dict(vowel)
            valid_word_list=[]
            decrypted_message=""
            for word in encrypted_message:
                        if word in VOWELS_LOWER:
                            for key in dic.keys():
                                if dic[key]==word:
                                    decrypted_message+=key
                        else:
                            decrypted_message+=word
            for words in decrypted_message.split():
                if is_word(self.valid_words, words)==True:
                   valid_word_list.append(words)
                   i=len(valid_word_list)
            if i > imax:
                imax=i
                valid_decryption=decrypted_message
    
        for vowel in vowel_upper_permutations:
                    dic_2=self.build_transpose_dict(vowel)
                    valid_word_list_2=[]
                    decrypted_message=""
                    for word in encrypted_message:
                        if word in VOWELS_UPPER:
                            for key_2 in dic_2.keys():
                                if dic_2[key_2]==word:
                                    decrypted_message+=key_2
                        else:
                            decrypted_message+=word
                    for words in decrypted_message.split():
                        if is_word(self.valid_words, words)==True:
                           valid_word_list_2.append(words)
                           i_2=len(valid_word_list_2)
                    if i_2 > imax_2:
                        imax_2=i_2
                        valid_decryption=decrypted_message
        return valid_decryption

            
        
            
            
                
               
            





#if __name__ == '__main__':
#
#    # Example test case
#    message = SubMessage("HELLO WORLD!")
#    permutation = "eaiuo"
#    enc_dict = message.build_transpose_dict(permutation)
#    print("Original message:", message.get_message_text(), "Permutation:", permutation)
#    print("Expected encryption:", "Hallu Wurld!")
#    print("Actual encryption:", message.apply_transpose(enc_dict))
#    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#    print("Decrypted message:", enc_message.decrypt_message())
#     

