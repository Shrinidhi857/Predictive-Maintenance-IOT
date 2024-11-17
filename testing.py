import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import subprocess


data = pd.read_csv("C:\\code\\python\\updateddataset2.csv") #main dataset
X = data.drop('machine_condition', axis=1)
y = data['machine_condition']


cred = credentials.Certificate("C:\\Users\\shrin\\Downloads\\esp32first-59ff4-firebase-adminsdk-f6sa9-9437a64dc5.json")


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esp32first-59ff4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


def get_data_from_firebase():
    ref = db.reference('sensor2')
    data = ref.get()
    return data

data = get_data_from_firebase()



st.header("Predictive Maintenance" ,divider='rainbow') #streamlit


st.write("Real-time Sensor plot using Streamlit and Matplotlib" )



message_holder2 = st.empty()    #these are placeholders
plot_placeholder1 = st.empty()
plot_placeholder2 = st.empty()
plot_placeholder3 = st.empty()
plot_placeholder4 = st.empty()
plot_placeholder5 = st.empty()
plot_placeholder6 = st.empty()


temperature_data = [28, 28, 29, 29, 27, 28, 29, 29, 28, 29] #Initialize data lists
time_data = list(range(1, 11))
rpm_data = [1000, 5000, 1210, 2020, 3030, 2000, 1900, 4220, 5502, 4000]
sound_data = [14.2, 14.5, 14.2, 14.6, 15.3, 15.6, 15.5, 17.1, 14.3, 14.2]
amplitude_data = [1.01, 1.50, 1.34, 2.50, 2.53, 0.90, 0.91, 0.67, 0.0, 0.0]
freq_data = [1000, 2000, 250, 100, 240, 300, 400, 550, 700, 400]
humidity_data = [61, 70, 67, 66, 71, 68, 69, 63, 64, 67]
window_size = 100

def run_script_and_get_result(script_path):   #this function is used to run train and predict files
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip() #will capture output
    else:
        raise RuntimeError(f"Script failed with return code {result.returncode} and error: {result.stderr}") #some error message if not working 
   

while True:

    data = get_data_from_firebase() #step firebase data fetching

    
    rpm_data.append(data.get('Rpm')) #appending the data into the lists
    freq_data.append(data.get('Frequency'))
    amplitude_data.append(data.get('Amplitude'))
    temperature_data.append(data.get('temperature_data'))
    humidity_data.append(data.get('Humidity'))
    sound_data.append(data.get('sound_dB'))
    time_data.append(len(time_data) + 1)
    
 
    scriptpath1="C:\\code\\python\\MainEL\\script1.py" 
    scriptpath2="C:\\code\\python\\MainEL\\script2.py" 
    script1result=run_script_and_get_result(scriptpath1) #calling train
    script2result=run_script_and_get_result(scriptpath2) #calling predict
    
    
    message_holder2.text(script2result)

    if len(time_data) > window_size:      #used to move the graph window while updating the graph
        temperature_data = temperature_data[-window_size:]
        time_data = time_data[-window_size:]
        rpm_data = rpm_data[-window_size:]
        sound_data = sound_data[-window_size:]
        amplitude_data = amplitude_data[-window_size:]
        freq_data = freq_data[-window_size:]
        humidity_data = humidity_data[-window_size:]

    
   
    
    
    fig1, ax = plt.subplots(figsize=(10, 3))                        #ploting temperature
    ax.plot(time_data, temperature_data, label='Temperature (°C)')
    ax.set_title('Real-Time Temperature Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder1.pyplot(fig1)
    plt.close(fig1)
    
    fig2, ax = plt.subplots(figsize=(10, 3))                        #ploting RPM
    ax.plot(time_data, rpm_data, label='RPM')
    ax.set_title('Real-Time RPM Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('RPM')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder2.pyplot(fig2)
    plt.close(fig2)
    
    fig3, ax = plt.subplots(figsize=(10, 3))                         #ploting Amplitude of vibration
    ax.plot(time_data, amplitude_data, label='Amplitude')
    ax.set_title('Real-Time Vibration Amplitude Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder3.pyplot(fig3)
    plt.close(fig3)
    
    fig4, ax = plt.subplots(figsize=(10, 3))                         #ploting Humidity
    ax.plot(time_data, humidity_data, label='Humidity')
    ax.set_title('Real-Time Humidity Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Humidity')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder4.pyplot(fig4)
    plt.close(fig4)
    
    fig5, ax = plt.subplots(figsize=(10, 3))                           #ploting sound in dB
    ax.plot(time_data, sound_data, label='Sound (dB)')
    ax.set_title('Real-Time Sound Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Sound (dB)')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder5.pyplot(fig5)
    plt.close(fig5)
    
    fig6, ax = plt.subplots(figsize=(10, 3))                            #ploting the ferquency of vibration
    ax.plot(time_data, freq_data, label='Frequency in HZ')
    ax.set_title('Real-Time Frequency Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('freq HZ')
    ax.set_xlim(time_data[0], time_data[-1])
    ax.legend()
    plot_placeholder6.pyplot(fig6)
    plt.close(fig6)
    time.sleep(1)

