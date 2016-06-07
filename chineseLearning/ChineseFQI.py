import random
import collections
import numpy as np
import pickle
import string
import math
import copy
import operator
import time
import pickle




from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.advanced_activations import PReLU
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adadelta, Adagrad
from keras.utils import np_utils, generic_utils
from six.moves import range



def has_converged(V, prev_V, epsilon):
    total = 0
    for s, v in V.iteritems():
        for a,v2 in v.iteritems():
            prev_v = prev_V[s][a]
            total += abs(v2 - prev_v)

    if total < epsilon:
        return True
    return False

class FittedQIteration(object):
    def __init__(self, max_iterations, epsilon, discount, learning_rate=0.1):
        self.max_iterations = max_iterations
        self.epsilon = epsilon
        self.discount = discount
        self.learning_rate = learning_rate
        self.Q_function = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        self.batch_size = 100
        self.grid = None
        self.inputSize = 5
        
        self.actions = [] #[(-1,0),(1,0),(0,-1),(0,1)] ^ d <  >
        self.states  = []
        
        self.init_neural_networks()
        self.old_learn = copy.deepcopy(self.learner)
            
        self.policy = collections.defaultdict()
        
        
    def update_Q_funtion(self):
        for state in self.states:
            for action in self.actions:
                self.Q_function[state][action] = self.getQ(state,action)
   
    def set_Policy(self):
        for state, actions in self.Q_function.iteritems(): #actions is a dict
            new_pi = max(actions.iteritems(), key=operator.itemgetter(1))[0] 
            #operator.itemgetter(1) is the value of actions.iteritems() , use this value as a key to get max action for per state
            self.policy[state] = new_pi
            
        output = open('policy.pkl', 'wb')
        pickle.dump(self.policy, output)            

    
    
    def get_feature(self,state,action):
        feature = np.array([state[0],state[1],state[2],state[3],action])
        feature = feature.reshape(1,feature.size)
        return feature
        
    
    def getQ(self, state, action):
        Q_value = self.learner.predict(self.get_feature(state, action))
        
        return Q_value

    def build_dataset(self, data):
        
        print "build dataset"
        time1 = time.time()
        dataset = []
        
        for key, (state, action, reward, newState) in data.iteritems():
            print "building"
            # over the newState and newAction because it's what's next
            
            target = reward + self.discount * max(self.getQ(newState, newAction) for newAction in self.actions)
            #if (state == (1,0) )& (action == (0,1)):
                #print reward,target
                #print max(self.getQ(newState, newAction) for newAction in self.actions)
                #for newAction in self.actions:
                    #print newState,newAction,self.getQ(newState, newAction)
                    #print 'maxQ',max(self.getQ(newState, newAction) for newAction in self.actions)
                    
            dataset.append((state, action, target))
        time2 = time.time();
        print "building end",time2-time1
        return dataset
    
    
    def set_V(self):
        V = collections.defaultdict(lambda: 0)
        for state in self.states:
            V[state] = max(self.getQ(state, action) for action in self.actions)
        self.V = V

    def set_actions_states(self, data):
        actions = set()
        states = set()
        for key, (state, action, reward, newState) in data.iteritems():
            #print reward
            actions.add(action)
            states.add(state)
        self.actions = list(actions)
        self.states  = list(states)        
    
    def init_neural_networks(self):
        print "init start"
        model = Sequential()
        model.add(Dense(input_dim = self.inputSize,output_dim = 20,init="he_normal",activation = "tanh"))
        model.add(Dense(input_dim = 20,output_dim = 1,init="he_normal",activation = "tanh"))
        model.add(Dense(input_dim=1 , output_dim = 1, init="he_normal",activation = "linear"))
        model.compile(loss = 'mean_squared_error',optimizer = 'rmsprop')
        weights = model.get_weights()
        self.learner = model
        print "init end"
    
    def train_neural_network(self,dataset):
        
        print 'train start'  
        #print max(self.getQ((1,0), newAction) for newAction in self.actions)
        for state, action, target in dataset:
            
            sample = np.random.randint(0,1,self.batch_size)
            d = np.zeros((self.batch_size,self.inputSize))
            y = np.zeros((self.batch_size,1))
            for i,row in enumerate(sample):  #i is index, row is value, totaly 100 rows repeat
                d[i,:] = self.get_feature(state,action)
                y[i] = target
                
            self.learner.train_on_batch(d,y)
                #if (state == (1,0) )& (action == (0,1)):    
                    #print target,self.learner.predict(self.get_feature((1,0), (0,1)))
        print 'train end'
        #self.learner = copy.deepcopy(self.learner)##??
        #print self.learner.predict(self.get_feature((1,0), (0,1)))
        debug = 0
    
    def run(self, data):
        print "run start"
        self.set_actions_states(data)
        prev_Q_function = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        
        
        #dataset = self.build_dataset(data)# even data is same ,the Q_function is different
        
        for iteration in range(self.max_iterations):
            print 'the ',iteration,'iteration'
            dataset = self.build_dataset(data)
            self.train_neural_network(dataset) 
            self.update_Q_funtion()
            #if has_converged(self.Q_function, prev_Q_function, self.epsilon):
                #break
            #prev_Q_function = self.Q_function
        self.set_V()
        self.set_Policy()
        
    def evaluate(self,features_targets):
        for feature,target in features_target:
            prediction = self.policy(feature);
            
            print "pediction is",prediction,"target is",target
        

