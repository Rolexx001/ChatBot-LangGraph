from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

class ChatbotState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def chat_node(state:ChatbotState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

checkpoint=InMemorySaver()

graph=StateGraph(ChatbotState)

graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpoint)
