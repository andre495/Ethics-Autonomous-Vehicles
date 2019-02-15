'''
This class defines the nodes that make up states in the grid.
It has various getters and setters to retrieve information about a node.
'''
import random,math

class state_node():
    def __init__(self, name, nextStates, reward):
        self.name=name
        self.nextStates=nextStates
        self.reward=reward
        self.isStart=False
        self.Qvals=[('l',0), ('r',0), ('u',0), ('d',0)]

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

    def getNextStates(self):
        return self.nextStates

    def setNextStates(self, newNextStates):
        self.nextStates=newNextStates

    def getReward(self):
        return self.reward

    def addReward(self, reward):
        self.reward=reward

    def isStart(self):
        return self.isStart

    def setStart(self):
        self.isStart=True

    def isTerminal(self):
        if len(self.getNextStates()) > 0:
            return False
        else:
            return True

    def setQval(self, action, value):
        for item in self.Qvals:
            if item[0] == action:
                item[1] == value

    def getQvals(self):
        return self.Qvals

    def actionToState(self, state, action):
        #takes current state and proposed action, returns next state
        for item in self.nextStates():
            if action == item[1]:
                return item[0]
