# Anne Tran (UCID: 30286177)
# Assign2_Q7

from bs4 import BeautifulSoup
import requests


headers={"User-Agent": "Mozilla/5.0"} # prevent website block the request from accessing the website

# Scrape webpage
web_html=requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers)
parsed_web_html=BeautifulSoup(web_html.text, "html5lib")

# Extract the page title
titlePage=parsed_web_html.find('title')
titlePage=titlePage.get_text()# find the title with 'title' tag

print(f"Page title is {titlePage}") # display page title

# Extract the first paragraph
content_div=parsed_web_html.find("div", id="mw-content-text") # find main content
                                                              # content_div indicates the main content
paragraph=content_div.find_all("p") # finds all paragraph

firstParagraph=""
for p in paragraph:
    text=p.text.strip() # get text from paragraph
                        # remove whitespace
    if len(text)>=50: # check if paragraph contain at least 50 characters
        firstParagraph=text
        break

print(firstParagraph) # display the valid first paragraph