import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift
data=pd.read_csv("A.csv",sep=";")
s=data[["G3","traveltime"]]
q=data[["G3","traveltime"]]
plt.scatter(s["traveltime"],s["G3"])
plt.title("The traveltime vs gradepoint graph")
plt.show()
kmeans=MeanShift()
kmeans.fit(q)
s["healthw"]=None#healthw is equivalent to traveltime in words
for i in range(0,len(s)):
    if s["traveltime"][i]==1:
        s["healthw"][i]="<15 min"
    elif s["traveltime"][i] == 2:
        s["healthw"][i] = "15 to 30 min"
    elif s["traveltime"][i] == 3:
        s["healthw"][i] = "30 min to 1 hour"
    elif s["traveltime"][i] == 4:
        s["healthw"][i] = "> 1 hour "
colors=np.array(["Red","Blue","Green"])
plt.scatter(s["healthw"],s["G3"],color=colors[kmeans.labels_])
plt.title("The traveltime vs Gradepoint cluster")
plt.xlabel("Travel time")
plt.ylabel("Grade point")
plt.show()
s=s.groupby(["traveltime","healthw"])["G3"].mean()
s=s.reset_index()
print(s)
q=s[["traveltime","G3"]]
kmeans=MeanShift()
kmeans.fit(q)
colors=np.array(["Red","Blue","Green","Brown"])
plt.scatter(s["healthw"],s["G3"],color=colors[kmeans.labels_])
plt.title("The traveltime vs Gradepoint cluster")
plt.xlabel("Travel time")
plt.ylabel("Grade point")
plt.show()
