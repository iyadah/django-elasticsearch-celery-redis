import requests
import html2text
import re
import lxml
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup
import urllib, os
from lxml import etree

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# def get_urls(link):
#     xmlDict = {}

#     r = requests.get("https://tarjama.com/sitemap.xml")
#     xml = r.text

#     soup = BeautifulSoup(xml)
#     sitemapTags = soup.find_all("sitemap")

#     print "The number of sitemaps are {0}".format(len(sitemapTags))

#     for sitemap in sitemapTags:
#         xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

#     print xmlDict
      


def cleanMe(html):
    soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text
urls = open("urls","r")
count_all = 0 
for slink in urls:
#  print(slink)
  f = requests.get(slink.strip())
  txt = cleanhtml(f.text)
  txt2 = cleanMe(f.text)
#print(txt2)

  wcount = len(txt2.split())
  count_all += wcount
  print('\n word count for the link '+slink+ " is: "+str(wcount)+ ' words')


# link = "https://www.tmnf.ae/terms-conditions"
# f = requests.get(link)
# txt = cleanhtml(f.text)
# txt2 = cleanMe(f.text)
# #print(txt2)
print("\n Overall word count is:" + str(count_all))
# wcount = len(txt2.split())
# print('\n word count: '+str(wcount)+ ' words')

#get_urls('https://tarjama.com/sitemap.xml')



