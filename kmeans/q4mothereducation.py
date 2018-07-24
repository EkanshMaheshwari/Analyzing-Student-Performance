import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data=pd.read_csv("A.csv",sep=";")
s=data[["Medu","G3"]]
q=s[["Medu","G3"]]
s["Meduw"]=None
for i in range(0,len(s)):
    if s["Medu"][i]==0:
        s["Meduw"][i]="None"
    elif s["Medu"][i]==1:
        s["Meduw"][i]="Primary"
    elif s["Medu"][i]==2:
        s["Meduw"][i]="Middle"
    elif s["Medu"][i]==3:
        s["Meduw"][i]="Secondary"
    elif s["Medu"][i]==4:
        s["Meduw"][i]="Higher"
print(s)
plt.scatter(s["Meduw"],s["G3"])
plt.xticks(s["Meduw"])
plt.xlabel("Education")
plt.ylabel("Final Marks")
plt.show()

kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["Meduw"],s["G3"],color=colors[kmeans.labels_])
plt.xticks(rotation="vertical")
plt.title("Mother education cluster")
plt.show()