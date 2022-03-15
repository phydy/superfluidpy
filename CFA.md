# The Constant Flow Agreement Module

This Module enables us to interact with the cfa interface from our python environment.

## Working ith the module

### Connect to an rpc endpoint using [**the provider Module**](/PROVIDE.md)
### Load an account using [**the account_provider module**](/ACOUNT.md)

### Import The module
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
Returns the flow info of a flow of token from sender to receiver