import scipy.io as scio
import math

from FQI import FittedQIteration

def oneToXY(position):
    width = 5.0
    row = position % width
    if row == 0.0:
        row = 5
    row = row - 1
    col = math.ceil(position / width) - 1
    return (int(row),int(col))
    
def oneToAction(position):
    if position == 4: #'^'
        return (-1,0)
    if position == 2: #'d'
        return (1,0)    
    if position == 3: #'<'
        return (0,-1)          
    if position == 1: #'>'
        return (0, 1)            

def readMat():
    dataFile = 'randTraj100.mat'
    data = scio.loadmat(dataFile)   
    #print type(data)
        
        
    memory_tmp_data = []
    memory_tmp_data2 = []
    
    firstFlag = 1
    for episode in data['Traj']:
        for value in episode:
            for steps in value:
                #print steps[0],steps[1], steps[2] , steps[3]
                #if steps[0] == 25 & steps[3] == 25:
                 #   if firstFlag == 0:
                  #      continue
                   # firstFlag = 0
                step_state = oneToXY(steps[0])
                step_action = oneToAction(steps[1])
                step_reward = steps[2]
                step_new_state = oneToXY(steps[3])
                step = (step_state,step_action,step_reward,step_new_state)  
                memory_tmp_data.append(step)
     
    memory_data = {} 
    index = 0;
    for i in memory_tmp_data:
        memory_data[index] = i
        index = index + 1 
    return memory_data
    

if __name__ == '__main__':
    data = readMat()
    
    FQI = FittedQIteration(max_iterations=1000, epsilon=0.00001, discount=0.9)
    FQI.run(data)    
    V_function  = FQI.V
    debug = 0
