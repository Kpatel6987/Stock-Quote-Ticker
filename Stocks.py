import urllib.request
import re
import time
import threading

stockInput = input("What Stocks?")
sym = stockInput.split(",")
newSym = []
for i in sym:
    x = i.lower().strip()
    newSym.append(x)

def partA():
    for i in newSym:
        url = "http://finance.yahoo.com/q?s=" +i + "&ql=1"
        a_file = urllib.request.urlopen(url)
        text = a_file.read()
        aString = '<span id="yfs_l84_'+ i +'">(.+?)</span>'
        bString = '<span id="yfs_p43_'+ i +'">(.+?)</span>'
        regex = aString.encode(encoding='UTF-8')
        regex2 = bString.encode(encoding='UTF-8')
        pattern = re.compile(regex)
        pattern2 = re.compile(regex2)
        price = re.findall(pattern,text)
        change = re.findall(pattern2,text)
        newPrice = []
        newChange = []
        for j in price:
            stringPrice = j.decode("utf-8")
            newPrice.append(stringPrice)
        for k in change:
            stringChange = k.decode("utf-8")
            newChange.append(stringChange)
        i = i.upper()
        print("The price of {0} is ${1} and the change is {2} ".format(i, newPrice[0], newChange[0]))      
    
def main():
    partA()
    print("\n")
    threading.Timer(5, main).start()
    

if __name__ == '__main__':
    main()
