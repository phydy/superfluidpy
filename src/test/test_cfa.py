
import pytest
import superfluid_finance.CFAV1 as cfa
from superfluid_finance import account_provider as a
import web3
from superfluid_finance.provider import infura_connect
from superfluid_finance.helper import AgreementDataGiver
from brownie import convert

@pytest.fixture(scope="module")
def data_giver():
    return AgreementDataGiver("kovan", "infura")

@pytest.fixture(scope="session")
def account1():
    return a.load_account("0")

@pytest.fixture(scope="session")
def account2():
    return a.load_account("1")

@pytest.fixture(scope="session")
def _cfa():
    return cfa.CFA("kovan", "infura")

@pytest.fixture(scope="module")
def w3():
    return infura_connect("kovan")

@pytest.fixture(scope="module")
def token(w3):
    return w3.toChecksumAddress("0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09")


def test_net_flow(w3, _cfa):
    #_cfa.get_DepositRequiredForFlowRate(w3.toChecksumAddress("0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09"), 256888555)
    net =_cfa.get_net_flow(
        w3.toChecksumAddress("0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09"),
        w3.toChecksumAddress("0xaC18157FFFdc96C9724eB1CF42eb05F8f70e645B")
    )

def test_get_flow(w3, _cfa):
    
    _cfa.get_flow(
        w3.toChecksumAddress("0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09"),
        w3.toChecksumAddress("0xaC18157FFFdc96C9724eB1CF42eb05F8f70e645B"),
        w3.toChecksumAddress("0xC6dfd274bB7ed085d7465CF848C1F0D4065d6dF6")
    )

def test_create_flow(token, account1):
    return _cfa.create_flow(
        token,
        "0xC6dfd274bB7ed085d7465CF848C1F0D4065d6dF6",
        120000000000000,
        "",
        account1
    )


