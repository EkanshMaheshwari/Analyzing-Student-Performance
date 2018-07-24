import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
data=pd.read_csv("A.csv",sep=";")
s=data[["G3","famsize"]]
q=data[["G3","famsize"]]
plt.scatter(s["famsize"],s["G3"])
plt.title("The famsize vs gradepoint graph")
plt.show()
