from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
base_url = "https://www.math.kit.edu/"
ssl._create_default_https_context = ssl._create_unverified_context

class HtmlImport():
    def __init__(self, path):
        self.text = self.getText()
        self.path = path
        self.soup = self.getSoup()
        

    def getSoup(self):
        with open(self.path) as html_file:
            soup = BeautifulSoup(html_file, features="html.parser")
            return soup

    # kill all script and style element
    def getText(self):
        soup = self.soup
        for script in self.soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

h = HtmlImport("pages/1.html")
text = h.getText

print(text)

