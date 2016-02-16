from bs4 import BeautifulSoup
import requests

url="http://www.web2py.com/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

links=soup.findAll('a')

for link in links:
    if link.contents[0]:
        print "Link Text: {} \n Link href: {}\n".format(link.contents[0],link['href'])