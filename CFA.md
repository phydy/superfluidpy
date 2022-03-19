# **The Constant Flow Agreement Module**

This Module enables us to interact with the cfa interface from our python environment.

## **Working ith the module**

## Load an account using 
[**the account_provider module**](/ACOUNT.md)

## Or using brownie
```
from brownie import accounts
```
```
account = accounts.load(<local account name>)
```

## Import The module
```
>>> from superfluid_finance.CFAV1 import CFA 
```
This module uses one class to create an instance of the contract that is used to create the methods in the module. like the super token module, this one also require us to instantiate a class before interacting with the interface. The class automatically loads the contract on the active chain.

This import gets us ready to use cfa functions

```
>>> cfa = CFA("kovan", "alchemy")
```

```
>>>cfa.getFlow(token, sender, receiver)
```
### Returns the flow info of a flow of token from sender to receiver

 . @dev Get the flow data between `sender` and `receiver`.
 . token Super token address.
 . sender Flow receiver.
 . receiver Flow sender.
 . timestamp Timestamp of when the flow is updated.
 . flowRate The flow rate.
 . deposit The amount of deposit the flow.
 . owedDeposit The amount of owed deposit of the flow.

```
>>>(0,0,0,0)
```
the return valueis a tuple
## **Create A Flow**

```
>>>cfa.createFlow(token, receiver, flowRate, context, account)
```
### Returns a transaction hash