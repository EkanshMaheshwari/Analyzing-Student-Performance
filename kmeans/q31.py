import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
data=pd.read_csv("data.csv")
s=data[["G3","address","traveltime"]]
le=LabelEncoder()
s["addressn"]=le.fit_transform(s["address"])
print(s)#Urban 1 Rural 0
#s["t"]=le.fit_transform(s["Mjob"])
print(s)
q=s[["addressn","G3","traveltime"]]#Urban = 1 Rural=0
fig=plt.figure()
a=[0,1]
b=[0,1,2,3,4]
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["traveltime"],s["addressn"],s["G3"])
ax.set_xlabel("Travel time")
b=[0,1]
a=[1,2,3,4]
ax.set_ylabel("Adress")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
ax.set_xticks(a)
ax.set_yticks(b)
#s["Fjobn"]
plt.show()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
a=[0,1]
b=[0,1,2,3,4]
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["traveltime"],q["addressn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Travel time")
b=[0,1]
a=[1,2,3,4]
ax.set_ylabel("Adress")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
ax.set_xticks(a)
ax.set_yticks(b)
#s["Fjobn"]
plt.show()
q=q.groupby(["traveltime","addressn"])["G3"].mean()
q=q.reset_index()
print(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
a=[0,1]
b=[0,1,2,3,4]
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["traveltime"],q["addressn"],q["G3"])
ax.set_xlabel("Travel time")
b=[0,1]
a=[1,2,3,4]
ax.set_ylabel("Adress")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
ax.set_xticks(a)
ax.set_yticks(b)
#s["Fjobn"]
plt.show()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
a=[0,1]
b=[0,1,2,3,4]
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["traveltime"],q["addressn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Travel time")
b=[0,1]
a=[1,2,3,4]
ax.set_ylabel("Adress")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
ax.set_xticks(a)
ax.set_yticks(b)
plt.show()