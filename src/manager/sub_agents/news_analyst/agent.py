from google.adk.agents import LlmAgent
import datetime

def get_top_headlines(topic: str) -> dict:
    """
    Fetches today's top headlines for a given topic.

    Args:
        topic (str): The news topic to search for.

    Returns:
        dict: A dictionary with the following structure:
              {'status': 'success'|'error', 'articles': [...]}.
              On success, 'articles' is a list of dictionaries, each with 'title', 'outlet', and 'date'.
              On error or if no articles are found, 'status' is 'error' and 'articles' is empty.
    """
    # This is a mock implementation. A real implementation would call a news API.
    print(f"--- Tool: get_top_headlines called for topic: {topic} ---")
    if "tech" in topic.lower():
        return {
            "status": "success",
            "articles": [
                {
                    "title": "New AI Model Released",
                    "outlet": "Tech Today",
                    "date": datetime.date.today().isoformat(),
                },
                {
                    "title": "Quantum Computing Breakthrough",
                    "outlet": "Science Weekly",
                    "date": datetime.date.today().isoformat(),
                },
            ],
        }
    else:
        return {"status": "error", "articles": []}

news_analyst = LlmAgent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="Summarizes today’s top headlines for a user topic; delegates back if none are found.",
    instruction="""- If `{news_topic?}` is missing, ask: "What topic should I check the news for today?"
- When the topic is known, use the `get_top_headlines` tool to fetch today's news.
- If the tool returns no results or an error, briefly say so and call `transfer_to_agent(agent_name="manager")`.
- Output format:
    - Bullet list (max 3): **title** — outlet (date)
    - One-sentence neutral summary after the bullets.""",
    tools=[get_top_headlines],
)