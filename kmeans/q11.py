import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("A.csv",sep=";")
s=data[["sex","G3"]]
q=data[["sex","G3"]]
plt.scatter(s["sex"],s["G3"])
plt.title("The age vs Grade point")
plt.xlabel("Age of the student")
plt.ylabel("Grade point")
plt.show()
lbmake=LabelEncoder()
s["numericalsex"]= lbmake.fit_transform(s["sex"])+1 #converting sex to numerical value because kmeans only uses numerical values and no character values
print(s)
q=s[["numericalsex","G3"]]
a=KMeans(n_clusters=3)
a.fit(q)
print(a.labels_)
colormap=np.array(['Blue','Red','Green'])
s=data.sex
plt.title("The sex vs grade point cluster")
z=plt.scatter(data["sex"],data["G3"],color=colormap[a.labels_])
plt.xlabel("Sex")
plt.ylabel("Performance on GP")
plt.show()
print(a)
