# DeepSeek Model Downloader

This Python script facilitates downloading and managing models from Hugging Face repositories. It is designed to simplify the process of fetching DeepSeek models and their metadata.

## Features
- **Interactive Menu**: Select and download models from a predefined list.
- **Command-line Options**: Download a specific model or fetch metadata using arguments.
- **Automatic Directory Setup**: Ensures storage directories exist before downloading.
- **Model Metadata Retrieval**: Check the latest version, modification date, and download count for any model.

## Prerequisites
- **Python 3.7 or later**
- **Dependencies**:
  - `huggingface_hub`
  - `tqdm`

Install dependencies using pip:
```bash
pip install huggingface_hub tqdm
```

## Usage

### Run the script interactively
To display the interactive menu:
```bash
python download_latest.py
```

### Command-line arguments
#### Download a specific model
```bash
python download_latest.py --model <model_key>
```
Example:
```bash
python download_latest.py --model deepseek-chat-7b
```

#### Fetch model metadata
```bash
python download_latest.py --info <model_key>
```
Example:
```bash
python download_latest.py --info deepseek-chat-7b
```

## Models Available
The following models can be downloaded:
- **deepseek-chat-7b** (~15GB)
- **deepseek-coder-33b** (~60GB)
- **deepseek-coder-6.7b** (~15GB)
- **deepseek-llm-7b** (~15GB)
- **deepseek-r1-zero** (Very Large ~700GB or more)
- **deepseek-r1** (Very Large ~700GB or more)
- **deepseek-r1-distill-qwen-1.5b** (~1.5B)
- **deepseek-r1-distill-qwen-7b** (~7B)
- **deepseek-r1-distill-qwen-14b** (~14B)
- **deepseek-r1-distill-qwen-32b** (~32B)
- **deepseek-r1-distill-llama-70b** (~70B)
- **deepseek-r1-distill-llama-8b** (~8B)

## Project Structure
```
.
├── download_latest.py   # Main script
├── models/              # Downloaded models are stored here
└── README.md            # Documentation (this file)
```

## Customization
- **Default Storage Path**: Update the `base_dir` attribute in the `ModelDownloader` class to change where models are stored (default: `e:/ds`).
- **Adding Models**: Add new models to the `available_models` dictionary with their respective details.

## Notes
- Ensure sufficient disk space for large models.
- The script creates directories automatically if they do not exist.

## License
This script is provided "as is" without warranty of any kind. Modify and use it as needed for your projects.

