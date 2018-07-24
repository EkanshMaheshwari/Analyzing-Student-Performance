import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("A.csv",sep=";")
s=data[["activities","romantic","G3"]]
m=LabelEncoder()
s["actn"]=m.fit_transform(s["activities"])#yes =1 and no =0
s["romn"]=m.fit_transform(s["romantic"])#yes =1 and no =0
print(s)
q=s[["romn","actn","G3"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["romn"],s["actn"],s["G3"])
ax.set_xlabel("Romantic")
ax.set_ylabel("Activites")
ax.set_zlabel("Grade point")
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["romn"],q["actn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Romantic")
ax.set_ylabel("Activites")
ax.set_zlabel("Grade point")
ax.set_xticks([0,1])
ax.set_yticks([0,1])
plt.show()
q=q.groupby(["romn","actn"])["G3"].mean()
q=q.reset_index()
print(q)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["romn"],q["actn"],q["G3"])
ax.set_xlabel("Romantic")
ax.set_ylabel("Activites")
ax.set_zlabel("Grade point")
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green","Brown"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(q["romn"],q["actn"],q["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Romantic")
ax.set_ylabel("Activites")
ax.set_zlabel("Grade point")
ax.set_xticks([0,1])
ax.set_yticks([0,1])
plt.show()
