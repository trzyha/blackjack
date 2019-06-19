import random
from colorama import Fore, Back, Style

cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K", 14:"A"}
points = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} #ace is 11 or 1
card_color = ("clubs", "diamonds", "hearts", "spades")
player_points = 0

def random_card(card_color, card_value):
    
    if card_color == "clubs":
        return (str(cards[card_value]) + u"\u2663")
    elif card_color == "diamonds":
        return (str(cards[card_value]) + u"\u2666")
    elif card_color == "hearts":
        return (str(cards[card_value]) + u"\u2665")
    elif card_color == "spades":
        return (str(cards[card_value]) + u"\u2660") 

#def check_game_over(player_points):
#    if player_points <= 21:
#        pass
#    else:
#        break
    
cards_pack_sorted = []
player_cards = []
while len(cards_pack_sorted) <= 51:
    x = random_card(random.choice(card_color), random.randint(2,14))
    if x in cards_pack_sorted:
        pass
    else:
        cards_pack_sorted.append(x)

print(cards_pack_sorted)

gameloop = True
while gameloop:
    take_card = input("Hit?: ")
    if take_card == '1':
        #x = random.choice(cards_pack_sorted)
        #print(cards_pack_sorted[0]) #first from the stock
        player_cards.append(cards_pack_sorted[0])
        player_cards_string = ' '.join(player_cards)
        player_points = 0 #reseting player points after taking new card
        for i in range (0, len(player_cards_string)):
            
            if '2' in player_cards_string[i]:
                print ('2')
                player_points = player_points + 2
            elif '3' in player_cards_string[i]:
                print ('3')
                player_points = player_points + 3
            elif '4' in player_cards_string[i]:
                print ('4')
                player_points = player_points + 4
            elif '5' in player_cards_string[i]:
                print ('5')
                player_points = player_points + 5
            elif '6' in player_cards_string[i]:
                print ('6')
                player_points = player_points + 6
            elif '7' in player_cards_string[i]:
                print ('7')
                player_points = player_points + 7
            elif '8' in player_cards_string[i]:
                print ('8')
                player_points = player_points + 8
            elif '9' in player_cards_string[i]:
                print ('9')
                player_points = player_points + 9
            elif ('1' in player_cards_string[i]) and ('0' in player_cards_string[i+1]):
                print ('10')
                player_points = player_points + 10
            elif 'J' in player_cards_string[i]:
                print ('10')
                player_points = player_points + 10
            elif 'Q' in player_cards_string[i]:
                print ('10')
                player_points = player_points + 10
            elif 'K' in player_cards_string[i]:
                print ('10')
                player_points = player_points + 10
            elif 'A' in player_cards_string[i]:
                if player_points + 11 <= 21: #if <= 21 adds 11 points else 1
                    player_points = player_points + 11
                else:
                    player_points = player_points + 1
            else:
                pass
                        
        print(player_cards)
        print(player_points)
        del cards_pack_sorted[0]
        #print(cards_pack_sorted) #printing stock (debug)
    elif take_card == '2':
        
        gameloop = False
    else:
        pass