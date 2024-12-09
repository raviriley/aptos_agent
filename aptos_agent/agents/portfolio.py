from swarm import Agent
from aptos_sdk.async_client import IndexerClient
from rich.console import Console
from rich.table import Table
from aptos_agent.agents.transfers import (
    get_account_address,
)
import asyncio

console = Console()


def get_account_balances(context_variables):
    account_address = context_variables["account_address"]
    if not account_address.startswith("0x") or len(account_address) != 66:
        return "Error: Invalid account address"
    account_balances = asyncio.run(_get_account_balances(context_variables))
    print(f"Account balances: {account_balances}")
    return account_balances


async def _get_account_balances(context_variables):
    """Get token balances for an account address."""
    account_address = context_variables["account_address"]
    client = IndexerClient("https://api.mainnet.aptoslabs.com/v1/graphql")

    graphql_query = """
    query GetFungibleAssetBalances($address: String) {
        current_fungible_asset_balances(
            where: {owner_address: {_eq: $address}},
            limit: 100,
            order_by: {amount: desc}
        ) {
            asset_type
            amount
        }
    }
    """
    variables = {"address": account_address}

    try:
        # Get account resources which include token balances
        asset_balances = await client.query(graphql_query, variables)

        # print(asset_balances)

        # Create a table to display balances
        table = Table(title=f"Token Balances for {account_address}")
        table.add_column("Token", style="cyan")
        table.add_column("Balance", style="green")

        for asset_balance in asset_balances["data"]["current_fungible_asset_balances"]:
            token_type = asset_balance["asset_type"]
            balance = int(asset_balance["amount"])
            table.add_row(token_type, str(balance))

        console.print(table)
        return f"Successfully retrieved account balances: {asset_balances}"

    except Exception as e:
        return f"Error getting account balances: {str(e)}"


portfolio_agent = Agent(
    name="Portfolio Analysis Agent",
    instructions="""You are a portfolio analysis agent that helps users understand their token balances on Aptos.
    When asked about balances, use the get_account_balances() function to fetch and display them.
    If users ask about transaction history or unusual activity, transfer them to the unusual activity agent.
    If the user supplies an account address or asks for information about a new account address, call the get_account_address function.""",
    functions=[get_account_balances, get_account_address],
)
