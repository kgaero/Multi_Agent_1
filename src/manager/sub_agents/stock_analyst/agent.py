from google.adk.agents import LlmAgent
import datetime
import random

def get_stock_quote(ticker: str) -> dict:
    """
    Fetches today's stock price for a given company ticker.

    Args:
        ticker (str): The stock ticker symbol (e.g., GOOGL, MSFT).

    Returns:
        dict: A dictionary with the following structure:
              {'status': 'success'|'error', 'price': float, 'changePct': float, 'timestamp': str}.
              On success, all fields are populated.
              On error, 'status' is 'error' and other fields may be null.
    """
    # This is a mock implementation. A real implementation would call a financial data API.
    print(f"--- Tool: get_stock_quote called for ticker: {ticker} ---")
    if ticker.upper() in ["GOOGL", "MSFT", "AAPL"]:
        return {
            "status": "success",
            "price": round(random.uniform(100, 500), 2),
            "changePct": round(random.uniform(-5, 5), 2),
            "timestamp": datetime.datetime.now().isoformat(),
        }
    else:
        return {"status": "error", "price": None, "changePct": None, "timestamp": None}

stock_analyst = LlmAgent(
    name="stock_analyst",
    model="gemini-2.0-flash",
    description="Looks up today’s stock price for a company; returns price and % change; delegates back if ticker can’t be resolved.",
    instruction="""- If `{company?}` is missing, ask: "Which company?"
- Resolve the company name to a ticker symbol.
- Use the `get_stock_quote` tool to fetch the quote.
- If ticker lookup or the quote tool fails, briefly say so and call `transfer_to_agent(agent_name="manager")`.
- Output the result in the format: "{TICKER}: ${price} ({changePct}%) — as of {timestamp}"
- If the market is closed, note it in your response.""",
    tools=[get_stock_quote],
)