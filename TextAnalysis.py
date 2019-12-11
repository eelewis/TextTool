#This program will input data about a text conversation from a .txt file and
#perform analysis upon that data to provide useful information for the user.


#use custom made class and functions
import Message
from Functions import makeList

FILENAME = input('Enter the name of the file please: ')

#open input file and display the header info
inputFile = open(FILENAME, encoding='utf8')
header = inputFile.readline()
print(header)


#initialize and assign some variables
line = inputFile.readline()
lineList = []
messageCount = 0
messages = []



#main data creation loop, iterates over each line in the file and creates a list with
#each message as an element in that list
while line != '':
    if line == '\n':
        line = inputFile.readline()


    elif line.startswith('[') == False:
        line = line.rstrip('\n')
        messages[messageCount - 1].addContent(line)
        line = inputFile.readline()
        
    else:
        messageData = makeList(line)

        messages.append(Message.Message(messageData[0], messageData[1], messageData[2]))
        
        line = inputFile.readline()
        messageCount += 1


        

#now I need to iterate through all the messages from the beginning and group each message by what date it was sent

index = 0


#create a new list to store all the contents of a day's texts, set the date to determine the day
dayContents = []
date = messages[index].getDate()
dayContents = Message.DayMessages(date)

#this list will hold an element for each day that has texts exchanged
allDays = []
newDay = True
while index < messageCount:
    

    if index < messageCount - 1:
        date = messages[index].getDate()
        nextDate = messages[index + 1].getDate()

    else:
        allDays.append(dayContents)

    if newDay == True:
        dayContents.setSender(messages[index].getSender())
    


    if date == nextDate:

        if messages[index]._Message__sender == 'Me':
            dayContents.addMyMessageContent(messages[index].getContent())
            newDay = False
        else:
            dayContents.addTheirMessageContent(messages[index].getContent())
            newDay = False
            
    else:
        if messages[index]._Message__sender == 'Me':
            dayContents.addMyMessageContent(messages[index].getContent())
            newDay = True

        else:
            dayContents.addTheirMessageContent(messages[index].getContent())
            newDay = True


        allDays.append(dayContents)
        dayContents = []
        date = nextDate
        dayContents = Message.DayMessages(date)
    
    index += 1


print('DATE\t\t # \t First Text \t Me \t Them')

for i in range(len(allDays)):
    print(allDays[i].getDate(), '\t', allDays[i].getTotalNumberOfMessages(), '\t', 
          format(allDays[i].getSender(), '12'), '\t', allDays[i].getNumberOfMine(), '\t', allDays[i].getNumberOfTheirs())





    
        


inputFile.close()
