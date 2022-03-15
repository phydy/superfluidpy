# Superfluid Python Module

## How to work with the package
You need to have python3 installed on your machine

### Quick start
Open the terminal then run these commands in your terminal.

**1. Install the project**
```
$ pip3 install superfluid_finance
```
**2. set your environment variables**

set your environment variables for the RPC provider

if infura,
```
$ export WEB3_INFURA_PROJECT_ID="0xhdgfyugwOFGF..."
```
if you use moralis endpoints

```
$ export MORALIS_{CHAIN}_URL="https://morali....."
```
`**eg:** MORALIS_KOVAN_URL`

For Alchemy,
```
$ export ALCHEMY_{CHAIN}_URL= "https://alchemy....."
```

if you wish for another provider, open an issue on github and we will try to includ it soonest

**3. Navigate to the python interpreter**
```
$ python3
```
```
Python 3.9.7 (default, Sep 10 2021, 14:59:43) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>|
```
**4. import the package:**
```
>>> 
>>> from superfluid_finance.host import Host
```

Cconfirm the pachage is imported by running these commands.

**NOTE:** ensure you have exported the appropirate environment variables
```
>>> import provider
>>> provider.infura_connect(kovan)
```

### Test the host contract of your chain by running

```
>>> 
>>> ht = Host("kovan", "infura")
>>> ht.get_address()
'0xF0d7d1D47109bA426B9D8A3Cde1941327af1eea3'
```

## Specialized examples

**Working with accounts [accounts](/ACOUNT.md)**

**Connecting to an [RPC Endpoint](/PROVIDE.md)**

**Interacting with The [Factory Contract](/FACTORY.md)**

**Interacting with a [Super Token](/SUPERTOKEN.md)**

**Interacting with The [Host Contract](/HOST.md)**

**Interacting with The [Constant Flow Agreement](/CFA.md)**

**Interacting with The [Instant Distribution Agreement](/IDA.md)**
