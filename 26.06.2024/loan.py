import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, f1_score, recall_score, confusion_matrix
# load the dataset data.csv
data = pd.read_csv('data.csv')

# selection the features which need to be used in the case
X = data[['loan_amount', 'term', 'interest_rate','income','credit_score','age','employment_length']]
y = data['loan_repaid']

# split train_test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initiate the model
model = DecisionTreeClassifier(random_state=42)

# train the model
model.fit(X_train, y_train)

# make a prediction
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Generate the confusion matrix
conf_mat = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_mat)
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

#recall
recall = recall_score(y_test,y_pred)
print("recall:",recall)

#F1 score
F1Score = f1_score(y_test,y_pred)
print("F1score:",F1Score)