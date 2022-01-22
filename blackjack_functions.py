def bet(chips):
    bets=0
    while bets<=0 or bets>chips:
        try:
            bets=int(input(f'You have {chips} chips. How much would you like to bet? '))
        except:
            print("Looks like you did not enter a integer!")
            continue
        else:
            if 0<bets<chips:
                print(f'You bet {bets} chips.')
            elif bets>chips:
                print(f'You do not have {bets} chips. You have {chips} chips. Please try again.')
    return bets

def hit_or_stand():
    v=input('Would you like to hit? Type Hit or Stand: ').lower().startswith('h')
    return v

def replay():
    want_to_play=input(f'Do you want to continue to play Blackjack? Enter Yes or No: ').lower().startswith('y')    
    return want_to_play

def reset_game(bj_deck, dealer, newplayer):
    bj_deck.reset_deck()
    bj_deck.shuffle()
    dealer.clear_hand()
    newplayer.clear_hand()