import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data=pd.read_csv("A.csv",sep=";")
s=data[["Fedu","Medu","G3"]]
q=s[["Fedu","Medu","G3"]]
s["Feduw"]=None
s["Meduw"]=None
"""
for i in range(0,len(s)):
    if s["Fedu"][i]==0:
        s["Feduw"][i]="None"
    elif s["Fedu"][i]==1:
        s["Feduw"][i]="Primary"
    elif s["Fedu"][i]==2:
        s["Feduw"][i]="Middle"
    elif s["Fedu"][i]==3:
        s["Feduw"][i]="Secondary"
    elif s["Fedu"][i]==4:
        s["Feduw"][i]="Higher"
    if s["Medu"][i]==0:
        s["Meduw"][i]="None"
    elif s["Medu"][i]==1:
        s["Meduw"][i]="Primary"
    elif s["Medu"][i]==2:
        s["Meduw"][i]="Middle"
    elif s["Medu"][i]==3:
        s["Meduw"][i]="Secondary"
    elif s["Medu"][i]==4:
        s["Meduw"][i]="""
print(s)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
#ax.set_xticks()
ax.set_title("Clustering in the on the basis of parentts education")
ax.scatter(s["Medu"],s["Fedu"],s["G3"])
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
print(kmeans.labels_)
colors=np.array(["Red","Blue","Green"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["Fedu"],s["Medu"],s["G3"],color=colors[kmeans.labels_])
ax.set_title("Mean shift Clustering in the on the basis of parent's education")
ax.set_xlabel("Fathers education")
ax.set_ylabel("Mothers Education education")
ax.set_zlabel("Gradepoint")
ax.set_xticks([0,1,2,3,4])
ax.set_yticks([0,1,2,3,4])
plt.show()