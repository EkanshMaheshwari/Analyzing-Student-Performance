import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
data=pd.read_csv("data.csv")
s=data[["G3","freetime","studytime"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["freetime"],s["studytime"],s["G3"])
ax.set_xlabel("Free time")
ax.set_ylabel("Study time")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
plt.show()
colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["freetime"],s["studytime"],s["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Free time")
ax.set_ylabel("Study time")
ax.set_zlabel("Grade point")
a=[1,2,3,4,5]
ax.set_xticks(a)
ax.set_yticks(a)
plt.show()
s=s.groupby(["freetime","studytime"])["G3"].mean()
s=s.reset_index()
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["freetime"],s["studytime"],s["G3"])
ax.set_xlabel("Free time")
ax.set_ylabel("Study time")#Mothers job at home-0health 1 other 2 services 3  teacher 4
ax.set_zlabel("Grade point")#Father teacher-4 other 2 services 3  health 1 at home 0
plt.show()
colors=np.array(["Red","Blue","Green"])
kmeans=KMeans(n_clusters=3)
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["freetime"],s["studytime"],s["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Free time")
ax.set_ylabel("Study time")
ax.set_zlabel("Grade point")
ax.set_label("Kmeans label")
plt.show()