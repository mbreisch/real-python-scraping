import time
import requests

i=0

stock_list=['GOOG','YHOO','MSF']

while i<2:
    base_url="http://download.finance.yahoo.com/d/quotes.csv"
    for stock in stock_list:
        data=requests.get(base_url,params={'s':stock,'f':'sl1d1t1c1ohgv','e':'.csv'})
        print data.content
    i +=1
    time.sleep(3)

