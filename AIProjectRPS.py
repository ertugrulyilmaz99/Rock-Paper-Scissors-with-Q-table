import random
import numpy as np

def gameRules(agent, player, winLostDraw):

    if (player == 'R' and agent == 'P') or (player == 'P' and agent == 'S') or (player == 'S' and agent == 'R'):
        winLostDraw[0] += 1
        print("Agent Won!")
    elif player == agent:
        winLostDraw[2] += 1
        print("It is a draw!")
    else:
        winLostDraw[1] += 1
        print("Player Won!")

def randomChoice():
    return random.choice(['P', 'R', 'S'])

def agentChoice(probabilityArray, lastTwoChoice):
    if lastTwoChoice == "PP":
        row = 0
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "PR":
        row = 1
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "PS":
        row = 2
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "RP":
        row = 3
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "RR":
        row = 4
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "RS":
        row = 5
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "SP":
        row = 6
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "SR":
        row = 7
        column = np.argmax(probabilityArray[row])
    elif lastTwoChoice == "SS":
        row = 8
        column = np.argmax(probabilityArray[row])

    if column == 0:
        return 'S'
    elif column == 1:
        return 'P'
    else:
        return 'R'

def calculateEstimation(counterArray, probabilityArray, lastTwoChoice, current):
    if current == 'P':
        column = 0
    elif current == 'R':
        column = 1
    else:
        column = 2

    if lastTwoChoice == "PP":
        counterArray[0][column] += 1
    elif lastTwoChoice == "PR":
        counterArray[1][column] += 1
    elif lastTwoChoice == "PS":
        counterArray[2][column] += 1
    elif lastTwoChoice == "RP":
        counterArray[3][column] += 1
    elif lastTwoChoice == "RR":
        counterArray[4][column] += 1
    elif lastTwoChoice == "RS":
        counterArray[5][column] += 1
    elif lastTwoChoice == "SP":
        counterArray[6][column] += 1
    elif lastTwoChoice == "SR":
        counterArray[7][column] += 1
    elif lastTwoChoice == "SS":
        counterArray[8][column] += 1

    for i in range(0, len(probabilityArray)):
        sampleSpace = counterArray[i][0] + counterArray[i][1] + counterArray[i][2]
        for j in range(0, len(probabilityArray[i])):
            probabilityArray[i][j] = (counterArray[i][j] / sampleSpace) * 100

string = ''
for i in range (0, 3):
    string = string + randomChoice()
#print(string)

current = randomChoice()
lastFirst = randomChoice()
lastSecond = randomChoice()
lastTwoChoice = lastSecond + lastFirst

#print(lastTwoChoice)

counterArray = [[1 for x in range(3)] for y in range(9)]

probabilityArray = [[0.33 for x in range(3)] for y in range(9)]

#string = "SSPSSPSSPSSPRRRSSP"
#print(string)



for i in range (2,len(string)):
    lastSecond = string[i-2]
    lastFirst = string[i-1]
    current = string[i]
    lastTwoChoice = lastSecond + lastFirst

    calculateEstimation(counterArray, probabilityArray, lastTwoChoice, current)


#print(counterArray)
#print(probabilityArray)

winLostDraw = [0] * 3
counter = 0

while(True):
    who = input("1. Agent vs Player\n2. Agent vs Random Agent(1000 times)")
    if who == '1' or who == '2':
        break
    else:
        print("NOT A VALID INPUT!!!")
while(counter < 1000):
    who = int(who)
    if who == 1:
        playerChoice = input("Choose:\nR or P or S or end\n")
    else:
        playerChoice = randomChoice()

    if playerChoice == "end":
        break

    lastSecond = lastFirst
    lastFirst = current
    current = playerChoice
    lastTwoChoice = lastSecond + lastFirst

    agentEstimation = agentChoice(probabilityArray, lastTwoChoice)

    print("Player Choice:", playerChoice, "Agent Estimation:", agentEstimation)

    gameRules(agentEstimation, playerChoice, winLostDraw)

    calculateEstimation(counterArray, probabilityArray, lastTwoChoice, current)


    counter += 1

print("\nResults:\nAgent Wins:", winLostDraw[0])
print("Agent Loses:", winLostDraw[1])
print("Agent Draw:", winLostDraw[2])