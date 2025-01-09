import os
import hashlib
import json
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    """Calculate the hash of a file."""
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def verify_model_integrity(model_path):
    """Verify the integrity of a model by checking its files and hashes."""
    print(f"Verifying model at: {model_path}")

    # Load the model configuration
    try:
        config = AutoConfig.from_pretrained(model_path)
        print("Model configuration loaded successfully.")
    except Exception as e:
        print(f"Error loading model configuration: {e}")
        return False

    # Check for required files
    required_files = ["config.json", "tokenizer.json", "tokenizer_config.json"]
    if config.model_type == "gpt2":
        required_files.extend(["pytorch_model.bin", "vocab.json", "merges.txt"])
    elif config.model_type == "deepseek-coder":
        # Add files specific to deepseek-coder models
        required_files.extend(["model.safetensors.index.json", "pytorch_model.bin.index.json"])

    missing_files = []
    for file in required_files:
        file_path = os.path.join(model_path, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    if missing_files:
        print(f"Missing files: {missing_files}")
        return False
    else:
        print("All required files are present.")

    # Verify file integrity (optional: compare hashes)
    print("Verifying file integrity...")
    for file in required_files:
        file_path = os.path.join(model_path, file)
        file_hash = calculate_file_hash(file_path)
        print(f"{file}: {file_hash}")

    # Verify split model files
    if config.model_type == "deepseek-coder":
        print("Verifying split model files...")
        index_file = os.path.join(model_path, "model.safetensors.index.json")
        if os.path.exists(index_file):
            with open(index_file, "r") as f:
                index_data = json.load(f)
                for weight_file in index_data["weight_map"].values():
                    weight_path = os.path.join(model_path, weight_file)
                    if not os.path.exists(weight_path):
                        print(f"Missing weight file: {weight_file}")
                        return False
                    else:
                        print(f"Found weight file: {weight_file}")

    return True

def main():
    # Path to your models directory
    models_dir = "E:/DS/models"

    # Iterate through each model in the directory
    for model_name in os.listdir(models_dir):
        model_path = os.path.join(models_dir, model_name)
        if os.path.isdir(model_path):
            print(f"\nChecking model: {model_name}")
            if verify_model_integrity(model_path):
                print("Model is complete and valid.")
            else:
                print("Model is incomplete or invalid.")
        else:
            print(f"Skipping non-directory: {model_name}")

if __name__ == "__main__":
    main()