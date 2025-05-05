#AI Chatbot using moondream LLM model

A terminal-based AI chatbot implementation using the Moondream LLM model through Ollama. 

This chatbot can understand and respond to text prompts while also having the capability to perceive and analyze images.

Moondream is a lightweight, multimodal vision-language model designed to process both images and text, making it capable of tasks like image captioning and visual question answering. Ollama is a platform that allows to easily run, manage, and interact with various open-source AI models-including Moondream-locally on your own machine, without the need for cloud services or subscriptions.

Moondream is available as a downloadable model within the Ollama library. moondream can pulled from ollama library using a simple terminal command.

## Prerequisites

- [Ollama](https://ollama.ai/) installed on your system
- Python 3.8 or higher
- Basic understanding of terminal/command line operations

## Installation

1. First, install Ollama by following the instructions at [ollama.ai](https://ollama.ai)

2. Pull the Moondream model using Ollama:
```bash
ollama pull moondream
```

3. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

4. Install the required Python packages:
```bash
pip install ollama
```

## Usage

1. Make sure Ollama is running in the background:
```bash
ollama serve
```

2. Run the chatbot script:
```bash
python chatbot.py
```

3. The chatbot will now be ready to accept your inputs in the terminal. You can:
   - Enter text prompts for general conversation
   - Provide image paths for image analysis
   - Type 'quit' or 'exit' to end the session

## Features

- Text-based conversation capabilities
- Image analysis and understanding
- Terminal-based interface
- Powered by the efficient Moondream LLM model
- Local execution through Ollama

## Example Interactions

```
You: What can you do?
Bot: I am an AI assistant powered by the Moondream model. I can:
- Engage in text-based conversations
- Analyze and describe images
- Answer questions about images
- Help with various tasks through natural language interaction

You: [Provide image path]
Bot: [Describes the contents of the image]
```

## Limitations

- Requires local system resources to run the model
- Image processing speed depends on your hardware capabilities
- Model responses are based on its training data cutoff

## Troubleshooting

If you encounter any issues:

1. Ensure Ollama is running (`ollama serve`)
2. Verify the Moondream model is properly installed (`ollama list`)
3. Check your Python version and package installations
4. Make sure you have sufficient system resources available



## License

This project is licensed under the MIT License - see the LICENSE file for details.


