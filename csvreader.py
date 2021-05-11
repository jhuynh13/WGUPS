import csv
from package import package
from hashtable import hashtable
import datetime
from datetime import time
import calculator

#Variables
hashtable = hashtable()
addressList = []
distanceList = []

#Read in package data from csv    
with open('data/packages.csv') as packageFile:
    reader = csv.reader(packageFile, delimiter=',')
    
    for row in reader:
        timestamp = time(hour=0, minute=0, second=0, microsecond=0)
        temp = package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], timestamp)
        hashtable.insert(int(temp.id) -1, temp)

#Read in distance data from csv
with open('data/distances_table.csv') as distanceFile:
    reader = csv.reader (distanceFile, delimiter=',')
    for row in reader:
        distanceList.append(row)

#Read in address data from csv
with open('data/addresses.csv') as addressFile:
    reader = csv.reader (addressFile, delimiter=',')
    for row in reader:
        list1 = [row[0]]
        list1.append(row[2])
        addressList.append(list1)

#Return address list
def getAddresses():
    return addressList

#Return distances list
def getDistances():
    return distanceList

#Return package list
def getPackages():
   return hashtable

# Complexity is O(n)
# This function calculates the distance between two locations and returns it
def calcDistance (curr, loc):

    for z in addressList:
        if z[1] == curr:
            currIndex = int(z[0])
        if z[1] == loc:
            locIndex = int(z[0])
    
    if currIndex > locIndex:
        return float(distanceList[currIndex][locIndex])
    else:
        return float(distanceList[locIndex][currIndex])

# Complexity is O(n)
# This function calculates the time and distance between two locations
def getDistance (curr, loc, time):

    distance = 0.0

    for z in addressList:
        if z[1] == curr:
            currIndex = int(z[0])
        if z[1] == loc:
            locIndex = int(z[0])

    if currIndex > locIndex:
        distance = float(distanceList[currIndex][locIndex])
    else:
        distance = float(distanceList[locIndex][currIndex])
    
    new_time = calculator.getTime(distance)
    round(new_time, 3)
    new_time = datetime.timedelta(hours=new_time)

    time = time + new_time
    
    return [distance, time]

# Complexity is O(n^2)
# This function uses the nearest neighbor algorithm to find the closest
# location compared to current location
def getRoute (curr, truck, currTime):

    #set first item in truck as default location
    tempId = truck[0].id
    shortDistance = calcDistance(curr,truck[0].address)
    tempAddress = truck[0].address
    tempPackage = truck[0]

    #loop through truck looking for shortest distance
    if len(truck) != 1:
        for x in truck:
            distance = calcDistance(curr,x.address)
            if distance < shortDistance:
                shortDistance = distance
                tempId = x.id
                tempAddress = x.address
                tempPackage = x

    # Calculate time of route
    time = calculator.getTime(shortDistance)
    round(time, 3)
    time = datetime.timedelta(hours=time)

    # Update delivery timestamp of that package delivered
    currTime = currTime + time
    tempPackage.timestamp = currTime
    hashtable.update(tempId, tempPackage)

    #Return data of that route and package  
    return [shortDistance, tempId, tempAddress, time]