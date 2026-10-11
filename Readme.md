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
- AI API
- JSON
- Object-Oriented Programming (OOP)

## Requirements

- Python 3.10 or newer
- An API key for the AI provider configured in the code
- The `requests` Python library

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/python-ai-assistant.git
cd python-ai-assistant
```

Replace `YOUR-USERNAME` with your GitHub username.

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure your API key**

Set your API key in the `api_key` variable in `main.py`.

The current implementation uses the Google Gemini API. The project can be adapted to work with other AI providers by updating the API endpoint, request headers, and request body to match their APIs.

**4. Run the application**

```bash
python main.py
```

## Usage

Enter a message in the terminal and press Enter to receive a response from the AI model.

Type `exit` to end the session.

## What I Learned

- Sending HTTP POST requests using `requests`.
- Working with JSON data, dictionaries, and lists.
- Processing API responses and HTTP status codes.
- Using `try` and `except` for error handling.
- Applying loops and conditional statements.
- Practicing Object-Oriented Programming (OOP).

## Future Improvements

- Improve network error handling.
- Separate API logic from the user interface.
- Support multiple AI providers.
- Improve configuration and user experience.

## Author

Created as part of my journey learning Python and working toward becoming an AI Engineer.