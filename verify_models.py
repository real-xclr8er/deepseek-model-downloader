import os
import hashlib

# Path to models directory (default set to match the downloader)
MODELS_DIR = "e:/ds/models"

# List of models and their expected files
EXPECTED_MODELS = {
    "deepseek-chat-7b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-coder-33b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-coder-6.7b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-llm-7b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-zero": ["config.json", "model-00001-of-00005.safetensors"],
    "deepseek-r1": ["config.json", "model-00001-of-00005.safetensors"],
    "deepseek-r1-distill-qwen-1.5b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-distill-qwen-7b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-distill-qwen-14b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-distill-qwen-32b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-distill-llama-70b": ["config.json", "pytorch_model.bin", "tokenizer.json"],
    "deepseek-r1-distill-llama-8b": ["config.json", "pytorch_model.bin", "tokenizer.json"]
}

def calculate_checksum(file_path):
    """Calculate SHA256 checksum for a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error calculating checksum for {file_path}: {e}")
        return None

def verify_model_files():
    """Verify the existence and integrity of expected model files."""
    for model_name, files in EXPECTED_MODELS.items():
        model_path = os.path.join(MODELS_DIR, model_name)

        if not os.path.exists(model_path):
            print(f"[ERROR] Model directory not found: {model_name}")
            continue

        print(f"\nVerifying files for model: {model_name}")
        for file_name in files:
            file_path = os.path.join(model_path, file_name)

            if os.path.exists(file_path):
                checksum = calculate_checksum(file_path)
                if checksum:
                    print(f"  [OK] {file_name} - SHA256: {checksum}")
                else:
                    print(f"  [WARN] {file_name} - Checksum could not be calculated")
            else:
                print(f"  [MISSING] {file_name}")

def main():
    print(f"Verifying models in directory: {MODELS_DIR}")
    verify_model_files()

if __name__ == "__main__":
    main()
