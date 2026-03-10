import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("Student_performance_10k.csv")

# สร้าง total score
df["total_score"] = df["math_score"] + df["reading_score"] + df["writing_score"]

# กำหนด PASS ใหม่
df["pass"] = df["total_score"].apply(lambda x: 1 if x >= 150 else 0)

X = df[["math_score","reading_score","writing_score"]]
y = df["pass"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pickle.dump(model,open("model.pkl","wb"))
