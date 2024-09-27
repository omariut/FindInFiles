from langchain_openai import ChatOpenAI

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI model
llm = ChatOpenAI(model="gpt-4o")