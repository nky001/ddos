from flask import Flask, render_template
from flask_socketio import SocketIO
import joblib
import socket
import struct
import pandas as pd
from ipaddress import ip_address, IPv4Address



app = Flask(__name__)
socketio = SocketIO(app)


with open('random_forest_model.pkl', 'rb') as f:
    model = joblib.load(f)



def is_valid_ipv4(ip):
    try:
        return isinstance(ip_address(ip), IPv4Address)
    except ValueError:
        return False

def ipv4_to_int(ipv4_address):
    packed_ip = socket.inet_aton(ipv4_address)
    return struct.unpack("!I", packed_ip)[0]

def predict_ddos(model, features):
    feature_names = ['Flow Duration', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Tot Fwd Pkts', 'Init Bwd Win Byts', 'Protocol']
    features_df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(features_df)

    return prediction[0]


sample_data = {
    "benign": {
        "Src_IP": "192.168.1.1", 
        "Dst_IP": "192.168.1.2", 
        "Init_Bwd_Win_Byts": 100, 
        "Dst_Port": 80, 
        "Src_Port": 12345, 
        "Tot_Fwd_Pkts": 10, 
        "Flow_Duration": 200, 
        "Protocol": 6
    },
    "ddos": {
        "Src_IP": "192.168.4.118",
        "Dst_IP": "203.73.24.75",
        "Init_Bwd_Win_Byts": 5840, 
        "Dst_Port": 80, 
        "Src_Port": 4504, 
        "Tot_Fwd_Pkts": 29, 
        "Flow_Duration": 3974862, 
        "Protocol": 6
    }
}

@app.route('/')
def home():
    return render_template('index.html', sample_data=sample_data)

@socketio.on('predict_ddos')
def handle_prediction(data):
    try:
        input_data = [
            data['Flow_Duration'],
            data['Src_IP'], 
            data['Src_Port'],
            data['Dst_IP'], 
            data['Dst_Port'], 
            data['Tot_Fwd_Pkts'], 
            data['Init_Bwd_Win_Byts'],
            data['Protocol']
        ]

        
        if not (is_valid_ipv4(data['Src_IP']) and is_valid_ipv4(data['Dst_IP'])):
            socketio.emit('prediction_result', {'result': 'Invalid IP format'})
            return

        if not (0 <= int(data['Src_Port']) <= 65535) or not (0 <= int(data['Dst_Port']) <= 65535):
            socketio.emit('prediction_result', {'result': 'Invalid port number'})
            return

        if int(data['Protocol']) not in [6, 17]:
            socketio.emit('prediction_result', {'result': 'Invalid protocol'})
            return

        input_data[1] = ipv4_to_int(input_data[1]) 
        input_data[3] = ipv4_to_int(input_data[3]) 

        prediction = predict_ddos(model, input_data)

        
        result = "Benign" if prediction == 'Benign' else "Ddos"
        socketio.emit('prediction_result', {'result': result})

            

    except Exception as e:
        socketio.emit('prediction_result', {'result': 'error'})


if __name__ == '__main__':
    socketio.run(app, debug=True)

