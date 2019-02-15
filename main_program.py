'''
This program runs the study, calling upon other classes to perform functions on the agent and environment
'''

from State_Node import *
from Agent import *
from Grid import *
import csv
import random
import numpy as np

def getStats(textfile):
    #read textfile seperated by commas, return list of lists containing names and values
    data=[]
    with open(textfile, 'r') as csvfile:
        students_reader = csv.reader(csvfile, delimiter=',')
        for row in students_reader:
            row[1]=int(row[1])
            data+= [row]
    return data

def runIterations(numIterations, agent, grid):
    for i in range(numIterations):
        while not agent.getCurrentState().isTerminal():
            agent.makeMove(grid)
    results=grid.getPolicy()
    #print policy after iterations
    for i in range(5):
            print (results[0][i], results[1][i], results[2][i], results[3][i], results[4][i])
def newScenario(data, livingPenalty, noise, gamma, iterations):
        #Gather data points from external file
        myData=getStats(data)
        random.shuffle(myData)
        #Instantiate grid w/ parameters
        myGrid=grid(myData, livingPenalty, noise, gamma)
        myGrid.createGrid()
        #Instantiate car with beginning state
        car=agent(myGrid.getStartState())
        #Run certain amount of iterations on agent and grid combination
        runIterations(iterations, car, myGrid)
        #Print results and reset all
        print 'Obstacle 1: ', myData[0][0]
        print 'Obstacle 2: ', myData[1][0]
        print

def main():
    #run a unique scenario
    for i in range(20):
        newScenario("data.txt", -10, 0.90, 1.10, 1000)


if __name__ == '__main__':
    main()
