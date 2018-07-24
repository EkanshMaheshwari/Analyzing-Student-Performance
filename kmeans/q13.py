import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("A.csv",sep=";")
s=data[["Pstatus","G3"]]
plt.scatter(s["Pstatus"],s["G3"])
plt.title("Parental Status vs grade point")
plt.xlabel("Parental status")
plt.ylabel("Gradepoint")
plt.show()