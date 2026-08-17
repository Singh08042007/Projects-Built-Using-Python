# 🤖 Lightweight Python AI Chatbot (Google Gemini Powered)

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini API](https://img.shields.io/badge/API-Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Stdlib)-brightgreen?style=for-the-badge)](https://docs.python.org/3/library/)
[![License](https://img.shields.io/badge/License-MIT-blue.style=for-the-badge)](LICENSE)

A high-performance, lightweight Command-Line Interface (CLI) AI Chatbot built in **pure Python**. Powered by Google's **Gemini REST API**, this chatbot features zero external package dependencies, multi-model fallback resolution, session-persistent context memory, and graceful error handling.

---

## ✨ Key Features

* **⚡ Zero External Dependencies**: Built entirely using Python's standard libraries (`urllib.request`, `json`, `os`). No `pip install` required!
* **🔄 Smart Model Fallback**: Automatically tries candidate Gemini models sequentially (`gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-flash-preview`) to guarantee high availability and minimal latency.
* **💾 Persistent Chat History**: Saves your conversation state locally in `chat_history.json`, maintaining up to 40 past messages across sessions for continuous multi-turn dialogue.
* **🎮 Interactive CLI Commands**:
  * `clear`: Instantly reset the current chat memory and disk persistence.
  * `exit` / `quit`: Safely exit the application.
* **🛡️ Robust Error Handling**: Clean handling for missing API keys, network outages, HTTP status errors, and API response errors without crashing the shell.

---

## 📁 Project Structure

```text
AI-Chatbot/
├── main.py              # Main application logic & CLI loop
├── chat_history.json    # Local persistent storage for conversation history (auto-generated)
└── README.md            # Project documentation
```

---

## 📋 Prerequisites

* **Python 3.7+** installed on your system.
* A **Google Gemini API Key**. You can generate a free key at [Google AI Studio](https://aistudio.google.com/).

---

## 🚀 Quick Start

### 1. Set Your Gemini API Key

Set your API key as an environment variable in your terminal session before launching the chatbot.

#### **Windows (PowerShell)**
```powershell
$env:GEMINI_API_KEY="your_actual_gemini_api_key_here"
```

#### **Windows (Command Prompt)**
```cmd
set GEMINI_API_KEY=your_actual_gemini_api_key_here
```

#### **Linux / macOS (Bash / Zsh)**
```bash
export GEMINI_API_KEY="your_actual_gemini_api_key_here"
```

> **Note**: Alternatively, you can edit [main.py](file:///D:/Deepinder%20Folder/Courses/Python-Projects-Harry/Projects-Built-Using-Python/AI-Chatbot/main.py) and update the `HARDCODED_GEMINI_API_KEY` variable for quick local testing.

---

### 2. Run the Chatbot

Launch the application directly using standard Python:

```bash
python main.py
```

---

## 💬 Usage & Command Reference

Once started, type your query and press **Enter** to chat with Gemini.

```text
Gemini Chatbot is ready.
Type 'exit' to quit.

Loaded 4 past messages from chat_history.json.

You: Hi, explain quantum computing in one simple sentence.
Bot: Quantum computing uses subatomic particles to perform complex calculations much faster than classical computers.

You: clear
Bot: History cleared.

You: exit
Bot: Goodbye!
```

### Supported Commands

| Command | Action |
| :--- | :--- |
| `clear` | Clears both active session history and `chat_history.json`. |
| `exit` / `quit` | Terminates the chatbot session gracefully. |

---

## ⚙️ How It Works

1. **Context Management**: On startup, [main.py](file:///D:/Deepinder%20Folder/Courses/Python-Projects-Harry/Projects-Built-Using-Python/AI-Chatbot/main.py) loads existing dialogue from `chat_history.json`. Messages are formatted into `contents` arrays with user and model turns, capped at `MAX_HISTORY_MESSAGES = 40` to stay within optimal context windows.
2. **Model Candidate Chain**: Requests are sent to Google's REST API endpoint. If a specific model returns a 404 or fails, the script automatically attempts the next candidate model in `MODEL_CANDIDATES`.
3. **Persistence**: Every successfully received response updates the local `chat_history.json` file in UTF-8 JSON format.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
