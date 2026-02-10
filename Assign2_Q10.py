# Anne Tran (UCID: 30286177)
# Assign2_Q10

def find_lines_containing(filename, keyword):
    file=open(filename, mode="r")
    readFile=file.read() # read the file

    splitFile=readFile.split("\n") # split into lines (not words)
    matchLine={}

    for lineNum, line in enumerate(splitFile, start=1): #
        if keyword.lower() in line.lower(): # check if keyword in lines (formatted in lowercase)
            matchLine[lineNum]=line.strip() # collect all lines contain a keyword

    return matchLine

matchLine=find_lines_containing("sample-file.txt", "lorem") # input the filename and keyword
numOfMatchLine=len(matchLine) # count the number of matching line


print("There are", numOfMatchLine, "matching lines")

count=1
if numOfMatchLine>=3: # check if there are more than 3 matching lines
    for lineNum, line in matchLine.items():
        if count>3:
            break
        print(f"Line {lineNum}: {line}") # print the first 3 matching lines
        count+=1
else: # check if there are less than 3 matching lines
    for lineNum, line in matchLine.items():
        print(f"Line {lineNum}: {line}") # print line number & all matching lines

