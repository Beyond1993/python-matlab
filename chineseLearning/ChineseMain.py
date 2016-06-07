from ChineseFQI import FittedQIteration
from DBmodel import dataModel


if __name__ == '__main__':
  
    dataModel = dataModel()
    trainData = dataModel.buildRecords()    
    
    ChineseFQI = FittedQIteration(max_iterations=10, epsilon=0.00001, discount=0.9)
    ChineseFQI.run(trainData)
    
    dataModel.get_Features_Targets()
    ChineseFQI.evaluate(ChineseFQI.features_targets_dict)
    
    

    V_function  = ChineseFQI.V
    debug = 0
