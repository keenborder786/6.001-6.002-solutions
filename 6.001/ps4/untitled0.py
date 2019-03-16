# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:40:16 2018

@author: MMOHTASHIM
"""

#! /usr/bin/env python3

# Author: ravexina (Milad As) 
# https://github.com/ravexina

# Repo on github:
# https://github.com/ravexina/tic-tac-toe 

# ----------------------------------------------------------------------------

# MIT License

# Copyright (c) 2017 ravexina (Milad As)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ----------------------------------------------------------------------------

import os
import random
import math
from time import sleep

class Game:

    # Class initializer
    def __init__(self):

       self.w0 = self.w1 = self.w2 = self.w3 = self.w4 = \
               self.w5 = self.w6 = 0.1

       self.w7 = 10
       
       # Ask for user prefered word
       self.user = input("\nDo you want to be 'x' or '[o]' ? ")
       self.train = int(input("Train count: ") or 0)

       if self.user == 'x':
           self.ai = 'o'
       else:
           self.user = 'o'
           self.ai = 'x'
    
       self.guide = ['7','8','9','4','5','6','1','2', '3']
       self.map   = { 
                        '7' : 0,
                        '8' : 1,
                        '9' : 2,
                        '4' : 3,
                        '5' : 4,
                        '6' : 5,
                        '1' : 6,
                        '2' : 7,
                        '3' : 8 
                     }
  
    # Game initializer
    def gameInit(self):
        # Holdes the status of the game
        # Win, Loss, Draw
        self.game_status = False

        self.x1 = self.x2 = self.x3 = self.x4 = self.x5 = \
                self.x6 = self.x7 = 0
        
        # Init default lists
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

        # Holds each game history
        self.history = []
        #  self.hmatrix = [[0 for x in range(9)] for y in range(2)]
        self.hist = []

        self.vhdb = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 
        
        if self.train <= 0:
            print('w1 ', self.w1)
            print('w2 ', self.w2)
            print('w3 ', self.w3)
            print('w4 ', self.w4)
            print('w5 ', self.w5)
            print('w6 ', self.w6)
            print('w7 ', self.w7)
        
    def start(self):

        self.gameInit()
        # -------------

        # Draw the guide
        # print('\nThis is how you can play using numpad:')
        # self.drawBoard(True)
       
        # Draw the board itself
        #  print('\nHere is the board:')
        self.drawBoard()
        
        #  print("\n\n");

        # -------------

        Playing = True
        while Playing:

            # Ask player to move
            self.playerMove()
            self.clear()
            self.drawBoard()
            self.checkStatus()

            if self.game_status == 'lost':
                #  print("\n{{I lost the game :/}}\n")
                Playing = False
                #  print(self.vhdb)
                self.updatew(-10)
                return False

            sleep(0.06)
            
            self.aiMove()
            self.clear()
            self.drawBoard()
            self.checkStatus();

            if self.game_status == 'won':
                #  print("\n{{I won the game}}\n")
                #  print(self.vhdb)
                self.updatew(10)
                Playing = False
            elif self.game_status == 'draw':
                #  print("\n{{Draw...}}\n")
                #  print(self.vhdb)
                self.updatew(0)
                Playing = False

    # Updates the (W) Coefficients ratio
    def updatew(self, finalScore):
        #  print('score: ', finalScore)
        #  print(self.hist)
        #  print('----------\n\n')
        sScore = 0
        for vh in reversed(self.hist):
            if sScore != 0:
                vh[0] = sScore
                sScore = 0
            
            #  print(vh)
            #  print(finalScore - vh[0])
            #  print()
            #  sleep(3)
            self.w1 = self.w1 + 0.1 * ( finalScore - vh[0] ) * vh[1]
            self.w2 = self.w2 + 0.1 * ( finalScore - vh[0] ) * vh[2] 
            self.w3 = self.w3 + 0.1 * ( finalScore - vh[0] ) * vh[3]
            self.w4 = self.w4 + 0.1 * ( finalScore - vh[0] ) * vh[4]
            self.w5 = self.w5 + 0.1 * ( finalScore - vh[0] ) * vh[5]
            self.w6 = self.w6 + 0.1 * ( finalScore - vh[0] ) * vh[6]
            self.w7 = self.w7 + 0.1 * ( finalScore - vh[0] ) * vh[7]

            sScore = self.w0 + self.w1 * vh[1] + self.w2 * vh[2] + \
                       self.w3 * vh[3] + self.w4 * vh[4] + self.w5 * vh[5] + \
                       self.w6 * vh[6] + self.w7 * vh[7]
            
    def playerMove(self):
        # Auto training
        if self.train > 0:
            amoves = self.availableMoves()
            move = random.choice(amoves)
            self.board[move] = self.user
            self.history.append(move)
        else:
        # user is playing
            move = input('Your move: ')
            # Don't let user choose a unknown place (num/key)
            if not move.isdigit() or int(move) > 9 or int(move) < 0:
                self.playerMove()
            else:
                # Don't let user to choose an already taken place
                amoves = self.availableMoves()
                if int(self.map[move]) not in amoves:
                    self.playerMove();
                else:
                    self.board[self.map[move]] = self.user
                    self.history.append(self.map[move])

    def aiMove(self):
        # Get a list of available moves
        amoves = self.availableMoves()

        # There is no more move
        # No one has won the game till now
        # It's a draw situation
        if amoves == False:
            self.clear()
            self.drawBoard()
            self.game_status = 'draw'
            self.train -= 1
            return False

        # Get a move which has max score
        move = self.maxScoreMove()

        # Choose a random move - old dummy approach
        #  move = random.choice(amoves)

        self.board[move] = self.ai 
        self.history.append(move)

    def drawBoard(self, guide = False):
        for i in range(3):
            for j in range(3):
                if guide == True:
                    print(self.guide[j + (i*3)], end='' )
                else:
                    print(self.board[j + (i*3)], end='' )
                if j != 2:
                    print(' | ', end='')

            print() # New line for each board's line
        print(); # New line after drawing the board

        if self.train >= 0:
            print('Train: ', self.train)
            print()

    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def availableMoves(self):
        # list of available moves
        am_list = []

        for i in range(9):
            if self.board[i] == ' ':
                am_list.append(i)

        # No more moves
        if am_list == []:
            return False

        return am_list

    # Check game status
    # then take a decision
    # status can be won: +10, lost: -10, draw: 0
    def checkStatus(self):
        if self.checkWon('ai'):
            #  print("haha I won")
            #  self.printHistory()
            #  self.cal(10)
            self.game_status = 'won'
            self.train -= 1
        elif self.checkWon('user'):
            #  print("Ops I lost")
            #  self.printHistory()
            #  self.cal(-10)
            self.game_status = 'lost'
            self.train -= 1

    def printHistory(self):
        return
        print("\nHistory:\n")
        print(self.history)
    
    def maxScoreMove(self):
        # get available moves
        amoves = self.availableMoves() 
        
        # Create a dictonary of scores for each move
        score = {}
        for move in amoves:
            score[move] = self.calScore(move)

        #  sleep(2)
        #  if self.train <= 0:
            #  print(score)
            #  sleep(5)

        # Create a list of all max score moves 
        max_vals = []
        max_val_key = max(score, key=score.get)
        for i in score.keys():
            if score[i] == score[max_val_key]:
                max_vals.append(i)
        
        # Choose a random value from max values (when they have same score)
        selected_move = random.choice(max_vals)

        # Record the chosen move's score
        selected_score = score[selected_move]

        # solution 
        self.hist.append(
                [selected_score, self.x1, self.x2, self.x3, \
                self.x4, self.x5, self.x6, self.x7])

        # return the move
        return selected_move

    # Calculates the score of a specific move
    def calScore(self, move):

        # save a copy of the board
        stash_board = self.board[:]

        # Put the chosen move in the place
        self.board[move] = self.ai

        # Get a list of available moves
        # after choosing this move
        amoves = self.availableMoves()

        # x1 = number of ai finishing moves
        self.x1 = 0
        # x2 = number of user finishing moves
        self.x2 = 0
        # It's a winning move
        self.x7 = 0;

        # Check if this move is a winning move it self
        if self.checkWon('ai'):
             self.x7 = 1

        # It's not a winning move

        # Check how many winning move it will creates for us and for the user
        #  else:
        for i in amoves:
            # Put an available move in place for ai
            self.board[i] = self.ai
            # If it makes ai the winner x1++
            if self.checkWon('ai'):
                self.x1 += 1;

            # Put this move as user's
            self.board[i] = self.user
            # It it makes user the winner of the game x2++
            if self.checkWon('user'):
                self.x2 += 1;
            # Clear the choosen move for other checks
            self.board[i] = ' ';

        self.x3 = self.countWord('ai', 1)
        self.x4 = self.countWord('ai', 2)
        self.x5 = self.countWord('user', 1)
        self.x6 = self.countWord('user', 2)

        #  print('\nMove: ', move)
        #  print('ai 1: ', self.x3)
        #  print('ai 2: ', self.x4)
        #  print('user 1: ', self.x5)
        #  print('user 2: ', self.x6)
        #  print('--------------\n')


        score = self.w0 + self.w1 * self.x1 + self.w2 * self.x2 + \
                self.w3 * self.x3 + \
                self.w4 * self.x4 + self.w5 * self.x5 + \
                self.w6 * self.x6 + self.w7 * self.x7

        #  p2int("For the move ", move)
        #  print("x1 ", x1)
        #  print("x2 ", x2)
        #  print("The score of ", move, " is ", score, "\n")

        self.board = stash_board[:]


        #  print(self.x1)
        #  print(self.x2)

        return score

    # cType (check type) can be ai, user
    def checkWon(self, ctype):

        # select word for check
        if ctype == 'ai':
            w = self.ai
        else:
            w = self.user

        t = self.board;
        return ((t[0] == w and t[1] == w and t[2] == w) or
                (t[3] == w and t[4] == w and t[5] == w) or
                (t[6] == w and t[7] == w and t[8] == w) or
                (t[0] == w and t[4] == w and t[8] == w) or
                (t[2] == w and t[4] == w and t[6] == w) or
                (t[0] == w and t[3] == w and t[6] == w) or
                (t[1] == w and t[4] == w and t[7] == w) or
                (t[2] == w and t[5] == w and t[8] == w))

    def countWord(self, ctype, count):

        lst = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 4, 8],
                [2, 4, 6],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8] ]

        if ctype == 'ai':
            w = self.ai # check
            c = self.user # comptator
        else:
            w = self.user
            c = self.ai

        counter = 0;
        inlstCounter = 0;

        for l in lst:
            for i in l:

                # if comptator is in list skip it
                if self.board[i] == c:
                    inlstCounter = 0
                    break

                if self.board[i] == w:
                    inlstCounter += 1

            if inlstCounter == count:
                counter += 1;

            inlstCounter = 0
           
        return counter


play = True;

game = Game()

while play:

    game.start()

    if game.train == 0 :
        if input('\nDo you want to play  again? [y]/n\n') == 'n':
            play = False
