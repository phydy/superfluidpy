# The Instant Distribution Agreement Module

This Module enables us to interact with the ida interface from our python environment.

## Working ith the module

### Load an account using [**the account_provider module**](/ACOUNT.md)

### Import The module
```
>>> from superfluid_finance.ida import IDA
```
This module uses one class to create an instance of the contract that is used to create the methods in the module. Unlike the super token module, this one does not require us to instantiate a class before interacting with the interface. The class automatically loads the contract on the active chain.

This import gets us ready to use functions

```
>>>ida = IDA("mumbai", "infura")
```

with the ida oject created, you can interact with the agreement by calling the class functions and passing the parameters as you would in solidity or with the javascrip sdk

you can get the superfluid test tokens using the token_addresses module

```
from superfluid_finance import token_addresses
```
```
token = token_addresses.mumbai["fdaiX"]
```

### Get Index

    * @dev Query the data of a index.
    * @param token Super token address.
    * @param publisher The publisher of the index.
    * @param indexId Id of the index.

```
ida.get_index(token, <publisher_address>, <indexID>)
```

     * @return exist Does the index exist.
     * @return indexValue Value of the current index.
     * @return totalUnitsApproved Total units approved for the index.
     * @return totalUnitsPending Total units pending approval for the index.

### calculate distribution

```
ida.calculate_distribution(token, <publisher_address>, <indexID>, <amount>)
```
## Write functions
To send transactions on the blockchain instantiate an account using the [accout_provider module](./ACOUNT.md)

### create Idex
    * @param token Super token address.
    * @param indexId Id of the index

```
ida.create_index(token, <index>, <context>, account)
```
### update Index

     * @param token Super token address.
     * @param indexId Id of the index.
     * @param indexValue Value of the index.

```
ida.update_index(token, <IndexID>, <indexValue>, <ctx>, account)
```

### Distribute index

     * @param token Super token address.
     * @param indexId Id of the index.
     * @param amount The amount of tokens desired to be distributed.

```
ida.distribute_ida(tpken, <index>, <amount>, account)
```

