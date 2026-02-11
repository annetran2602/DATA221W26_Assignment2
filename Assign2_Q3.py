# Anne Tran (UCID 30286177)
# Assign2_Q3


def originalFile(file):
    originalFile=file.split('\n')
    for line in originalFile:
        if line=='':
            originalFile.remove(line)
        else:
            originalFile=originalFile
    return originalFile

def formattedFile(file):
    lowercaseFile=file.lower() # change to lowercase
    noPuncFile=lowercaseFile.replace(",", "")
    noPuncFile = noPuncFile.replace(".", "")  # Remove "."
    noPuncFile = noPuncFile.replace("real-world", "real world")
    noWhiteSpace=noPuncFile.replace(" ", "")

    splitFile=noWhiteSpace.split('\n')

    for line in splitFile: # Check if there is any empty element in the list
        if line=='': # remove empty element
            splitFile.remove(line)
        else:
            splitFile=splitFile
    return splitFile
def identicalLine(splitFile):
    lineDict={}
    for lineNum, line in enumerate(splitFile, start=1):
        if line not in lineDict:
            lineDict[line] = [lineNum]
        else:
            lineDict[line].append(lineNum) # dict contain unique line and its line numbers

    return lineDict

def identicalSets(lineDict):
    identicalLineDict={}
    for line, lineNum in lineDict.items():
        if len(lineDict[line])>1:
            identicalLineDict[line]=lineNum # only keep lines had multiple line numbers in the file
    return identicalLineDict

def main():
    inputFile = open('sample-file.txt', mode='r') # read s file
    file = inputFile.read()
    inputFile.close()

    origin=originalFile(file) # original formatted file
    splitFile=formattedFile(file) # formatted file
    lineDict=identicalLine(splitFile) # dict contain lines & its line numbers
    identicalLineDict=identicalSets(lineDict) # dict that contain lines that appears multiple times

    # number of identical sets of lines
    numberOfSets=len(identicalLineDict) # the number of sets

    print(f"The number of identical set is {numberOfSets}")

    count=0
    for line, lineNum in identicalLineDict.items():
        for num in lineNum:
            print(f"Line {num} -> {origin[num-1]}") # print line number and its original formatted lines
            count += 1
            if count>3: # print only 2 sets
                break
        if count>3:
            break
main()



