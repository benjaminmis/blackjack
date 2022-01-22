import random
import blackjack.create_suits as create_suits
from blackjack.card_class import Card

class Deck():
    
    def __init__(self):       
        self.all_cards = [] 
        for suit in create_suits.suits:            
            for rank in create_suits.ranks:                
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):       
        random.shuffle(self.all_cards)
        
    def deal_one(self):        
        return self.all_cards.pop()
    
    def reset_deck(self):        
        self.all_cards=[]
        for suit in create_suits.suits:
            for rank in create_suits.ranks:
                self.all_cards.append(Card(suit,rank))
            