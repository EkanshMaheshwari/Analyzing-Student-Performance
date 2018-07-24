import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
data=pd.read_csv("A.csv",sep=";")
s=data[["health","absences"]]
q=data[["health","absences"]]
plt.scatter(s["health"],s["absences"])
plt.show()
plt.title("The health vs absences graph")

kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
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
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["healthw"],s["absences"],color=colors[kmeans.labels_])
plt.title("Health vs Grade point Data")
plt.xlabel("Health")
plt.ylabel("Absences")
#plt.yticks(a)
plt.show()
s=s.groupby(["health","healthw"])["absences"].mean()
s=s.reset_index()
q=s[["health","absences"]]
print(s)
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["healthw"],s["absences"],color=colors[kmeans.labels_])
plt.title("Health vs Grade point Data")
plt.xlabel("Health")
plt.ylabel("Absences")
plt.show()