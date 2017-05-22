import csv
with open('Toread.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    test={}
    i=0
    for row in reader:
        #print(row['Restaurant'], row['Location']
        test[i]=row['Cuisines Colours']
	i=i+1

        #row['Restaurant'].values=row['Cuisines']
    #print test
for rest in test.keys():
	if(test[rest] != '' and test[rest].isalpha() == False):
		test[rest] = map(int, test[rest].split(','))
	else: test[rest] = [-1]
n = 85 #total_cuisines = 85
cuisines_graph = [[0 for x in range(n)] for y in range(n)]
cuisine_occurence = [0 for i in range(n)]
for rest in test.keys():
    for i in range(n):
        if i in test[rest]: cuisine_occurence[i] += 1

for i in range(n):
	if cuisine_occurence[i] == 0: cuisine_occurence[i] = 1
occurence_together = [[0 for x in range(n)] for y in range(n)]

for rest in test.keys():
	for i in range(n):
		for j in range(i):
			if (i in test[rest] and j in test[rest]):
				 occurence_together[j][i] += 1
				 



print occurence_together[0][10]
print cuisine_occurence[10]
for i in range(n):
	for j in range(n):
		cuisines_graph[i][j] = (occurence_together[min(i,j)][max(i,j)])*0.1/(cuisine_occurence[i]*0.1)
		
with open('result6.csv', 'w') as csvfile:
	csvfileWriter = csv.writer(csvfile)
	for i in range(0,n):
		array=[]
    		for j in range(0,n):
			array.append(cuisines_graph[i][j])
        	csvfileWriter.writerow(array)
  #     	            print '%.4f'%(cuisines_graph[i][j]),
 #               print ("\n")
