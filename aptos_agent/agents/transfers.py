from rich.prompt import Prompt
from swarm.core import Result

# This will store all agent transfer functions
_portfolio_agent = None
_unusual_activity_agent = None


def init_agents(portfolio, unusual):
    """Initialize agent references"""
    global _portfolio_agent, _unusual_activity_agent
    _portfolio_agent = portfolio
    _unusual_activity_agent = unusual


def transfer_to_portfolio(context_variables):
    """Transfer to the portfolio analysis agent."""
    if _portfolio_agent is None:
        raise RuntimeError("Portfolio agent not initialized. Call init_agents first.")
    return Result(
        value="Successfully transferred to portfolio agent",
        context_variables=context_variables,
        agent=_portfolio_agent,
    )


def transfer_to_unusual_activity(context_variables):
    """Transfer to the unusual activity monitoring agent."""
    if _unusual_activity_agent is None:
        raise RuntimeError(
            "Unusual activity agent not initialized. Call init_agents first."
        )
    return Result(
        value="Successfully transferred to unusual activity agent",
        context_variables=context_variables,
        agent=_unusual_activity_agent,
    )


def get_account_address():
    account_address = Prompt.ask("Enter Aptos account address to analyze")
    # validate account address
    if not account_address.startswith("0x") or len(account_address) != 66:
        return "Invalid account address"

    return Result(
        value="Successfully retrieved account address",
        context_variables={"account_address": account_address},
    )
