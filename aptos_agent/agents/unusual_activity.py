from swarm import Agent
from aptos_sdk.async_client import IndexerClient
from rich.console import Console
from rich.table import Table
from aptos_agent.agents.transfers import transfer_to_portfolio
import asyncio

console = Console()


def get_account_transactions(context_variables):
    account_address = context_variables["account_address"]
    if not account_address.startswith("0x") or len(account_address) != 66:
        return "Error: Invalid account address"
    account_transactions = asyncio.run(_get_account_transactions(context_variables))
    # print(f"Account transactions: {account_transactions}")
    return account_transactions


async def _get_account_transactions(context_variables):
    """Get recent transactions for an account address."""
    account_address = context_variables["account_address"]
    client = IndexerClient("https://api.mainnet.aptoslabs.com/v1/graphql")

    graphql_query = """
    query GetAccountTransactionsData($address: String, $limit: Int) {
        account_transactions(
            where: { account_address: { _eq: $address } }
            order_by: {transaction_version: desc}
            limit: $limit
        ) {
            fungible_asset_activities {
                amount
                asset_type
                entry_function_id_str
                is_frozen
                owner_address
            }
            transaction_version
        }
    }
    """
    variables = {"address": account_address, "limit": 200}

    try:
        # Get account transactions
        transactions = await client.query(graphql_query, variables)

        table = Table(title=f"Latest 10 Transactions for {account_address}")
        table.add_column("Version", style="cyan")
        table.add_column("Asset Type", style="green")
        table.add_column("Amount", style="green")
        table.add_column("Entry Function ID", style="green")
        table.add_column("Is Frozen", style="green")
        table.add_column("Owner Address", style="green")

        for txn in transactions["data"]["account_transactions"][
            :10
        ]:  # Show last 10 transactions
            table.add_row(
                str(txn["transaction_version"]),
                txn["fungible_asset_activities"][0]["asset_type"],
                str(txn["fungible_asset_activities"][0]["amount"]),
                txn["fungible_asset_activities"][0]["entry_function_id_str"],
                str(txn["fungible_asset_activities"][0]["is_frozen"]),
                txn["fungible_asset_activities"][0]["owner_address"],
            )

        console.print(table)
        return f"Successfully retrieved recent transactions: {transactions}"

    except Exception as e:
        return f"Error getting transactions: {str(e)}"


unusual_activity_agent = Agent(
    name="Unusual Activity Agent",
    instructions="""You are an unusual activity monitoring agent that helps users review their transaction history on Aptos.
    When asked about transactions or unusual activity, use the get_account_transactions() function to fetch and display them.
    If there are a large number of frozen transactions, alert the user.
    If there are sequential transactions by transaction version, alert the user.
    If users ask about token balances, transfer them to the portfolio agent.""",
    functions=[get_account_transactions, transfer_to_portfolio],
)
