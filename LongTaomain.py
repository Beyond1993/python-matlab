##this is the file using qlearning_FA_NN for test

from qlearning_FA_NN import DQN
import sys,os,subprocess,random,math
import numpy as np
import matplotlib.pylab as pl
import pickle

import scipy.io as scio
import math
PORT=8001


class chinese_application():

    def __init__(self,gamma=.9,alpha=.3,epsilon=.2,):
        self.actions = [1,2,3,4]
        inputSize = 2
        self.agent = DQN(self.feat_funct,inputSize,self.actions,gamma,alpha,epsilon, shape = (20,1))
        self.rewards = []
    def feat_funct(self,state,action):
        #f = np.zeros((10,2))
        #col = action
        #f[:,col] = state
        return np.array(state+[action])
    
    def readMat(self):
        dataFile = 'randTraj100.mat'
        data = scio.loadmat(dataFile)   
        #print type(data)
            
            
        memory_tmp_data = []
        memory_tmp_data2 = []
        
        firstFlag = 1
        for episode in data['Traj']:
            for value in episode:
                for steps in value:
                    print steps[0],steps[1], steps[2] , steps[3]
                    #if steps[0] == 25 & steps[3] == 25:
                     #   if firstFlag == 0:
                      #      continue
                       # firstFlag = 0
                    step_state = steps[0]
                    step_action = steps[1]
                    step_reward = steps[2]
                    step_new_state = steps[3]
                    step = (step_state,step_action,step_reward,step_new_state)  
                    memory_tmp_data.append(step)
         
        memory_data = {} 
        index = 0;
        for i in memory_tmp_data:
            memory_data[index] = i
            index = index + 1 
        return memory_data    
    from qlearning_FA_NN import DQN
import sys,os,subprocess,random,math
import numpy as np
import matplotlib.pylab as pl
import pickle

import scipy.io as scio
import math
PORT=8001


class chinese_application():

    def __init__(self,gamma=.9,alpha=.3,epsilon=.2,):
        self.actions = [1,2,3,4]
        inputSize = 2
        self.agent = DQN(self.feat_funct,inputSize,self.actions,gamma,alpha,epsilon, shape = (20,1))
        self.rewards = []
    def feat_funct(self,state,action):
        #f = np.zeros((10,2))
        #col = action
        #f[:,col] = state
        return np.array(state+[action])
    
    def readMat(self):
        dataFile = 'randTraj100.mat'
        data = scio.loadmat(dataFile)   
        #print type(data)
            
            
        memory_tmp_data = []
        memory_tmp_data2 = []
        
        firstFlag = 1
        for episode in data['Traj']:
            for value in episode:
                for steps in value:
                    print steps[0],steps[1], steps[2] , steps[3]
                    #if steps[0] == 25 & steps[3] == 25:
                     #   if firstFlag == 0:
                      #      continue
                       # firstFlag = 0
                    step_state = steps[0]
                    step_action = steps[1]
                    step_reward = steps[2]
                    step_new_state = steps[3]
                    step = (step_state,step_action,step_reward,step_new_state)  
                    memory_tmp_data.append(step)
         
        memory_data = {} 
        index = 0;
        for i in memory_tmp_data:
            memory_data[index] = i
            index = index + 1 
        return memory_data    
    
    
    def run(self):
        data = self.readMat()
        for key,(state,action,reward,new_state) in data.iteritems():
            self.agent.qUpdate([state], action, reward, [new_state])

    
    def run(self):
        data = self.readMat()
        for key,(state,action,reward,new_state) in data.iteritems():
            self.agent.qUpdate([state], action, reward, [new_state])
        debug = self.agent.chooseAction([24])
        print debug
        c= 0

    

FQI=chinese_application()
FQI.run()



