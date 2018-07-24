import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("A.csv",sep=";")
s=data[["higher","G3"]]
plt.scatter(s["higher"],s["G3"])
plt.xlabel("Higher education")
plt.ylabel("G3")
plt.show()
lbmake=LabelEncoder()
s["highern"]=lbmake.fit_transform(s["higher"])
print(s)#yes-1 and no-0
q=s[["highern","G3"]]
print(q)
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["higher"],s["G3"],color=colors[kmeans.labels_])
plt.xlabel("Higher")
plt.ylabel("G3")
plt.title("Kmeans for Higher educations versus grade point")
plt.show()
s=s.groupby(["higher"])["G3"].mean()
print(s)
s=s.reset_index()
print(s)
plt.scatter(s["higher"],s["G3"])
plt.xlabel("Higher")
plt.ylabel("G3")
plt.show()
s["highern"]=lbmake.fit_transform(s["higher"])
q=s[["highern","G3"]]
kmeans=KMeans(n_clusters=2)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["higher"],s["G3"],color=colors[kmeans.labels_])
plt.xlabel("Higher")
plt.ylabel("G3")
plt.title("Kmeans for Higher educations versus grade point")
plt.show()