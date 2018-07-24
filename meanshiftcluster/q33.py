import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import MeanShift
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv")
s=data[["G3","Dalc","freetime"]]
q=s[["G3","Dalc","freetime"]]#Urban = 1 Rural=0
fig=plt.figure()
b=[1,2,3,4,5]
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["freetime"],s["G3"])
ax.set_xlabel("Daily Alchol consumption")
a=[1,2,3,4]
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
ax.set_xticks(b)
ax.set_yticks(b)
#s["Fjobn"]
plt.show()

colors=np.array(["Red","Blue","Green"])
kmeans=MeanShift()
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["freetime"],s["G3"],color=colors[kmeans.labels_])
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
#s["Fjobn"]
plt.show()
s=s.groupby(["Dalc","freetime"])["G3"].mean()
s=s.reset_index()
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["freetime"],s["G3"])
ax.set_xlabel("Daily Alchol consumption")
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
ax.set_xticks(b)
ax.set_yticks(b)
plt.show()

colors=np.array(["Red","Blue","Green"])
kmeans=MeanShift()
kmeans.fit(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Dalc"],s["freetime"],s["G3"],color=colors[kmeans.labels_])
ax.set_xlabel("Daily Alchol consumption")
ax.set_ylabel("Free time")#Check the pics
ax.set_zlabel("Grade point")#Check the pic
ax.set_xticks(b)
ax.set_yticks(b)
plt.show()