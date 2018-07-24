import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.cluster import KMeans

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
data=pd.read_csv("A.csv",sep=";")
#print(data)
s=data[["schoolsup","famsup","G3"]]
lbmake=LabelEncoder()
s["famsupn"]=lbmake.fit_transform(s["famsup"])#yes-0 no 1
s["schoolsupn"]=lbmake.fit_transform(s["schoolsup"])#no-1 yes-1
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["schoolsupn"],s["famsupn"],s["G3"])
ax.set_xlabel("Schools up")
ax.set_ylabel("Fms support")
ax.set_zlabel("G3")
plt.show()
q=s[["schoolsupn","famsupn","G3"]]
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["schoolsupn"],q["famsupn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Extra educational support")
ax.set_ylabel("Family support")
ax.set_zlabel("Grade point")
ax.set_xticks([0,1])
ax.set_yticks([0,1])
plt.show()
s=s.groupby(["famsupn","schoolsupn"])["G3"].mean()
q=s.reset_index()
print(q)
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["schoolsupn"],q["famsupn"],q["G3"])
ax.set_xlabel("Schools up")
ax.set_ylabel("Fms support")
ax.set_zlabel("G3")
plt.show()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["schoolsupn"],q["famsupn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Extra educational support")
ax.set_ylabel("Family support")
ax.set_zlabel("Grade point")
ax.set_xticks([0,1])
ax.set_yticks([0,1])
plt.show()