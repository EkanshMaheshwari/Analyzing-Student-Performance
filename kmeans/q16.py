import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("data.csv")
s=data[["traveltime","address"]]
plt.scatter(s["address"],s["traveltime"])
plt.xlabel("Address")
plt.ylabel("Travel time")
plt.yticks([1,2,3,4])
plt.show()