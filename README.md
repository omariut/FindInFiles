

# FindInFiles

FindInFiles is a smart chatbot that helps you quickly retrieve, search, and summarize information from documents. Simply place your files in a folder (docs), ask your question, search for specific words, or request a summary, and the bot will process the content to provide precise responses. It's an efficient solution for professionals, students, and researchers to streamline document analysis and save time.

## Features

- **Intelligent Chat**: Engage in a conversational manner to ask questions and get accurate answers based on document content.
- **Quick Search**: Rapidly locate specific words or phrases within documents.
- **Document Summarization**: Generate concise summaries of document content.
- **Advanced Language Model**: Utilizes state-of-the-art natural language processing to understand and process queries.

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

   For chat mode:
   ```json
   {
     "query": "Your question here",
     "mode": "chat"
   }
   ```

   For search mode:
   ```json
   {
     "query": "search word",
     "mode": "search"
   }
   ```

   For summary mode:
   ```json
   {
     "query": "Number of lines for summary",
     "mode": "summary"
   }
   ```

3. The server will respond with the answer, search results, or summary based on the documents in the `docs` folder.

## Configuration

- Place your documents in the `docs` folder.
- Adjust the `max_history_size` in `chains.py` to control the chat history length.
- Modify the `chunk_size` and `chunk_overlap` in `retrievers.py` to fine-tune document processing.






