import requests
import json

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_dogs_greyhound():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    print(result)
    assert type(result) is dict
    assert result['message']['greyhound'] == ['italian']

def test_dogs_germanshepard():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    print(result)
    assert type(result) is dict
    assert result['message']['germanshepherd'] == []