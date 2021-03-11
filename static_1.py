
data_file = open("data.json","r")
data_raw = data_file.read()

tempMin = 1000.0
tempMax = 0.0
humMin = 1000.0
humMax = 0.0
windMin = 1000.0
windMax = 0.0

global data
global clusters



data = []

for i in data_raw.split("findname"):
    if i[0] != "{":
        name = i.split('"')
        #print "Name:  " + name[2]
        temperature = i.split("temp")[1].split(',')[0][2:]
        #print "Temperature:  " + temperature
        humidity = i.split("humidity")[1].split(',')[0][2:].split('}')[0]
        #print "Humidity:  " + humidity
        windSpeed = i.split("speed")[1].split(',')[0][2:].split('}')[0]
        #print "Wind Speed:  " + windSpeed
        data.append([name[2],float(temperature),float(humidity),float(windSpeed)])

        if humMin > float(humidity):
            humMin = float(humidity)
        if humMax < float(humidity):
            humMax = float(humidity)
        if tempMin > float(temperature):
            tempMin = float(temperature)
        if tempMax < float(temperature):
            tempMax = float(temperature)
        if windMin > float(windSpeed):
            windMin = float(windSpeed)
        if windMax < float(windSpeed):
            windMax = float(windSpeed)
        
        
tempCut1 = tempMin + (tempMax - tempMin) / 3
tempCut2 = tempMin + 2 * (tempMax - tempMin) / 3
humCut = (humMin + humMax) / 2
windCut = (windMin + windMax) / 2

print "HumMax: "+str(humMax)
print "HumMin: "+str(humMin)
print "TempMax: "+str(tempMax)
print "TempMin: "+str(tempMin)
print "WindMax: "+str(windMax)
print "WindMin: "+str(windMin)

#Temperature Humidity Wind

lll = []
llh = []
lhl = []
lhh = []
mll = []
mlh = []
mhl = []
mhh = []
hll = []
hlh = []
hhl = []
hhh = []

clusters = [lll,llh,lhl,lhh, mll ,mlh ,mhl ,mhh ,hll ,hlh ,hhl ,hhh]
global avg
avg = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],
       [0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],]
        # lll llh lhl lhh mll mlh mhl mhh hll hlh hhl hhh

for i in data:
    temp = ""
    hum = ""
    wind = ""
    index = 0
    if i[1] < tempCut1:
        index = index + 0
    elif i[1] < tempCut2:
        index = index + 4
    else:
        index = index + 8

    if i[2] < humCut:
        index = index + 0
    else:
        index = index + 2

    if i[3] < windCut:
        index = index + 0
    else:
        index = index + 1
    
    avg[index][0] = round(avg[index][0] + i[1],5)
    avg[index][1] = round(avg[index][1] + i[2],3)
    avg[index][2] = round(avg[index][2] + i[3],3)

    clusters[index].append(i)
        
for index in range(0,len(clusters)):
    if len(clusters[index]) != 0:
        avg[index][0] = round(avg[index][0] / len(clusters[index]),5)
        avg[index][1] = round(avg[index][1] / len(clusters[index]),3)
        avg[index][2] = round(avg[index][2] / len(clusters[index]),3)


def function_means(centeroid = []):
    lll = []
    llh = []
    lhl = []
    lhh = []
    mll = []
    mlh = []
    mhl = []
    mhh = []
    hll = []
    hlh = []
    hhl = []
    hhh = []
    d = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    avg = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],
       [0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],]

    temp = [lll,llh,lhl,lhh, mll ,mlh ,mhl ,mhh ,hll ,hlh ,hhl ,hhh]
    minD = 999999.0
    for i in data:
        for j in range(0,len(centeroid)):
            d[j] = (i[1] - centeroid[j][0])**2 + (i[2] - centeroid[j][1])**2 + (i[3] - centeroid[j][2])**2
        minD = min(d)
        for k in range(0,12):
            if d[k] == minD:
                minD = d[k]
                avg[k][0] = round(avg[k][0] + i[1],5)
                avg[k][1] = round(avg[k][1] + i[2],3)
                avg[k][2] = round(avg[k][2] + i[3],3)

                temp[k].append(i)
    for index in range(0,len(temp)):
        if len(temp[index]) != 0:
            avg[index][0] = round(avg[index][0] / len(temp[index]),5)
            avg[index][1] = round(avg[index][1] / len(temp[index]),3)
            avg[index][2] = round(avg[index][2] / len(temp[index]),3)
    return temp






def cluSize():
    for i in range(0,len(clusters)):
        print str(i)+"  "+str(len(clusters[i]))























