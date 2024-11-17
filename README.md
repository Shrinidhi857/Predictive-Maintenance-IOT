# Predictive Maintenance using IoT  

## Overview  
This project demonstrates an **IoT-based Predictive Maintenance System**. It uses real-time sensor data, machine learning models, and Firebase integration to monitor equipment health, predict failures, and determine reasons for malfunctions. The system includes visualization using **Streamlit** and **Matplotlib**, real-time data fetching from Firebase, and automated machine health and fault prediction.

---

## Features  
- **Real-time Data Monitoring:** Fetch sensor data from Firebase and visualize it dynamically.  
- **Machine Health Prediction:** Predict the condition of a machine using a pre-trained Random Forest Classifier.  
- **Fault Diagnosis:** Identify the reasons behind machine faults with another Random Forest model.  
- **Historical Data Logging:** Append predictions and sensor data to a CSV file for future analysis.  
- **Interactive Visualizations:** Real-time sensor plots displayed via Streamlit and Matplotlib.  
- **Automated Model Training:** Train Random Forest models for health and fault prediction.  

---

## Technologies Used  
- **Languages:** Python  
- **Libraries:**  
  - **Data Handling:** `pandas`, `numpy`  
  - **Machine Learning:** `scikit-learn`, `joblib`  
  - **Visualization:** `matplotlib`, `streamlit`  
- **Firebase:**  
  - Realtime Database for sensor data  
  - Admin SDK for secure data access  
- **Others:** `subprocess` for calling scripts dynamically  

---

## Project Structure  

```plaintext  
📂 Predictive-Maintenance-IoT  
├── testing.py                # Streamlit-based dashboard for real-time monitoring  
├── script1.py             # Script for prediction and data logging  
├── script2.py             # Script for model training  
├── updateddataset2.csv    # Main dataset for training and predictions  
├── machine_health_model.pkl  # Pre-trained machine health model  
├── reason_model.pkl       # Pre-trained fault diagnosis model  
├── firebase-adminsdk.json # Firebase service account key  
```  

---

## Workflow  

### 1. Real-Time Monitoring  
- Sensor data is fetched continuously from Firebase.  
- Live plots for temperature, RPM, vibration, and sound levels are updated in the Streamlit dashboard.  

### 2. Machine Health Prediction  
- **script1.py** processes incoming data and predicts machine health (`Healthy`, `Warning`, `Critical`).  
- The root cause of any issue is also predicted using the trained model.  

### 3. Data Logging  
- Predictions and real-time sensor data are appended to the `updateddataset2.csv` file for analysis.  

### 4. Model Training  
- **script2.py** trains Random Forest Classifiers for health and fault prediction using the main dataset.  

---

## Setup Instructions  

### Prerequisites  
1. Install Python (>=3.8).  
2. Install the required libraries using:  
   ```bash  
   pip install pandas numpy scikit-learn matplotlib firebase-admin streamlit  
   ```  

3. Set up a Firebase Realtime Database and download the service account key JSON file.  

### Running the Project   

1. **Start the real-time monitoring:**  
   ```bash  
   streamlit run testing.py  
   ```  

2. **Train the models (if needed):**  
   ```bash  
   python script2.py  
   ```  

3. **Perform predictions:**  
   ```bash  
   python script1.py  
   ```  

---

## Dataset Details  
The dataset (`updateddataset2.csv`) includes the following features:  
- **Temperature:** Sensor data in degrees Celsius.  
- **Humidity:** Percentage of relative humidity.  
- **RPM:** Rotational speed of the machine.  
- **Sound (dB):** Noise levels recorded.  
- **Amplitude:** Vibration amplitude of the machine.  
- **Frequency:** Vibration frequency in Hz.  
- **Machine Condition:** Health labels (`Healthy`, `Warning`, `Critical`).  
- **Reason:** Root cause labels for machine faults.  

---

## Future Enhancements  
- Integration with **IoT edge devices** like ESP32 for direct data streaming.  
- Advanced ML models (e.g., Deep Learning) for better accuracy.  
- Mobile app integration for real-time health notifications.  

---

## Screenshots  

### Streamlit Dashboard  
![Screenshot 2024-11-17 112704](https://github.com/user-attachments/assets/aeab8791-eba8-40b1-a3e1-cf91548a7356)



### Real-Time Sensor Plots  
 
![image](https://github.com/user-attachments/assets/a6873556-35f4-4cc1-8c67-ecf2766da8cc)

---

Feel free to fork and customize the project for your use case! 🌟
