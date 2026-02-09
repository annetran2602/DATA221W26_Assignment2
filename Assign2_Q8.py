# Anne Tran (UCID: 30286177)
# Assign2_Q8

from bs4 import BeautifulSoup
import requests

# Scrape the website
headers={"User-Agent": "Mozilla/5.0"} # prevent website block the requests from accessing the webpage
webpage=requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)

parsed_website=BeautifulSoup(webpage.text, "html5lib") # convert format to extract

# Extract all <h2> section heading
content_div=parsed_website.find("div", id="mw-content-text") # select the main contain in the webpage

h2Content=content_div.find_all("h2") # extract all h2 tag
removeHeading=["References", "External links", "See also", "Notes"] # list of invalid heading

# Validating <h2> heading
finalHeading=[]
for heading in h2Content:
    heading=heading.get_text().replace("[Edit]", "").strip() # remove html tag & remove [Edit] & remove whitespace
    if heading in removeHeading: # check if heading is valid
        continue # remove the invalid heading
    else:
        finalHeading.append(heading) # adding valid heading

with open("headings.txt", mode="w") as file:
    for validHeading in finalHeading:
        file.write(validHeading+"\n")


