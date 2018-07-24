import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift
data=pd.read_csv("A.csv",sep=";")
q=data[["health","G3"]]
s=data[["health","G3"]]
a=[i for i in range(0,5)]
s["healthw"]=None
for i in range(0,len(s)):
    if s["health"][i]==1:
        s["healthw"][i]="Very Poor"
    elif s["health"][i] == 2:
        s["healthw"][i] = "Poor"
    elif s["health"][i] == 3:
        s["healthw"][i] = "Satisfactory"
    elif s["health"][i] == 4:
        s["healthw"][i] = "Good"
    elif s["health"][i] == 5:
        s["healthw"][i] = "Very Good"
"""print("a")
plt.scatter(s["healthw"],s["G3"])
print("b")
plt.title("Health vs Grade point Data")
plt.xlabel("Health")
plt.ylabel("Gradepoint")
plt.yticks(a)
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["healthw"],s["G3"],color=colors[kmeans.labels_])
plt.title("Health vs Grade point clusters")
plt.xlabel("Health")
plt.ylabel("Grade point")
plt.xticks(a,rotation="vertical")
c=[i for i in range(1,21)]
plt.yticks(c)
plt.show()"""
q=s[["healthw","G3"]]
q=s.groupby(["healthw","health"])["G3"].mean()
print(q)
q=q.reset_index()
print(q)
s=q[["health","G3"]]
kmeans=MeanShift()
print(s)
kmeans.fit(s)
print(kmeans.labels_)
colors=np.array(["Red","Blue","Green","Yellow","Brown"])
print(kmeans.labels_)
plt.scatter(q["healthw"],s["G3"],color=colors[kmeans.labels_])
plt.title("Health vs Grade point clusters")
plt.xlabel("Health")
plt.ylabel("Grade point")
plt.xticks(a,rotation="vertical")
c=[i for i in range(1,21)]
plt.yticks(c)
plt.show()
