import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("A.csv",sep=";")
s=data[["nursery","G3"]]
plt.scatter(s["nursery"],s["G3"])
plt.xlabel("Nursery")
plt.ylabel("G3")
plt.show()
s=s.groupby(["nursery"])["G3"].mean()
print(s)
s=s.reset_index()
print(s)
plt.scatter(s["nursery"],s["G3"])
plt.xlabel("Nursery")
plt.ylabel("G3")
plt.show()