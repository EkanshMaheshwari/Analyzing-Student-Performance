import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("A.csv",sep=";")
s=data[["sex","G3","age"]]
lab=LabelEncoder()
s["sexn"]=lab.fit_transform(s["sex"])#Male = and Female =0
q=s[["sexn","G3","age"]]
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["age"],q["sexn"],q["G3"])
ax.set_ylabel("Sex")
ax.set_xlabel("Age of the student")
ax.set_zlabel("Grade point")
ax.set_zticks([i for i in range(0,21)])
ax.set_yticks([0,1])
plt.show()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["age"],q["sexn"],q["G3"],color=colors[kmeans.labels_])
ax.set_ylabel("Sex")
ax.set_xlabel("Age of the student")
ax.set_zlabel("Grade point")
ax.set_zticks([i for i in range(0,21)])
ax.set_yticks([0,1])
plt.show()
q=q.groupby(["age","sexn"])["G3"].mean()#Female=0 Male=1
q=q.reset_index()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
print(q)

ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["age"],q["sexn"],q["G3"],color=colors[kmeans.labels_])
ax.set_ylabel("Sex")
ax.set_xlabel("Age of the student")
ax.set_zlabel("Grade point")
ax.set_zticks([i for i in range(0,21)])
ax.set_yticks([0,1])
plt.show()
