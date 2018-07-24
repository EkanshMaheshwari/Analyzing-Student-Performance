import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("A.csv",sep=";")
s=data[["romantic","G3"]]#activities
q=data[["romantic","G3"]]
plt.scatter(s["romantic"],s["G3"])
plt.title("The romantic  vs Grade point")
plt.xlabel("Wether the student is romantic or not")
plt.ylabel("Grade point")
plt.show()
s=s.groupby(["romantic"])["G3"].mean()
print(s)
