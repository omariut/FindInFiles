from prompts import qa_prompt,search_prompt,summary_prompt
from retrievers import history_aware_retriever
from langchain.chains import create_retrieval_chain
from config import llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, SystemMessage
import json

chat_history = []  # Collect chat history here (a sequence of messages)
max_history_size = 10  # Limit chat history to the last 10 messages

def get_rag_chain():
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    return rag_chain
# Chat processing chain
def chat_chain(query,chat_history=None):
    rag_chain=get_rag_chain()
    result = rag_chain.invoke({"input": query, "chat_history": chat_history})
    chat_history.append(HumanMessage(content=query))
    chat_history.append(SystemMessage(content=result["answer"]))

    # Limit chat history to the last max_history_size messages
    if len(chat_history) > max_history_size * 2:
        chat_history = chat_history[-max_history_size * 2:]

    return result["answer"]


def search_chain(query):
    """Search processing chain"""
    # Use the history_aware_retriever to get relevant documents for the query
    search_chain = create_stuff_documents_chain(llm, search_prompt)
    search_chain = create_retrieval_chain(history_aware_retriever, search_chain)
    search_results = search_chain.invoke({"input": query})
    
    if not search_results:
        return f"No relevant documents found for '{query}'"
    search_results = search_results["answer"]
    response = search_results.strip('```json').strip('```')
    return json.loads(response)

    # Now convert it into a proper JSON format



def summary_chain(query):
    """Summary processing chain"""
    summary_chain = create_stuff_documents_chain(llm, summary_prompt)
    summary_chain = create_retrieval_chain(history_aware_retriever, summary_chain)
    summary_results = summary_chain.invoke({"input": query})
    return summary_results["answer"]

def router_chain(query, mode="chat"):
    """Router chain to determine the processing logic based on mode"""
    if mode == "chat":
        return chat_chain(query, chat_history=chat_history)
    elif mode == "search":
        return search_chain(query)
    elif mode == "summary":
        return summary_chain(query)
    else:
        return "Invalid mode"
