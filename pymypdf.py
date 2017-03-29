#!/usr/bin/env python3

from urllib.request import Request, urlopen
import re

def downloadPDF():
    # Attempt to download all pdf files on the page
    # until an error is encountered
    try:
      url = "http://www.princexml.com/samples/"
      req = Request(
          url,
          data=None,
          headers={
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)'
              + 'AppleWebKit/602.3.12 (KHTML, like Gecko)'
              + 'Chrome/55.0.2883.95 Safari/537.36'
          }
      )
      home_page = urlopen(req)
      page = str(home_page.read().decode('utf-8'))

      links = re.findall('"(http://.*?.pdf)"', page)

      for link in links:
          name = link[link.rfind("/") + 1:]
          print("Downloading '" + name + "'...")
          g = urlopen(link)
          with open(name, 'b+w') as f:
              f.write(g.read())
          print("Download successful!")

    # Generate an error if a PDF cannot be read and terminate
    except IncompleteRead as error:
        print("Error found: " + error)

if __name__ == "__main__":
    downloadPDF()
