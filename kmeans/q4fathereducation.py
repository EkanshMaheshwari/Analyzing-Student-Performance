import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data=pd.read_csv("A.csv",sep=";")
s=data[["Fedu","G3"]]
q=s[["Fedu","G3"]]
s["Feduw"]=None
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
print(s)
plt.scatter(s["Feduw"],s["G3"])
plt.xticks(s["Feduw"])
plt.xlabel("Education")
plt.ylabel("Final Marks")
plt.show()

kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["Feduw"],s["G3"],color=colors[kmeans.labels_])
plt.xticks(rotation="vertical")
plt.title("Father education cluster")
plt.show()