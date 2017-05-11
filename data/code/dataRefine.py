# -*- coding: utf-8 -*-
import csv

chars = {
    '\xc2\x82' : ',',        # High code comma
    '\xc2\x84' : ',,',       # High code double comma
    '\xc2\x85' : '...',      # Tripple dot
    '\xc2\x88' : '^',        # High carat
    '\xc2\x91' : '\x27',     # Forward single quote
    '\xc2\x92' : '\x27',     # Reverse single quote
    '\xc2\x93' : '\x22',     # Forward double quote
    '\xc2\x94' : '\x22',     # Reverse double quote
    '\xc2\x95' : ' ',
    '\xc2\x96' : '-',        # High hyphen
    '\xc2\x97' : '--',       # Double hyphen
    '\xc2\x99' : ' ',
    '\xc2\xa0' : ' ',
    '\xc2\xa6' : '|',        # Split vertical bar
    '\xc2\xab' : '<<',       # Double less than
    '\xc2\xbb' : '>>',       # Double greater than
    '\xc2\xbc' : '1/4',      # one quarter
    '\xc2\xbd' : '1/2',      # one half
    '\xc2\xbe' : '3/4',      # three quarters
    '\xca\xbf' : '\x27',     # c-single quote
    '\xcc\xa8' : '',         # modifier - under curve
    '\xcc\xb1' : ''          # modifier - under line
}

def extractNum(s):
    num=""
    s=str(s)
    for i in range(len(s)):
        if(s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            num=num+s[i]
    if(num==""):
        num="NA"
    return num

def extractHours(time):
    opening=[]
    closing=[]
    word=""
    c=0
    for i in range(len(time)):
        if(time[i]!=" "):
            if(time[i] in chars):
                time[i]=chars[time[i]]
            word=word+time[i]
        else:
            if(extractNum(word)!="NA"):
                nextWord=time[i+1:i+3]
                word=extractNum(word)
                if(c%2==0):
                    opening.append(extractNum(word)+" "+nextWord)
                else:
                    closing.append(extractNum(word)+" "+nextWord)
                c+=1
            word=""
    return opening, closing

def extractList(s):
    s=s.replace(" ", "")
    s=s.replace("\n", "")
    s=s.replace(",", " ")
    lst=[]
    word=""
    for i in range(len(s)):
        if(s[i]!=" "):
            word=word+s[i]
        else:
            lst.append(word)
            word=""
    return lst

def extractData(s):
    s=s+"\n"
    s=s.replace("\n", ",")
    lst=[]
    word=""
    for i in range(len(s)):
        if(s[i]!=","):
            word=word+s[i]
        else:
            if(word!=''):
                lst.append(word.strip())
            word=""
    while("" in lst):
        lst.remove("")
    if('null' in lst or "Highlights" in lst):
        lst.remove(lst[0])
    return lst

files=["Banashankari.csv", "Brigade Road.csv", "Electronic City.csv", "Indiranagar.csv", "JP Nagar.csv", "Koramangala.csv", "Malleshwaram.csv", "Old Airport Road.csv", "Sarjapur Road.csv", "Whitefield.csv"]
for fileName in files:
    tomato=[]
    with open(fileName, 'rb') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            location=row[0][:fileName.index(".")]
            name=row[4]
            phone=row[8]
            cuisines=row[9]
            cost=extractNum(row[10])
            highlights=extractData(row[11])
            featuredIn=extractData(row[12])
            rate=extractNum(row[13])
            rating=""
            votes=""
            if(rate!="NA"):
                rating=rate[0]+"."+rate[1]
                votes=rate[2:]
            else:
                rating="NA"
                votes="Not enough"
            if(extractNum(row[14])!="NA"):
                openingHours, closingHours=extractHours(row[14])
            else:
                openingHours="NA"
                closingHours="NA"
            knownFor=extractList(row[15])
            favFood=extractList(row[16])
            favService=extractList(row[17])
            favLook=extractList(row[18])
            recommended=extractList(row[19])
            tomato.append([name, location, rating, votes, cost, openingHours, closingHours, cuisines, highlights, featuredIn, knownFor, favFood, favService, favLook, recommended])

    with open('Tomato Head.csv', 'a') as writeFile:
        writer=csv.writer(writeFile)
        writer.writerows(tomato)
