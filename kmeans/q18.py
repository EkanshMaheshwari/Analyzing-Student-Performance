import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("A.csv",sep=";")
s=data[["guardian","G3"]]
plt.scatter(s["guardian"],s["G3"])
plt.title("Guardian vs gradepoint")
plt.xlabel("Guardian of the student")
plt.ylabel("Grade point")
plt.show()
s=s.groupby(["guardian"])["G3"].mean()
print(s)
