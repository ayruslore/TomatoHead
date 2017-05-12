import pandas as pd
import numpy as np

#select the right csv file 
df = pd.read_csv("./Data/data/locationwise/Indiranagar.csv")
########feature seperator to build extra columns like one hot encoding for column cuisines
cuisines = df['cuisines']

cuisine_list = []

#adding all possible cuisine tags
for item in cuisines:
	if(isinstance(item,str)):
		cuisine_list_rest = item.split(',')
		for cuisine in cuisine_list_rest:
			cuisine_list.append(cuisine)

df1 = pd.DataFrame({'cuisine':cuisine_list})
#removing duplicate cuisines
df2 = df1.cuisine.unique()


#print df2 

#removing unnescessary space in the beginning
for item in range(len(df2)-1):
	if df2[item][0] == ' ':
		df2[item] = df2[item][1:]
	print(df2[item])

#adding additional columns
d = {}
one_hot_cuisine = pd.DataFrame(data=d)

for item in df2:
	one_hot_cuisine[item] = np.zeros_like(df['cuisines'])

#print df.head()['cuisines'], df.head()['North Indian']

for row in range(len(cuisines)):
	if(isinstance(cuisines[row], str)):
		cuisine_list_rest = cuisines[row].split(',')

	for item in cuisine_list_rest:
		if (item[0] == ' '):
			item = item[1:]
		one_hot_cuisine.ix[row, item] = 1


one_hot_cuisine.to_csv('example.csv')

'''
highlights = df['highlights']
highlight_list = []

for item in highlights:
		for highlight in items:
			highlight_list.append(highlight)


hf1 = pd.DataFrame({'highlights':highlight_list})	

hf2 = hf1.cuisine.unique()
'''