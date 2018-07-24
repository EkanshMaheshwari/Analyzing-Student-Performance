import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import MeanShift
import numpy as np
data=pd.read_csv("A.csv",sep=";")
s=data[["goout","G3"]]
q=data[["goout","G3"]]
s["healthw"]=None
for i in range(0,len(s)):
    if s["goout"][i]==1:
        s["healthw"][i]="Very poor"
    elif s["goout"][i] == 2:
        s["healthw"][i] = "Poor"
    elif s["goout"][i] == 3:
        s["healthw"][i] = "ok"
    elif s["goout"][i] == 4:
        s["healthw"][i] = "High "
    elif s["goout"][i] == 5:
        s["healthw"][i] = "Very high"
plt.scatter(s["healthw"],s["G3"])
plt.title("The gout vs Grade point")
plt.xlabel("Gout of the student")
plt.ylabel("Grade point")
plt.show()
q=s[["goout","G3"]]
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["healthw"],q["G3"],color=colors[kmeans.labels_])
plt.title("The gout vs Grade point")
plt.xlabel("Gout of the student")
plt.ylabel("Grade point")
plt.show()
s=s.groupby(["healthw","goout"])["G3"].mean()
s=s.reset_index()
print(s)
q=s[["goout","G3"]]
plt.scatter(s["healthw"],q["G3"])
plt.title("The gout vs Grade point")
plt.xlabel("Gout of the student")
plt.ylabel("Grade point")
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green","Brown","Yellow"])
plt.scatter(s["healthw"],q["G3"],color=colors[kmeans.labels_])
plt.title("The gout vs Grade point")
plt.xlabel("Gout of the student")
plt.ylabel("Grade point")
plt.show()
