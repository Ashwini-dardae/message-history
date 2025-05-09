import os  
from dotenv import load_dotenv
import streamlit as st  ## using streamlit for frontend web ui
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY") 
st.write(groq_api_key)

from langchain_groq import ChatGroq 
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)


from langchain_core.messages import HumanMessage
model.invoke([HumanMessage(content="Hi, My name is Krish and I am a Chief AI Engineer")])

from langchain_core.messages import AIMessage
model.invoke(
    [
        HumanMessage(content="Hi, My name is Krish and I am a Chief AI Engineer"),
        AIMessage(content="It's nice to meet you, Krish! \n\nThat's a fascinating title. As a Chief AI Engineer, I imagine you're involved in some cutting-edge work. What are you currently working on that you're most excited about?  \n\nI'm always eager to learn more about the applications of AI.\n"),
        HumanMessage(content="Hey, What's my name and what I do?")

    ]
)

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store={}

def get_session_history(session_id:str)->BaseChatMessageHistory:
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]
with_message_history=RunnableWithMessageHistory(model,get_session_history)

config = {"configurable":{"session_id":"chat1"}}

response = with_message_history.invoke(
    [HumanMessage(content="Hi, My name is Krish and I am a Chief AI Engineer")],
    config=config
)
st.write(response.content)

response1 = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)
st.write(response1.content)
config1 = {"configurable":{"session_id":"chat3"}}
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config1
)
response.content
response = with_message_history.invoke(
    [HumanMessage(content="My name is john")],
    config=config1
)
response.content


response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config1
)
response.content

### Prompt Template
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your are a helpful assistant. Asnwer all the question to the nest of your ability"
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

chain=prompt|model

chain.invoke({"messages":[HumanMessage(content="Hi, My name is Krish")]})

with_message_history=RunnableWithMessageHistory(chain,get_session_history)
config = {"configurable":{"session_id":"chat3"}}
response = with_message_history.invoke(
    [HumanMessage(content="Hi, Ny name is Krish")],
    config=config
)
response

## Add more complexity

prompt =  ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your are a helpful assistant. Answer all questions to the best of your ability in {language}"
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain=prompt|model
response=chain.invoke({"messages":[HumanMessage(content="Hi My name is Krish")],"language":"Hindi"})
st.write(response.content)

with_message_history=RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="messages"
)

config = {"configurable": {"session_id": "chat5"}}
repsonse=with_message_history.invoke(
    {'messages': [HumanMessage(content="Hi,I am Krish")],"language":"Hindi"},
    config=config
)
st.write(response.content)
repsonse=with_message_history.invoke(
    {'messages': [HumanMessage(content="What's my name")],"language":"Hindi"},
    config=config
)
repsonse.content
st.write(response.content)
st.write("Hello Krish2..")

from langchain_core.messages import SystemMessage,trim_messages
trimmer=trim_messages(
    max_tokens=70,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human"    
)
messages = [
    SystemMessage(content="you are a good assistant"),
    HumanMessage(content="hi! i am bob "),
    AIMessage(content="hi!"),
    HumanMessage(content="I like choclate ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="Whats 2+2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem"),
    HumanMessage(content="Having fun"),
    AIMessage(content="yes"),
]
trimmer.invoke(messages)
st.write("Hello Krish1..")

from operator import itemgetter

from langchain_core.runnables import RunnablePassthrough

chain=(
    RunnablePassthrough.assign(messages=itemgetter("messages")|trimmer)
    | prompt
    | model
    
)

response1=chain.invoke(
    {
    "messages":messages + [HumanMessage(content="What ice cream do i like")],
    "language":"English"
    }
)
response1.content
st.write("Hello Krish...")
 