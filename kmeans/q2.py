import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
data=pd.read_csv("A.csv",sep=";")
s=data[["G1","G2"]]
q=0
l=0
for i in range(0,len(s)):
    #print(i)
    #print(s["G1"][i])
    #print(s["G2"][i])
    if s["G1"][i] > s["G2"][i] :
        q=q+1
    else:
        l=l+1
print("Number of students having marks of First period greater than Second Period in percentage"+str(q))
per=(q/(q+l))*100
print("Percentage of students having first period grade grater than second period is "+str(per))
plt.scatter(data["G1"],data["G2"])
plt.xlabel("First period Grade")
plt.ylabel("Second period Grade")
a=[i for i in range(0,21)]
print(a)
plt.xticks(a)
plt.yticks(a)
plt.show()
kmeans=KMeans(n_clusters=5)
kmeans.fit(s)
colors=np.array(["Red","Blue","Green","Yellow","Black"])
plt.scatter(s["G1"],s["G2"],color=colors[kmeans.labels_])
plt.xlabel("Marks of First period")
plt.ylabel("Marks of Second period")
plt.xticks(a)
plt.yticks(a)
plt.show()