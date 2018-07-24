import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("data.csv")
s=data[["G3","address"]]
plt.scatter(s["address"],s["G3"])
plt.xlabel("Address")
plt.ylabel("Gradepoint")
plt.show()
s=s.groupby(["address"])["G3"].mean()
print(s)