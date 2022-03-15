# The Provider module

This module is built ontop of Web3py module.

It allows us to easily connect to an RPC endpoind in the python interpreter

## Functions

This module has four functions that enable one to easily connect to an RPC endpiont

Each function uses a different provider

### local development network

```
>>> from superfluid_finance import provider as p
```
```
>>> p.connect_to_local()
```
This will listen at port 8545 and connect to a local development network if active and revert when a local instance is not running

Confirm this works by running
```
>>> from brownie import network
```
```
>>>network.is_connected()
True
```

### Live Networks

```
>>> from superfluid-finance import provider as p
```
```
>>> p.infura_connect("kovan")
```
```
>>> p.moralis_connect("KOVAN")
```
```
>>> p.alchemy_connect("KOVAN")
```

***NOTE:*** **The arguments for alchemy and Moralis should be given in upercase**

This will return an accounts object that you can use to sign transactions on a live network.