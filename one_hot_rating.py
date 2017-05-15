import pandas as pd
import numpy as np

#select the right csv file 
df = pd.read_csv("./Data/data/locationwise/Indiranagar.csv")
print(df.ix[3,'rating'],"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
########feature seperator to build extra columns like one hot encoding for column cuisines
rating = df['rating']


#adding additional columns
d = {}
one_hot_rating = pd.DataFrame(data=d)

one_hot_rating['1 star'] = np.zeros_like(df['rating'])
one_hot_rating['2 star'] = np.zeros_like(df['rating'])
one_hot_rating['3 star'] = np.zeros_like(df['rating'])
one_hot_rating['4 star'] = np.zeros_like(df['rating'])
one_hot_rating['5 star'] = np.zeros_like(df['rating'])
one_hot_rating['not rated'] = np.zeros_like(df['rating'])

#print df.head()['cuisines'], df.head()['North Indian']
print()
for row in range(len(rating)):
	if (isinstance(rating[row],str)):
		token = rating[row][:3]
		if token[0] == '-':
			one_hot_rating.ix[row, 'not rated']=1
		else:
			token = float(token)
		
			if(token>4):
				one_hot_rating.ix[row, '5 star']=1
			elif(token>3):
				one_hot_rating.ix[row, '4 star']=1
			elif(token>2):
				one_hot_rating.ix[row, '3 star']=1
			elif(token>1):
				one_hot_rating.ix[row, '2 star']=1
			elif(token>0):
				one_hot_rating.ix[row, '1 star']=1




cloumn_names = one_hot_rating.columns
cloumn_names = cloumn_names.tolist()
i = 0 
#for x in cloumn_names:
	#occurance_count = one_hot_rating[x].sum()

	#if (occurance_count < 5):
	#	one_hot_cuisine = one_hot_cuisine.drop([x], axis = 1)
	#	print(x ," : ", occurance_count)

one_hot_rating.to_csv('one_hot_rating.csv')

'''
highlights = df['highlights']
highlight_list = []

for item in highlights:
		for highlight in items:
			highlight_list.append(highlight)


hf1 = pd.DataFrame({'highlights':highlight_list})	

hf2 = hf1.cuisine.unique()
'''









