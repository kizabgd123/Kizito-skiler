import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from search import HFSearchClient

def test_client_initialization():
    """
    Test that the client initializes correctly with and without a token.
    """
    client_no_token = HFSearchClient()
    assert client_no_token.api_token is None
    assert client_no_token.headers == {}

    client_with_token = HFSearchClient(api_token="test_token")
    assert client_with_token.api_token == "test_token"
    assert client_with_token.headers == {"Authorization": "Bearer test_token"}

@patch('requests.get')
def test_search_models(mock_get):
    """
    Test the search_models method with a mocked response.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = [{"modelId": "test-model", "downloads": 100}]
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    client = HFSearchClient()
    results = client.search_models("test-query", limit=1)

    assert len(results) == 1
    assert results[0]["modelId"] == "test-model"
    assert results[0]["downloads"] == 100
    mock_get.assert_called_once()

@patch('requests.get')
def test_get_model_details(mock_get):
    """
    Test the get_model_details method with a mocked response.
    """
    mock_response = MagicMock()
    mock_response.json.return_value = {"modelId": "test-model", "pipeline_tag": "text-generation"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    client = HFSearchClient()
    details = client.get_model_details("test-model")

    assert details["modelId"] == "test-model"
    assert details["pipeline_tag"] == "text-generation"
    mock_get.assert_called_once()
