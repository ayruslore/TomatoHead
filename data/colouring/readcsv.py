import csv
with open('Toread.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    test={}
    for row in reader:
        #print(row['Restaurant'], row['Location']
        test[row['Restaurant']]=row['Cuisines Colours']

        #row['Restaurant'].values=row['Cuisines']
    #print test
n = 85 #total_cuisines = 85
cuisines_graph = [[0 for x in range(n)] for y in range(n)]
for rest in test.keys():
    for i in range(0,n):
        for j in range(0,i):
            if str(i) in test[rest] and str(j) in test[rest]:
                if len(test[rest]) == 2: cuisines_graph[i][j] += 1.0
                else: cuisines_graph[i][j] += 2.0/(len(test[rest])*(len(test[rest])-1))
with open('result2.csv', 'w') as csvfile:
	csvfileWriter = csv.writer(csvfile)
	for i in range(0,n):
		array=[]
    		for j in range(0,n):
			array.append(cuisines_graph[i][j])
        	csvfileWriter.writerow(array)
  #     	            print '%.4f'%(cuisines_graph[i][j]),
 #               print ("\n")
