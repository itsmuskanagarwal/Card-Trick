import random
import itertools
import messagebox

#Generate a deck
full_deck = list(itertools.product(range(1,14),['of ❤', "of ♠", "of ♦", "of ♣"]))

#Pile creation
def create_pile(current_deck):
    # Generating three piles
    pile1 = []
    pile2 = []
    pile3 = []
    temp1 = 2
    temp2 = 1

    for i in range(0, len(current_deck)):
        if i == 0 or i % 3 == 0:
            pile1.append(current_deck[i])
        elif i == temp2:
            pile2.append(current_deck[i])
            temp2+=3
        elif i == temp1 :
            pile3.append(current_deck[i])
            temp1 += 3

    # Printing all three pile in top down approach
    for i in range(0, 7):
        print(f"{pile1[i]}        {pile2[i]}        {pile3[i]}")

    # Ask user to pick a card and input the pile number where the card is
    messagebox.showinfo(title="Card Trick", message="Select any one card")
    answer = input("\nWhich pile is you card in? 1/2/3")

    if  answer == "1":
        new_deck = pile2+pile1+pile3
        return new_deck
    elif answer =="2":
        new_deck = pile1 + pile2 + pile3
        return new_deck
    elif answer == "3":
        new_deck = pile1 + pile3 + pile2
        return new_deck
    else:
        print("Wrong input")


#Play the trick for once
def play():
    random.shuffle(full_deck) #shuffle deck everytime you play

    #Creating a 21 card deck- random
    deck=[]
    for i in range(0,21):
        deck.append(random.choice(full_deck))

    #Create 3 pile and ask user for the pile number and combine all piles and repeat
    new_deck=[]
    for i in range(0,2):
        next_deck = create_pile(deck)
        deck = [item for item in next_deck]


    for elements in deck:
        print(elements)



#Keep your game on until user asks to end
play()
game_on = True
while game_on:
    if input("\nYou want to play again? 'Y'/'N'").lower() == "y":
        play()
    else:
        print("Game Over!")
        game_on = False



