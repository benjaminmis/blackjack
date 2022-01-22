import blackjack.create_suits as create_suits

class Card(): 
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=create_suits.values[rank] 
        
    def __str__(self): 
        return self.rank + " of " + self.suit