import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("Student_performance_10k.csv")

df["pass_math"] = df["math_score"].apply(lambda x: 1 if x >= 50 else 0)

X = df.drop(["pass_math","math_score"], axis=1)
y = df["pass_math"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
