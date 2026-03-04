from google.adk.agents import Agent
from google.adk.models import Gemini
from tools import extract_pdf_tool

SYSTEM_PROMPT = """
You are an expert PDF summarization agent.

Steps:
1. Use extract_pdf_text tool to read the PDF.
2. Analyze structure.
3. Produce:
   - Executive Summary
   - Detailed Summary
   - Key Points
   - Actionable Insights
"""

def create_agent():

    model = Gemini(model="gemini-1.5-pro")

    agent = Agent(
        name="pdf_summarizer",
        model=model,
        description="Summarizes PDF documents.",
        instruction=SYSTEM_PROMPT,
        tools=[extract_pdf_tool],
    )

    return agent