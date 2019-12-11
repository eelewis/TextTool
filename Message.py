class Message():

    #initialize data attributes
    def __init__(self, timestamp, sender, content):
        self.__timestamp = timestamp
        self.__date = timestamp[:timestamp.find(' ')] + ']'
        self.__time = '[' + timestamp[timestamp.find(' ') + 1:]
        self.__sender = sender
        self.__content = content
    


    #methods

    def addContent (self, newContent):
        self.__content += ' ' + newContent
        return

    def getTimestamp(self):
        return self.__timestamp

    def getDate (self):
        return self.__date
        
    def getTime (self):
        return self.__time

    def getSender (self):
        return self.__sender

    def getContent (self):
        return self.__content
    

    def printAll (self):
        print(self.__timestamp, self.__sender, self.__content)
        return



class DayMessages ():

    #initialize data attributes
    def __init__(self, date):
        self.__date = date
        
        self.__myMessageContent = []
        self.__theirMessageContent = []

        self.__firstMessageSender = ''

        self.__numberOfMessages = 0
        
        self.__numberOfMine = 0
        
        self.__numberOfTheirs = 0
        
    

    #methods
    def addMyMessageContent(self, message):
        self.__myMessageContent.append(message)
        return
    def addTheirMessageContent(self, message):
        self.__theirMessageContent.append(message)
        return
    
    def setSender(self, sender):
        self.__firstMessageSender = sender


    def getSender(self):
        return self.__firstMessageSender

    def getNumberOfMine(self):
        self.__numberOfMine = len(self.__myMessageContent)
        return self.__numberOfMine

    def getNumberOfTheirs(self):
        self.__numberOfTheirs = len(self.__theirMessageContent)
        return self.__numberOfTheirs

    
    def getDate(self):
        return self.__date

    def getMyContent(self):
        return self.__myMessageContent

    def getTheirContent(self):
        return self.__theirMessageContent

    def getTotalNumberOfMessages(self):
        self.__numberOfMine = len(self.__myMessageContent)
        self.__numberOfTheirs = len(self.__theirMessageContent)


        self.__numberOfMessages = self.__numberOfMine + self.__numberOfTheirs
        return self.__numberOfMessages

        

    
                                                                     
        
    





                           
    
    
