import json
def load(fileName): #this function I made class object where  I call class .
    meraDb =MeraDB(fileName) # this line I call class . and make object.
    meraDb.load_file() # this line we use load function call.
    return meraDb 
class MeraDB():
                            # this is my class where I create All function like load and dump and I make constructor also
    fileName = ""
    jObject={}
    def __init__(self, fileName):
        self.fileName = fileName
        print self.fileName

    def load_file(self):
                            # this is my load function there my all data loading """
        print "Loading Database from ", self.fileName, " !"
        content = open(self.fileName).read()
        self.jObject = json.loads(content)
        print "DB loaded successfully!"
        print  self.jObject

    def dump(self):
                         #this is my dump function There i dump my all database data """
        print "Dumping database to ", self.fileName, " !"
        # open(self.fileName, 'w').write(json.dumps(self.jObject))
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        print "DB dumped successfully!"
        return "OK"