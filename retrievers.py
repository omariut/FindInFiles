
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from prompts import contextualize_q_prompt
from langchain.chains import create_history_aware_retriever
from langchain_community.document_loaders import TextLoader
from config import llm

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("docs", glob="**/*.txt", loader_cls=TextLoader)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

