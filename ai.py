import requests
import json
import argparse
import time
import os
from datetime import datetime
from dotenv import load_dotenv, set_key


class CLIA:
    def __init__(self):
        self.api_key = None
        self.env_file = ".env"
        self.conversation = []
        self.current_model = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
        self.models = [
            ("DeepSeek R1", "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"),
            ("Llama 3.3", "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"),
            ("Qwen3 32B FP8", "qwen-qwen3-32b-fp8-serverless"),
            ("AFM 4.5B", "arcee-ai/AFM-4.5B-Preview"),
            ("EXAONE 3.5 32B", "lgai/exaone-3-5-32b-instruct"),
            ("EXAONE Deep 32B", "lgai/exaone-deep-32b")
        ]
        self.session_start = datetime.now()
        self.message_count = 0
        self.model_usage = {}
        self.load_api_key()

    def load_api_key(self):
        try:
            load_dotenv(self.env_file)
            self.api_key = os.getenv('TOGETHER_API_KEY')

            if self.api_key:
                print("API key loaded from .env file!")
                return True
        except Exception as e:
            print(f"Warning: Could not load .env file: {e}")
        return False

    def ensure_api_key(self):
        if not self.api_key:
            print("\nAPI Key Required")
            print("=" * 40)
            print("Before we can start chatting, you need to provide your API key.")
            print("Get your free API key from: https://api.together.xyz/")
            print("=" * 40)

            while True:
                self.api_key = input("\nEnter your Together AI API key: ").strip()
                if self.api_key:
                    print("API key entered successfully!")

                    save_choice = input("Save API key to .env file for future use? (y/n): ").strip().lower()
                    if save_choice in ['y', 'yes']:
                        self.save_api_key()
                    return True
                else:
                    print("Please enter a valid API key.")
        return True

    def save_api_key(self):
        try:
            if not os.path.exists(self.env_file):
                with open(self.env_file, 'w') as f:
                    f.write("# CLIA - Command Line Intelligent Assistant Environment Variables\n")

            set_key(self.env_file, 'TOGETHER_API_KEY', self.api_key)
            print("API key saved to .env file!")
            print("Your API key is now stored securely in environment variables")
        except Exception as e:
            print(f"Warning: Could not save API key to .env: {e}")

    def reset_api_key(self):
        try:
            if 'TOGETHER_API_KEY' in os.environ:
                del os.environ['TOGETHER_API_KEY']

            if os.path.exists(self.env_file):
                with open(self.env_file, 'r') as f:
                    lines = f.readlines()

                with open(self.env_file, 'w') as f:
                    for line in lines:
                        if not line.startswith('TOGETHER_API_KEY='):
                            f.write(line)

            self.api_key = None
            print("API key reset! You'll be prompted for a new one.")
        except Exception as e:
            print(f"Error resetting API key: {e}")

    def get_api_key(self):
        if not self.api_key:
            print("\nAPI Key Setup Required")
            print("Get your free API key from: https://api.together.xyz/")
            print("=" * 50)

            while True:
                self.api_key = input("Enter your API key: ").strip()
                if self.api_key:
                    print("API key entered successfully!")

                    save_choice = input("Save API key for future use? (y/n): ").strip().lower()
                    if save_choice in ['y', 'yes']:
                        self.save_api_key()
                    break
                else:
                    print("Please enter a valid API key.")

        return self.api_key

    def send_message(self, prompt):
        if not self.get_api_key():
            return "No API key"

        self.conversation.append({"role": "user", "content": prompt})
        self.message_count += 1

        model_name = self.get_current_model_name()
        self.model_usage[model_name] = self.model_usage.get(model_name, 0) + 1

        try:
            print("Thinking...", end="", flush=True)
            start_time = time.time()

            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.current_model,
                    "messages": self.conversation,
                    "max_tokens": 1000,
                    "temperature": 0.7
                }
            )

            response_time = time.time() - start_time
            print(f"\rResponse time: {response_time:.2f}s")

            if response.status_code == 200:
                result = response.json()["choices"][0]["message"]["content"]
                self.conversation.append({"role": "assistant", "content": result})
                return result
            else:
                self.conversation.pop()
                return f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            self.conversation.pop()
            return f"Error: {e}"

    def show_models(self):
        print("\nAvailable AI Models:")
        print("=" * 50)
        for i, (name, model_id) in enumerate(self.models, 1):
            current = " <- CURRENT" if model_id == self.current_model else ""
            usage = self.model_usage.get(name, 0)
            usage_text = f" ({usage} messages)" if usage > 0 else ""
            print(f"{i}. {name}{usage_text}{current}")
        print("=" * 50)

    def change_model(self, model_number=None):
        if model_number is None:
            self.show_models()
            try:
                choice = input(f"Select model (1-{len(self.models)}) or 'q' to cancel: ").strip()
                if choice.lower() == 'q':
                    return
                model_number = int(choice)
            except ValueError:
                print("Invalid input")
                return

        if 1 <= model_number <= len(self.models):
            old_model = self.get_current_model_name()
            self.current_model = self.models[model_number - 1][1]
            new_model = self.get_current_model_name()
            print(f"Switched from {old_model} to {new_model}")
        else:
            print(f"Invalid choice. Please select 1-{len(self.models)}")

    def get_current_model_name(self):
        for name, model_id in self.models:
            if model_id == self.current_model:
                return name
        return "Unknown"

    def show_stats(self):
        session_time = datetime.now() - self.session_start
        print(f"\nSession Statistics:")
        print("=" * 30)
        print(f"Session Duration: {str(session_time).split('.')[0]}")
        print(f"Total Messages: {self.message_count}")
        print(f"Current Model: {self.get_current_model_name()}")
        print(f"Conversation Length: {len(self.conversation)} turns")

        if self.model_usage:
            print("\nModel Usage:")
            for model, count in self.model_usage.items():
                print(f"  • {model}: {count} messages")

    def save_conversation(self, filename=None):
        if not self.conversation:
            print("No conversation to save")
            return

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    "session_start": self.session_start.isoformat(),
                    "model_used": self.get_current_model_name(),
                    "conversation": self.conversation
                }, f, indent=2, ensure_ascii=False)
            print(f"Conversation saved to {filename}")
        except Exception as e:
            print(f"Failed to save: {e}")

    def chat(self):
        if not self.ensure_api_key():
            print("Cannot start chat without API key. Exiting...")
            return

        current_model = self.get_current_model_name()
        print(f"\nCLIA - Command Line Intelligent Assistant")
        print(f"Connecting to {current_model}")
        print("Commands: 'models', 'change [1-6]', 'stats', 'save', 'clear', 'help', 'quit'")
        print("=" * 60)

        while True:
            try:
                user_input = input(f"\n[{current_model}] You: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['quit', 'exit', 'q']:
                    self.show_stats()
                    save_choice = input("\nSave conversation before exit? (y/n): ").strip().lower()
                    if save_choice in ['y', 'yes']:
                        self.save_conversation()
                    print("Goodbye!")
                    break

                elif user_input.lower() == 'models':
                    self.show_models()

                elif user_input.lower().startswith('change'):
                    parts = user_input.split()
                    if len(parts) > 1 and parts[1].isdigit():
                        self.change_model(int(parts[1]))
                        current_model = self.get_current_model_name()
                    else:
                        self.change_model()
                        current_model = self.get_current_model_name()

                elif user_input.lower() == 'stats':
                    self.show_stats()

                elif user_input.lower() == 'save':
                    self.save_conversation()

                elif user_input.lower() == 'clear':
                    self.conversation = []
                    print("Conversation cleared!")

                elif user_input.lower() == 'help':
                    print("\nAvailable Commands:")
                    print("=" * 25)
                    print("• models         - Show available AI models")
                    print("• change [1-6]   - Change current model (optional number)")
                    print("• stats          - Show session statistics")
                    print("• save           - Save conversation to file")
                    print("• clear          - Clear conversation history")
                    print("• reset-key      - Change/reset your API key")
                    print("• help           - Show this help")
                    print("• quit           - Exit the assistant")

                elif user_input.lower() in ['reset-key', 'resetkey', 'key']:
                    self.reset_api_key()
                    current_model = self.get_current_model_name()

                else:
                    print(f"\n[{current_model}]: ", end="")
                    response = self.send_message(user_input)
                    print(response)

            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                break

    def single_prompt(self, prompt):
        if not self.ensure_api_key():
            print("Cannot process prompt without API key. Exiting...")
            return

        current_model = self.get_current_model_name()
        print(f"Using {current_model}")
        print("=" * 40)
        response = self.send_message(prompt)
        print(response)


def main():
    client = CLIA()

    parser = argparse.ArgumentParser(
        description="CLIA - Command Line Intelligent Assistant with Multi-Model Switching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai.py                         # Start interactive chat
  python ai.py -p "Hello world"        # Single prompt mode
  python ai.py -m 2 -p "Hello"         # Use specific model
  python ai.py --list-models           # Show all available models
        """
    )
    parser.add_argument("-p", "--prompt", help="Single prompt mode")
    parser.add_argument("-m", "--model", type=int, choices=range(1, len(client.models) + 1),
                       help=f"Select model (1-{len(client.models)})")
    parser.add_argument("--list-models", action="store_true",
                       help="List all available models and exit")

    args = parser.parse_args()

    if args.list_models:
        client.show_models()
        return

    if args.model:
        client.current_model = client.models[args.model - 1][1]
        model_name = client.models[args.model - 1][0]
        print(f"Using {model_name}")

    if args.prompt:
        client.single_prompt(args.prompt)
    else:
        client.chat()


if __name__ == "__main__":
    main()
