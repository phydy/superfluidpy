import pytest
from superfluid_finance.IDAV1 import IDA
from superfluid_finance import account_provider as a
import web3
from superfluid_finance.provider import infura_connect

@pytest.fixture
def account1():
    return a.load_account("0")

@pytest.fixture
def account2():
    return a.load_account("1")

@pytest.fixture
def _ida():
    return IDA("kovan", "infura")

@pytest.fixture
def w3():
    return infura_connect("kovan")
