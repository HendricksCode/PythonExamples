import random

# These are the unicode characters
suits = ["\u2663", "\u2660", "\u2665", "\u2666"] 
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]*4
full_deck = []
player_cards = []
dealer_cards = []         

while True:
    def prompt_player():
        print("\n-----WELCOME TO BLACKJACK-----")
        print("\n1) Play")
        print("2) Exit")
        prompt = input("\nWould you like to play or exit the game? Choose 1 or 2: ")
        if prompt == "1":
            # This for loop creates the full deck of cards
            for suit in suits:
                for face in faces:
                    full_deck.append(face + suit)
        else:
            print("\nGoodbye")
            return

        player_hand = []
        dealer_hand = []

        # This for loop deals 2 cards to the player
        for i in range(2):
            random.shuffle(full_deck)
            card = full_deck.pop()
            player_hand.append(card)
        print("\nYou were dealt: ", player_hand)
        
        # This calculates the total of the players hand 
        total = 0
        dealer_total = 0
        for card in player_hand:
            if card[0] == "J":
                total += 10
            elif card[0] == "Q":
                total += 10
            elif card[0] == "K":
                total += 10
            elif card[0] == "T":
                total += 10
            elif card[0] == "A":
                if total >= 11: total += 1
                else: total += 11
            else:
                total += int(card[0])

        # This for loop deals 1 card to the dealer
        for i in range(1):
            random.shuffle(full_deck)
            card = full_deck.pop()
            dealer_hand.append(card)
        print("The dealer was dealt: ", dealer_hand, "and the other card is facedown")

        if total == 21:
            print("BLACKJACK, YOU WIN!!!")
            return 
        print("your current total is:", total)

        # This while loop, loops the "hit" or "stay" prompt
        while True:
            prompt2 = input("\nWould you like to Hit or Stay? ")
            if prompt2.lower() == "hit":
                for i in range(1):
                    random.shuffle(full_deck)
                    card = full_deck.pop()
                    player_hand.append(card)
                print("\nYou were dealt: ", card)
                print("You now have", player_hand)

                if card[0] == "J":
                    total += 10
                elif card[0] == "Q":
                    total += 10
                elif card[0] == "K":
                    total += 10
                elif card[0] == "T":
                    total += 10
                elif card[0] == "A":
                    if total >= 11: total += 1
                    else: total += 11
                else:
                    total += int(card[0])

                print("your current total is:", total)
                
                if total == 21:
                    print("BLACKJACK! YOU WIN!!!")
                if total > 21:
                    print("Sorry, you busted!!!")
                    break
               
            
            if prompt2.lower() == "stay":
                # The dealer must continue until their total is at least 17, that is the reason for this While loop
                while dealer_total < 17:
                    for i in range(1):
                        random.shuffle(full_deck)
                        card = full_deck.pop()
                        dealer_hand.append(card)
                    print("\nThe dealers card is: ", card)
                    print("The dealer now has", dealer_hand)

                    dealer_total = 0
                    for card in dealer_hand:
                        if card[0] == "J":
                            dealer_total += 10
                        elif card[0] == "Q":
                            dealer_total += 10
                        elif card[0] == "K":
                            dealer_total += 10
                        elif card[0] == "T":
                            dealer_total += 10
                        elif card[0] == "A":
                            if dealer_total >= 11: dealer_total += 1
                            else: dealer_total += 11
                        else:
                            dealer_total += int(card[0])
                    print("The dealer now has a total of:", dealer_total)

                if dealer_total > 21:
                    print("The dealer busted, YOU WIN!!!")
                    break
                elif dealer_total < total:
                    print("The dealer has", dealer_total, "and you have", total, "YOU WIN!!!")
                    break
                elif dealer_total > total:
                    print("The dealer has", dealer_total, "and you have", total, "sorry, you lose =(")
                    break 
                else:
                    print("The dealer has", dealer_total, "and you have", total, "it's a tie!")
                    break

    prompt_player() 
