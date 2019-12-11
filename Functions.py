#Takes the line as input and separates out the different fields into a list
def makeList(line):
    startBracket = line.find('[')
    endBracket = line.find(']')

    timestamp = line[startBracket: endBracket + 1]

    line = line[endBracket + 2:]

    secondColon = line.find(':')
    sender = line[:secondColon]

    content = line[secondColon + 2:]
    content = content.rstrip('\n')

    
    #print(timestamp, sender, content)
                  
    return (timestamp, sender, content)



#if the line is not the beginning of a new message (when there is a newline within the content of the message)
#append the line to the previous message content
#def addToList(lastLine, thisLine):
