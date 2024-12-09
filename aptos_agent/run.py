from swarm import Agent
from swarm.repl import run_demo_loop
from dotenv import load_dotenv
from agents.unusual_activity import unusual_activity_agent
from agents.portfolio import portfolio_agent
from agents.transfers import (
    init_agents,
    transfer_to_portfolio,
    transfer_to_unusual_activity,
    get_account_address,
)


load_dotenv()

init_agents(portfolio_agent, unusual_activity_agent)


triage_agent = Agent(
    name="Financial Services Triage Agent",
    instructions="""You are a triage agent for financial services on Aptos blockchain.
    - If there is no account address in the context variables, call the get_account_address function
    - For questions about token balances and portfolio analysis, transfer to the portfolio agent
    - For questions about transaction history and unusual activity monitoring, transfer to the unusual activity agent
    Be helpful and guide users to the right specialized agent.""",
    functions=[
        transfer_to_portfolio,
        transfer_to_unusual_activity,
        get_account_address,
    ],
)


def main():
    # client = Swarm()

    # Set up context variables
    context_variables = {"account_address": ""}

    # Get account address from user
    account_address_response = get_account_address()
    print(f"Account address update: {account_address_response}")
    print(f"Context variables: {context_variables}")

    run_demo_loop(triage_agent, context_variables, stream=True, debug=False)


if __name__ == "__main__":
    main()
