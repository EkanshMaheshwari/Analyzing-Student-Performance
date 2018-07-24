import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import MeanShift
data=pd.read_csv("A.csv",sep=";")
s=data[["reason","G3"]]
lbmake=LabelEncoder()
s["reasonn"]=lbmake.fit_transform(s["reason"])
plt.scatter(s["reason"],s["G3"])
plt.title("Reason vs gradepoint")
plt.xlabel("Reason of joing school")
plt.ylabel("Grade point")
plt.show()
q=s[["reasonn","G3"]]
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["reason"],s["G3"],color=colors[kmeans.labels_])
plt.title("Reason vs gradepoint")
plt.xlabel("Reason of joing school")
plt.ylabel("Grade point")
plt.show()

s=s.groupby(["reason","reasonn"])["G3"].mean()
s=s.reset_index()
print(s)
plt.scatter(s["reason"],s["G3"])
plt.title("Reason vs gradepoint")
plt.xlabel("Reason of joing school")
plt.ylabel("Grade point")
plt.show()
kmeans=MeanShift()
q=s[["reasonn","G3"]]
kmeans.fit(q)
colors=np.array(["Red","Blue","Green","Yellow"])
plt.scatter(s["reason"],s["G3"],color=colors[kmeans.labels_])
plt.title("Reason vs gradepoint")
plt.xlabel("Reason of joing school")
plt.ylabel("Grade point")
plt.show()
