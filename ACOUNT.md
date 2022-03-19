# The account module

This module is built ontop of the brownie framework.

You can choose to stick with the brownie accounts if you understand how to use the bronie accounts object

## Functions

This module has only three functions that enable one to easily access a user's accounts

### local development acoounts

```
>>> from superfluid import accounts_provider as a
```
```
>>> account = a.account(0)
```
This will return an accounts object that you can use to sign transactions when working in a local development environment

### Locally stored accounts

```
>>> import accounts_provider as a
```
```
>>> account = a.load_account("string")
```
This will return an accounts object that you can use to sign transactions on a live network.

### Accounts stored as enviroment Variables
```
>>> import accounts_provider as a
```
```
>>> account = a.get_account("STRING")
```

>you will be promtedt to enter the `account password` to unlock the account

## **NOTE** the sting is the name of the localy stored account.
### You can find more about storing an account locally with [brownie](https://eth-brownie.readthedocs.io/en/stable/account-management.html#local-accounts)

With this account object, you can sign and send transactions from your console in the superfluid_finance module