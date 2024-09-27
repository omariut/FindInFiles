from prompts import qa_prompt,search_prompt
from retrievers import history_aware_retriever
from langchain.chains import create_retrieval_chain
from config import llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, SystemMessage

chat_history = []  # Collect chat history here (a sequence of messages)
max_history_size = 10  # Limit chat history to the last 10 messages

# Chat processing chain
def chat_chain(query, chat_history):
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
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
    return search_results["answer"]


def router_chain(query, mode="chat"):
    """Router chain to determine the processing logic based on mode"""
    if mode == "chat":
        return chat_chain(query, chat_history)
    elif mode == "search":
        return search_chain(query)
    else:
        return "Invalid mode"
