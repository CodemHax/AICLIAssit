import requests
import json
import argparse
import time
import os
import re
import subprocess
from datetime import datetime
from dotenv import load_dotenv, set_key


class CLIA:
    def __init__(self):
        self.api_key = None
        self.env_file = ".env"
        self.workspace = "workspace"
        os.makedirs(self.workspace, exist_ok=True)

        self.conversation = []
        self.current_model = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
        self.models = [
            ("DeepSeek R1 Distill", "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"),
            ("DeepSeek R1 ", "deepseek-ai/DeepSeek-R1-0528"),
            ("Llama 3.3", "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"),
            ("AFM 4.5B", "arcee-ai/AFM-4.5B-Preview"),
            ("EXAONE 3.5 32B", "lgai/exaone-3-5-32b-instruct"),
            ("EXAONE Deep 32B", "lgai/exaone-deep-32b")
        ]
        self.session_start = datetime.now()
        self.message_count = 0
        self.model_usage = {}
        self.load_api_key()

    def _full_path(self, filename):
        return os.path.join(self.workspace, filename)

    def write_file(self, filename):
        filepath = self._full_path(filename)
        print(f"Enter content for {filename}. End with 'EOF' on a new line.")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "EOF":
                break
            lines.append(line)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            print(f"File saved to {filepath}")
        except Exception as e:
            print(f"Error writing file: {e}")

    def read_file(self, filename):
        filepath = self._full_path(filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                print(f"\nContent of {filename}:\n{'='*40}")
                print(f.read())
        except Exception as e:
            print(f"Error reading file: {e}")

    def run_file(self, filename):
        filepath = self._full_path(filename)
        try:
            result = subprocess.run(['python', filepath], capture_output=True, text=True)
            print(f"\nOutput:\n{result.stdout}")
            if result.stderr:
                print(f"Errors:\n{result.stderr}")
        except Exception as e:
            print(f"Error running file: {e}")

    def list_files(self):
        try:
            print("\nFiles in workspace directory:")
            for f in os.listdir(self.workspace):
                print(f)
        except Exception as e:
            print(f"Error listing files: {e}")

    def load_api_key(self):
        try:
            load_dotenv(self.env_file)
            self.api_key = os.getenv('TOGETHER_API_KEY')
            if self.api_key:
                print("API key loaded from .env file")
                return True
        except Exception as e:
            print(f"Could not load .env file: {e}")
        return False

    def ensure_api_key(self):
        if not self.api_key:
            print("\nAPI Key Required")
            print("=" * 40)
            print("Get your free API key from: https://api.together.xyz/")
            print("=" * 40)

            while True:
                self.api_key = input("\nEnter your Together AI API key: ").strip()
                if self.api_key:
                    print("API key entered successfully")

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
                    f.write("# CLIA environment variables\n")
            set_key(self.env_file, 'TOGETHER_API_KEY', self.api_key)
            print("API key saved to .env file")
        except Exception as e:
            print(f"Could not save API key: {e}")

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
            print("API key reset")
        except Exception as e:
            print(f"Error resetting API key: {e}")

    def get_api_key(self):
        if not self.api_key:
            print("API Key Setup Required")
            while True:
                self.api_key = input("Enter your API key: ").strip()
                if self.api_key:
                    print("API key entered")
                    save_choice = input("Save API key? (y/n): ").strip().lower()
                    if save_choice in ['y', 'yes']:
                        self.save_api_key()
                    break
                else:
                    print("Enter a valid API key")
        return self.api_key

    @staticmethod
    def clean_thinking_text(text):
        cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.IGNORECASE | re.DOTALL)
        cleaned = re.sub(r'<thought>.*?</thought>', '', cleaned, flags=re.IGNORECASE | re.DOTALL)
        cleaned = re.sub(r'</thought>', '', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'</think>', '', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
        return cleaned.strip()

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
                result = self.clean_thinking_text(result)
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
                choice = input(f"Select model (1-{len(self.models)}): ").strip()
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
            print(f"Invalid choice. Select 1-{len(self.models)}")

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
                print(f"  {model}: {count} messages")

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

    #def get_workspace_context(self):
    # context = []
    #     try:
    #         files = os.listdir(self.workspace)
    #         context.append(f"Workspace contains {len(files)} files:")
    #
    #         for filename in files:
    #             filepath = self._full_path(filename)
    #             if os.path.isfile(filepath):
    #                 try:
    #                     _, ext = os.path.splitext(filename)
    #                     context.append(f"- {filename} ({ext or 'no extension'})")
    #
    #                     if os.path.getsize(filepath) < 2048:
    #                         with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    #                             content = f.read()
    #                             if len(content) < 500:
    #                                 context.append(f"  Content preview: {content[:200]}...")
    #                 except Exception:
    #                     context.append(f"- {filename} (binary or unreadable)")
    #
    #     except Exception as e:
    #         context.append(f"Error reading workspace: {e}")
    #
    #     return "\n".join(context)

    def ai_create_file(self, description, filename=None):
        if not self.get_api_key():
            print("API key required for AI file creation")
            return

        prompt = f"""You are a coding assistant. Create a file based on the following description.
USER REQUEST: {description}

IMPORTANT RULES:
- Output ONLY executable code, no explanations, comments, or markdown
- Do NOT include ```python, ```html, or any code block markers
- Do NOT include file paths or comments like "// filepath:"
- Do NOT add explanatory text before or after the code
- Generate clean, working code that can be saved and run directly
- If it's a Python file, start directly with imports or code
- If it's HTML, start directly with <!DOCTYPE html>
- If it's CSS, start directly with selectors

Please generate the complete, working file content:"""

        try:
            print("AI is generating file content...", end="", flush=True)
            start_time = time.time()

            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.current_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 2000,
                    "temperature": 0.2
                }
            )

            response_time = time.time() - start_time
            print(f"\rGeneration time: {response_time:.2f}s")

            if response.status_code == 200:
                file_content = response.json()["choices"][0]["message"]["content"].strip()
                file_content = self.clean_thinking_text(file_content)

                if file_content.startswith('```'):
                    lines = file_content.split('\n')
                    if lines[0].startswith('```'):
                        lines = lines[1:]
                    if lines and lines[-1].strip() == '```':
                        lines = lines[:-1]
                    file_content = '\n'.join(lines)

                lines = file_content.split('\n')
                cleaned_lines = []
                for line in lines:
                    if not (line.strip().startswith('// filepath:') or
                           line.strip().startswith('# filepath:') or
                           line.strip().startswith('<!-- filepath:')):
                        cleaned_lines.append(line)

                file_content = '\n'.join(cleaned_lines).strip()

                if not filename:
                    filename = input("Enter filename for the generated content: ").strip()
                    if not filename:
                        print("No filename provided, canceling file creation")
                        return

                show_content = input("Show generated content? (y/n): ").strip().lower()
                if show_content in ['y', 'yes']:
                    print(f"\nGenerated content:\n{'='*50}")
                    print(file_content)
                    print('='*50)

                save_choice = input("Save to file? (y/n): ").strip().lower()
                if save_choice in ['y', 'yes']:
                    filepath = self._full_path(filename)
                    try:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(file_content)
                        print(f"File saved to {filepath}")
                    except Exception as e:
                        print(f"Error saving file: {e}")
                else:
                    print("File not saved")
            else:
                print(f"Error generating content: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Error: {e}")

    def single_prompt(self, prompt):
        if not self.ensure_api_key():
            print("Cannot process prompt without API key. Exiting...")
            return
        current_model = self.get_current_model_name()
        print(f"Using {current_model}")
        print("=" * 40)
        response = self.send_message(prompt)
        print(response)

    def chat(self):
        print("CLIA - Command Line Intelligent Assistant")
        print("=" * 50)
        print("Commands:")
        print("  help             - Show this help message")
        print("  models           - Show available models")
        print("  switch [num]     - Switch to model number")
        print("  stats            - Show session statistics")
        print("  save [filename]  - Save conversation")
        print("  clear            - Clear conversation")
        print("  write <file>     - Create file manually")
        print("  read <file>      - Read file")
        print("  run <file>       - Run Python file")
        print("  list             - List workspace files")
        print("  create           - AI assisted file creation")
        print("  reset-key        - Reset API key")
        print("  quit             - Exit program")
        print("=" * 50)

        while True:
            try:
                current_model = self.get_current_model_name()
                user_input = input(f"\n[{current_model}]: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif user_input == 'help' or user_input.startswith('/help'):
                    print("\nCommands:")
                    print("  help             - Show this help message")
                    print("  models           - Show available models")
                    print("  switch [num]     - Switch to model number")
                    print("  stats            - Show session statistics")
                    print("  save [filename]  - Save conversation")
                    print("  clear            - Clear conversation")
                    print("  write <file>     - Create file manually")
                    print("  read <file>      - Read file")
                    print("  run <file>       - Run Python file")
                    print("  list             - List workspace files")
                    print("  create           - AI assisted file creation")
                    print("  reset-key        - Reset API key")
                    print("  quit             - Exit program")
                elif user_input == 'models' or user_input.startswith('/models'):
                    self.show_models()
                elif user_input.startswith('switch') or user_input.startswith('/switch'):
                    parts = user_input.split()
                    if len(parts) == 2 and parts[1].isdigit():
                        self.change_model(int(parts[1]))
                    else:
                        self.change_model()
                elif user_input == 'stats' or user_input.startswith('/stats'):
                    self.show_stats()
                elif user_input.startswith('save') or user_input.startswith('/save'):
                    parts = user_input.split(maxsplit=1)
                    filename = parts[1] if len(parts) > 1 else None
                    self.save_conversation(filename)
                elif user_input == 'clear' or user_input.startswith('/clear'):
                    self.conversation = []
                    print("Conversation cleared")
                elif user_input.startswith('write') or user_input.startswith('/write'):
                    parts = user_input.split(maxsplit=1)
                    if len(parts) > 1:
                        self.write_file(parts[1])
                    else:
                        filename = input("Enter filename: ").strip()
                        if filename:
                            self.write_file(filename)
                elif user_input.startswith('read') or user_input.startswith('/read'):
                    parts = user_input.split(maxsplit=1)
                    if len(parts) > 1:
                        self.read_file(parts[1])
                    else:
                        filename = input("Enter filename: ").strip()
                        if filename:
                            self.read_file(filename)
                elif user_input.startswith('run') or user_input.startswith('/run'):
                    parts = user_input.split(maxsplit=1)
                    if len(parts) > 1:
                        self.run_file(parts[1])
                    else:
                        filename = input("Enter filename: ").strip()
                        if filename:
                            self.run_file(filename)
                elif user_input == 'list' or user_input.startswith('/list'):
                    self.list_files()
                elif user_input == 'create' or user_input.startswith('/ai-create'):
                    description = input("Describe the file you want to create: ").strip()
                    if description:
                        self.ai_create_file(description)
                elif user_input == 'reset-key' or user_input.startswith('/reset-key'):
                    self.reset_api_key()
                else:
                    response = self.send_message(user_input)
                    print(response)

            except KeyboardInterrupt:
                print("\nInterrupted. Goodbye.")
                break

    def res(self, prompt):
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
        description="CLIA - Command Line Intelligent Assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai.py                   # Start interactive chat
  python ai.py -p "Hello world"  # Single prompt mode
  python ai.py -m 2 -p "Hello"   # Use specific model
  python ai.py --list-models     # List models
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
