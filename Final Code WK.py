from bs4 import BeautifulSoup
import requests
import re
import urllib2
import urllib
import json
import numpy as np
#from sklearn.cluster import MeanShift, estimate_bandwidth
from pprint import pprint

url = "https://www.townscountiespostcodes.co.uk/towns-in-uk/"
temperature1 = "http://api.openweathermap.org/data/2.5/weather?q="
temperature2 = "&APPID=7e4d32d870359dd58ad029c13d3e1adf"

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

countyNames = soup.find_all("td",{"class":"hide county"})
j = 0

for i in countyNames:
    #print j
    j = j+1
    #print i.text.lower().replace(" ","-")


########
#################     HREF FOR TOWN
temp1 = soup.find_all("a")
hrefTown = []
comp = "Towns in "
for i in temp1:
    if i.get("title") == None:
        #print "misss"
        x=1
    elif i.get("title")[0:8] != comp[0:8]:
        #print "miss"
        x=1
    elif i.get("href") != None:
        #print i.get("href")
        hrefTown.append("https://www.townscountiespostcodes.co.uk"+i.get("href"))

del hrefTown[0:7]

#######
############### ACCESSING TOWN NAMES
nn = 0
townNames = []

x = []
for i in hrefTown:
    r = requests.get(i)
    soup = BeautifulSoup(r.content,"html.parser")
    k = 1
    temp1 = soup.find_all("td")
    comp = " Information"
    for j in range (0, len(temp1)):
        if temp1[j].text == str(k):
            nn = nn +1
            k = k+1
            temp2 = temp1[j+1].text.strip()
            try:
                weather = requests.get(temperature1+temp2.replace(" ","%20")+temperature2)
                temperature = weather.json()["main"]["temp"]
                humidity = weather.json()["main"]["humidity"]
                x.append(float(temperature))
                townNames.append([temp2,temperature,humidity])
                #print "City:   "+temp2+".   Temperature:   "+temperature
                #print temp1[j+1].text.strip()
                print "Temperature of "+temp2+" is: "+str(temperature)+" and humidity is: "+str(humidity)
                #print temperature
                if nn % 10 == 0:
                    print nn

                    
                    
            except:
                ignore = "once"

print "done"
