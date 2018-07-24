import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
data=pd.read_csv("data.csv")
s=data[["G3","Mjob","Fjob"]]
le=LabelEncoder()
s["Fjobn"]=le.fit_transform(s["Fjob"])
s["Mjobn"]=le.fit_transform(s["Mjob"])
print(s)
q=s[["Fjobn","Mjobn","G3"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Fjobn"],s["Mjobn"],s["G3"])
ax.set_xlabel("Fathers job")
ax.set_ylabel("Mothers job")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
#s["Fjobn"]
plt.show()
colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["Fjobn"],q["Mjobn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Fathers job")
ax.set_ylabel("Mothers job")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
a=[0,1,2,3,4]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()
q=q.groupby(["Fjobn","Mjobn"])["G3"].mean()
q=q.reset_index()
print(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["Fjobn"],q["Mjobn"],q["G3"])
ax.set_xlabel("Fathers job")
ax.set_ylabel("Mothers job")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
a=[0,1,2,3,4]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()
colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["Fjobn"],q["Mjobn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Fathers job")
ax.set_ylabel("Mothers job")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
a=[0,1,2,3,4]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()