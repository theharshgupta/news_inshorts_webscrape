import textwrap
import time
import io
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import re

from selenium.common.exceptions import UnexpectedAlertPresentException

op = webdriver.ChromeOptions()
# op.add_argument('--incognito')
# op.add_argument('headless')
driver = webdriver.Chrome(chrome_options=op)
url = "https://www.inshorts.com/en/read"
driver.get(url=url)

def loadMore():
    xp = '//*[@id="load-more-btn"]'
    for x in range(1, 10000):
        try:
            driver.execute_script('loadMoreNews()')
            time.sleep(1)
            print(str(x))
        except UnexpectedAlertPresentException:
            aob = driver.switch_to.alert
            aob.accept()

def bsparse():
    # with io.open("pgs.txt", "w", encoding="utf-8") as f:
    #     f.write(driver.page_source)
    soup = BeautifulSoup(driver.page_source, "lxml")
    articleBody = soup.findAll("div", {"itemprop": "articleBody"})
    authors = soup.findAll("span", {"class": "author"})
    times = soup.findAll("span", {"class": "time"})
    dates = soup.findAll("span", {"class": "date"})
    heads = soup.findAll("a", {"class": "clickable"})
    sources = soup.findAll("a", {"class": "source"})
    for div in heads:
        print(textwrap.fill(div.text, width=75))
    for a in articleBody:
        print(textwrap.fill(a.text, width=75))
    for author in authors:
        print(author.text)
    for source in sources:
        print(source.text)
def selparse():
    cards = driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]')

    # print()
    # for x in range(1, 100):
    #     card_xpath = "/html/body/div[4]/div/div[%d]" % x
    #     heading_xpath = "/html/body/div[4]/div/div[2]/div[%d]/div/div[2]/a/span" % x
    #     heading = driver.find_element_by_xpath(heading_xpath)
    #     print(heading.text)

    for card in driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]"):
        print(re.search('by (.+?) /', card.text)
)
def mainSel():
    #  headings, text, author, time, date, source
    jdata = {}
    data = [[],[],[],[],[],[]]
    hd = []
    text = []
    au = []
    emit= []
    dt = []
    src = []


    authors = driver.find_elements_by_class_name('author')
    for author in authors:
        # data[2].append(author.text)
        au.append(author.text)

    headings = driver.find_elements_by_class_name('clickable')
    for head in headings:
        hd.append(head.text)
        # data[0].append(head.text)
        # print(head.text)

    articleTexts = driver.find_elements_by_xpath('//div[@itemprop="articleBody"]')
    for bodyText in articleTexts:
        # data[1].append(bodyText.text)
        text.append(bodyText.text)
        # print(bodyText.text)

    sources = driver.find_elements_by_class_name('source')
    for source in sources:
        src.append(source.text)
        # data[5].append(source.text)
        # print(source.text)

    times = driver.find_elements_by_class_name('time')
    dates = driver.find_elements_by_xpath('//span[@clas="date"]')

    for date in dates:
        dt.append(date.text)
        # data[4].append(date.text)
        # print(date.text)
    for ti in times:
        emit.append(ti.text)
        # data[3].append(ti.text)
        # print(ti.text)

    #  headings, text, author, time, date, source

    hd.remove("toggle menu\nMenu")
    timeList = list(filter(None, emit))
    dateList = list(filter(None, dt))
    headList = list(filter(None, hd))
    textList = list(filter(None, text))
    srcList = list(filter(None, src))
    authorList = list(filter(None, au))

    lenOfData = len(timeList) -1
    print(lenOfData)

    jdata['inshorts'] = []
    for iterate in range(0, lenOfData):

        # jdata['inshorts'].append({
        #     'heading': headList[iterate],
        #     'body': textList[iterate],
        #     'author': authorList[iterate],
        #     'source': srcList[iterate],
        #     'time': timeList[iterate],
        #     'date': dateList[iterate]
        #     'date': dateList[iterate]
        # })

        rowData = [headList[iterate], textList[iterate], authorList[iterate], srcList[iterate], timeList[iterate], dateList[iterate]]
        with open('c.csv', 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(rowData)

            # with open("data.json", 'w') as f:

                #json.dump(jdata, f)


def ojson():

    with open("data.json") as f:
        data = json.load(f)
        for p in data['inshorts']:
            print(p['author'])
def readCSv():
    with open("c.csv") as f:
        pd = csv.DictReader(f)
        for line in pd:
            print(line)
# readCSv()
loadMore()
mainSel()

