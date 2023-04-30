import random


def holdAt20():
    turnTotal = 0
    while turnTotal < 20:
        roll = random.randint(1,6)
        #print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            #print("Turn Total:", turnTotal)
            return turnTotal

        else:
            turnTotal += roll
    #print("Turn Total:", turnTotal)
    return turnTotal


def holdat20outcomes(trials):
    outcomes = {0:0}
    for value in range(20,26):
        outcomes[value] = 0
    for _ in range(trials):
        score = holdAt20()
        outcomes[score] += 1

    for score in outcomes:
        print(score, outcomes[score]/trials)

holdat20outcomes(100)


x = holdAt20()
print(x)

