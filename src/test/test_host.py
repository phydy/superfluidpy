import pytest
from superfluid_finance.host import Host
from superfluid_finance import account_provider as a, con_addresses, CFAV1
import web3
from superfluid_finance.provider import infura_connect

@pytest.fixture
def account1():
    return a.load_account("0")

@pytest.fixture
def account2():
    return a.load_account("1")

@pytest.fixture
def _host():
    return Host("kovan", "infura")

@pytest.fixture
def w3():
    return infura_connect("kovan")

@pytest.fixture(scope="module")
def token(w3):
    return w3.toChecksumAddress("0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09")

@pytest.fixture(scope="session")
def _cfa():
    return CFAV1.CFA("kovan", "infura")

def test_get_factory(_host):
    factory = _host.get_SuperTokenFactory()
    factory2 = con_addresses.addresses[_host.network]["factory"]

    assert(factory == factory2)

def test_call_agreement(account1, _host, token, w3, _cfa):
    amount = 25000000000000000
    encoded_data = _cfa.encodeABI(
        fn_name="createFlow",
        args=[
            token,
            "0xC6dfd274bB7ed085d7465CF848C1F0D4065d6dF6",
            amount,
            ""
        ]
    )
    bytes_data = w3.toBytes(hexstr=f"{encoded_data}")
    actual_data = bytes_data[:(len(bytes_data) - 32)]
    return_value = _host.call_agreement(
        _cfa.get_address(),
        actual_data, 
        "",
        account1
    )

    flow_tuple = _cfa.get_flow(
        token,
        account1.address,
        "0xC6dfd274bB7ed085d7465CF848C1F0D4065d6dF6",
    )

    assert(
        flow_tuple[1] == amount
    )