import os
from typing import List, Dict, Any
import requests

class HFSearchClient:
    """
    A client for interacting with the Hugging Face Hub for semantic search and discovery.
    """
    def __init__(self, api_token: str = None):
        self.api_token = api_token or os.getenv("HF_TOKEN")
        self.base_url = "https://huggingface.co/api"
        self.headers = {"Authorization": f"Bearer {self.api_token}"} if self.api_token else {}

    def search_models(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for models on the Hugging Face Hub.
        """
        params = {"search": query, "limit": limit, "sort": "downloads", "direction": -1}
        response = requests.get(f"{self.base_url}/models", params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_model_details(self, model_id: str) -> Dict[str, Any]:
        """
        Fetch detailed information for a specific model.
        """
        response = requests.get(f"{self.base_url}/models/{model_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_papers(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for research papers on the Hugging Face Hub.
        Note: This is a simplified representation of the paper search capability.
        """
        # In a real scenario, this might use a different endpoint or the MCP tool logic
        print(f"Searching for papers with query: {query}")
        return []

if __name__ == "__main__":
    client = HFSearchClient()
    try:
        results = client.search_models("bert", limit=3)
        for model in results:
            print(f"Model: {model.get('modelId')} | Downloads: {model.get('downloads')}")
    except Exception as e:
        print(f"Error: {e}")
