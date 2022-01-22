class Player():
    
    def __init__(self,name):
        
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def hand_value(self):
        self.hand_total=0
        for card in range(len(self.all_cards)):
            self.hand_total += self.all_cards[card].value
        
    def check_ace(self):
        self.hand_value()
        is_ace=[]
        for card in range(len(self.all_cards)):
            is_ace.append(self.all_cards[card].value)
        if 11 in is_ace:
            #self.hand_total=self.hand_total-10
            return True
    def clear_hand(self):
        for card in range(len(self.all_cards)):
            self.all_cards.pop(-1)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    