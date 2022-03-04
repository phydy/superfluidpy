# The Constant Host Module

This Module enables us to interact with the superfluid interface from our python environment.

## Working ith the module

### Connect to an rpc endpoint using [**the provider Module**](/PROVIDE.md)
### Load an account using [**the account_provider module**](/ACOUNT.md)

### Import The module
```
>>> from superfluidpy.host import * 
```
This module uses one class to create an instance of the contract that is used to create the methods in the module. Unlike the super token module, this one does not require us to instantiate a class before interacting with the interface. The class automatically loads the interface on the active chain.

This import gets us ready to use functions withought having to specify the host address



