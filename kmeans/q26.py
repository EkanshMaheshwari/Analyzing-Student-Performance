import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
data=pd.read_csv("A.csv",sep=";")
s=data[["activities","G3"]]#activities
q=data[["activities","G3"]]
plt.scatter(s["activities"],s["G3"])
plt.title("The extra curricular activites vs Grade point")
plt.xlabel("Agctivites extracuricular the student")
plt.ylabel("Grade point")
plt.show()
s=s.groupby(["activities"])["G3"].mean()
s=s.reset_index()
print(s)