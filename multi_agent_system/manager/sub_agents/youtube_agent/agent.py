
from google.adk.agents import Agent
import requests


SERP_API_KEY = "300ab6471e1121698607ab6dd8e501b6ead0500837a2c4fd6ae44b2937e79fd4" #settings.SERPAPI_API_KEY #os.getenv("SERPAPI_API_KEY")

def search_youtube_videos(query: str) -> dict:
    """
    Searches YouTube videos using SerpAPI and returns titles, links, and snippets.
    
    Parameters:
    - query (str): The search query.
    - max_results (int): Maximum number of results to return.
    - gl (str): Country code for localization (default: 'us').
    - hl (str): Language code for localization (default: 'en').
    - sp (str): Parameter for sorting and filtering (optional).
    
    Returns:
    - dict: A dictionary containing the search status, query, and list of video results.
    """
    print(f"[DEBUG] Starting 'search_youtube_videos'")
    print(f"[DEBUG] Query received: {query}")

    try:
        serp_api_url = "https://serpapi.com/search"
        max_results = 3
        params = {
            "engine": "youtube",
            "search_query": query,
            "api_key": SERP_API_KEY,
            "gl": "us",
            "hl": "en",
            "num": max_results
        }

        print(f"[DEBUG] Sending request to SerpAPI with params: {params}")
        response = requests.get(serp_api_url, params=params)
        data = response.json()

        video_results = []

        for result in data.get("video_results", []):
            video_data = {
                "title": result.get("title"),
                "link": result.get("link"),
                "description": result.get("description", "")
            }
            video_results.append(video_data)

        print(f"[DEBUG] Extracted {len(video_results)} YouTube results.")
        for i, video in enumerate(video_results, 1):
            print(f"  [{i}] {video['title']} - {video['link']}")

        return {
            "status": "success",
            "query": query,
            "results": video_results
        }

    except Exception as e:
        print(f"[EXCEPTION] {str(e)}")
        return {"status": "error", "message": str(e)}


youtube_agent = Agent(
    name="youtube_agent",
    model="gemini-2.0-flash",
    description="A YouTube agent that provides 3 latest videos on given topic.",
    instruction="""
    You are a YouTube agent that provides 3 latest videos on given topic.
    
    When asked for the latest videos:
    1. Use the search_youtube_videos tool to find the latest YouTube videos on the requested topic.
    2. If no specific topic is mentioned, use a default topic like "technology" or "AI & ML".
    3. Format the response to show the titles, links, and descriptions of the top 3 videos found.
    
    Example response format:
    "Here are the latest YouTube videos on <TOPIC>:
    1. <TITLE> - <LINK> - <description>
    2. <TITLE> - <LINK> - <description>
    3. <TITLE> - <LINK> - <description>
    
    To watch the full videos, you can visit the links provided."
    
    If the user asks about anything else other than YouTube videos, 
    you should delegate the task to the manager agent.
    """,
    tools=[search_youtube_videos],
)