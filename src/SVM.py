from sklearn import svm
import numpy as np
import pymongo as mongo
import csv
y = []
z = []
X = []
count = []
with open("above6updatedCountoveryear.csv") as f:
	reader = csv.DictReader(f)
	for row in reader:
		y.append(int(float(row['magnitude'])))
		z.append(int(float(row['count'])))
		X.append([int(float(row['latitude'])),int(float(row['longitude']))])
with open("above6full2016.csv") as f:
	reader = csv.DictReader(f)
	for row in reader:
		count.append(int(float(row['count'])))
	
#X = [[52.376, -169.4458],[-10.4012, 165.1409],[13.8672, -58.5479]]
#np.genfromtxt('part.csv', delimiter=',', dtype=[('date','S25'),('x','f8'), ('y','f8'), ('mag','f8')], usecols= (1,2))
#print y
#np.genfromtxt('part.csv', delimiter=',', dtype=[('date','S25'),('x','f8'), ('y','f8'), ('mag','f8')], usecols= (3))
clf = svm.SVC()
clf.fit(X, y)
#clf1 = svm.SVC()
#clf1.fit(X, z)
results = []
ctr = 0
for elems in X:
	if (count[ctr] > 800):
		#print elems
		#print count[ctr]
		a = clf.predict([[elems[0], elems[1]]])
		results.append([elems[0], elems[1], a[0]]) 
	ctr = ctr+1
#print len(results)
#Creating JSON
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
fasia = open('asia.json','w+')
fafrica = open('africa.json','w+')
feurope = open('europe.json','w+')
faustralia = open('australia.json','w+')
fna = open('northamerica.json','w+')
fsa = open('southamerica.json','w+')
fasia.write("[\n")
fafrica.write("[\n")
feurope.write("[\n")
faustralia.write("[\n")
fna.write("[\n")
fsa.write("[\n")

for each_elem in results:
	#print str(each_elem[1])+"," + str(each_elem[0])
	if (-180 <= int(each_elem[1]) <= -30) and (-90 <= int(each_elem[0]) <= 15):
		if (f1 == 1):
			fsa.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		fsa.write(str1)
		#print "SA"
		f1=1
	elif -180 <= int(each_elem[1]) <= -15 and 15 <= int(each_elem[0]) <= 90:
		if (f2 == 1):
			fna.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		fna.write(str1)
		f2=1
		#print "North America"
	elif (70 <= int(each_elem[1]) <= 180) and (-90 <= int(each_elem[0]) <= -15):
		if (f3 == 1):
			faustralia.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		faustralia.write(str1)
		f3=1
		#print "Australia"
	elif -15 <= int(each_elem[1]) <= 70 and 45 <= int(each_elem[0]) <= 90:
		if (f4 == 1):
			feurope.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		fafrica.write(str1)
		f4=1
		#print "Africa"
	elif -15 <= int(each_elem[1]) <= 45 and 45 <= int(each_elem[0]) <= 90:
		if (f5 == 1):
			feurope.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		feurope.write(str1)
		f5=1
		#print "Europe"
	else :
		if (f6 == 1):
			fasia.write(",\n")
		str1 = "	{\"latitude\": "+str(each_elem[0])+",\"longitude\": "+str(each_elem[1])+", \"label\": \""+str(each_elem[2])+"\", \"labelShiftY\": 2, \"type\": \"circle\" }"
		fasia.write(str1)
		f6=1
		#print "Asia"
fasia.write("\n]")
fafrica.write("\n]")
feurope.write("\n]")
faustralia.write("\n]")
fna.write("\n]")
fsa.write("\n]")
fasia.close()
fafrica.close()
feurope.close()
faustralia.close()
fna.close()
fsa.close()