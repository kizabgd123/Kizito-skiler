# Hugging Face Semantic Search & Discovery

A production-quality Python interface for interacting with the Hugging Face Hub, designed for semantic search, model discovery, and technical metadata retrieval.

## 🚀 Features

- **Model Discovery**: Search for models based on tasks, libraries, and popularity.
- **Technical Metadata**: Retrieve detailed information about model architectures, parameter counts, and live inference providers.
- **Research Paper Access**: Interface for discovering machine learning research papers.
- **Modular Design**: Clean, extensible code structure following best practices.

## 📁 Project Structure

```text
hf-semantic-search/
├── src/                # Core source code
│   └── search.py       # HFSearchClient implementation
├── examples/           # Usage examples
│   └── usage_example.py
├── tests/              # Unit and integration tests
├── docs/               # Documentation and guides
├── requirements.txt    # Project dependencies
├── LICENSE             # MIT License
└── README.md           # Project overview
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kizito-skiler/hf-semantic-search.git
   cd hf-semantic-search
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Set up Hugging Face Token**:
   Create a `.env` file or export your token:
   ```bash
   export HF_TOKEN="your_huggingface_token_here"
   ```

## 📖 Usage Example

```python
from src.search import HFSearchClient

client = HFSearchClient()

# Search for trending models
models = client.search_models("llama", limit=5)
for model in models:
    print(f"Model: {model['modelId']} | Downloads: {model['downloads']}")

# Get detailed metadata for a specific model
details = client.get_model_details("google/gemma-2-9b-it")
print(f"Task: {details['pipeline_tag']}")
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
