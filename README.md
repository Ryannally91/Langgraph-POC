# LangGraph Chatbot Application

This application is a chatbot built using LangGraph.

## Setup

### 1. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

_Note: Ensure you have Python 3.12 or a compatible version installed, as specified in [`langgraph.json`](/Users/ryannally/side_projects/sud_langgraph_poc/langgraph.json)._

### 2. Install Dependencies

Install the required Python packages using the [`requirements.txt`](/Users/ryannally/side_projects/sud_langgraph_poc/requirements.txt) file:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

This project uses an `.env` file to manage environment variables. Create a `.env` file in the root of the project if it doesn't exist.
You will need to add your `OPENAI_API_KEY` to this file or ensure it's set in your environment, as it's used in [`chatbot.py`](/Users/ryannally/side_projects/sud_langgraph_poc/chatbot.py).

Example [`./.env`](/Users/ryannally/side_projects/sud_langgraph_poc/.env) file content:

```env
OPENAI_API_KEY="your_openai_api_key_here"
# Other environment variables if needed
```

## Running LangGraph Studio (Development Server)

Once the setup is complete, you can run the LangGraph development server (LangGraph Studio). This will allow you to interact with and visualize your graph.

Install the langgraph-cli:

```bash
pip install -U "langgraph-cli[inmem]"
```

To start the development server, run the following command from the project's root directory:

```bash
langgraph dev
```

This will typically start a server, and you can access LangGraph Studio by navigating to `http://localhost:8000` (or the port indicated in the terminal output) in your web browser.
