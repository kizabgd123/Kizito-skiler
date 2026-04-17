import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from search import HFSearchClient

def main():
    """
    Demonstrates the usage of the HFSearchClient for model discovery.
    """
    client = HFSearchClient()
    
    print("--- Searching for trending models ---")
    try:
        models = client.search_models("llama", limit=5)
        for model in models:
            model_id = model.get('modelId', 'Unknown')
            downloads = model.get('downloads', 0)
            likes = model.get('likes', 0)
            print(f"Model: {model_id:30} | Downloads: {downloads:10} | Likes: {likes:5}")
            
    except Exception as e:
        print(f"Failed to fetch models: {e}")

    print("\n--- Fetching details for a specific model ---")
    try:
        model_id = "google/gemma-2-9b-it"
        details = client.get_model_details(model_id)
        print(f"Model ID: {details.get('modelId')}")
        print(f"Task: {details.get('pipeline_tag')}")
        print(f"Library: {details.get('library_name')}")
        print(f"Last Modified: {details.get('lastModified')}")
        
    except Exception as e:
        print(f"Failed to fetch model details: {e}")

if __name__ == "__main__":
    main()
