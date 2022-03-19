import py
import pytest
from superfluid_finance.supertoken_factory import SupertokenFatory 
from superfluid_finance import accounts_provider as a, con_addresses

@pytest.fixture(scope="modeule")
def factory():
    return SupertokenFatory("kovan", "infura")

def test_view_function(factory):
    host =factory.get_Host()
    host_local = con_addresses.addresses[factory.network]["host"]

    assert(host == host_local)