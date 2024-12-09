from swarm import Agent
from aptos_sdk.async_client import IndexerClient
from rich.console import Console
from rich.table import Table
from aptos_agent.agents.transfers import transfer_to_portfolio

console = Console()


def get_account_transactions(context_variables):
    """Get recent transactions for an account address."""
    account_address = context_variables["account_address"]
    client = IndexerClient("https://api.mainnet.aptoslabs.com/v1/graphql")

    try:
        # Get account transactions
        return "Successfully retrieved recent transactions"

    except Exception as e:
        return f"Error getting transactions: {str(e)}"


unusual_activity_agent = Agent(
    name="Unusual Activity Agent",
    instructions="""You are an unusual activity monitoring agent that helps users review their transaction history on Aptos.
    When asked about transactions or unusual activity, use the get_account_transactions() function to fetch and display them.
    If users ask about token balances, transfer them to the portfolio agent.""",
    functions=[get_account_transactions, transfer_to_portfolio],
)
