import requests
import pytest

URL = 'https://api.pokemonbattle.ru'

def test_get_trainers():
    '''
    KTI-1. Get trainers
    '''
    response = requests.get(url=f'{URL}/v2/trainers', params={"trainer_id": 6917})
    assert response.status_code == 200, 'Expected status code 200, but got {response.status_code}'

def test_get_trainer_by_id():
    '''
    KTI-2. Get trainer by ID
    '''
    response = requests.get(url=f'{URL}/v2/trainers', params={"trainer_id": 6917})
    assert response.status_code == 200, 'Expected status code 200, but got {response.status_code}'
    
    json_response = response.json()
    
    assert "trainer_name" in json_response, 'Key "trainer_name" not found in response'
    
    assert json_response["trainer_name"] == "Raak", f'Expected "Raak", but got {json_response["trainer_name"]}'
