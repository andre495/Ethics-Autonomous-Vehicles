'''
What does this class do?
'''

from State_Node import *
from Grid import *
import random
import numpy as np
from copy import deepcopy
class agent():

    def __init__(self, startState):
        self.currentState=startState

    def getCurrentState(self):
    #Returns current state of agent
        return self.currentState

    def setCurrentState(self, state):
        self.currentState=state

    def getValuefromQvals(self, state):
    #Returns list of values of legal actions
        if len(state.getNextStates())==0:
            return (None,0)
        lst=[]
        #list of possible actions
        for item in state.getNextStates():
            lst+=[item[1]]
        max=(None, -100000)
        for item in state.getQvals():
            if item[1] >= max[1] and item[0] in lst:
                max=item
        return max

    def getNextStatesAndProbs(self, state_node, action, grid):
    #Returns list of tuples of containing possible next states and their probabilities given 'action' in 'state_node'
        statesAndProbs=[]
        globalNoise=grid.getGlobalNoise()
        nextStates=deepcopy(state_node.getNextStates())
        found=False
        for possibility in nextStates:
            if possibility[1] == action:
                found=True
                statesAndProbs+= [(possibility, globalNoise)]
                nextStates.remove(possibility)
        if found and len(nextStates) != 0:
            prob=(1-globalNoise)/len(nextStates)
            for possibility in nextStates:
                statesAndProbs+= [(possibility, prob)]
        else:
            for item in nextStates:
                statesAndProbs+=[(item, 1/len(nextStates))]
        return statesAndProbs

    def makeMove(self, grid):
        #This function controls each move in an iteration
        #First update current state's Q values
        currentQvalList=self.currentState.getQvals()
        for Q in currentQvalList:
            #Bellman EQ
            probs=self.getNextStatesAndProbs(self.currentState, Q[0], grid)
            list=[]
            for item in probs:
                a=self.getValuefromQvals(probs[0][0][0])[1]
                b=probs[0][1]
                list+=[a*b]
                print b
            update=self.currentState.getReward()+(grid.getGamma()*sum(list))
            self.currentState.setQval(Q[0], update)

        #Check max Q val and make optimal move w/ probability of random move
        bestAction=self.getValuefromQvals(self.currentState)[0]
        if bestAction != None:
            #Not in terminal state--can move agent
            odds=grid.getGlobalNoise()
            s=np.random.uniform(0,1)
            if s < odds:
                for item in self.currentState.getNextStates():
                    if item[1]==bestAction:
                        self.currentState=item[0]
            #random new state picking
            else:
                l=['r','l','u','d']
                l.remove(bestAction)
                ss=np.random.uniform(0,1)
                if ss > 0 and ss < 0.33:
                    for item in self.currentState.getNextStates():
                        if item[1]==l[0]:
                            self.currentState=item[0]
                elif ss >= 0.33 and ss < 0.66:
                    for item in self.currentState.getNextStates():
                        if item[1]==l[1]:
                            self.currentState=item[0]
                else:
                    for item in self.currentState.getNextStates():
                        if item[1]==l[2]:
                            self.currentState=item[0]
        #End state
        if bestAction == None:
            self.currentState=grid.getStartState()
