from flask import Flask
from flask import request, Response
from vehicle import Vehicle
import os
import pandas as pd

app = Flask(__name__)

vehicle = Vehicle()

@app.route('/')
def index():
    return 'Vehicle estimation'

@app.route('/telemetry', methods=['POST'])
def record_movement():
    data = request.get_json(silent=True)
    if set(['speed','heading','time']).issubset(data):
        print('--------------------', data)

        filtered_data = dict((k, data[k]) for k in ('speed', 'heading', 'time'))
        vehicle.record_movement(filtered_data)
        return 'Movement recorded'
    else:
        return "Received invalid movement data. Make sure the data contains 'speed', 'heading' and 'time' "
    return(data)

@app.route('/kpis', methods=['GET'])
def get_estimat():
    results = {
        'average_speed':vehicle.average_speed,
        'distance_driven':vehicle.distance_driven,
        'distance_from_start':vehicle.distance_from_start
    }
    return results

@app.route('/download', methods=['GET'])
def download():
    data = vehicle.get_movements_data()
    df = pd.DataFrame(data)
    return Response(
       df.to_csv(),
       mimetype="text/csv",
       headers={"Content-disposition":
       "attachment; filename=telemetry_data.csv"})

@app.route('/clear', methods=['GET'])
def _clear():
    global vehicle
    vehicle = Vehicle()

@app.route('/health', methods=['GET'])
def health_check():
    return f'SERVICE RUNNING OK - Movements recorded: {len(vehicle.get_movements_data())}'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)