import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("A.csv",sep=";")
s=data[["failures","G3"]]
plt.scatter(s["failures"],s["G3"])
plt.title("Failure vs gradepoint")
plt.xlabel("Failure of the student")
plt.ylabel("Grade point")
plt.show()
s=data[["failures","G3"]]
s=s.groupby(["failures"])["G3"].mean()

print(s)
fig = s.plot.bar()
fig.figure.show()
plt.show()
s=s.reset_index()
print(s)
plt.scatter(s["failures"],s["G3"])
plt.xlabel("Failures")
plt.ylabel("Grade point")
plt.show()