# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lUg9QhuVWG0THC-IAYVmdyQR2YaXAQUM
"""

pip install -r ./requirements.txt -q

"""# Custom ChatGTT App with LangChain"""

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate


llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=1)

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        SystemMessage(content="You are a chatbot having a conversation with a human."),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True
)

while True:
    content = input('Your prompt: ')
    if content.lower() in ['quit', 'exit', 'bye']:
        print('Goodbye!')
        break

    response = chain.invoke({'content': content})
    print(response)
    print('-' * 50)

"""# Adding Chat Memory Using ConversationBufferMemory"""

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=False)

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder


llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=1)


memory = ConversationBufferMemory(
    memory_key='chat_history',
    return_messages=True
)


prompt = ChatPromptTemplate(
    input_variables=["content", "chat_history"],
    messages=[
        SystemMessage(content="You are a chatbot having a conversation with a human."),
        MessagesPlaceholder(variable_name="chat_history"), # Where the memory will be stored.
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=False
)

while True:
    content = input('Your prompt: ')
    if content.lower() in ['quit', 'exit', 'bye']:
        print('Goodbye!')
        break

    response = chain.invoke({'content': content})
    print(response)
    print('-' * 50)

"""## Saving Chat Sessions"""

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=False)

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=1)

history = FileChatMessageHistory('chat_history.json')
memory = ConversationBufferMemory(
    memory_key='chat_history',
    chat_memory=history,
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables=["content", "chat_history"],
    messages=[
        SystemMessage(content="You are a chatbot having a conversation with a human."),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=False
)

while True:
    content = input('Your prompt: ')
    if content.lower() in ['quit', 'exit', 'bye']:
        print('Goodbye!')
        break

    response = chain.invoke({'content': content})
    print(response)
    print('-' * 50)

