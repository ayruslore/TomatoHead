import numpy as np
from kmodes import kmodes

data = np.random.randint(low = 0,high = 2, size =(1000, 20),  dtype=np.int64) #hundred rows three columns taking values {0,1}

model = kmodes.KModes(n_clusters = 20, init='Huang', n_init=5, verbose=1)

#Train step
clusters = model.fit_predict(data)

print model.cluster_centroids_

print clusters #prints a list corresponding to [0:k) buckets