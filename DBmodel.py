import sqlite3
import collections

class dataModel():
    def __init__(self):
        self.users = []
        self.cards = []
        self.conn = sqlite3.connect('data10000.db')
        self.allRecordsDict = collections.defaultdict(lambda: 0)
        self.allRecordsList = []
        
        self.rewardFunction = [
         [0,-1,-2,-3,-4,-5], 
         [1, 0,-1,-2,-3,-4],
         [2, 1, 0,-1,-2,-3],
         [3, 2, 1, 0,-1,-2],
         [4, 3, 2, 1, 0,-1],
         [5, 4, 3, 2, 1, 0]
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
    
    def buildRecord(self,user,card):
        
        # u'string' is unicode string
        
        sql = "select * from log where user_id = \'"+user+"\' and object_id= \'"+card+"\'"
        #print sql
        res = self.conn.execute(sql)
        
        
        records = []
        last_state = 0
        last_action = 0        self.destory()

        last_reward = 0
        count = 0
        for row in res:
            state  = last_state
            action = last_action
            
            reward = self.getReward(last_reward,row[4]);
            
            next_state = (row[9],row[10],row[11],row[12])
            
            if count != 0:
                records.append((state,action,reward,next_state))
                
            last_state = (row[9],row[10],row[11],row[12])
            last_action = row[5] #easiness = row[5]
            last_reward = row[4] #grade = row[4]
            count = count + 1
        if len(records) == 0:
            #print "None"
            debug  =1
        else:
            print "building"
            self.allRecordsDict[(user,card)] = records
    
    def convertDictToList(self):
        for key,records in self.allRecordsDict.iteritems():
            for record in records:
                self.allRecordsList.append(record)
        
        for value in self.allRecordsList:
            print value        
        
       
    def buildRecords(self):    
        for user in self.users:
            for card in self.cards:
                self.buildRecord(user, card)
        self.convertDictToList()
        self.destory()
                
    def destory(self):
        self.conn.close()
        
if __name__ == '__main__':
    
    dataModel = dataModel()
    #dataModel.printData()
    dataModel.calculateUsers()
    dataModel.calculateCards()
    dataModel.buildRecords()
    
    
    debug = 0




