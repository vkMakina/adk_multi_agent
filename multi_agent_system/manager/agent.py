from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.news_agent.agent import news_agent
from .sub_agents.joke_agent.agent import joke_agent
from .sub_agents.youtube_agent.agent import youtube_agent
from .tools.current_time_tool import get_current_time
from .config import settings

root_agent = Agent(
    name="manager",
    model= settings.DEFAULT_MODEL,    #"gemini-2.0-flash",
    description="A Manager agent that directs the calls to relevant sub-agents",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - youtube_agent

    You also have access to the following tools:
    - news_agent
    - get_current_time
    """,
    sub_agents=[youtube_agent, joke_agent],
    tools=[
        AgentTool(news_agent),
        get_current_time,
    ],
)
