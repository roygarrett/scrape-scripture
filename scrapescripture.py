import re
import requests
from bs4 import BeautifulSoup

#enter book and chapters and file to write to
book = str(input("Enter Book (No spaces capitalized): "))
chaps_range = int(input("Enter Number of Chapters: ")) + 1
write_file = str(input("Enter file to write to: "))

#open write file
with open(write_file, "a", encoding="utf-8") as file:
  
  #iterate through chapter pages
  for ch in range(1,chaps_range):
    print("Chapter " + str(ch))
    URL = "https://read.lsbible.org/?q=" + book + "+" + str(ch)
    page = requests.get(URL)

    #parse source code
    soup = BeautifulSoup(page.content, "html.parser")
    
    #find all the elements with the text
    result = list(soup.findAll(attrs={'class' : re.compile(".*poetry.*|.*prose.*|.*block-quote.*|.*quote.*|.*verse.*")}))
    scripture = list(soup.findAll(attrs={'class' : re.compile(".*poetry.*|.*prose.*|.*block-quote.*|.*quote.*")}))
    verse_nums = list(soup.findAll("span", class_="verse"))

    #turning results into text
    results = []
    for s in result:
      if s in verse_nums:
        results.append("\n")
      elif s in scripture:
        results.append(s.text)
        results.append(" ")
    
    #write text from elements to file
    for i in results:
      file.write(i)