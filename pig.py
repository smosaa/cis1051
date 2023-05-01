import random

def holdAt20(limit=20):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randint(1,6)
        if roll == 1:
            turnTotal = 0
            return turnTotal
        else:
            turnTotal += roll
            
    return turnTotal

def holdAt20Outcomes(trials):
    outcomes = {0:0}
    for val in range(20,26):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20()
        outcomes[score] +=1
    for score in outcomes:
        print(score, outcomes[score]/trials)

def holdAtXOutcomes(trials, limit):
    outcomes = {0:0}
    for val in range(limit,limit+6):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20(limit)
        outcomes[score] +=1
    for score in outcomes:
        print(score, outcomes[score]/trials)


def holdAt20orGoal(limit ,score):
    turnTotal = 0
    while turnTotal < limit and turnTotal + score < 100 :
        roll =  random.randint(1,6)
 
        if roll  == 1:
            turnTotal = 0
            return 0, score
        else:
            turnTotal += roll
    return turnTotal, score+turnTotal

def holdAt20orGoalGame():
    score = 0
    turns = 0
    while score < 100:
        turnTotal, newScore = holdAt20orGoal(18,score)
        turns += 1

        score = newScore
    return turns

def averagePigTurns():
    totalTurns = 0
    TRIALS = 100000
    for _ in range(TRIALS):
        turns = holdAt20orGoalGame()
        totalTurns += turns
    print(totalTurns / TRIALS)


    

def twoplayerpig():
    player1score = 0
    player2score = 0
    turntotal = 0
    player1turn = True
    player2turn = True
    gameisplaying = True
    while gameisplaying:
        print("Player 1 score:", player1score)
        print("Player 2 score:", player2score)
        print("It is player 1's turn")
        player1turntotal = 0
        player2turntotal = 0
        turntotal += 1
        while player1turn:
            x = random.randint(1,6)
            if x == 1:
                print("Roll:", x)
                break
            else:
                print("Roll:", x)
                player1turntotal += x
                if player1turntotal >=  20:
                    player1score += player1turntotal
                    break
                if player1score + player1turntotal >= 100:
                    print("New score:", player1score+player1turntotal)
                    gameisplaying = False
                    player1turn = False
                    player2turn = False
                    break
        if player2turn:
            print("It is player 2's turn")
        while player2turn:
            
            x = random.randint(1,6)
            if x == 1:
                print("Roll:", x)
                break
            else:
                print("Roll:", x)
                player2turntotal += x
                if player2turntotal >= 20:
                    player2score += player1turntotal
                    break
                if player2score + player2turntotal >= 100:
                    print("New score:" ,player2score+player2turntotal)
                    gameisplaying = False
                    player1turn = False
                    player2turn = False
                    break
                
twoplayerpig()
