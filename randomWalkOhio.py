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
		self.businesses = {}
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
	#print(users)
	print("\n")


def printRev(r):
	print("Id " +r.id)
	print("uid " + r.uid)
	print("bid " + r.bid)
	print("stars " + r.stars)
	print("date " + str(r.date))
	print("\n")


fullListB = []
with open('ohioBusinesses.csv', 'r') as f:
	reader = csv.reader(f)
	fullListB = list(reader)	


fullListR = []
with open('ohioReviews.csv', 'r') as f:
	reader = csv.reader(f)
	fullListR = list(reader)	


businesses = []
for i in fullListB:
	businesses.append(business(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
	

del fullListB



reviews = []
for i in fullListR:
	reviews.append(review(i[0],i[1],i[2],i[3],i[4]))
	
del fullListR





ohioBus = {}
userDict = {}

for i in businesses:
	ohioBus[i.id] = i
	

del businesses



for i in reviews:
	uid = i.uid
	if uid in userDict:
		pass
	else:
		userDict[(i.uid).strip()] = user((i.uid).strip())



reviews.sort(key = lambda r: r.date)


'''
Businesses: ohioBus dictionary
Users: userDict dictionary
Reviews: reviews sorted list by date

'''

print(len(ohioBus))
print(len(userDict))
print(len(reviews))


print("setting up graph")


for i in reviews:
	uid = (i.uid).strip()
	bid = (i.bid).strip()
	user = userDict[uid]
	bus = ohioBus[bid]
	if uid in bus.users:
		pass
	else:
		bus.users[uid] = user
	
	if bid in user.businesses:
		pass
	else:
		(user.businesses)[bid] = bus


print("starting random walk")

probMatrix = {}

for i in range(100000):
	b1 = random.choice(list(ohioBus.items()))
	bus1 = b1[1]
	bid1= b1[0]
	if len(bus1.users) >0:		
		u = random.choice(list(bus1.users.items()))
		user1 = u[1]
		if len(user1.businesses) >0:
			b2 = random.choice(list(user1.businesses.items()))
			bid2 =b2[0]
			bus2 = b2[1]
			#print(bus2)
			
			if bid1 in probMatrix:
				if bid2 in probMatrix[bid1]:
					probMatrix[bid1][bid2] +=1
				else:
					probMatrix[bid1][bid2] = 1
			else:
				probMatrix[bid1] = {}
				probMatrix[bid1][bid2] = 1
			#print(b1)
			#print(b2)
			#print(probMatrix[b1][b2])
			#print("\n")


for k,v in probMatrix.items():
	print(k)	
	for k2,v2 in v.items():
		print(str(k2) + " " + str(v2) )
	print("\n")
