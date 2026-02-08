# Anne Tran (UCID: 30286177)
# Assign2_Q2

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

# Only keep word has more than and equal to 2 characters
for word in splitFile:
    if len(word)>=2:
        twoCharList.append(word)
    else:
        twoCharList=twoCharList #remove word has 1 character

# Pair 2 consecutive words into one element in the list
bigramsList=[]

for i in range (0, len(twoCharList),2):
    if i+1<len(twoCharList): # check if word and next word can be combined
        bigramsList.append(twoCharList[i] + " " + twoCharList[i+1]) # combine two words into one element & add to the new list
    else:
        bigramsList.append(twoCharList[i]) # check if word have the next word to pair

# Create dictionary containing word and its word count
wordDict={} # empty dict
for word in bigramsList:
    if word not in wordDict.keys(): # check if this word in the key & start count at 1
        wordDict[word]=1
    else: # check if the word already exits & count its frequency in the file
        wordDict[word]+=1

# Sort the dictionary based on its values descending
sortedWordDict=dict(sorted(wordDict.items(), key=lambda item:item[1],reverse=True))

# Print out the 5 most frequency word bigrams in descending order
count=1
for word, wordCount in sortedWordDict.items():
    if count >5:
        break # stop printing
    print(word, "->", wordCount, end=" ") # print word and its word count in one line
    count+=1

inputFile.close()


