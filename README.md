# 🔥 Nexus AI

An intelligent command-line AI assistant with advanced multi-model switching capabilities, built for seamless interaction with multiple AI models through the Together AI API.

## ✨ Features

### 🔄 **Advanced Model Switching**
- **6 AI Models** with unique capabilities
- **Quick switching** with `change [1-6]` command
- **Real-time model indicators** in conversation
- **Usage tracking** for each model

### 📊 **Session Analytics**
- **Response timing** for performance monitoring
- **Message counting** and session duration tracking
- **Model usage statistics** per session
- **Conversation length tracking**

### 💾 **Data Management**
- **Session backup** functionality
- **Secure API key storage** with `.env` file support
- **Environment variable management**

### 🎯 **Flexible Usage Modes**
- **Interactive chat mode** for extended conversations
- **Single prompt mode** for quick queries
- **Command-line arguments** for automation

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Together AI API key ([Get yours here](https://api.together.xyz/))

### Installation

1. **Clone or download** this project
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Nexus AI**:
   ```bash
   python ai.py
   ```

## 🎮 Usage

### Interactive Chat Mode
```bash
python ai.py
```
Start a conversation with the AI. Nexus AI will prompt for your API key on first use and securely save it to a `.env` file.

### Single Prompt Mode
```bash
python ai.py -p "Your question here"
```

### Specify Model
```bash
python ai.py -m 2 -p "Hello world"
```

### List Available Models
```bash
python ai.py --list-models
```

## 🧠 Available AI Models

| # | Model | Emoji | Description |
|---|-------|-------|-------------|
| 1 | **DeepSeek R1** | 🧠 | Advanced reasoning and problem-solving |
| 2 | **Llama 3.3** | 🦙 | Meta's latest open-source model |
| 3 | **Qwen3 32B FP8** | 🌟 | Alibaba's high-performance model |
| 4 | **AFM 4.5B** | ⚡ | Fast and efficient responses |
| 5 | **EXAONE 3.5 32B** | 🔥 | LG's advanced language model |
| 6 | **EXAONE Deep 32B** | 💎 | Enhanced deep learning capabilities |

## 🎛️ Interactive Commands

| Command | Description |
|---------|-------------|
| `models` | Show all available AI models |
| `change [1-6]` | Switch to specific model (optional number) |
| `stats` | Display session statistics |
| `clear` | Clear conversation history |
| `reset-key` | Change/reset your API key |
| `help` | Show all available commands |
| `quit` | Exit the assistant |

## 📁 Project Structure

```
├── ai.py               # Main Nexus AI application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .env               # Environment variables (auto-generated)
```

## 🔧 Configuration

### API Key Setup
Nexus AI will prompt for your Together AI API key on first use and securely store it in a `.env` file. Get your free API key from [Together AI](https://api.together.xyz/).

### Model Customization
You can modify the available models by editing the `models` list in `ai.py`:

```python
self.models = [
    ("Model Name", "model-id", "emoji"),
    # Add more models here
]
```

## 📋 Command Line Arguments

```bash
python ai.py [OPTIONS]

Options:
  -p, --prompt TEXT       Single prompt mode
  -m, --model [1-6]      Select model (1-6)
  --list-models          List all available models and exit
  -h, --help            Show help message
```

## 💡 Examples

### Basic Conversation
```bash
$ python ai.py
🔥 NEXUS AI - Connecting 🧠 DeepSeek R1
Commands: 'models', 'change [1-6]', 'stats', 'clear', 'help', 'quit'
============================================================

[🧠 DeepSeek R1] You: Hello, how are you?
🤔 Thinking...⏱️  Response time: 1.23s

🤖 [🧠 DeepSeek R1]: Hello! I'm doing well, thank you for asking...
```

### Quick Model Switch
```bash
[🧠 DeepSeek R1] You: change 2
✅ Switched from DeepSeek R1 to 🦙 Llama 3.3

[🦙 Llama 3.3] You: What's the weather like?
```

### Session Statistics
```bash
[🧠 DeepSeek R1] You: stats

📊 Session Statistics:
==============================
Session Duration: 0:05:23
Total Messages: 12
Current Model: 🧠 DeepSeek R1
Conversation Length: 24 turns

📈 Model Usage:
  • DeepSeek R1: 8 messages
  • Llama 3.3: 4 messages
```

## 🛠️ Advanced Features

### Secure API Key Storage
- **Environment variables** with `.env` file support
- **Automatic key loading** on startup
- **Reset functionality** with `reset-key` command
- **Industry-standard security** practices

### Error Handling
- **Network error recovery**
- **API key validation**
- **Graceful interruption handling**
- **Input validation**

### Performance Monitoring
- **Response time tracking**
- **Model performance comparison**
- **Session analytics**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is open source. Feel free to use, modify, and distribute.

## 🆘 Troubleshooting

### Common Issues

**"No API key" error**
- Ensure you have a valid Together AI API key
- Check your internet connection

**Model switching not working**
- Use numbers 1-6 for model selection
- Type `models` to see available options

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify your API key is valid
3. Ensure all dependencies are installed
4. Try restarting the application

## 🔗 Links

- [Together AI Platform](https://api.together.xyz/)
- [Python Requests Documentation](https://docs.python-requests.org/)

---

**Made with ❤️ for the AI community**

*Power up your AI conversations with Nexus AI! 🔥✨*
