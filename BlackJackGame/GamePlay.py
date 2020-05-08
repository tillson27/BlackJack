class GamePlay():

    def aces(hand):
        total = 0
        for el in hand:
            if el.get_value() == 0:
                x = 0
                for el in hand:
                    x += el.get_value()
                x += 1
                y = x + 10

                if y > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += el.get_value()

        return total



    def game():

        print("WELCOME TO BLACKJACK!!!")
        print("")
        print("The goal of the game is to get as close to 21 without going over. Closer than the dealer")
        print("Numerical cards are worth their value, face cards are worth 10 and Aces are worth either 1 or 11")
        print("Each round you can choose to hit, and take another card, or stick with what you currently have")
        print("Goodluck")
        print("")

        player_account = Account(balance = 0)

        while True:
            start_balance = int(input("How much money would you like to start with in your betting account?:  "))
            if start_balance < 0:
                print("You cannot start with a negative balance! \n")
                continue
            elif start_balance >= 0:
                player_account.add_funds(start_balance)
                print("")
                print(player_account)
                break
            else:
                print("Please enter a valid amount!")
                continue


        while True:
            print('\n'*10)
            start_game = input("Would you like to begin a hand? Please answer 'Yes' or 'No':  ")

            if start_game == 'No':
                print("")
                print("Thank you for playing!!")
                print(player_account)
                break
            else:
                print("Shuffling Cards...")
                print("")
                deck = Deck(cards = [])
                deck.new_deck()

                bet = player_account.place_bet()

                player_card1 = Card(value = deck.cards.pop())
                player_card2 = Card(value = deck.cards.pop())

                dealer_upcard = Card(value = deck.cards.pop())
                dealer_downcard = Card(value = deck.cards.pop())

                player_cards = [player_card1, player_card2]
                dealer_cards = [dealer_upcard, dealer_downcard]

                player_curr_val = GamePlay.aces(player_cards)
                dealer_curr_val = GamePlay.aces(dealer_cards)

                deck.starting_cards()
                print("")
                print(f"Player Card 1: {player_card1}")
                print("")
                print(f"Player Card 2: {player_card2}")
                print("")
                print(f"Player 1 Score: {player_curr_val}")
                print("")
                print("==================================")
                print("")
                print(f"Dealer Card 1: {dealer_upcard}")
                print("")
                print(f"Dealer Card 2: <<HIDDEN>>")
                print("")
                print("")

                while True:


                    decision = input("Would you like to hit or stand? Type 'h' or 's'")

                    if not decision == 'h' and not decision == 's':
                        print("Please enter a valid option, 'h' or 's'!!")
                        continue

                    elif decision == 'h':

                        new_playercard = deck.hit()
                        player_cards.append(new_playercard)
                        player_curr_val = GamePlay.aces(player_cards)

                        print("")
                        print(f"New Player Card: {new_playercard}")
                        print("")
                        print(f"Player 1 Score: {player_curr_val}")
                        print("")
                        print("==================================")
                        print("")
                        print(f"Dealer Card 1: {dealer_upcard}")
                        print(f"Dealer Card 2: <<HIDDEN>>")
                        print("")
                        print("")

                        if player_curr_val > 21:
                            print(f"Bust!! You lost {bet} dollars to the dealer")
                            player_account.lose_funds(bet)
                            break

                        if dealer_curr_val < 17:
                            new_dealercard = deck.hit()
                            dealer_cards.append(new_dealercard)
                            dealer_curr_val = GamePlay.aces(dealer_cards)
                            continue

                    else:
                        print("Player Cards")
                        for el in player_cards:
                            print(el)
                        print("")
                        print(f"PlayerScore: {player_curr_val}")

                        print("")

                        print("Dealer Cards")
                        for el in dealer_cards:
                            print(el)
                        print("")
                        print(f"Dealer Score: {dealer_curr_val}")


                        if dealer_curr_val > 21:
                            print(f"Dealer bust! You won {bet} from the dealer")
                            player_account.add_funds(bet)
                            break

                        elif dealer_curr_val > player_curr_val:
                            print(f"Dealer was closer!! You lost {bet} dollars to the dealer")
                            player_account.lose_funds(bet)
                            break

                        elif dealer_curr_val < player_curr_val:
                            print(f"You were closer!! You won {bet} dollars from the dealer")
                            player_account.add_funds(bet)
                            break








GamePlay.game()
