from rich.prompt import Prompt
from swarm.core import Result

# This will store all agent transfer functions
portfolio_agent = None
unusual_activity_agent = None


def init_agents(portfolio, unusual):
    """Initialize agent references"""
    global portfolio_agent, unusual_activity_agent
    portfolio_agent = portfolio
    unusual_activity_agent = unusual


def transfer_to_portfolio():
    """Transfer to the portfolio analysis agent."""
    return portfolio_agent


def transfer_to_unusual_activity():
    """Transfer to the unusual activity monitoring agent."""
    return unusual_activity_agent


def get_account_address():
    account_address = Prompt.ask("Enter Aptos account address to analyze")
    # validate account address
    if not account_address.startswith("0x") or len(account_address) != 66:
        return "Invalid account address"

    return Result(
        value="Successfully retrieved account address",
        context_variables={"account_address": account_address},
    )
