from ChineseFQI import FittedQIteration
from DBmodel import dataModel


if __name__ == '__main__':
  
    dataModel = dataModel()
    trainData = dataModel.buildRecords()    
    #testData=dataModel.get_Features_Targets()
    
    ChineseFQI = FittedQIteration(max_iterations=10, epsilon=0.00001, discount=0.9)
    ChineseFQI.run(trainData)
    
    
    #ChineseFQI.evaluate(testData)
    
    

    V_function  = ChineseFQI.V
    debug = 0
