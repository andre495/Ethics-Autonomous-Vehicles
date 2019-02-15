'''
This class defines the grid world and methods to retrieve ceratain data
'''

from State_Node import *
from Agent import *

class grid():
    def __init__(self, data, livingReward, globalNoise, gamma):
        self.livingReward=livingReward
        self.globalNoise=globalNoise
        self.gamma=gamma
        self.data=data
        self.Gridworld=[]
        self.policy=[]

    def createGrid(self):
        #This function creates a grid using input of reward values, noise, and list of 2 external 'life value' data points

        #Create Grid with state_nodes
        self.Gridworld=[[state_node('normal', [], self.livingReward) for x in range(5)] for y in range(5)]
        self.policy=[[None for x in range(5)] for y in range(5)]

        for x in range(5):
            for y in range(5):
                #Set legal actions
                if x != 0:
                    self.Gridworld[x][y].setNextStates(self.Gridworld[x][y].getNextStates()+[(self.Gridworld[x-1][y], 'l')])
                if x != 4:
                    self.Gridworld[x][y].setNextStates(self.Gridworld[x][y].getNextStates()+[(self.Gridworld[x+1][y], 'r')])
                if y != 0:
                    self.Gridworld[x][y].setNextStates(self.Gridworld[x][y].getNextStates()+[(self.Gridworld[x][y-1], 'd')])
                if y != 4:
                    self.Gridworld[x][y].setNextStates(self.Gridworld[x][y].getNextStates()+[(self.Gridworld[x][y+1], 'u')])

                #set end states
                if (x,y) == (3,0):
                #obstacle 1
                    self.Gridworld[x][y].setNextStates([])
                    self.Gridworld[x][y].addReward(self.data[0][1])
                    self.Gridworld[x][y].setName(self.data[0][0])
                if (x,y) == (3,4):
                #obstacle 2
                    self.Gridworld[x][y].setNextStates([])
                    self.Gridworld[x][y].addReward(self.data[1][1])
                    self.Gridworld[x][y].setName(self.data[1][0])

                #Start state
                if (x,y) == (0,2):
                    self.Gridworld[x][y].setName('Start State')
                    self.Gridworld[x][y].setStart()

    def getStates(self):
        return self.states

    def getGlobalNoise(self):
        return self.globalNoise

    def getLivingReward(self):
        return self.livingReward

    def getGamma(self):
        return self.gamma

    def getPolicy(self):
        for x in range(5):
            for y in range(5):
                policyTuple=(None, 0)
                for val in self.Gridworld[x][y].getQvals():
                    if val[1]>=policyTuple[1]:
                        val=policyTuple
                if policyTuple[1]>0:
                    self.policy[x][y]=policyTuple
                else:
                    self.policy[x][y]=(policyTuple[0], self.Gridworld[x][y].getReward())
        return self.policy

    def getStartState(self):
    #Returns starting state in the MDP
        for row in self.Gridworld:
            for state in row:
                if state.isStart:
                    return state
