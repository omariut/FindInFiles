from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

search_system_prompt=(
    "You are an assistant for search tasks. Use "
    "the following pieces of retrieved context to "
    "search the file. your response should like this: "
    "count:total_word_count,lines:[line1,line2,line3],"
    "here line is the text on the line from the document that contains the search term"
    "don't include the lines that don't contain the search term"
    "your response should be in json format only"
    "if the search term is not found, return 'not found'"
    "return only the result, no need of any other text"
    "\n\n"
    "{context}"
    "\n\n"
    "search term: {input}"
)

search_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", search_system_prompt),
        ("human", "{input}"),
    ]
)


summary_system_prompt=(
    "You are an assistant for summary tasks."
    "Summarize the following context in a concise manner."
    "number of lines in the summary should be less than {input}"
    "{context}"
)

summary_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", summary_system_prompt),
        ("human", "{input}"),
    ]
)
