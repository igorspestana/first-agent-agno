# First Agent Agno

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A project focused on building and experimenting with AI agents using the Agno framework.

## 📋 Description

First Agent Agno is a project that serves as a starting point for developing and testing AI agents. It provides a foundation for building intelligent systems that can perform various tasks autonomously.

## ✨ Features

- Basic agent architecture
- Example implementations
- Easy-to-extend design
- Configuration management
- Logging and monitoring

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Git](https://git-scm.com/) - Version control system
- [uv](https://github.com/astral-sh/uv) - A fast Python package installer and resolver. You can install it with the following command:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/first-agent-agno.git
   cd first-agent-agno
   ```

2. Create a virtual environment (recommended):
   ```bash
   uv venv .venv
   source .venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   uv add agno fastapi google-genai
   ```

## 🛠️ Usage

```python
# Example usage
from agent import Agent

agent = Agent()
response = agent.process("Hello, world!")
print(response)
```

## 📂 Project Structure

```
first-agent-agno/
├── .env                 # Environment variables
├── .env.show           # Example environment variables
├── .git/               # Git directory
├── .gitignore          # Git ignore file
├── .python-version     # Python version specification
├── .venv/              # Python virtual environment
├── main.py             # Main application file
├── notes.md            # Project notes
├── pyproject.toml      # Python project configuration
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request