from dotenv import find_dotenv, load_dotenv
import todo_app.app as app 
import pytest
from unittest.mock import patch, Mock

@pytest.fixture
def client():
 # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
 # Create the new app.
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')
    assert 'Test' in response.data.decode()

def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/N46znsdT/cards':
        response = Mock()

        response.json.return_value = [{"id":'60f6b47a3e8f8e45325c31e4', "idList": '60c73323b5d71d7a754a20fc', "name": 'Test'}]
        return response
    return None