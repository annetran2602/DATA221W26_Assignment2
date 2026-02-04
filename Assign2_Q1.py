# Anne Tran (UCID: 30286177)
# Assign2_Q1

# Open the file
inputFile=open('sample-file.txt', mode='r')
file=inputFile.read()

lowercaseFile=file.lower() # change to lowercase

#Remove punctuation
noPuncFile=lowercaseFile.replace(",", " ") # Remove ","
noPuncFile=noPuncFile.replace(".", " ") # Remove "."

# Split into words
splitFile=noPuncFile.split()
twoCharList=[]


for word in splitFile:
    if len(word)>=2:
        twoCharList.append(word)
    else:
        twoCharList=twoCharList


wordDict={}
for word in twoCharList:
    if word not in wordDict:
        wordDict[word]=1
    else:
        wordDict[word]+=1


sortedWordDict=dict(sorted(wordDict.items()))
print(sortedWordDict)

