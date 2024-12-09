import os
import pytest
from dotenv import load_dotenv
from aptos_agent.agents.portfolio import portfolio_agent
from aptos_agent.agents.unusual_activity import unusual_activity_agent
from aptos_agent.agents.transfers import init_agents


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and before performing collection
    and entering the run test loop.
    """
    load_dotenv()  # Load environment variables from .env file
    init_agents(portfolio_agent, unusual_activity_agent)


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment variables."""
    # Set up any test-specific environment variables here
    os.environ["APTOS_NODE_URL"] = "https://api.mainnet.aptoslabs.com/v1/graphql"
    yield
    # Clean up after tests if needed
