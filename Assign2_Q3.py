# Anne Tran (UCID 30286177)
# Assign2_Q3


def originalFile(file):
    originalFile=file.split('\n')
    for line in originalFile:
        if line=='':
            originalFile.remove('')
        else:
            originalFile=originalFile
    return originalFile

def formattedFile(file):
    lowercaseFile=file.lower() # change to lowercase
    noPuncFile=lowercaseFile.replace(",", "") # Remove ","
    noPuncFile=noPuncFile.replace(".", "") # Remove "."
    splitFile=noPuncFile.split('\n')

    for element in splitFile: # Check if there is any empty element in the list
        if element =='':
            splitFile.remove(element)# remove empty space
        else:
            splitFile=splitFile
    return splitFile

def identicalLine(splitFile):
    lineDict={}

    for index, line in enumerate(splitFile):
        if line not in lineDict:
            lineDict[line]=[index]
        else:
            lineDict[line].append(index)
    return lineDict

def main():
    inputFile = open('sample-file.txt', mode='r')
    file = inputFile.read()
    inputFile.close()

    splitFile=formattedFile(file)
    identicalDict=identicalLine(splitFile)

    print(splitFile)
    print(identicalDict)
main()



