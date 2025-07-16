# 🤖 CLIA - Command Line Intelligent Assistant

A powerful and intuitive command-line AI assistant that brings multiple state-of-the-art AI models to your terminal. Built with Python and powered by Together AI, CLIA offers seamless interaction with cutting-edge language models through an elegant CLI interface.

## ✨ Key Features

### 🔄 **Multi-Model AI Support**
- **6 Advanced AI Models** including DeepSeek R1, Llama 3.3, EXAONE, and more
- **Instant model switching** with simple commands
- **Real-time performance tracking** for each model
- **Smart response time monitoring** and usage analytics

### 🛠️ **Advanced Workspace Management**
- **Integrated file operations** (read, write, execute Python files)
- **AI-powered file creation** with intelligent content generation
- **Clean workspace organization** in dedicated directory
- **Seamless file manipulation** through chat commands

### 📊 **Intelligent Session Management**
- **Conversation persistence** with JSON export functionality
- **Comprehensive session analytics** and usage statistics
- **Response time monitoring** across all interactions
- **Model usage tracking** for optimization insights

### 🎯 **Flexible Interaction Modes**
- **Interactive chat mode** for extended conversations with context
- **Single prompt mode** for quick queries and automation
- **Command-line argument support** for scripting
- **File-based AI operations** for content generation

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+**
- **Together AI API key** ([Get yours free here](https://api.together.xyz/))

### Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/CodemHax/CLIA
   cd CLIA
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch CLIA**:
   ```bash
   python ai.py
   ```

4. **Enter your API key** when prompted (automatically saved for future use)

## 🎮 Usage Examples

### Interactive Chat Mode
```bash
python ai.py
```
Start an intelligent conversation with context-aware responses and full command access.

### Quick AI Query
```bash
python ai.py -p "Explain quantum computing in simple terms"
```

### Use Specific Model
```bash
python ai.py -m 1 -p "Write a Python function to sort a list"
```

### List All Available Models
```bash
python ai.py --list-models
```

## 🧠 Available AI Models

| # | Model Name | Specialization | Best For |
|---|------------|---------------|----------|
| 1 | **DeepSeek R1 Distill** | Advanced reasoning & problem-solving | Complex analysis, mathematics, coding |
| 2 | **DeepSeek R1** | Latest reasoning capabilities | Advanced problem solving, research |
| 3 | **Llama 3.3** | General-purpose conversation | Versatile tasks, creative writing |
| 4 | **AFM 4.5B** | Fast, efficient responses | Quick queries, simple tasks |
| 5 | **EXAONE 3.5 32B** | Advanced language understanding | Natural conversation, explanations |
| 6 | **EXAONE Deep 32B** | Deep learning capabilities | Research, complex reasoning tasks |

## 🎛️ Interactive Commands

### Core Commands
| Command | Description | Example |
|---------|-------------|---------|
| `models` | Show all available AI models | `models` |
| `switch [1-6]` | Switch to specific model | `switch 2` |
| `stats` | Display detailed session statistics | `stats` |
| `save [filename]` | Save conversation to JSON file | `save my_chat` |
| `clear` | Clear current conversation history | `clear` |
| `help` | Show comprehensive help menu | `help` |
| `quit` / `exit` / `q` | Exit CLIA gracefully | `quit` |

### File Operations
| Command | Description | Example |
|---------|-------------|---------|
| `read <file>` | Read file from workspace | `read script.py` |
| `write <file>` | Create/edit file in workspace | `write app.py` |
| `run <file>` | Execute Python file | `run my_script.py` |
| `list` | List all workspace files | `list` |

### AI-Powered Creation
| Command | Description | Example |
|---------|-------------|---------|
| `create` | AI generates custom files based on description | `create` |
| `reset-key` | Reset stored API key | `reset-key` |

## 📁 Project Structure

```
AiCli/
├── ai.py                         # Main CLIA application (clean, comment-free)
├── requirements.txt              # Python dependencies
├── README.md                     # This documentation
├── .env                         # Secure API key storage (auto-created)
├── workspace/                   # AI workspace directory
│   ├── *.py                    # Python scripts
│   ├── *.html                  # Web files
│   └── ...                     # Other generated/user files
└── conversation_*.json          # Saved conversation exports
```

## 🔧 Configuration & Setup

### API Key Management
CLIA automatically handles secure API key storage:
- **First run**: Prompts for API key and saves to `.env` file
- **Subsequent runs**: Automatically loads key from environment
- **Reset key**: Use `reset-key` command anytime to update

### Model Customization
Easily modify available models by editing the `models` list in `ai.py`:
```python
self.models = [
    ("Custom Model Name", "model-identifier"),
    # Add your preferred models here
]
```

## 📋 Command Line Arguments

```bash
python ai.py [OPTIONS]

Options:
  -p, --prompt TEXT       Execute single prompt and exit
  -m, --model [1-6]       Select specific model (1-6)
  --list-models          Display all available models and exit
  -h, --help             Show help message and exit
```

## 💡 Real-World Examples

### AI-Powered Code Generation
```bash
[DeepSeek R1 Distill]: create
Describe the file you want to create: Create a REST API for user management with FastAPI
🤖 AI is generating file content...
Generation time: 2.35s
Enter filename for the generated content: user_api.py
Show generated content? (y/n): y
Save to file? (y/n): y
✓ File saved to workspace/user_api.py
```

### File Operations Workflow
```bash
[DeepSeek R1 Distill]: write hello.py
Enter content for hello.py. End with 'EOF' on a new line.
print("Hello, CLIA!")
print("AI-powered development made easy!")
EOF
File saved to workspace/hello.py

[DeepSeek R1 Distill]: run hello.py

Output:
Hello, CLIA!
AI-powered development made easy!
```

### Quick Problem Solving
```bash
python ai.py -p "Optimize this Python code for better performance: [code snippet]"
Using DeepSeek R1 Distill
Thinking...
Response time: 1.24s
Here are several optimizations for your code...
```

## 🛠️ Advanced Features

### Smart Content Processing
- **Automatic cleaning** of AI thinking tags (`<think>`, `<thought>`)
- **Clean code generation** without markdown formatting
- **File path comment removal** for production-ready output
- **Streamlined responses** for better readability

### Session Analytics
```bash
[DeepSeek R1 Distill]: stats

📊 Session Statistics:
==============================
Session Duration: 0:25:18
Total Messages: 42
Current Model: DeepSeek R1 Distill
Conversation Length: 84 turns

📈 Model Usage:
  • DeepSeek R1 Distill: 28 messages
  • Llama 3.3: 10 messages
  • AFM 4.5B: 4 messages
```

## 📜 License

This project is open source and available under the **MIT License**. Feel free to use, modify, and distribute according to the license terms.

## 🆘 Troubleshooting

### Common Issues & Solutions

**"No API key" Error**
```bash
# Reset your API key
python ai.py
[Model]: reset-key
Enter your Together AI API key: [paste-key-here]
```

**Model Not Responding**
- Verify internet connection stability
- Check API key validity at https://api.together.xyz/
- Try switching models: `switch [1-6]`
- Check Together AI service status

**File Operations Failing**
- Ensure Python has write permissions in project directory
- Verify workspace directory exists (auto-created on first run)
- Check file paths are relative to workspace
- Confirm Python files have valid syntax for execution

**Performance Issues**
- Try faster models (AFM 4.5B) for simple queries
- Use `clear` command to reset conversation context
- Monitor response times with built-in timing

### Getting Support

1. **Check error messages** - they often contain specific solutions
2. **Try different models** - each excels at different task types
3. **Use `help` command** for quick command reference
4. **Review session stats** to identify usage patterns
5. **Restart CLIA** if persistent issues occur




