import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib


data = pd.read_csv("C:\\code\\python\\updateddataset2.csv") #preparing features


X = data[['temperature_data', 'Humidity', 'Rpm', 'sound_dB', 'Amplitude', 'Frequency']]


y_health = data['machine_condition']   #target columns
y_reason = data['reason']  


X_train, X_test, y_health_train, y_health_test, y_reason_train, y_reason_test = train_test_split(X, y_health, y_reason, test_size=0.3, random_state=42) #30% for testing  and 42 makesure that is it reproducable


health_model = RandomForestClassifier(n_estimators=100, random_state=42)  #random forest is initialized with 100 decision trees
reason_model = RandomForestClassifier(n_estimators=100, random_state=42) 

health_model.fit(X_train, y_health_train) #prediction are made using the test set
reason_model.fit(X_train, y_reason_train)


y_health_pred = health_model.predict(X_test) #prediction are made using the test set
y_reason_pred = reason_model.predict(X_test)


print("Health Condition Classification Report:")
print(classification_report(y_health_test, y_health_pred))


print("Reason Classification Report:")
print(classification_report(y_reason_test, y_reason_pred))


joblib.dump(health_model, 'machine_health_model.pkl')  #storing trained model
joblib.dump(reason_model, 'reason_model.pkl')

'''
1.Data Loading
2.Feature and Label Preparation
3.Data Splitting
4.Model Initialization
5.Model Training
6.Prediction
7.Evaluation
8.Model Saving

'''