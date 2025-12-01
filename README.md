# LLaMA Ollama Integration

This project uses Ollama to run local LLaMA models for email rewriting and code completion tasks.

## Prerequisites

1. **Install Ollama** (if not already installed):
   - Visit https://ollama.com and download for your system
   - Or on macOS: `brew install ollama`

2. **Install Python dependencies**:
   ```bash
   pip install requests
   ```

## Setup and Run

1. **Start the Ollama server** (in a separate terminal):
   ```bash
   ollama serve
   ```

2. **Create the custom models** from the Modelfiles:
   ```bash
   ollama create email-rewriter -f Modelfile
   ollama create copilot -f CopilotModelfile

   ## List Models
   ollama ls 
   ```

3. **Run the scripts**:

   For the email rewriter:
   ```bash
   python llama_integration.py
   ```

   For the simple agent (demo/template):
   ```bash
   python simple_agent.py
   ```

## Project Files

- **llama_integration.py** - Rewrites rude emails to be more polite using the `email-rewriter` model
- **simple_agent.py** - Demo showing function definitions for home automation and search
- **my_copilot.py** - Empty file (placeholder)
- **Modelfile** - Defines an email rewriting assistant based on llama3.2
- **CopilotModelfile** - Defines a code completion assistant based on llama3.2

## Example Usage

The `llama_integration.py` script takes a potentially rude email and rewrites it professionally:

```python
rewritten_email = submit_prompt("This is the stupidest idea I've ever heard!")
print("Here is the reworded email:")
print(rewritten_email)
```
