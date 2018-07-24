import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv")
s=data[["G3","Dalc","failures"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["failures"],s["G3"])
ax.set_xlabel("Daily Alchol consumption")
a=[1,2,3,4]
ax.set_ylabel("Failures")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
plt.show()

colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["failures"],s["G3"],color=colors[kmeans.labels_])
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
ax.set_xlabel("Daily Alchol consumption")
#s["Fjobn"]
plt.show()

s=s.groupby(["Dalc","failures"])["G3"].mean()
s=s.reset_index()
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["failures"],s["G3"])
ax.set_xlabel("Daily Alchol consumption")
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
plt.show()

colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["failures"],s["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Daily Alchol consumption")
ax.set_ylabel("Filures")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
plt.show()