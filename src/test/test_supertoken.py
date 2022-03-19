import pytest
from superfluid_finance import supertoken, account_provider

def test_name():
    token = supertoken.SuperToken("kovan", "infura", "0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09")
    print(token.name())

def test_transfer():
    token = supertoken.SuperToken(
        "kovan",
        "infura",
        "0x43F54B13A0b17F67E61C9f0e41C3348B3a2BDa09"
    )
    x = token.balance_of("0xaC18157FFFdc96C9724eB1CF42eb05F8f70e645B")
    account = account_provider.load_account("0")
    amount = 1000000000000000000000
    token.transfer("0xC6dfd274bB7ed085d7465CF848C1F0D4065d6dF6", amount, account)
    