from huggingface_hub import snapshot_download, model_info as hf_model_info
import os
import argparse
from tqdm import tqdm

class ModelDownloader:
    def __init__(self, base_dir="E:/DS"):
        self.base_dir = base_dir
        self.models_dir = os.path.join(base_dir, "models")
        
        # Available models
        self.available_models = {
            "chat-7b": {
                "repo": "deepseek-ai/deepseek-llm-7b-chat",
                "dir": "deepseek-chat-7b",
                "size": "~15GB"
            },
            "coder-33b": {
                "repo": "deepseek-ai/deepseek-coder-33b-base",
                "dir": "deepseek-coder-33b",
                "size": "~60GB"
            },
            "coder-6.7b": {
                "repo": "deepseek-ai/deepseek-coder-6.7b-base",
                "dir": "deepseek-coder-6.7b",
                "size": "~15GB"
            },
            "llm-7b": {
                "repo": "deepseek-ai/deepseek-llm-7b-base",
                "dir": "deepseek-llm-7b",
                "size": "~15GB"
            }
        }

    def setup_directories(self):
        """Create necessary directories if they don't exist"""
        os.makedirs(self.models_dir, exist_ok=True)
        print(f"Storage directory ready at: {self.models_dir}")

    def download_model(self, model_key):
        """Download a specific model"""
        if model_key not in self.available_models:
            print(f"Error: {model_key} is not a valid model selection")
            return False

        model_data = self.available_models[model_key]
        model_dir = os.path.join(self.models_dir, model_data["dir"])
        
        print(f"\nPreparing to download {model_key}")
        print(f"Approximate size: {model_data['size']}")
        print(f"Target directory: {model_dir}")
        
        try:
            snapshot_download(
                repo_id=model_data["repo"],
                local_dir=model_dir,
                local_dir_use_symlinks=False
            )
            print(f"\nSuccessfully downloaded {model_key}")
            return True
        except Exception as e:
            print(f"Error downloading {model_key}: {e}")
            return False

    def get_latest_model_info(self, model_key):
        """Get the latest version and metadata for a model"""
        if model_key not in self.available_models:
            print(f"Error: {model_key} is not a valid model selection")
            return

        model_data = self.available_models[model_key]
        print(f"\nChecking latest version for {model_key}...")
        try:
            info = hf_model_info(model_data["repo"])
            print(f"Latest version: {info.sha}")
            print(f"Last modified: {info.lastModified}")
            print(f"Downloads: {info.downloads}")
        except Exception as e:
            print(f"Error fetching model info: {e}")

def display_menu():
    """Display the main interactive menu"""
    print("\nAvailable models:")
    print("1. deepseek-chat-7b (~15GB)")
    print("2. deepseek-coder-33b (~60GB)")
    print("3. deepseek-coder-6.7b (~15GB)")
    print("4. deepseek-llm-7b (~15GB)")
    print("5. Get model info (without downloading)")
    print("6. Exit")

def display_info_menu():
    """Display the submenu for selecting a model to get info on"""
    print("\nSelect a model to get info:")
    print("1. deepseek-chat-7b")
    print("2. deepseek-coder-33b")
    print("3. deepseek-coder-6.7b")
    print("4. deepseek-llm-7b")
    print("5. Back to main menu")

def main():
    parser = argparse.ArgumentParser(description='Download DeepSeek models')
    parser.add_argument('--model', type=str, choices=['chat-7b', 'coder-33b', 'coder-6.7b', 'llm-7b'],
                      help='Which model to download')
    parser.add_argument('--info', type=str, choices=['chat-7b', 'coder-33b', 'coder-6.7b', 'llm-7b'],
                      help='Get latest version and metadata for a model')
    
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
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                downloader.setup_directories()
                downloader.download_model("chat-7b")
            elif choice == "2":
                downloader.setup_directories()
                downloader.download_model("coder-33b")
            elif choice == "3":
                downloader.setup_directories()
                downloader.download_model("coder-6.7b")
            elif choice == "4":
                downloader.setup_directories()
                downloader.download_model("llm-7b")
            elif choice == "5":
                while True:
                    display_info_menu()
                    info_choice = input("\nEnter your choice (1-5): ").strip()
                    
                    if info_choice == "1":
                        downloader.get_latest_model_info("chat-7b")
                    elif info_choice == "2":
                        downloader.get_latest_model_info("coder-33b")
                    elif info_choice == "3":
                        downloader.get_latest_model_info("coder-6.7b")
                    elif info_choice == "4":
                        downloader.get_latest_model_info("llm-7b")
                    elif info_choice == "5":
                        break  # Go back to the main menu
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()