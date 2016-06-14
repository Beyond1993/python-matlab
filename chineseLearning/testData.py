import sqlite3
import collections
import pickle

class testDataModel():
    def __init__(self):
        self.users = []
        self.cards = []
        self.conn = sqlite3.connect('data10000.db')
        print 'connect successfully'
        self.allRecordsDict = collections.defaultdict(lambda: 0)
        self.allRecordsList = []
        
        self.features_targets_dict = collections.defaultdict()
        self.features_targets_list = []        
        
        self.rewardFunction = [
         [0,-1,-2,-4,-7,-10], 
         [1, 0,-1,-2,-4,-7],
         [2, 1, 0,-1,-2,-4],
         [4, 2, 1, 0,-1,-2],
         [7, 3, 2, 1, 1, 1],
         [10,4, 4, 2, 1, 2]
        ]   
        """
        for lastReward in range(6):
            for currentReward in range(6):
                print self.rewardFunction[lastReward][currentReward]
        """  
                
        
        sql="SELECT user_id,event,timestamp,object_id, grade, easiness, acq_reps,ret_reps,lapses, acq_reps_since_lapse, ret_reps_since_lapse, scheduled_interval, actual_interval, thinking_time, next_rep from LOG"
        self.cursoser = self.conn.execute(sql)
    
    def printData(self):
        for row in self.cursoser:
            user_id = row[0]
            event = row[1]
            timestamp = row[2]
            object_id = row[3]
            grade = row[4]
            easiness = row[5]
            acq_reps = row[6]
            ret_reps = row[7]
            lapses = row[8]
            acq_reps_since_lapse = row[9]
            ret_reps_since_lapse = row[10]
            scheduled_interval = row[11]
            actual_interval  = row[12]
            thinking_time  = row[13]
            next_rep = row[14]
           
        debug = 0
          
    def getReward(self,lastReward,currentReward):
        return self.rewardFunction[lastReward][currentReward]
         
    def calculateUsers(self):
        sql = "select user_id from log group by user_id"
        users = [] 
        res = self.conn.execute(sql)
        for user in res:
            users.append(user[0])
            
        self.users = users;
    def calculateCards(self):
        sql = "select object_id from log group by object_id"
        cards = []
        res = self.conn.execute(sql)
        for card in res:
            cards.append(card[0])
        
            
        self.cards = cards

        

    def get_Feature_Target(self,user,card):
        sql = "select * from log where user_id = \'"+user+"\' and object_id= \'"+card+"\'"
        res = self.conn.execute(sql)
        
      
        feature_target = []
        last_state = 0
        last_action = 0      
        last_reward = 0
        isFiveShowFirst = 0
        for row in res:
            if row[4] == 5:
                state  = (row[9],row[10],row[11],row[12])
                action = row[5] #easiness = row[5]
                grade = row[4] #grade = row[4]
                isFiveShowFirst = 1
            if row[4] == 1 & isFiveShowFirst == 1:
                next_state = (row[9],row[10],row[11],row[12])
                next_action = row[5] #easiness = row[5]
                next_grade = row[4]
                easiness = row[5] 
                feature_target.append(((state,action,self.getReward(grade,next_grade),next_state),easiness))
        
        return feature_target
                

    def get_Features_Targets(self):
        self.calculateUsers()
        self.calculateCards()                
        for user in self.users:
            for card in self.cards:
                feature_target = self.get_Feature_Target(user,card)
                if len(feature_target) == 0:
                    print "None"
                    debug  =1
                else:
                    print "get feature_target"
                    self.features_targets_dict[(user,card)] = feature_target    
            
        self.destory()
        
        output = open('features_targets_dict.pkl', 'wb')
        pickle.dump(self.features_targets_dict, output)          
        return self.features_targets_dict
        
        
        
        
    def destory(self):
        self.conn.close()
        
if __name__ == '__main__':
    
    testDataModel = testDataModel()
    #testDataModel.printData()

    testDataModel.get_Features_Targets()
    
    
    debug = 0




