from celery import Celery
import os
from bs4 import BeautifulSoup
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

@app.task
def cleanMe(link):
    html = requests.get(link)
    print(link)
    return
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
    print(text)
    return text

