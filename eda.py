import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Student_performance_10k.csv")

plt.figure()
sns.histplot(df["math_score"], bins=20)
plt.title("Math Score Distribution")
plt.show()

plt.figure()
sns.boxplot(x="gender", y="math_score", data=df)
plt.title("Math Score by Gender")
plt.show()
