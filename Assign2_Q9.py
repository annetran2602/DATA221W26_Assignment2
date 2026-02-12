# Anne Tran (UCID: 30286177)
# Assign2_Q9

from bs4 import BeautifulSoup
import requests
import csv

# Scrape the website
headers={"User-Agent":"Mozilla/5.0"} # prevent the website block the requests from accessing the webpage
website=requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=headers)

parsed_website=BeautifulSoup(website.text, "html5lib") # convert to python format for extraction

# Select the main content
content_div=parsed_website.find("div", id="mw-content-text") # locate the main content

tables=content_div.find_all("table") # find table with table tag

# Find the first table which has at least 3 data rows
dataRows=[]

for table in tables:
    rows=table.find_all("tr") # table rows (tr stands for table rows)
    for row in rows:
        if row.find_all("td"):
            dataRows.append(row) # collect only rows has data (not header)
    if len(dataRows)>=3: # check if table contain at least 3 data rows
        firstTable=table
        break

# Extract the first table's header
tableHeaders=firstTable.find_all("th")

headers=[]
if tableHeaders: # if there is existing headers
    for header in tableHeaders:
        headers.append(header.get_text().strip())

else: # create headers name if there is no existing headers
    firstTableRow=firstTable.find("tr") # extract the first row to determine the num of column
    numOfColumn=len(firstTableRow.find_all(["td", "th"])) # find all cells
    for num in range(1, numOfColumn+1):
        headers.append(f"col{num}")

# Create formatted table
dataTable=[]
rowData=[]
tableRows=firstTable.find_all("tr")
for eachRow in tableRows: #
    dataCells=eachRow.find_all("td")
    if not dataCells:
        continue

    for dataCell in dataCells:
        rowData.append(dataCell.get_text().strip())

    while len(headers)>len(rowData):
        rowData.append("")

    dataTable.append(rowData)
# Save to csv file
with open ("wiki_table.csv", mode="w") as file:
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(dataTable)









