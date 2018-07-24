import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
data=pd.read_csv("data.csv")
s=data[["G3","address","internet"]]
labmake=LabelEncoder()
s["addressn"]=labmake.fit_transform(data["address"])#rural =0 urban=1
s["internetn"]=labmake.fit_transform(data["internet"])#yes=1 no 1
print(s)
q=s[["addressn","internetn","G3"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["addressn"],q["internetn"],q["G3"])#
ax.set_xlabel("Address")
ax.set_ylabel("Intenet")
ax.set_zlabel("Grade point")
plt.show()
colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["addressn"],q["internetn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Address")
ax.set_ylabel("Intenet")
ax.set_zlabel("Grade point")
a=[0,1]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()

q=q.groupby(["addressn","internetn"])["G3"].mean()
q=q.reset_index()
print(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["addressn"],q["internetn"],q["G3"])
ax.set_xlabel("Address")
ax.set_ylabel("Intenet")
ax.set_zlabel("Grade point")

a=[0,1]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()

colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["addressn"],q["internetn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Address")
ax.set_ylabel("Intenet")
ax.set_zlabel("Grade point")
a=[0,1]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()