from player_class import Player
from deck_class import Deck
from blackjack_functions import hit_or_stand, bet, replay, reset_game

bj_deck=Deck()
bj_deck.shuffle()
newplayer=Player('NewPlayer')
dealer=Player('Dealer')
chips=100
gameon=True

while gameon==True and chips>0:
    if replay()==False:
        print('Thanks for playing. It was fun! Bye.')
        gameon=False
    else:
        playerbet=bet(chips)

        for x in range(2):
            dealer.add_cards(bj_deck.deal_one())
            newplayer.add_cards(bj_deck.deal_one())
                    
        newplayer.hand_value()
        dealer.hand_value()
        print(f'{newplayer.name} has {newplayer.all_cards[0]} and {newplayer.all_cards[1]} for a total of {newplayer.hand_total}')
     
        print(f'Dealer shows {dealer.all_cards[1]}')
        while newplayer.hand_total<21 and hit_or_stand()==True and newplayer.hand_total!=21:
            newplayer.add_cards(bj_deck.deal_one())
            newplayer.hand_value()
            print(f'You got a {newplayer.all_cards[-1]} for a new total of {newplayer.hand_total}')
            if newplayer.hand_total>21 and newplayer.check_ace()==True:
                newplayer.hand_total=newplayer.hand_total-10
                print(f'Since you have an ace, your total is {newplayer.hand_total}') 

        while 17>dealer.hand_total<newplayer.hand_total and newplayer.hand_total<22:
            dealer.hand_value()
            print(f'Dealer has {dealer.all_cards[0]} and {dealer.all_cards[1]} for a total of {dealer.hand_total}')
            dealer.add_cards(bj_deck.deal_one())
            dealer.hand_value()
            print(f'The new dealer card is {dealer.all_cards[-1]} and their total is {dealer.hand_total}')
            if dealer.hand_total>21 and dealer.check_ace()==True:
                dealer.hand_total=dealer.hand_total-10
                print(f'Since the dealer has an ace, their total is {dealer.hand_total}')
        
        print(f'The dealer has a total of {dealer.hand_total}')
        if newplayer.hand_total==21 and len(newplayer.all_cards)==2:
            print('You have BLACKJACK! You win double your bet.')
            chips=chips+(2*playerbet)
            print(f'You now have {chips} chips.')
            reset_game(bj_deck, dealer, newplayer)
        
        elif newplayer.hand_total>21:
            print('You have gone over 21. You Lose.')
            chips=chips-playerbet
            print(f'You now have {chips} chips.')
            reset_game(bj_deck, dealer, newplayer)
        
        elif dealer.hand_total==21 and newplayer.hand_total!=21:
            print(f'Dealer has {dealer.all_cards[0]} and {dealer.all_cards[1]} for a total of 21.')
            chips=chips-playerbet
            print('You lose. Haha.')
            reset_game(bj_deck, dealer, newplayer)
            
        elif 22>dealer.hand_total>newplayer.hand_total:
            dealer.hand_value()
            print('You lose.')
            chips=chips-playerbet
            print(f'you now have {chips} chips')
            reset_game(bj_deck, dealer, newplayer)
            
        elif dealer.hand_total==newplayer.hand_total and dealer.hand_total>15:
            print(f'You have {newplayer.hand_total} and the dealer has {dealer.hand_total}. It is a tie.')
            print(f'You still have {chips} chips')
            reset_game(bj_deck, dealer, newplayer)
        
        else:
            dealer.hand_value()
            print('You win')
            chips=chips+playerbet
            print(f'You now have {chips} chips')
            reset_game(bj_deck, dealer, newplayer)
