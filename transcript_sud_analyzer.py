from typing_extensions import TypedDict
from typing import Optional

from langgraph.graph import StateGraph
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI 
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

class TranscriptState(TypedDict):
    transcript: str
    concern_detected: Optional[bool]
    # concern_type: Optional[str]
    explanation: Optional[str]

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

def analyze_transcript(state: TranscriptState) -> TranscriptState:
    messages = [
        SystemMessage(content=(
            "You are a behavioral health assistant. "
            "Analyze the following therapy session transcript for signs of alcohol or substance abuse or potential risks and signs of abuse. "
            "If there is concern, provide a summary explaining why. "
            "If there is no concern, say clearly 'No concern detected.'"
        )),
        HumanMessage(content=state["transcript"]),
    ]

    response = llm.invoke(messages)
    response_text = response.content.strip().lower()

    concern_detected = "no concern" not in response_text

    return {
        **state,
        "concern_detected": concern_detected,
        # "concern_type": concern_type,
        "explanation": response.content.strip(),
    }

# Build graph
builder = StateGraph(TranscriptState)
builder.add_node("analyze", analyze_transcript)
builder.set_entry_point("analyze")
builder.set_finish_point("analyze")
graph = builder.compile()
