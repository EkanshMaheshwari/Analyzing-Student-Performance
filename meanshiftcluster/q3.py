import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
data=pd.read_csv("A.csv", sep=";")
s=data[["G1","G2","G3"]]
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["G1"],s["G2"],s["G3"])
ax.set_xlabel("G1")
ax.set_ylabel("G2")
ax.set_zlabel("G3")
plt.show()
ms=MeanShift()
ms.fit(s)
print(ms.labels_)
colors=np.array(["Red","Blue","Green","Yellow","Black"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(s["G1"],s["G2"],s["G3"],color=colors[ms.labels_])
ax.set_xlabel("First period Grade")
ax.set_ylabel("Second period Grade")
ax.set_zlabel("Final period Grade")
a=[i for i in range(0,21)]
ax.set_xticks(a)
ax.set_yticks(a)
ax.set_zticks(a)
plt.show()
