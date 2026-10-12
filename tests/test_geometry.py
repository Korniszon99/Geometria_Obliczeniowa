from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cartesian_left_right_and_segment_bounds():
    for point, message in [([0, 1], "lewej"), ([0, -1], "prawej"), ([0.5, 0], "na odcinku"), ([2, 0], "poza odcinkiem")]:
        response = client.post('/sprawdz-punkt', json={'A': [0,0], 'B': [1,0], 'P': point})
        assert response.status_code == 200
        data = response.json()
        assert message in data['message']
        assert data['roznica'] == 0

def test_invalid_points_are_rejected_without_server_error():
    for points in [{'A':[0], 'B':[1,0], 'P':[0,1]}, {'A':[0,0], 'B':[0,0], 'P':[0,1]}, {'A':['bad',0], 'B':[1,0], 'P':[0,1]}]:
        assert client.post('/sprawdz-punkt', json=points).status_code == 422

def test_index_and_random_points():
    assert client.get('/').status_code == 200
    data = client.get('/losuj-wspolrzedne').json()
    assert all(len(data[key]) == 2 for key in ['A','B','P'])
