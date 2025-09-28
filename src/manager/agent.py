from google.adk.agents import LlmAgent
from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst

# The root_agent variable is what the ADK discovers and runs.
root_agent = LlmAgent(
    name="manager",
    model="gemini-2.0-flash",
    description="Coordinator that greets the user, asks: 'joke', 'news', or 'stock?', then delegates to the correct specialist; handles fallbacks.",
    global_instruction="Be brief, safe, and factual. If a request is out-of-scope or information is missing, say so and route back to the Manager.",
    instruction="""- Start by asking exactly: "What would you like: joke, news, or stock?"
- Routing rules (LLM transfer):
    - If the user chooses “joke” → call `transfer_to_agent(agent_name="funny_nerd")`.
    - If the user chooses “news” → call `transfer_to_agent(agent_name="news_analyst")`.
    - If the user chooses “stock” → call `transfer_to_agent(agent_name="stock_analyst")`.
- If a specialist transfers back (can’t answer), ask a concise clarifying question or offer a different option.
- Output style: 1–2 short sentences per turn.""",
    sub_agents=[funny_nerd, news_analyst, stock_analyst],
)