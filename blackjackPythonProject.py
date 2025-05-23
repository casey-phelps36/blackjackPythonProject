# Name:        Casey Phelps
# Class:       CSC 110 - Spring 2025
# Assignment:  Programming Project - Blackjack
# Due Date:    April 28, 2025

# Program Title:  Blackjack
  
# Project Description:
# --------------------
# This program will play the game of Blackjack.  The computer will be the dealer
# and the user will be the player
# The object of the game is to get the sum of your cards as close to 21 without going over
# The player can choose to take more cards if the total is lower than 21
# The dealer must follow specified rules about whether to take another card
# This version of the game will not have betting but will keep an overall score for the player
# based on wins, losses, and ties
# An ace can be counted as a 1 or 11, and will take the value of whichever one
# gets the hand value closest to 21 but not over (if possible)


# General Solution:
# -----------------
# Deal two cards to the dealer and the player by putting them into their own lists
# Dealt in the order player, dealer, player, dealer
# Display both of the user's cards and one of the dealer's cards
# Ask the user if they want to be dealt another card
# If the user wants another card, it is added to their list
# Calculate the totals of the list, if the player does not go over 21 ask if they want another card
# Keep doing this until the user says they want to stay or their total goes over 21
# If the player decides to stay, then it is the dealer's turn
# Calculate the end totals of both hands to determine a winner (if the dealer doesn't bust)
# Add a win, loss, or tie to the player's score list
# If the deck runs out of cards, a new deck will be created

# Dealer Rules:
# -------------
# If the total of the dealer's cards is 17 or more, it must stand
# If the total of the dealer's cards is 16 or less, it must draw
# The dealer must continue to take cards until the total is 17 or more
# If the dealer has an ace, and counting it as 11 would bring the total to 17 or more
# (but not over 21), the dealer must count the ace as 11 and stand


# Pseudocode:
# -----------
# Player and dealer are dealt two cards each, the order is player, dealer, player, dealer
# Display both of the user's cards, and one of the dealers cards
# Ask the player if they want to "HIT" or "STAY"
# If the player chooses "HIT" 
#       Player is dealt another card
#       If player total is 21 or less
#           Ask the player if they want to "HIT" or "STAY"
#       Else
#           Player has "BUSTED" -- Automatic loss
# Elif the player chooses "STAY"
#       Display the dealer's second card
#       While the dealer total is less than 21
#           If the dealer total is 17 or more
#               dealer "STAY"
#           Else
#               dealer "HIT"
#       If the dealer total is over 21
#           Dealer "BUSTED" -- player win 
# Else
#       Invalid word, ask user to enter "HIT" or "STAY"



# Function Design:
# ----------------

import random


def createDeck():
    # This function creates a deck of cards where each card
    # is represented by two characters:  Face and Suit
    # It will return a deck of cards in the form of a list of 52 cards
    # Example card: 'JS' is Jack of Spades

    # lists of all the face and suit values
    faces = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['D','C','S','H']
    # initialize the blank deck list
    deck = []

    # loop through each suit
    for i in range(len(faces)):
        # loop through each face value for each suit
        for j in range(len(suits)):
            # concatenate the face value and the suit into one string
            # and add it to the deck list
            card = faces[i] + suits[j]
            deck.append(card)
        
    return deck
 

def dealingTheHand(deck):
    # This function will randomly choose 2 cards to deal
    # to the player and 2 cards to deal to the dealer
    # Order is player, dealer, player, dealer
    # Each hand will be represented as a list of two strings

    # initialize each hand
    playerHand = []
    dealerHand = []

    # need to deal out 4 cards
    # use range(1, 5) for the if statement logic
    for i in range(1, 5):
        # if i is an odd number, deal the card to the player
            # the player needs to be dealt the first and third cards
        if i % 2 != 0:
            card, deck = dealACard(deck)
            playerHand.append(card)
        # if i is an even number, deal the card to the dealer
             # the dealer needs to be dealt the second and fourth cards
        else:
            card, deck = dealACard(deck)
            dealerHand.append(card)

    return playerHand, dealerHand, deck

def dealACard(deck):
    # This function will randomly choose one card from the deck and remove it from the deck
    card = random.choice(deck)
    deck.remove(card)
    return card, deck
    

def playerTurn(cardsDealt, playerHand, dealerHand, deck, playerStay, totalScore, playerBust, roundOver):
    # This function will ask the player if they want to "HIT" or "STAY"
    # If the player chooses to hit
        # they are dealt a new card
        # the total is calculated
    # If the player chooses to stay
        # the total is calculated
        # the player's turn is ended
    # If the player is dealt an Ace, call the handlingAces function
    # If the hand dealt to the player is a face card or a 10 and an Ace, this is BlackJack
    # and the player wins 2 points, game over
        # If the dealer also has BlackJack, they tie and the player gets no points

    # print a blank space between anything that happened before 
    print()

    # error handling to make sure the user can only input h or s
    goodChoice = False
    while goodChoice == False:
        try:
            # ask the user if they want to hit or stay
            choice = input("Type H to hit or S to stay: ")
            # if they enter h or s, goodChoice is true and the while loop will not run again
            if choice == "H" or choice == "h" or choice == "S" or choice == "s":
                goodChoice = True
            # if they enter anything else, they will be prompted to try again
            else:
                print("Must choose either H or S, please try again")
        except ValueError:
            print("Invalid character, please try again")

    # hit
    if choice == "h" or choice == "H":

        # check if the cardsDealt counter has hit 52 (a whole deck)
            # if yes, create a new deck and reset the counter
        if cardsDealt == 52:
            print("Dealing new deck")
            deck = createDeck()
            cardsDealt = 0

        # call the playerHit function to get the hand and current deck
        # increment the cardsDealt counter by 1
        hand, deck = playerHit(playerHand, deck)
        cardsDealt += 1

        # print out the player's hand
        # use a for loop to go through the hand list and print each card value
            # use end = " " to print at the end of the onput instead of on a new line
        print("Your hand is: ", end = " ")
        for i in range(len(playerHand)):
            if i != len(playerHand) - 1:
                print(playerHand[i], end = " ")
            else:
                print(playerHand[i])

        # print only the dealer's second card
        print("Dealer is showing: ", dealerHand[1])

        # call computePlayerHandValue to get the player's current score and number of aces
        playerScore, numAces = computePlayerHandValue(playerHand)

        # if the score is over 21, the player busts
        # set playerBust, playerStay, and roundOver to TRUE
            # these are used in the main function
        if playerScore > 21:
            print("Your current hand value is: ", playerScore)
            print("You have busted - too bad")
            playerBust = True
            playerStay = True
            totalScore -= 1
            print()
            print("You busted, your score for this round is -1")
            print("Your total score is: ", totalScore)
            print()
            roundOver = True
            
        # if the player's score is less than or equal to 21 and they have no aces
            # just print the current hand value
        elif playerScore <= 21 and numAces == 0:
            print("Your current hand value is: ", playerScore)
            
        # if the player has one ace
        elif numAces == 1:
            noAceValue = 0 # initialze the value of the hand without the aces
            # loop through each card in the hand
            for card in playerHand:
                # check if the first character of the card is an Ace
                if card[0] != 'A':
                    # if it is not an ace, and not a 10 or a face card
                    # add whatever that value is to noAceValue
                    if card[0].isdigit():
                        noAceValue += int(card[0])
                    # if the card is a 10 or a face card
                    # add 10 to noAceValue
                    elif card[0] in ['T', 'J', 'Q', 'K']:
                        noAceValue += 10
            # create variables for if the ace is counted as a 1 or an 11
                # add 1 or 11 to noAceValue
            # and print out the number of aces and the possible values of the hand
            value1 = noAceValue + 1 # ace as 1
            value2 = noAceValue + 11 # ace as 11
            print("You have 1 ace(s) in your hand. Your current hand value is:", value1)
            print("or ", value2)
            
        # if the player has more than one ace
        elif numAces > 1:
            # print out the number of aces and what the value of the player's hand would be if the ace is a 1
                # this would be playerScore - 10 because in computePlayerHandValue
                # aces are initially given a value of 11
            print("You have ", numAces, " ace(s) in your hand. Your current hand value is: ", playerScore - 10)
            # create a local variable that starts with the current playerScore value
            value = playerScore
            # loop through each ace
            for aces in range(numAces):
                # add 10 to the value for each new ace
                # by multiplying the ace index by 10
                    # the first time through will add 0 because the value of the first ace
                    # being valued at 11 (how it is initially scored in computePlayerHandValue)
                    # needs to be printed
                value += aces * 10
                print("or ", value)

    # stay
    elif choice == "s" or choice == "S":
        playerStay = True

    return cardsDealt, playerHand, deck, playerStay, totalScore, playerBust, roundOver


def dealerTurn(cardsDealt, dealerHand, playerHand, deck, dealerStay, totalScore, dealerBust, roundOver):
    # This function handles the dealer's turn
    # If the player busts, the dealer does not need to take the turn
    # If the dealer busts, the player wins
    # If the dealer has an Ace in their hand, and counting it as 11 would bring the total value
    # to 17 or more (but not over 21), the dealer must count the ace as 11 and stay


    # print out the dealer's full hand
    # use a for loop to go through the hand list and print each card value
            # use end = " " to print at the end of the onput instead of on a new line
    print("Dealer hand is: ", end = " ")
    for i in range(len(dealerHand)):
        if i != len(dealerHand) - 1:
            print(dealerHand[i], end = " ")
        else:
            print(dealerHand[i])

    # call checkBlackjack to see if the dealer got black jack
    # if they did, update the total score for the game and the round ends
        # dealerStay needs to be set to true for the main function
    dealerBlackjack = checkBlackjack(dealerHand)
    if dealerBlackjack == True:
        print("Dealer has BLACK JACK")
        print()
        print("The dealer beat your hand, so your score for this round is -1")
        totalScore -= 1
        print("Your total score is: ", totalScore)
        roundOver = True
        dealerStay = True

    # if the dealer did not get black jack
    if dealerBlackjack == False and roundOver == False:
        # compute the score and print it
        dealerScore = computeDealerHandValue(dealerHand)
        print("Dealer hand value is: ", dealerScore)        

        # if the dealer's score is under 17
        while dealerScore < 17 and dealerStay == False:

            # check if the cardsDealt counter has hit 52 (a whole deck)
                # if yes, create a new deck and reset the counter
            if cardsDealt == 52:
                print("Dealing new deck")
                deck = createDeck()
                cardsDealt = 0

            # print that the dealer is taking
            # call dealerHit to get the dealer's hand and current deck
            # increment the cardsDealt counter
            print("Dealer taking")
            dealerHand, deck = dealerHit(dealerHand, deck)
            cardsDealt += 1
            print()
            
            # print out the dealer's hand, compute the value, and print the hand value
            print("Dealer hand is: ", end = " ")
            for i in range(len(dealerHand)):
                if i != len(dealerHand) - 1:
                    print(dealerHand[i], end = " ")
                else:
                    print(dealerHand[i])
            dealerScore = computeDealerHandValue(dealerHand)
            print("Dealer hand value is: ", dealerScore)
            
        # when the dealer's hand value is 17 or more
        # the dealer stays, and the while loop will not run
        dealerStay = True

        # if the dealer busts (hand value is over 21)
            # print out that the dealer busted, and what the round and total scores are
            # set dealerBust and roundOver to true
        if dealerScore > 21:
            print("Dealer BUSTS")
            print()
            dealerBust = True
            print("Dealer Busted, your score for this round is 1")
            totalScore += 1  
            print("Your total score is: ", totalScore)
            print()
            roundOver = True
        
    return cardsDealt, dealerHand, deck, dealerStay, totalScore, dealerBust, roundOver

def computePlayerHandValue(hand):
    # This function adds up the value of the given hand
    # Ignore the suit of each card
    # Face cards (Jack, Queen King) all have the value of 10
    # An ace can be 1 or 11

    # initialize the total and numAces variables
    total = 0
    numAces = 0

    # loop through each card in the hand
        # the hand is stored as a list, and each card is an element of the list
    for card in hand:
        # set the face value as the first character of the card
        face = card[0]
        # if the face is a number/digit, add that number to the total
            # .isdigit() found here: https://www.w3schools.com/python/ref_string_isdigit.asp
        if face.isdigit():
            total += int(face)
        # if the face is a 10 ("T") or a face card ("J", "Q", "K"), add 10 to the total
        elif face == "T" or face == "J" or face == "Q" or face == "K":
            total += 10
        # if the face is an Ace, increment the numAces counter and add 11 to the total
        elif face == "A":
            numAces += 1
            total += 11 # for now, may be adjusted after


    # the aces are initially given the value of 11
    # if that makes the total go over 21
    if numAces > 0 and total > 21:
        # loop though each ace
        for aces in range(numAces):
            # subtract 10 from the total (essentially turning the ace into a 1)
            # if that still causes a bust, keep the change
            # because we still want the number closest to 21 even if it is a bust
            if total - 10 > 21:
                total -= 10
            else:
                # if subtracting 10 (making the ace a 1) keeps the total 21 or less
                # keep that change
                total -= 10
                break

    return total, numAces

def computeDealerHandValue(hand):
    # computes the hand value the same way until the aces
    total = 0
    numAces = 0
    for card in hand:
        face = card[0]
        # .isdigit() found here: https://www.w3schools.com/python/ref_string_isdigit.asp
        if face.isdigit():
            total += int(face)
        elif face == "T" or face == "J" or face == "Q" or face == "K":
            total += 10
        # if the face is an ace, increment numAces
        elif face == "A":
            numAces += 1

    # if the dealer has an ace
        # if counting the ace as an 11 would bring the total to 17 or more but not over 21
        # it must be counted as an 11 and the dealer stays
    if numAces > 0:
        # loop through each ace
        for aces in range(numAces):
            # if adding 11 to the total would bring the value to 17 or more but not over 21
                # the ace is counted as an 11 and add 11 to the total
            if total + 11 >= 17 and total + 11 <= 21:
                total += 11
            # if adding 11 to the total would bring the value to less than 17
                # the ace is counted as an 11 and add 11 to the total
            elif total + 11 < 17:
                total += 11
            # if adding 1 to the total would bring the value to 17 or more but not over 21
                # # the ace is counted as a 1 and add 1 to the total
            elif total + 1 >= 17 and total + 1 <= 21:
                total += 1
            else:
                total += 1
        

    return total


def computeTotalScore(playerHand, dealerHand, totalScore):
    # This function will compute the player's overall score based on wins, losses, and ties
    # If the Player Busts with a hand value greater than 21, that hand earns a score of -1.
    # If the Dealer Busts and the Player does not, the Player earns a score of 1 for that hand.
    # If the Player does not Bust, but has a score less than the Dealer, the Player earns a score of -1 for that hand.
    # If the Player and the Dealer have the same hand value, this is a Push, and the Player earns a score of 0 for the hand.
    # If the Player has Blackjack, and the Dealer does not have Blackjack, the Player earns a score of 2 for the hand.

    # calculate both the player and the dealer final hand values
    playerHandValue, numAces = computePlayerHandValue(playerHand)
    dealerHandValue = computeDealerHandValue(dealerHand)

    if playerHandValue > 21:
        # player busts, dealer wins
        print()
        print("The dealer beat your hand, your score for this round is -1")
        print("Your total score is: ", totalScore)
    elif dealerHandValue > 21:
        # dealer busts, player wins
        print()
        print("You beat the dealer, your score for this round is 1")
        print("Your total score is: ", totalScore)
    elif playerHandValue > dealerHandValue:
        # player wins with a greater hand value
        totalScore += 1 # increment total score for player win
        print()
        print("You beat the dealer, your score for this round is 1")
        print("Your total score is: ", totalScore)
    elif playerHandValue < dealerHandValue:
        # dealer wins with a greater hand value
        totalScore -= 1 # decrement total score for player loss
        print()
        print("The dealer beat your hand, so your score for this round is -1")
        print("Your total score is: ", totalScore)
    else:
        # tie/push
        print()
        print("You tied with the dealer, that is a push and your score for this round is 0")
        print("Your total score is: ", totalScore)

    print()

    return totalScore

def checkBlackjack(hand):
    # initialize a variable
    blackjackHand = 0
    
    # loop through each card in the hand
    for card in hand:
        # set the face as the first element in the hand
        face = card[0]
        # if the face is a 10 or a face card, add 1 to the blackjackHand variable
        if face == "T" or face == "J" or face == "Q" or face == "K":
            blackjackHand += 1
        # if the face is an ace, add 2 to the blackjackHand variable
        elif face == "A":
            blackjackHand += 2


    # the only way the total can be 3 is if there is a face card AND an ace
    # so if the total is 3, blackjack is true
    if blackjackHand == 3:
        blackjack = True
        return blackjack
    else:
        blackjack = False
        return blackjack

def playerHit(playerHand, deck):
    # deal a new card to the player using dealACard
    newCard, deck = dealACard(deck)
    # add it to the playerHand list
    playerHand.append(newCard)
    return playerHand, deck

def dealerHit(dealerHand, deck):
    # deal a new card to the player using dealACard
    newCard, deck = dealACard(deck)
    # add it to the playerHand list
    dealerHand.append(newCard)
    return dealerHand, deck

def playAgain(gameOver):
    print()

    # error handling, like in playerTurn for H and S
    goodChoice = False
    while goodChoice == False:
        try:
            # ask the user if they want to play again and to enter "Y" or "N" 
            choice = input("Play again? Y or N: ")
            if choice == "Y" or choice == "y" or choice == "N" or choice == "n":
                goodChoice = True
            else:
                print("Must choose either Y or N, please try again")
        except ValueError:
            print("Invalid character, please try again")
            
    print()
    # if they enter y
        # gameOver is false, the while loop in the main function will keep going
    if choice == "Y" or choice == "y":
        gameOver = False
    # if they enter n
        # gameOver is true, the while loop in the main function will stop
    elif choice == "N" or choice == "n":
        gameOver = True
        print("Thanks for playing, good-bye...")
    
    return gameOver


def startGame(deck, totalScore):
    # deal out the initial hand with the dealingTheHand function
    # set roundOver as false
    playerHand, dealerHand, deck = dealingTheHand(deck)
    roundOver = False
    
    # print the player's hand, and the second card of the dealer's hand
    print("Your hand is: ", playerHand[0], playerHand[1])
    print("Dealer is showing: ", dealerHand[1])

    # check if the player had black jack
    playerBlackjack = checkBlackjack(playerHand)
    # if they have black jack
    if playerBlackjack == True:
        # print that they have it and print out the dealer's whole hand
        print("You have BLACK JACK!!")
        print("Dealer hand is: ", end = " ")
        for i in range(len(dealerHand)):
            if i != len(dealerHand) - 1:
                print(dealerHand[i], end = " ")
            else:
                print(dealerHand[i])

        # check if the dealer had black jack
        dealerBlackjack = checkBlackjack(dealerHand)
        # if the dealer also has black jack
        if dealerBlackjack == True:
            # its a tie, so the player gets 0 points, and the round is over
            print("Dealer has BLACK JACK")
            print()
            print("You tied with the dealer, that is a push and your score for this round is 0")
            print("Your total score is: ", totalScore)
            roundOver = True
        # if the dealer does not have black jack
        else:
            # the player wins and gets 2 points towards their total score, and the round is over
            print("Dealer does not have BLACK JACK")
            print()
            print("BLACK JACK yields a score of 2")
            totalScore += 2
            print("Your total score is: ", totalScore)
            roundOver = True
    
    # calculate player's hand value and print it
    # done the same way as in the playerTurn function above
    if roundOver == False:
        playerScore, numAces = computePlayerHandValue(playerHand)
        if playerScore <= 21 and numAces == 0:
            print("Your current hand value is: ", playerScore)
        elif numAces == 1:
            noAceValue = 0
            for card in playerHand:
                if card[0] != 'A':
                    if card[0].isdigit():
                        noAceValue += int(card[0])
                    elif card[0] in ['T', 'J', 'Q', 'K']:
                        noAceValue += 10
            value1 = noAceValue + 1 # ace as 1
            value2 = noAceValue + 11 # ace as 11
            print("You have 1 ace(s) in your hand. Your current hand value is:", value1)
            print("or ", value2)
        elif numAces > 1:
            print("You have ", numAces, " ace(s) in your hand. Your current hand value is: ", playerScore - 10)
            value = playerScore
            for aces in range(numAces):
                value += aces * 10
                print("or ", value)

    return playerHand, dealerHand, deck, roundOver, totalScore


def main(seedValue):
    # The main function implements the pseudocode by using the functions defined above.
    random.seed(seedValue)
    deck = createDeck()
    gameOver = False
    totalScore = 0  # initialize totalScore outside the while loop
    cardsDealt = 0 # initialze the counter for cards dealt, if it hits 52 a new deck is dealt

    while gameOver == False:
        
        if cardsDealt == 52:
            print("Dealing new deck")
            deck = createDeck()
        
        playerHand, dealerHand, deck, roundOver, totalScore = startGame(deck, totalScore)

        # initialize stay and bust variables for the player and dealer
        playerStay = False
        playerBust = False
        dealerStay = False
        dealerBust = False
        while playerStay == False and playerBust == False and roundOver == False:
            cardsDealt, playerHand, deck, playerStay, totalScore, playerBust, roundOver = playerTurn(cardsDealt, playerHand, dealerHand, deck, playerStay, totalScore, playerBust, roundOver)

        if playerBust == False and roundOver == False:
            while dealerStay == False and dealerBust == False:
                cardsDealt, dealerHand, deck, dealerStay, totalScore, dealerBust, roundOver = dealerTurn(cardsDealt, dealerHand, playerHand, deck, dealerStay, totalScore, dealerBust, roundOver)
                if dealerStay == True or dealerBust == True:
                    break  # exit the dealer's turn loop when they stay or bust

        
        if roundOver == False: # only call computeTotalScore if the round isn't over due to a bust
            totalScore = computeTotalScore(playerHand, dealerHand, totalScore)

        # play again
        gameOver = playAgain(gameOver)

    return





    
