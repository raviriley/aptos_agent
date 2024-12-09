import pytest
from aptos_agent.agents.portfolio import get_account_balances


@pytest.fixture
def valid_account():
    return {
        "account_address": "0x8824ebb6e0d60656f6d4d5bbc408805d9ca6b984aad78b16f42b1dae545d6762"
    }


@pytest.fixture
def invalid_account():
    return {"account_address": "invalid_address"}


def test_get_account_balances_success(valid_account):
    """Test successful retrieval of account balances."""
    response = get_account_balances(valid_account)
    assert response is not None
    assert isinstance(response, str)
    assert "Successfully" in response


def test_get_account_balances_invalid_address(invalid_account):
    """Test handling of invalid account address."""
    response = get_account_balances(invalid_account)
    assert response is not None
    assert isinstance(response, str)
    assert "Error" in response


def test_get_account_balances_missing_address():
    """Test handling of missing account address."""
    with pytest.raises(KeyError):
        get_account_balances({})
