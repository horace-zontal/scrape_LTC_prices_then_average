from lxml import html
import requests, sys, datetime, re, time


while True:

    reload(sys)
    sys.setdefaultencoding('utf-8')


    page = requests.get('http://www.litecoinrate.co.uk')
    tree = html.fromstring(page.content)
    price = tree.xpath('//*[@id="tablepress-1"]/tbody/tr[1]/td/strong/text()')


    string = price[0]
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)


    fh = open("ltcscraped.txt", "a")
    scraped_and_stripped_text = new_str
    fh.write(scraped_and_stripped_text + ' ')
    fh.close()


    time.sleep(3600)


