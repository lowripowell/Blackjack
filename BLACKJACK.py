import numpy as np

def peopleBlackJack(decks):
    if decks == 0:
        goal_state = 21
        starting_state = 0
        C = starting_state
        actions = []
        states = []
        text_states = []
        reward = 0
        while C < goal_state:
            nC = np.random.randint(1,13)
            if nC >= 2 and nC <=10:
                textC = nC
            elif nC == 1:
                textC = "A"
                if C < 11:
                    nC = 11
            elif nC == 11:
                nC = 10
                textC = "J"
            elif nC == 12:
                nC = 10
                textC = "Q"
            elif nC == 13:
                nC = 10
                textC == "K"                
            action = int(input("Type '1' for hit or '0' for hold: "))
            if action == 1:
                print("\n")
                C = C + nC
                states.append(nC)
                reward = (reward+nC)^2
                text_states.append(textC)
            else:
                break
            print("Current hand: ", text_states)
            print("Current total: " + str(C))
            actions.append(action)
        if C > 21:
            states.append(nC)
            print("Final Hand: ", text_states)
            print("stupid a$$ hoe")
        elif C == 21:
            print("YASS, Slay queen")
            print("Score = " + str(C))
        else:
            print("Pussy")
            print("Score = " + str(C))
        restart = input("Press 'e' and 'Enter' to play again: ")
        if restart == "e":
            peopleBlackJack(0)
