import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
data=pd.read_csv("A.csv",sep=";")
s=data[["age","G3"]]
q=data[["age","G3"]]
plt.scatter(s["age"],s["G3"])
plt.title("The age vs Grade point")
plt.xlabel("Age of the student")
plt.ylabel("Grade point")
a=[i for i in range(1,21)]
plt.yticks(a)
plt.show()
kmeans=KMeans(n_clusters=3)
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["age"],s["G3"],color=colors[kmeans.labels_])
plt.title("The age vs Grade point cluster")
plt.xlabel("Age of the student")
plt.ylabel("Grade point")
plt.show()