# 🤖 CLIA - Command Line Intelligent Assistant

A powerful and intuitive command-line AI assistant that brings multiple AI models to your terminal. Built with Python and powered by Together AI, CLIA offers seamless interaction with cutting-edge language models through an elegant CLI interface.

## ✨ Key Features

### 🔄 **Multi-Model AI Support**
- **AI Models** including DeepSeek R1, Llama 3.3, and more
- **Instant model switching** with simple commands
- **Real-time performance tracking** for each model
- **Smart model recommendations** based on task type

### 🛠️ **Advanced Workspace Management**
- **Integrated file operations** (read, write, execute)
- **AI-powered file creation** with intelligent templates
- **Workspace context awareness** for better AI responses
- **Project file organization** in dedicated workspace

### 📊 **Intelligent Session Management**
- **Conversation persistence** with JSON export
- **Session analytics** and usage statistics
- **Response time monitoring**
- **Model usage tracking** across sessions

### 🎯 **Flexible Interaction Modes**
- **Interactive chat mode** for extended conversations
- **Single prompt mode** for quick queries
- **Command-line automation** support
- **File-based AI operations**

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+**
- **Together AI API key** ([Get yours free here](https://api.together.xyz/))

### Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch CLIA**:
   ```bash
   python ai.py
   ```
4. **Enter your API key** when prompted (saved securely for future use)

## 🎮 Usage Examples

### Interactive Chat Mode
```bash
python ai.py
```
Start an intelligent conversation with context-aware responses.

### Quick AI Query
```bash
python ai.py -p "Explain quantum computing in simple terms"
```

### Use Specific Model
```bash
python ai.py -m 1 -p "Write a Python function to sort a list"
```

### List All Models
```bash
python ai.py --list-models
```

## 🧠 Available AI Models

| # | Model Name | Specialization | Best For |
|---|------------|---------------|----------|
| 1 | **DeepSeek R1** | Advanced reasoning & problem-solving | Complex analysis, mathematics |
| 2 | **Llama 3.3** | General-purpose conversation | Versatile tasks, creative writing |
| 3 | **Qwen3 32B FP8** | High-performance processing | Technical documentation, coding |
| 4 | **AFM 4.5B** | Fast responses | Quick queries, simple tasks |
| 5 | **EXAONE 3.5 32B** | Advanced language understanding | Natural conversation, explanations |
| 6 | **EXAONE Deep 32B** | Deep learning capabilities | Research, complex reasoning |

## 🎛️ Interactive Commands

### Core Commands
| Command | Description | Example |
|---------|-------------|---------|
| `models` | Show all available AI models | `models` |
| `change [1-6]` | Switch to specific model | `change 2` |
| `stats` | Display detailed session statistics | `stats` |
| `save` | Save conversation to JSON file | `save` |
| `clear` | Clear current conversation history | `clear` |
| `help` | Show comprehensive help menu | `help` |
| `quit` | Exit CLIA gracefully | `quit` |

### File Operations
| Command | Description | Example |
|---------|-------------|---------|
| `read <file>` | Read file from workspace | `read script.py` |
| `write <file>` | Create/edit file in workspace | `write app.py` |
| `run <file>` | Execute Python file | `run my_script.py` |
| `ls` | List all workspace files | `ls` |

### AI-Powered Creation
| Command | Description | Example |
|---------|-------------|---------|
| `create <description>` | AI generates custom files | `create a web calculator` |
| `create <type> [filename]` | Use predefined templates | `create game snake.py` |

#### Available Templates
- **valorant** - Valorant-related programs
- **game** - Simple games and interactive apps
- **web** - HTML/CSS/JavaScript web applications  
- **api** - REST APIs and web services
- **cli** - Command-line tools
- **bot** - Discord/Telegram bots
- **data** - Data analysis scripts
- **ml** - Machine learning projects
- **gui** - Desktop GUI applications
- **utils** - Utility functions and helpers

## 📁 Project Structure

```
AiCli/
├── ai.py                           # Main CLIA application
├── requirements.txt                # Python dependencies
├── README.md                      # Documentation (this file)
├── .env                          # Secure API key storage (auto-created)
├── workspace/                    # AI workspace directory
│   ├── *.py                     # Python scripts
│   └── ...                      # Other generated/user files
└── conversation_*.json           # Saved conversations
```

## 🔧 Configuration & Setup

### API Key Management
CLIA automatically handles API key storage:
- **First run**: Prompts for API key and saves securely
- **Subsequent runs**: Loads key automatically from `.env`
- **Reset key**: Use `reset-key` command anytime

### Model Customization
Easily modify available models in `ai.py`:
```python
self.models = [
    ("Model Name", "model-identifier"),
    # Add your preferred models here
]
```

## 📋 Command Line Arguments

```bash
python ai.py [OPTIONS]

Arguments:
  -p, --prompt TEXT       Execute single prompt and exit
  -m, --model [1-6]      Select specific model (1-6)
  --list-models          Display all models and exit
  -h, --help            Show help message and exit
```

## 💡 Real-World Examples

### Code Generation
```bash
[DeepSeek R1] You: create a REST API for user management
🤖 AI is generating file content...
✓ AI-generated file saved as: user_api.py
```

### Data Analysis
```bash
[DeepSeek R1] You: create data analysis script for CSV files
🤖 Creating data program: Create a data analysis or processing script
✓ File saved to workspace/data_analyzer.py
```

### Quick Problem Solving
```bash
python ai.py -p "How do I reverse a string in Python?"
Using DeepSeek R1
========================================
🤖 [DeepSeek R1]: You can reverse a string in Python using...
```

## 🛠️ Advanced Features

### Workspace Intelligence
- **Context-aware responses** based on workspace files
- **File content analysis** for better AI suggestions
- **Automatic file management** in organized workspace

### Session Analytics
```bash
[DeepSeek R1] You: stats

📊 Session Statistics:
==============================
Session Duration: 0:15:42
Total Messages: 28
Current Model: DeepSeek R1
Conversation Length: 56 turns

📈 Model Usage:
  • DeepSeek R1: 15 messages
  • Llama 3.3: 8 messages
  • Qwen3 32B FP8: 5 messages
```

### Robust Error Handling
- **Network resilience** with automatic retry
- **API validation** and helpful error messages
- **Graceful interruption** handling (Ctrl+C)
- **Input sanitization** and validation

## 🔒 Security & Privacy

- **Secure API key storage** using environment variables
- **No conversation data** sent to external servers
- **Local file operations** only
- **Industry-standard practices** for credential management

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
git clone <your-fork>
cd CLIA
pip install -r requirements.txt
python ai.py --help
```

## 📜 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute.

## 🆘 Troubleshooting

### Common Issues

**"No API key" Error**
```bash
# Solution: Reset your API key
python ai.py
[CLIA] You: reset-key
```

**Model Not Responding**
- Check internet connection
- Verify API key validity
- Try switching models with `change [1-6]`

**File Operations Failing**
- Ensure workspace directory exists
- Check file permissions
- Verify file paths are correct

### Getting Support

1. **Check error messages** carefully - they often contain solutions
2. **Try different models** - some excel at specific tasks
3. **Use `help` command** for quick reference
4. **Restart CLIA** if issues persist

## 🔗 Useful Links

- **[Together AI Platform](https://api.together.xyz/)** - Get your API key
- **[Python Requests Docs](https://docs.python-requests.org/)** - HTTP library documentation
- **[OpenAI API Reference](https://platform.openai.com/docs/api-reference)** - API format reference

> **Star this project** if you find it useful! Your support helps us improve. 🌟
