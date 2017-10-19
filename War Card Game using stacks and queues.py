#Abdirahman Mohamed CSC 236 A11
# Credits : Alexander Sharron

import random  # imports the random module
from Stack import*
from Queue_personal import*



class Deck:
    """This is the deck class. It returnes the card's deck,shuffle it for players and remove it from the deck"""

    def __init__(self):
        self.cards = []
        cards = [0,1,2,3,4,5,6,7,8,9] # Deck of cards
        for i in range(5):
            for j in cards:
                self.cards.append(j)
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards) # Shuffling the cards
        return self.cards



class War:
    """Initilizes war game"""
    def __init__(self):
        deck = Deck() # Class Deck object
        print(deck.cards)
        shuffled_cards = deck.shuffle()
        self.currentstate = True
        self.dealingpile = Queue()
        print(shuffled_cards)
        for i in shuffled_cards:
            self.dealingpile.enqueue(i) # Add the shuffled cards to the dealing pile
        self.myplayingpile = Stack()
        self.mystoragepile = Queue()
        self.otherplayingpile = Stack()
        self.otherstoragepile = Queue()
        self.lootpile = Stack()
    def deal(self):
        """Deals 25 cards to player and computer"""
        for i in range (25):
            self.myplayingpile.push(self.dealingpile.dequeue()) # Player has 25 cards
        for i in range (25):
            self.otherplayingpile.push(self.dealingpile.dequeue()) # Computer has 25 cards
    def game(self):
        """War game between player and computer and who ever have all the cards at the end wins."""
        print("Welcome to WAR!")
        turn = 1
        while self.currentstate: # While True
            self.player1 = self.myplayingpile.top() # Player's first card
            self.player2 = self.otherplayingpile.top() # Computer's first card
            if self.player1==self.player2:
                self.check_equal() # A call to the check equal function
            elif self.player1>self.player2:
                self.mystoragepile.enqueue(self.otherplayingpile.pop()) # Add computer's card to player's storage pile
                self.mystoragepile.enqueue(self.myplayingpile.pop()) # Add player's card to player's storage pile
            else:
                self.otherstoragepile.enqueue(self.otherplayingpile.pop()) # Add computer's card to computer's storage pile
                self.otherstoragepile.enqueue(self.myplayingpile.pop()) # Add player's card to computer's storage pile
            turn+=1
            if self.myplayingpile.size()==0 or self.otherplayingpile.size()==0:

                self.currentstate = False # Stop the while loop
    def check_equal(self):
        """Adds player's and computer's cards to the loot pile"""
        if self.myplayingpile.size()>1 and self.otherplayingpile.size()>1:

            self.lootpile.push(self.myplayingpile.pop())
            self.lootpile.push(self.otherplayingpile.pop())
        else:
            self.currentstate=False
        if self.myplayingpile.size()>4 and self.otherplayingpile.size()>4:
            for i in range(3):
                self.lootpile.push(self.otherplayingpile.pop())
                self.lootpile.push(self.myplayingpile.pop())
            self.player1 = self.myplayingpile.top()
            self.player2 = self.otherplayingpile.top()
        else:
            self.currentstate = False

        if self.player1>self.player2: # if the player's card after the war round is bigger than the computer's
            self.mystoragepile.enqueue(self.myplayingpile.pop())
            self.mystoragepile.enqueue(self.otherplayingpile.pop())
            for i in range(self.lootpile.size()):
                self.mystoragepile.enqueue(self.lootpile.pop())
        elif self.player2>self.player1:
            self.otherstoragepile.enqueue(self.myplayingpile.pop())
            self.otherstoragepile.enqueue(self.otherplayingpile.pop())
            for i in range(self.lootpile.size()):
                self.otherstoragepile.enqueue(self.lootpile.pop())
        else:
            if self.currentstate:
                self.check_equal()




    def win(self):
        """The winnig function. If the size of the player's playing pile is zero, computer wins. If computer's size is zero, player wins."""
        if self.myplayingpile.size()==0: # If player's list is empty
            print("Computer Wins")
        else:
            print("Player wins")


def main():
    """The war game. A player plays against a computer and the winner is the player who accumulates all the cards wins the game."""
    game = War() # War class object
    game.deal()
    game.game()
    game.win()
if __name__ == '__main__':
    main()













