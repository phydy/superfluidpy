from curses.ascii import isupper
from brownie import accounts
import os


'''
    @dev: loads a local development accounts
    NOTE: the argument should be an ineger
'''
def account(account):
    return accounts[account]

'''
    @dev: loads a locEally stored account
    NOTE: you will be prompted to input a password
'''
def load_account(account):
    return accounts.load(account)


'''
    @dev: gets an account from an environment variable stored at $ENV_NAME
'''
def get_account(ENV_NAME):
    #name = isupper(ENV_NAME)
    return os.environ.get(ENV_NAME)

account = "ACCOUNT"
#load_account("0")

print(get_account(account))