# -*- coding: utf-8 -*-
"""
Spyder Editor
此程式的架構為 :
若要更改K值
可直接更改變數K即可
"""

# Import 
import numpy as np
import math as m

#LaodData
training_data = np.loadtxt('training_data.txt')
testing_data = np.loadtxt('testing_data.txt')
#Setting K
k=3
category=[]
center=[]
data_size = len(training_data[0])

# Distance Function
def distance_between_2_dots(x1,x2):
    distance_square=0
    for i in range(4):
        add=(x1[i]-x2[i])**2
        distance_square+=add
    distance = m.sqrt(distance_square)
    return distance

#Initial Center
def ini_center():
    global k,center
    center=np.array(training_data[np.random.randint(1,len(training_data),k)])
    print('\nInitial Center :\n',center)
#Clustering (Training data) 
def clustering():
    global training_data,category
    category=[]
    for i in training_data:
        distance=[]
        for j in center:
            distance.append(distance_between_2_dots(j,i))
        category.append(distance.index(min(distance)))

#Clustering (Testingdata)
def TesttingData_clustering():
    global category,testing_data
    category=[]
    for i in testing_data:
        distance=[]
        for j in center:
            distance.append(distance_between_2_dots(j,i))
        category.append(distance.index(min(distance)))
    print(category)

#Reset the center
def reset_center():
    global k,category
    for i in range(k):
        temp=np.zeros(data_size)
        c=0
        for j in range(len(training_data)):
                if category[j]==i:
                    temp+=training_data[j]
                    c+=1
        center[i]=temp/c

#Main
pre_center=np.zeros(data_size)
ini_center()
count=0
print("\n--Training Start--\nCenter : ")
while True:
    if count>50:
        print("Can't converged\n")
        break
    count+=1
    clustering()
    reset_center()
    print(count,".\n",center,'\n')
    if np.array_equal(pre_center,center ):
        break
        print("The clustering converged\n")
    pre_center=center

print("--Training Done--\n\nTesting Data Output:")
TesttingData_clustering()