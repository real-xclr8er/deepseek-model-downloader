# DeepSeek Model Downloader

A Python utility for downloading and managing DeepSeek AI models from Hugging Face Hub. This tool simplifies the process of downloading large language models while providing version tracking and storage management features.

## Features

- Download multiple DeepSeek models with size verification
- Track latest model versions and updates
- View model metadata including download statistics
- Interactive CLI menu for ease of use
- Command-line arguments for automation
- Progress tracking during downloads
- Automatic directory management

## Available Models

| Model Name | Size | Description |
|------------|------|-------------|
| deepseek-chat-7b | ~15GB | Chat-optimized 7B parameter model |
| deepseek-coder-33b | ~60GB | Code-specialized 33B parameter model |
| deepseek-coder-6.7b | ~15GB | Lightweight code model |
| deepseek-llm-7b | ~15GB | Base 7B parameter model |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/deepseek-model-downloader.git
cd deepseek-model-downloader
```

2. Install dependencies:
```bash
pip install huggingface_hub tqdm
```

## Usage

### Interactive Mode
Run the script without arguments to use the interactive menu:
```bash
python download_latest.py
```

### Command Line Arguments
Download a specific model:
```bash
python download_latest.py --model chat-7b
```

Get model information:
```bash
python download_latest.py --info chat-7b
```

## Storage Requirements

Ensure you have sufficient disk space available:
- Minimum 15GB for individual 7B models
- 60GB for the coder-33b model
- Additional space for temporary files during download

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
