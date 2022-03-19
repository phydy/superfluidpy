import pytest

from superfluid_finance import account_provider, provider


def test_local_stored():
    account = account_provider.load_account("0")
    w3 = provider.infura_connect("kovan")
    assert(w3.isChecksumAddress(account.address))