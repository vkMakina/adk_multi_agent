# ADK Multi-Agent System

A multi-agent system built using [Google ADK](https://google.github.io/adk-docs/). This project demonstrates a manager agent that delegates tasks to specialized sub-agents and tools, such as fetching news, jokes, YouTube content, and the current time.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Agents & Tools](#agents--tools)
- [Extending the System](#extending-the-system)
- [License](#license)
- [References](#references)

---

## Project Structure

```
multi_agent_system/
│
├── manager/
│   ├── agent.py
│   ├── config.py
│   └── ...
│
├── sub_agents/
│   ├── news_agent/
│   │   └── agent.py
│   ├── joke_agent/
│   │   └── agent.py
│   └── youtube_agent/
│       └── agent.py
│
├── tools/
│   └── current_time_tool.py
│
├── requirements.txt
└── README.md
```

---

## Features

- **Manager Agent**: Delegates tasks to the appropriate sub-agent or tool.
- **Sub-Agents**:
  - News Agent: Fetches current news.
  - Joke Agent: Provides jokes.
  - YouTube Agent: Handles YouTube-related queries.
- **Tools**:
  - Current Time Tool: Returns the current time.
- **Extensible**: Easily add new agents or tools.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/adk_multi_agent.git
   cd adk_multi_agent
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Configuration

- Edit `manager/config.py` to set up your environment variables and model settings.
- If using API keys (for news, YouTube, etc.), store them securely and load them in your config.

---

## Usage

Run the manager agent:

```sh
python -m multi_agent_system.manager.agent
```

Or import and use the agents in your own scripts.

---

## Agents & Tools

### Manager Agent

- Delegates tasks based on user input.
- Uses sub-agents and tools as needed.

### Sub-Agents

- **News Agent**: Handles news queries.
- **Joke Agent**: Handles joke requests.
- **YouTube Agent**: Handles YouTube-related queries.

### Tools

- **Current Time Tool**: Returns the current time.

---

## Extending the System

To add a new agent or tool:

1. Create a new folder in `sub_agents/` or `tools/`.
2. Implement the agent/tool following the ADK documentation.
3. Register the new agent/tool in `manager/agent.py`.

---

## License

This project is licensed under the MIT License.

---

## References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Python Official Documentation](https://docs.python.org/3/)