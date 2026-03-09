from sklearn.ensemble import RandomForestClassifier
from preprocessing import X_train, y_train

model = RandomForestClassifier()

model.fit(X_train, y_train)
