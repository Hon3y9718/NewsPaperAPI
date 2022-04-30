import requests
from bs4 import BeautifulSoup as bs

class NewsPaperData():
    def getNewsPaper(self):  
        # Make a request
        self.r = requests.get("https://mystudytown.in/navbharat-times-epaper/")
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

        # Return News Paper Date and Link in Dictionary Format
        return dic

    def writeToHTML(self, html):
        # Open inde.html and write data in it.
        with open('index.html', 'w', encoding="utf-8") as f:
            f.write(html)

    def getPDF(self, url):
        r = requests.get(url)
        soup = bs(r.text, "lxml")
        iframeSource = soup.find("iframe", attrs={"id": "iframe"})['src']
        print(iframeSource)
        return iframeSource

obj = NewsPaperData()
obj.getPDF("https://vk.com/doc722551386_632706138?hash=HCd9nq5EiMDYoXkdoyHTJ9Zxji5prQ9hN9HumXFPdLw&dl=nEkMaa09bRlzTgugEcWmczVIoj161Cc4WzzkVto4IVs")