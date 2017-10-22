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
		userDict[uid] = user(i.uid)



reviews.sort(key = lambda r: r.date)


'''
Businesses: OhioBus dictionary
Users: userDict dictionary
Reviews: reviews sorted list by date

'''

print(len(ohioBus))
print(len(userDict))
print(len(reviews))



