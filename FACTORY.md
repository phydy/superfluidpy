# The Super Token Factory Class

## This class gives us all the functionality to work with the superToken Factory contract

To interact with the supertoken Factory contract on a particular chain, You first connect to the target chain

### Importing the pachage
```
>>> from superfluid import supertoken_factory
>>> import accounts_provider as a
```
### instanciate an account object
```
>>> account = a.get_account("ENV_VARIABLE_NAME")
```
### Instantiate The factory contract on that chain

```
>>> factory = supertoken_factory.SupertokenFatory("kovan", "infura")
```

Now you have a factory object connected to a factory contract on the active chain

Interactig with the factory contract is as easy as calling methods of the factory object

## Functions on the factory object

## View Functions
**There are only two view functions**

### Get Host
```
>>> factory.get_host()
```
It returns the host address

### Get Super Token Logic

```
>>> factory.get_supertoken_logic()
```
Get the current super token logic used by the factory

## Write functions
**Write functions change the state of the blockchain hence, require you to sign the transaction with an acount**

```
>>> factory.initialize(account)
```
@dev Initialize the contract


## Wrapping Tokens
### Wrap with decmals
```
>>> factory.create_ERC20Wraper_decimals(
        underlying_token,
        underlyingDecimals,
        upgradability,
        name,
        symbol,
        account
    )
```
### Breakdown
 * Creates new super token wrapper for the underlying ERC20 token
 * @param underlyingToken Underlying ERC20 token
 * @param underlyingDecimals Underlying token decimals
 * @param upgradability Upgradability mode
 * @param name Super token name
 * @param symbol Super token symbol

### Wrap without decimals
```
>>> factory.create_ERC20Wraper(
        underlying_token,
        upgradability,
        name,
        symbol,
        account
    )
```
### Breakdown
 * @dev Create new super token wrapper for the underlying ERC20 token with extra token info
 * @param underlyingToken Underlying ERC20 token
 * @param upgradability Upgradability mode
 * @param name Super token name
 * @param symbol Super token symbol
 *
 * NOTE:
 * - It assumes token provides the .decimals() function

## Initialize custom Super Token
```
>>> factory.initialize_custom_supertoken(
        customSuperTokenProxy,
        account
    )