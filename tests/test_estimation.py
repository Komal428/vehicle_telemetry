
from tests.fixture import client
import json


def test_average_speed(client):
    client.get('/clear')
    data={
        "speed": 1,
        "heading": 0,
        "nottime":1
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b"Received invalid movement data. Make sure the data contains 'speed', 'heading' and 'time'" in res.data

    res = client.get('/kpis')
    data = res.get_json(silent=True)
    assert data['average_speed']==round(5/3,2)

def test_index(client):
    client.get('/clear')
    res = client.get('/')
    assert b'Vehicle estimation' in res.data
    

def test_average_speed(client):
    client.get('/clear')
    data={
        "speed": 1,
        "heading": 0,
        "time":1
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    data={
        "speed": 2,
        "heading": 0,
        "time":2
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    res = client.get('/kpis')
    data = res.get_json(silent=True)
    assert data['average_speed']==round(5/3,2)

def test_distance_driven(client):
    client.get('/clear')
    data={
        "speed": 1,
        "heading": 180,
        "time":2
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    data={
        "speed": 3,
        "heading": 0,
        "time":20
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    res = client.get('/kpis')
    data = res.get_json(silent=True)
    assert data['distance_driven']==62
    

def test_distance_from_start(client):
    client.get('/clear')

    data={
        "speed": 10,
        "heading": 0,
        "time":10
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    data={
        "speed": 5,
        "heading": 180,
        "time":10
    }
    res = client.post("/telemetry",data=json.dumps(data),content_type='application/json')
    assert b'Movement recorded' in res.data

    res = client.get('/kpis')
    data = res.get_json(silent=True)
    assert data['distance_from_start']==50


