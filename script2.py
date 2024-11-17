#prediction part
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
import joblib
from datetime import datetime


cred = credentials.Certificate("C:\\Users\\shrin\\Downloads\\esp32first-59ff4-firebase-adminsdk-f6sa9-9437a64dc5.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esp32first-59ff4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


health_model = joblib.load('machine_health_model.pkl') #loading the pretrained the model form the memory
reason_model = joblib.load('reason_model.pkl')



def fetch_real_time_data():
    ref = db.reference('sensor2/')
    data = ref.get()
    return data

def predict_health_and_reason(data):
    processed_data = preprocess(data)
    health_prediction = health_model.predict([processed_data])[0]
    reason_prediction = reason_model.predict([processed_data])[0]
    return health_prediction, reason_prediction

def preprocess(data):  #process the raw data and prepare it for prediction
    processed_data = [
        data['temperature_data'],
        data['Humidity'],
        data['Rpm'],
        data['sound_dB'],
        data['Amplitude'],
        data['Frequency']
    ]
    return processed_data

def append_data_to_historical(data, health_prediction, reason_prediction, file_path="C:\\code\\python\\updateddataset2.csv"):
    new_data = pd.DataFrame([{
        'timestamp': datetime.now(),
        'temperature_data': data['temperature_data'],
        'Humidity': data['Humidity'],
        'Rpm': data['Rpm'],
        'sound_dB': data['sound_dB'],
        'Amplitude': data['Amplitude'],
        'Frequency': data['Frequency'],
        'machine_condition': health_prediction,
        'reason': reason_prediction
    }])
    historical_data = pd.read_csv(file_path) #just add the data at hte end
    updated_data = pd.concat([historical_data, new_data], ignore_index=True)
    updated_data.to_csv(file_path, index=False)


real_time_data = fetch_real_time_data()
health_prediction, reason_prediction = predict_health_and_reason(real_time_data) #function already 


print(f"Predicted Machine Health: {health_prediction}")
print(f"Reason: {reason_prediction}")


append_data_to_historical(real_time_data, health_prediction, reason_prediction)