# Python AI Assistant

A simple command-line AI assistant built with Python and an AI API.

This project is part of my journey toward learning Python and AI Engineering. It helped me practice working with APIs, processing JSON responses, using classes and objects, and handling errors in Python.

## Features

- Interacts with an AI model through an API.
- Accepts user prompts directly from the terminal.
- Supports continuous interaction within the same session.
- Processes API responses and handles common response-related errors.
- Displays a simple, formatted command-line interface.
- Allows users to exit the session by typing `exit`.

## Technologies Used

- Python
- Requests
- python-dotenv
- AI API
- JSON
- Object-Oriented Programming (OOP)

## Requirements

- Python 3.10 or newer
- An API key from the configured AI provider
- The Python libraries listed in `requirements.txt`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nourmhmedf7-maker/simple-ai-assistant.git
cd simple-ai-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Create a file named `.env` in the project directory and add the following line:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Important:** Never share your API key or upload your `.env` file to GitHub.

Make sure your `.gitignore` file includes:

```text
.env
```

### 4. Run the application

```bash
python "ai assistant.py"
```

## Usage

Once the application starts, enter a message in the terminal and press Enter to receive a response from the AI model.

Type `exit` to end the session.

## What I Learned

- Sending HTTP POST requests using `requests`.
- Working with JSON data, dictionaries, and lists.
- Processing API responses and HTTP status codes.
- Using `try` and `except` for error handling.
- Applying loops and conditional statements.
- Practicing Object-Oriented Programming (OOP).
- Managing API keys through environment variables.

## Future Improvements

- Improve network error handling.
- Separate API logic from the user interface.
- Support multiple AI providers.
- Improve configuration and user experience.

## Author

Created as part of my journey learning Python and working toward becoming an AI Engineer.