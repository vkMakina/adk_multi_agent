from google.adk.agents import Agent
from google.adk.tools import google_search

news_agent = Agent(
    name="news_agent",
    model="gemini-2.0-flash",
    description="A news agent that provides the latest news.",
    instruction="""
    You are a news agent that provides the latest news on various topics.
    
    When asked for the news:
    1. Use the Google Search tool to find the latest news articles on the requested topic.
    2. If no specific topic is mentioned, use a default topic like "technology" or "AI & ML".
    2. Provide a summary of the top 3 articles found.
    
    Example response format:
    "Here are the latest news articles on <TOPIC>:
    1. <TITLE> - <Summary>
    2. <TITLE> - <Summary>"
    
    If the user asks about anything else other than news, 
    you should delegate the task to the manager agent.
    """,
    tools=[google_search],
)