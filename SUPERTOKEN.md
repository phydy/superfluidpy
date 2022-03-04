# SuperToken Class

This class avails all the methods required to interact with a Super token.

Initializing the class requires one to give the address of the supretoken as an argument.

This creates a Super Token object linked to the interface of the token address provided.

You can use the token addresses module to get common supertoken addresses available on the superfluid's network page

## Working with the class
### Connect to an rpc endpoint using [**the provider Module**](/PROVIDE.md)
### Load an account using [**the account_provider module**](/ACOUNT.md)

### import the supertoken and token_addresses modules

**You can ignore the token_addresses if you are working with a custom supertoken**

```
>>> from superfluidpy import supertoken, token_addresses
```

```
>>> address = kovan["fDAIx"]
```
You now have the fake DAI address wrapper address provided by superfluid

```
>>> token = SuperToken(address)
```
This creates an object with all the supertoken functions.

One can now interact with the Super Token interface by referencing this token object.

## Functions

### View Functions

#### **Name**
Get the name of the SuperToken

```
>>> token.name()
```
It returns a string of the name

#### **Symbol**
Get the name of the SuperToken

```
>>> token.symbol()
```
It returns a string of the token symbol

#### **Decimals**
Get the number of decimals supported by the token
```
>>> token.decimals()
```
It returns an unsigned integer of the number of decimals used to get its user representation.

For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`).

Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called.

#### **Total Supply**
Get the token's total supply

```
>>> token.total_supply()
```
Returns an unsigned integer of the token's total supply

#### **Balance of**

Get the token balance of an address

```
>>> token.balance_of(address_to_check)
```
Returns an unsigned integer

#### **Allowance**

Checks the allowance of an address against another addresse's tokens

```
>>> token.allowance(
        _owner,
        _spender
    )
```
@param _owner The address of the account owning tokens

@param _spender The address of the account able to transfer the tokens.

@return remaining Amount of remaining tokens allowed to spent

#### **Granularity**
@dev Returns the smallest part of the token that is not divisible. This means all token operations (creation, movement and destruction) must have amounts that are a multiple of this number.

For super token contracts, this value is 1 always

```
token.granularity()
```

#### **Is operator For**
Checks if an `_operator` is an operator to another `_holder` tokens

```
>>> token.is_operator_for()
```
It returns a bool

#### **Default Operator**

@dev Returns the list of default operators. These accounts are operators
for all token holders, even if {authorizeOperator} was never called on
them.
This list is immutable, but individual holders may revoke these via
{revokeOperator}, in which case {isOperatorFor} will return false.

```
>>> token.default.operator()
```

#### Get underlying token
Get the underlying ERC20 token
```
>>> token.get_uderlying_token()
```
Returns an `address` of the underlying token contract 

### **Write Functions**

#### **Transfer Supertokens**
Transfer tokens to an address from the message signer
@param _to The address of the recipient
@param _value The amount of token to be transferred


```
>>> token.transfer(
        _to,
        _value,
        account
    )
```
#### **Transfer From**
Transfer tokens from an address to a destination address. Requires the message signer to have an allowance equal to the value being transfered.

```
>>> token.transfer_from(
        _from,
        to,
        _value,
        account
    )
```

#### **Approve**
@notice `msg.sender` approves `_addr` to spend `_value` tokens
@param _spender The address of the account able to transfer the tokens
@param _value The amount of wei to be approved for transfer

```
>>> token.approve(
        _spender,
        _value,
        account
    )
```

#### **Increase Allowance**
@dev Atomically increases the allowance granted to `spender` by the caller.
This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve

```
>>> token.increase_allowance(
        __spender,
        _value,
        account
    )
```

#### **Decrease Allowance**
@dev Atomically decreases the allowance granted to `spender` by the caller.
This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve
```
>>> token.decrease_allowance(
        _spender,
        value,
        account
    )
```

#### **Send**
 @dev Moves `_amount` tokens from the caller's account to `_recipient`.

 If send or receive hooks are registered for the caller and `recipient`,
 the corresponding functions will be called with `_calldata` and empty
 `operatorData`.
 Requirements
 - the caller must have at least `_amount` tokens.
 - `_recipient` cannot be the zero address.
 - if `recipient` is a contract, it must implement the {IERC777Recipient}
 interface.


```
>>> token.send(
        _rcepient,
        _amount,
        _calldata,
        account
    )
```

#### **Burn**

@dev Destroys `_amount` tokens from the caller's account, reducing the
total supply.
If a send hook is registered for the caller, the corresponding function
will be called with `data` and empty `operatorData`. See {IERC777Sender}.

```
>>>token.burn(
        _amount,_data,
        account
    )
```

#### Authorize Operator
@dev Make an account an operator of the caller
`operator` cannot be calling address
```
>>> token.authorize_operator(
        operator,
        account
    )
```

#### Revoke Operator
@dev Revoke an account's operator status for the caller
`operator` cannot be calling address.

```
>>> token.revoke_operator(
        operator,
        account
    )
```
#### Transfer All
@dev Transfer all available balance from `transaction signer` to `recipient`

```
>>> token.transfer_all()
```

#### Upgrade

@dev Upgrade ERC20 to SuperToken.
@param amount Number of tokens to be upgraded (in 18 decimals)
NOTE: It will use ´transferFrom´ to get tokens. Before calling this
function you should ´approve´ this contract

```
>>> token.ugrade(
        amount,
        account
    )
```


#### Upgrade To

@dev Upgrade ERC20 to SuperToken and transfer immediately
@param to The account to received upgraded tokens
@param amount Number of tokens to be upgraded (in 18 decimals)
@param data User data for the TokensRecipient callback
NOTE: It will use ´transferFrom´ to get tokens. Before calling this
function you should ´approve´ this contract


```
>>> token.ugrade_to(
        _to,
        amount,
        data,
        account
    )
```

#### Downgrade
@dev Downgrade SuperToken to ERC20.
@dev It will call transfer to send tokens
@param amount Number of tokens to be downgraded
```
>>> token.downgrade(
        amount,
        account
    )
```