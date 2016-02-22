from urllib.request import urlopen
import re
import time
import threading

stockInput = input("What Stocks?")
sym = stockInput.split(",")
newSym = []
for i in sym:
    x = i.lower()
    newSym.append(x)
print (newSym)
def partA():
    for i in newSym:
        url = "http://finance.yahoo.com/q?s=" + i + "&ql=1"
        a_file = urlopen(url)
        print(url)
        text = a_file.read()
        regex = '<span id="yfs_l84_'+ i +'">(.+?)</span>'
        regex2 = '<span id="yfs_p43_'+ i +'">(.+?)</span>'
        pattern = re.compile(regex)
        pattern2 = re.compile(regex2)
        price = re.findall(pattern,text)
        change = re.findall(pattern2,text)
        print ("The price of", i , " is ", price[0], change[0])        
       
    
def run():
    partA()
    print ("\n")
    threading.Timer(5, run).start()

partA()

    

