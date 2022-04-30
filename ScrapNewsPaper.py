import requests
from bs4 import BeautifulSoup as bs

class NewsPaperData():

    def __init__(self):
        self.newsPaperLinks = {
            # Hindi
            'NBT': "https://mystudytown.in/navbharat-times-epaper/",
            'hindustan': "https://mystudytown.in/hindustan-dainik-epaper-pdf/",
            'DJ': "https://mystudytown.in/dainik-jagran-epaper/",
            'Amar': "https://mystudytown.in/amar-ujala/",

            # English
            'HT': "https://mystudytown.in/hindustan-times-epaper/",
            'Times': "https://mystudytown.in/times-of-india-epaper-pdf/",
            'ET': "https://mystudytown.in/the-economic-times-epaper/",
            'Telegraph': "https://mystudytown.in/the-telegraph-epaper-pdf-free-download/"
        }

    def getNewsPaper(self, newspaperName):  
        # Make a request
        self.r = requests.get(self.newsPaperLinks[newspaperName])
        self.html = self.r.text

        # Parse the html content
        soup = bs(self.html, "lxml")

        # Find out table
        table = soup.find('table', attrs={"data-ninja_table_instance": "ninja_table_instance_0"})

        dic = {}

        # Loop and find out date and Link from Table
        for row in range(0, 8):
            tableTr = table.tbody.find("tr", attrs={"data-row_id": f'{row}'})
            Alltd = tableTr.find_all("td")
            for link in Alltd[1].find_all('a'):
                dic[Alltd[0].text] = link.get('href')

        print(dic)
        # Return News Paper Date and Link in Dictionary Format
        return dic

    def writeToHTML(self, html):
        # Open inde.html and write data in it.
        with open('index.html', 'w', encoding="utf-8") as f:
            f.write(html)

    def getPDF(self, url):
        r = requests.get(url)
        soup = bs(r.text, "lxml")
        title = soup.find('title').text
        if(title == "त्रुटि | वीके" or title == "Error | VK"):
            return "Error"
        
        iframeSource = soup.find("iframe", attrs={"id": "iframe"})['src']
        print(iframeSource)
        return iframeSource
