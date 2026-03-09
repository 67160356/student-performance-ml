from sklearn.metrics import accuracy_score
from preprocessing import X_test, y_test
from train_model import model

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
