import numpy as np
from kmodes import kmodes
import pandas
import statistics
data =  pandas.read_csv('./example.csv')#hundred rows three columns taking values {0,1}
restaurant_data = pandas.read_csv("./Data/data/locationwise/Indiranagar.csv")
mini = 2000
j = 0
if True:
	model = kmodes.KModes(n_clusters = 30, init='Huang', n_init=5, verbose=1)

	#Train step
	clusters = model.fit_predict(data)

	print(model.cluster_centroids_)

	print(clusters) #prints a list corresponding to [0:k) buckets
	print(len(clusters))
	for i in range(len(clusters)):
		print("{} : {}".format(restaurant_data.loc[i]['restaurant'],clusters[i]))

	print(statistics.mode(clusters))
	print(model.cost_)
	if(model.cost_<mini):
		mini = model.cost_
		size = j

print(mini)
print(size)
super_class = pandas.DataFrame(model.cluster_centroids_)
model2 = kmodes.KModes(n_clusters = 5, init='Huang', n_init=5, verbose=1)
clusters2 = model2.fit_predict(super_class)
for i in range(len(clusters2)):
		print("{} : {} ".format(model.cluster_centroids_[i],clusters2[i]))