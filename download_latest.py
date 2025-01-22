from huggingface_hub import snapshot_download, model_info as hf_model_info
import os
import argparse
from tqdm import tqdm

class ModelDownloader:
    def __init__(self, base_dir="e:/ds"):
        self.base_dir = base_dir
        self.models_dir = os.path.join(base_dir, "models")

        # Available models
        self.available_models = {
            "deepseek-chat-7b": {
                "repo": "deepseek-ai/deepseek-llm-7b-chat",
                "dir": "deepseek-chat-7b",
                "size": "~15gb"
            },
            "deepseek-coder-33b": {
                "repo": "deepseek-ai/deepseek-coder-33b-base",
                "dir": "deepseek-coder-33b",
                "size": "~60gb"
            },
            "deepseek-coder-6.7b": {
                "repo": "deepseek-ai/deepseek-coder-6.7b-base",
                "dir": "deepseek-coder-6.7b",
                "size": "~15gb"
            },
            "deepseek-llm-7b": {
                "repo": "deepseek-ai/deepseek-llm-7b-base",
                "dir": "deepseek-llm-7b",
                "size": "~15gb"
            },
            "deepseek-r1-zero": {
                "repo": "deepseek-ai/deepseek-r1-zero",
                "dir": "deepseek-r1-zero",
                "size": "very large (~700gb or more)"
            },
            "deepseek-r1": {
                "repo": "deepseek-ai/deepseek-r1",
                "dir": "deepseek-r1",
                "size": "very large (~700gb or more)"
            },
            "deepseek-r1-distill-qwen-1.5b": {
                "repo": "qwen/qwen2.5-math-1.5b",
                "dir": "deepseek-r1-distill-qwen-1.5b",
                "size": "~1.5b"
            },
            "deepseek-r1-distill-qwen-7b": {
                "repo": "qwen/qwen2.5-math-7b",
                "dir": "deepseek-r1-distill-qwen-7b",
                "size": "~7b"
            },
            "deepseek-r1-distill-qwen-14b": {
                "repo": "qwen/qwen2.5-14b",
                "dir": "deepseek-r1-distill-qwen-14b",
                "size": "~14b"
            },
            "deepseek-r1-distill-qwen-32b": {
                "repo": "qwen/qwen2.5-32b",
                "dir": "deepseek-r1-distill-qwen-32b",
                "size": "~32b"
            },
            "deepseek-r1-distill-llama-70b": {
                "repo": "meta-llama/llama-3.3-70b-instruct",
                "dir": "deepseek-r1-distill-llama-70b",
                "size": "~70b"
            },
            "deepseek-r1-distill-llama-8b": {
                "repo": "meta-llama/llama-3.1-8b",
                "dir": "deepseek-r1-distill-llama-8b",
                "size": "~8b"
            }
        }

    def setup_directories(self):
        """Create necessary directories if they don't exist"""
        os.makedirs(self.models_dir, exist_ok=True)
        print(f"storage directory ready at: {self.models_dir}")

    def download_model(self, model_key):
        """Download a specific model"""
        if model_key not in self.available_models:
            print(f"error: {model_key} is not a valid model selection")
            return False

        model_data = self.available_models[model_key]
        model_dir = os.path.join(self.models_dir, model_data["dir"])

        print(f"\npreparing to download {model_key}")
        print(f"approximate size: {model_data['size']}")
        print(f"target directory: {model_dir}")

        try:
            snapshot_download(
                repo_id=model_data["repo"],
                local_dir=model_dir,
                local_dir_use_symlinks=False
            )
            print(f"\nsuccessfully downloaded {model_key}")
            return True
        except Exception as e:
            print(f"error downloading {model_key}: {e}")
            return False

    def get_latest_model_info(self, model_key):
        """Get the latest version and metadata for a model"""
        if model_key not in self.available_models:
            print(f"error: {model_key} is not a valid model selection")
            return

        model_data = self.available_models[model_key]
        print(f"\nchecking latest version for {model_key}...")
        try:
            info = hf_model_info(model_data["repo"])
            print(f"latest version: {info.sha}")
            print(f"last modified: {info.lastModified}")
            print(f"downloads: {info.downloads}")
        except Exception as e:
            print(f"error fetching model info: {e}")

def display_menu():
    """Display the main interactive menu"""
    print("\navailable models:")
    for index, (key, data) in enumerate(ModelDownloader().available_models.items(), 1):
        print(f"{index}. {key} ({data['size']})")
    print(f"{len(ModelDownloader().available_models) + 1}. get model info (without downloading)")
    print(f"{len(ModelDownloader().available_models) + 2}. exit")

def main():
    parser = argparse.ArgumentParser(description='download deepseek models')
    parser.add_argument('--model', type=str, choices=list(ModelDownloader().available_models.keys()),
                      help='which model to download')
    parser.add_argument('--info', type=str, choices=list(ModelDownloader().available_models.keys()),
                      help='get latest version and metadata for a model')

    args = parser.parse_args()

    downloader = ModelDownloader()

    if args.model:
        downloader.setup_directories()
        downloader.download_model(args.model)
    elif args.info:
        downloader.get_latest_model_info(args.info)
    else:
        while True:
            display_menu()
            choice = input("\nenter your choice: ").strip()
            try:
                choice = int(choice)
                if 1 <= choice <= len(downloader.available_models):
                    model_key = list(downloader.available_models.keys())[choice - 1]
                    downloader.setup_directories()
                    downloader.download_model(model_key)
                elif choice == len(downloader.available_models) + 1:
                    while True:
                        print("\nselect a model to get info:")
                        for index, key in enumerate(downloader.available_models.keys(), 1):
                            print(f"{index}. {key}")
                        print(f"{len(downloader.available_models) + 1}. back to main menu")
                        info_choice = input("\nenter your choice: ").strip()
                        try:
                            info_choice = int(info_choice)
                            if 1 <= info_choice <= len(downloader.available_models):
                                model_key = list(downloader.available_models.keys())[info_choice - 1]
                                downloader.get_latest_model_info(model_key)
                            elif info_choice == len(downloader.available_models) + 1:
                                break
                            else:
                                print("invalid choice, try again.")
                        except ValueError:
                            print("invalid input, enter a number.")
                elif choice == len(downloader.available_models) + 2:
                    print("exiting...")
                    break
                else:
                    print("invalid choice, try again.")
            except ValueError:
                print("invalid input, enter a number.")

if __name__ == "__main__":
    main()
