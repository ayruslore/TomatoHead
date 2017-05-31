import pandas as pd
import numpy as np
import operator
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)
df = pd.read_csv('TomatoHead.csv')

rest_vectors = pd.read_csv('one_hot_cuisine.csv')
column_names = rest_vectors.columns
column_names = column_names.tolist()
rest_vectors = rest_vectors.drop(column_names[0],axis =1)
#rest ---> (location, price, rating, cuisines, vector...etc)
d = {}
matrix = rest_vectors.as_matrix()
bars={}
nobooze={}

'''
print rest_vectors.head()
print "------------------"
print df.head()
'''
for i in range(len(df)):
	tupl = (df.ix[i,"Location"], df.ix[i,"Cost for 2"], df.ix[i,"Rating"], df.ix[i, "Cuisines"], matrix[i])
	d[df.ix[i,"Restaurant"]] = tupl
	if('Full Bar Available' in df.ix[i, "Highlights"] or 'Beer' in df.ix[i, "Highlights"]):
		bars[df.ix[i,"Restaurant"]] = tupl
	else:
		nobooze[df.ix[i,"Restaurant"]] = tupl

def filter_by_location(diction, location):
	d2={}
	for i in diction:
		loc,_,_,_,_ = diction[i]
		if(loc==location):
			d2[i]=diction[i]
	return (d2)

def find_similar_to(diction, rest_name):
	d2={}
	for i in diction:
		_,_,_,_,vctr=diction[i]
		_,_,_,_,vctr2=d[rest_name]
		cosine_sim=(np.dot(vctr, vctr2)*1.0)/pow(np.dot(vctr, vctr)*np.dot(vctr2, vctr2), 0.5)
		if(cosine_sim>=0.7):
			d2[i]=diction[i]
	return (d2)

def filter_min_rating(diction, min_value):
	d2={}
	for i in diction:
		_,_,rtng,_,_=diction[i]
		if(rtng>=min_value):
			d2[i]=diction[i]
	return (d2)

def filter_cost_range(diction, min_price, max_price):
	d2={}
	for i in diction:
		_,cost,_,_,_=diction[i]
		if(min_price<=cost<=max_price):
			d2[i]=diction[i]
	return (d2)
#dictionary to filter-diction
#price
#fraction : value betweeen 0-1
def filter_cost_approx(diction, price, fraction):
	lower=(1.0 - fraction) * price
	upper=(1.0 + fraction) * price
	return filter_cost_range(diction, lower, upper)

def filter_bars(diction, response):
	d2={}
	if(response=="YES" or response=="Yes" or response=="yes"):
		for i in diction:
			if(i in bars):
				d2[i]=diction[i]
	else:
		for i in diction:
			if(i in nobooze):
				d2[i]=diction[i]
	return (d2)

def filter_by(diction, filter, filter_var):
	if(filter=="Location"):
		diction=filter_by_location(diction, filter_var)
	elif(filter=="Cuisine"):
		diction=filter_by_cuisine(diction, filter_var)
	elif(filter=="Price"):
		diction=filter_cost_approx(diction, filter_var, 0.5)
	elif(filter=="Alcohol"):
		diction=filter_bars(diction, filter_var)
	elif(filter=="Rating"):
		diction=filter_min_rating(diction, filter_var)
	elif(filter=="Restaurant"):
		diction=find_similar_to(diction, filter_var)
	return diction

def filter_by_cuisine(diction, cuisine):
	d2={}
	for i in diction:
		_,_,_,csn,_=diction[i]
		csn=str(csn)
		if(cuisine in csn):
			d2[i]=diction[i]
	return (d2)

if(__name__=="__main__"):
	d3=d
	choice_list=[]
	while True:
		print "\nWelcome to Restaurant Filtering System!"
		if(1 not in choice_list):
			print "Press 1 to filter by Location"
		print "Press 2 to filter by Cuisine"
		if(3 not in choice_list):
			print "Press 3 to filter by Price"
		if(4 not in choice_list):
			print "Press 4 to filter by a Minimum Rating"
		if(5 not in choice_list):
			print "Press 5 to filter by Booze Availability"
		print "Press 6 to filter by Restaurants similar to your favourite Restaurant"
		print "Press 7 to exit"
		choice=int(input("Enter your choice: "))
		choice_list.append(choice)
		if(choice==1):
			loc=raw_input("Location: ")
			d3=filter_by(d3, "Location", loc)
		elif(choice==2):
			csn=raw_input("Cuisine: ")
			d3=filter_by(d3, "Cuisine", csn)
		elif(choice==3):
			price=int(input("Around Price Range: "))
			d3=filter_by(d3, "Price", price)
		elif(choice==4):
			min_rating=raw_input("Minimum Rating: ")
			d3=filter_by(d3, "Rating", float(min_rating))
		elif(choice==5):
			ch=raw_input("Type \"YES\" for Bars, \"NO\" for Non-Drinking Places Only.\n")
			d3=filter_by(d3, "Alcohol", ch)
		elif(choice==6):
			rest_similar=raw_input("Similar To: ")
			d3=filter_by(d3, "Restaurant", rest_similar)
		else:
			break
	#rest ---> (location, price, rating, cuisines, vector...etc)
	print "Recommended Restaurants:"
	d4={}
	for rest in d3:
		location,price,rating,_,_=d3[rest]
		d4[rest]={}
		d4[rest]["Location"]=location
		d4[rest]["Cost for 2"]=price
		d4[rest]["Rating"]=rating
	pp.pprint(d4)
	d4=json.dumps(d4)
	#print(d4)
