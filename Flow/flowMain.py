import json
from glob import glob 
import os
import sys
import csv
import random
from datetime import datetime
import operator
import matplotlib.pyplot as plt

import numpy as np


k = 2


class business:
	def __init__(self,id, n, nbhd,addy, c, st, pCode, lat, log, star, rCount):
		self.id = id
		self.name = n
		self.neighborhood = nbhd	
		self.address = addy
		self.city = c
		self.state = st
		self.postalCode = pCode
		self.latitude = lat
		self.longitude = log
		self.stars = star
		self.reviewCount = rCount
		self.users = {}

class review:
	def __init__(self, id, uid, bid, stars, date):
		self.id = id
		self.uid = uid
		self.bid = bid
		self.stars = stars
		self.date = datetime.strptime(date.strip(), "%Y-%m-%d").date()
		
class user:
	def __init__(self, id):
		self.id = id
		self.businesses = []
		self.currBus = []

def printBus(bus):
	print("Id " +bus.id)
	print("name " + bus.name)
	print("neighborhood " + bus.neighborhood)
	print("address " + bus.address)
	print("city " + bus.city)
	print("state " + bus.state)
	print("postal code " + bus.postalCode)
	print("lat " + bus.latitude)
	print("long " + bus.longitude)
	print("stars " + bus.stars)
	print("review count " + bus.reviewCount)
	print("number of reviews "+ str(len(bus.users))) 
	print(users)
	print("\n")


def printRev(r):
	print("Id " +r.id)
	print("uid " + r.uid)
	print("bid " + r.bid)
	print("stars " + r.stars)
	print("date " + str(r.date))
	print("\n")

print("reading businesses")
fullListB = []
with open('ohioBusinesses.csv', 'r') as f:
	reader = csv.reader(f)
	fullListB = list(reader)	

print("reading reviews")
fullListR = []
with open('ohioReviews.csv', 'r') as f:
	reader = csv.reader(f)
	fullListR = list(reader)	


businesses = []
for i in fullListB:
	businesses.append(business(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))

del fullListB

print("finished businesses " + str(len(businesses)))


reviews = []
for i in fullListR:
	reviews.append(review(i[0],i[1],i[2],i[3],i[4]))
	
print("number of reviews "+ str(len(reviews)))

del fullListR





print("converting to dictionary")
ohioBus = {}
userDict = {}
reviewDict = {}

for i in businesses:
	ohioBus[i.id] = i

del businesses



for i in reviews:
	uid = i.uid
	if uid in userDict:
		pass
	else:
		userDict[uid] = user(i.uid)




print("sorting reviews by date")
reviews.sort(key = lambda r: r.date)

print(reviews[0].date)
print(reviews[-1].date)



#print(len(reviews))
#print(len(userDict))
#print(len(ohioBus))


def handleReviews(r):
	for i in r:
		user = i.uid
		bid= (i.bid).strip()
		bus = ohioBus[bid]
		if user in bus.users:
			print("repeat")
		else:
			bus.users[user] = k
		#print(bus.users)

		
		
timesInTop={}

#f = open("ohioBusMostPop.csv", 'w')
lengthList = []
def handleBusinesses():
	for k,v in ohioBus.items():
		temp={}	
		for k2,v2 in v.users.items():
			v2-=1			
			if v2 > 0:
				temp[k2] = v2		
		v.users = temp
		#print(len(temp))
	ohioBusTemp = {}
	for k,v in ohioBus.items():
		ohioBusTemp[k] = len(v.users)
		#print(len(v.users))
	sorted_x = sorted(ohioBusTemp.items(), key = operator.itemgetter(1), reverse = True)
	c = 0
	for i in sorted_x:
		if i[1] > 0:
			c+=1			
			if c < 50:
				#f.write(str(i))
				#f.write("\n")
					if i[0] in timesInTop:
						timesInTop[i[0]] += 1
					else:
						timesInTop[i[0]] = 1
	#f.write("\n")

print("flow commencing")


periodReviews = []

d1 = reviews[0].date

count = 0

for i in reviews:
	d2 = i.date
	bid= (i.bid).strip()
	bus = ohioBus[bid]
	#user = userDict[(i.uid).strip()]
	if abs(d2-d1).days > 6:
        
		print(str(d2) + " " + str(d1))
		#f.write(str(d2) + " " + str(d1))
		#f.write("\n")
		lengthList.append(len(periodReviews))
		handleReviews(periodReviews)
		handleBusinesses()
		d1 = i.date
		periodReviews = []
		count +=1
	else:
		periodReviews.append(i)	


print(count)



sorted_y = sorted(timesInTop.items(), key = operator.itemgetter(1), reverse = True)

c= 0
for i in sorted_y:
	if c < 50:
		c+=1		
		#print(i)

#print(lengthList)


print(lengthList)
print(str(np.var(lengthList)))
print(str(np.average(lengthList)))


plt.plot(lengthList, 'ro')
plt.ylabel("Number of active businesses")
plt.xlabel("time")
plt.show()





