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

        filtered_data = dict((k, data[k]) for k in ('speed', 'heading', 'time'))
        vehicle.record_movement(filtered_data)
        return 'Movement recorded'
    else:
        return "Received invalid movement data. Make sure the data contains 'speed', 'heading' and 'time' "
    return(data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
