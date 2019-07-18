import json
import os.path
def load(fileName): #this function I made class object where  I call class .
    meraDb =MeraDB(fileName) # this line I call class . and make object.
    meraDb.load_file() # this line we use load function call.
    return meraDb 
class MeraDB():                        # this is my class where I create All function like load and dump and I make constructor also
    fileName = ""
    jObject={}
    def __init__(self, fileName):
        self.fileName = fileName

    def load_file(self):
        if self.fileName not in self.jObject:
            self.dump() 
        if os.path.exists(self.fileName):                    # this is my load function there my all data loading """
                print "Loading Database from ", self.fileName, " !"
                content = open(self.fileName).read()
                self.jObject = json.loads(content)
                print "DB loaded successfully!"
                return self.jObject
        else:
            self.dump()


    def dump(self): #this is my dump function There i dump my all database data """
        print "Dumping database to ", self.fileName, " !"
        # open(self.fileName, 'w').write(json.dumps(self.jObject))
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        print "DB dumped successfully!"
        print "ok"
    def setData(self,key,value):
        self.jObject[key]=value
        self.dump()
        return self.jObject
    
    def getData(self,key):
        get_value=self.jObject[key]
        return get_value

    def getAll(self,all_data):
        for key,value in all_data.items():
            print key,"-", value
    def rem(self,key):
        if key in self.jObject:
            del(self.jObject[key])
        self.dump()
    def existsKey(self,key):
        if key in self.jObject:
            return True
        else:
            return False

    def totalKeys(self,all_data):
        total_Keys=0
        for key in all_data:
            total_Keys=total_Keys+1
        print total_Keys

    def delDb(self,all_db):
        del(self.jObject)
        self.dump()
    
    def randomInsertKeys(self,str):
        for word in str:
            if word not in self.jObject:
                self.jObject[word] =+ 1
            else:
                self.jObject[word] =+ 1
        self.dump()