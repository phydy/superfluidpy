# The Constant Host Module

This Module enables us to interact with the superfluid interface from our python environment.

## Working ith the module

### Load an account using [**the account_provider module**](/ACOUNT.md)

### Import The module
```
>>> from superfluid_finance.host import Host 
```

```
>>> host = Host("kovan", "infura")
```
This module uses one class to create an instance of the contract that is used to create the methods in the module.

Unlike the super token module, this one does not require us to instantiate a class before interacting with the interface.

The class automatically loads the interface on the active chain.

This import gets us ready to use functions withought having to specify the host address

### Get the address of the supertoken factoey contract
```
>>>host.get_SuperTokenFactory()
```

### Calling an aggreement

The best way to call one of the superfluid agreements is to use the individual agreement class.

However you can also call an agreement using the host class but you will have to instantiate the agreement class you intend to call

```
from superfluid_finance.IDAV1 import IDA

>>> ida = IDA("kovan", "infura").get_interface()
```
the you will have to encode the function you want to call with its arguments

```
>>> encoded_data = ida.encodeABI(
>>>     fn_name="updateIndex",
>>>     args=[
>>>         token,
>>>         IndexID,
>>>         indexValue,
>>>         ""
>>>     ]
>>> )
```
Then you convert the data to bytes

```
>>> bytes_data = self.w3.toBytes(hexstr=f"{encoded_data}")
```
After that you remove the last 32 bytes of the encoded data
```
>>> actual_data = bytes_data[:(len(bytes_data) - 32)]
```
then call the call_agreement function on the Host class with the `actual_data` as the call data

```
>>>  host.call_agreement(
>>>     self.get_address(), 
>>>     actual_data,
>>>     ctx,
>>>     account
>>> )
```


