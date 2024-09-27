# FindInFiles

FindInFiles is a smart chatbot that helps you quickly retrieve information from multiple documents. Simply place your files in a folder, ask your question, and the bot will search the content to provide precise answers. It's an efficient solution for professionals, students, and researchers to streamline document searching and save time.

## Features

- **Intelligent Search**: Utilizes advanced language models to understand and answer questions based on document content.
- **Chat Interface**: Engage in a conversational manner to refine your queries and get more accurate results.
- **Search Mode**: Quickly locate specific information within documents.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/FindInFiles.git
   cd FindInFiles
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy `.env-example` to `.env`
   - Fill in your API keys and other required information

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Send POST requests to `http://localhost:5000/process` with the following JSON structure:

- for chat
   ```json
   {
     "query": "Your question here",
     "mode": "chat" // or "search"
   }
   ```
- for search
   ```json
   {
     "query": "search word",
     "mode": "search" // or "search"
   }
   ```

3. The server will respond with the answer or search results based on the `info.txt` in the `docs` folder.

## Configuration

- Adjust the `config.py` file to change the language model or other settings.
- Modify `retrievers.py` to customize document loading and splitting behavior.


