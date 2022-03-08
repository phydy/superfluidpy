from brownie import *
from brownie import accounts, chain
from con_addresses import addresses, is_allowed_network
from Supertoken import abi
from provider import *
import json

addresses

class SuperToken:
    def __init__(self, network, provider, address):
        self.address = address
        self.network=network
        self.provider=provider

    
    def get_interface(self):
        w3 = provider_connect(self.provider, self.network)
        return w3.eth.contract(address=self.address, abi=json.dumps(abi))
    
    '''
        /**
        * @dev Returns the name of the token.
        */
    '''
    def name(self):
        interface = self.get_interface()
        return interface.functions.name().call()
    
    '''
    /**
        * @dev Returns the symbol of the token, usually a shorter version of the
        * name.
     */
    '''
    def symbol(self):
        interface = self.get_interface()
        return interface.functions.symbol().call()
    

    '''
    /**
         * @dev Returns the number of decimals used to get its user representation.
         * For example, if `decimals` equals `2`, a balance of `505` tokens should
         * be displayed to a user as `5,05` (`505 / 10 ** 2`).
         *
         * Tokens usually opt for a value of 18, imitating the relationship between
         * Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is
         * called.
         *
         * NOTE: SuperToken always uses 18 decimals.
         *
         * Note: This information is only used for _display_ purposes: it in
         * no way affects any of the arithmetic of the contract, including
         * {IERC20-balanceOf} and {IERC20-transfer}.
         */
    '''
    def decimals(self):
        interface = self.get_interface()
        return interface.functions.decimals()
    

    '''
    /**
         * @dev See {IERC20-totalSupply}.
    */
    '''
    def total_supply(self):
        interface = self.get_interface()
        return interface.functions.totalSupply()
    
    '''
        /// @param _owner The address from which the balance will be retrieved
        /// @return balance the balance
    '''
    def balance_of(self, _owner):
        interface = self.get_interface()
        return interface.functions.balanceOf(_owner).call()


    '''
        /// @notice send `_value` token to `_to` from `account`
        /// @param _to The address of the recipient
        /// @param _value The amount of token to be transferred
        /// @return success Whether the transfer was successful or not

    '''

    def transfer(self, _to, _value, account):
        interface = self.get_interface()
        return interface.functions.transfer(
            _to,
            _value
        ).transact({"from": account})

    '''
        * @param _owner The address of the account owning tokens
        * @param _spender The address of the account able to transfer the tokens
        * @return remaining Amount of remaining tokens allowed to spent

    '''
    def allowance(self, _owner, _spender):
        interface = self.get_interface()
        return interface.functions.allowance(
            _owner,
            _spender
        ).call()

    '''
        * @notice `msg.sender` approves `_addr` to spend `_value` tokens
        * @param _spender The address of the account able to transfer the tokens
        * @param _value The amount of wei to be approved for transfer
        * @return success Whether the approval was successful or not

    '''
    def transfer_from(
        self, 
        _from, 
        _to,
        _value,
        account
    ):
        interface = self.get_interface()
        return interface.functions.transferFrom(
            _from,
            _to,
            _value
        ).transact({"from": account})
    '''
    * @notice `msg.sender` approves `_addr` to spend `_value` tokens
    * @param _spender The address of the account able to transfer the tokens
    * @param _value The amount of wei to be approved for transfer
    * @return success Whether the approval was successful or not

    '''
    def approve(self, _spender, _value, account):
        interface = self.get_interface()
        return interface.functions.approve(
            _spender,
            _value
        ).transact({"from": account})
    ''' 
        /**
         * @dev Atomically increases the allowance granted to `spender` by the caller.
         *
         * This is an alternative to {approve} that can be used as a mitigation for
         * problems described in {IERC20-approve}.
         *
         * Emits an {Approval} event indicating the updated allowance.
         *
         * Requirements:
         *
         * - `spender` cannot be the zero address.
    */
    '''
    def increase_allowance(self, _spender, value, account):
        interface = self.get_interface()
        return interface.functions.increaseAllowance(
            _spender,
            value
        ).transact({"from": account})


    '''
        /**
         * @dev Atomically decreases the allowance granted to `spender` by the caller.
         *
         * This is an alternative to {approve} that can be used as a mitigation for
         * problems described in {IERC20-approve}.
         *
         * Emits an {Approval} event indicating the updated allowance.
         *
         * Requirements:
         *
         * - `spender` cannot be the zero address.
         * - `spender` must have allowance for the caller of at least
         * `subtractedValue`.
         */
    '''
    def decrease_allowance(self, _spender, value, account):
        interface = self.get_interface()
        return interface.functions.decreaseAllowance(
            _spender,
            value
        ).transact({"from": account})
    '''
        /**
         * @dev Returns the smallest part of the token that is not divisible. This
         * means all token operations (creation, movement and destruction) must have
         * amounts that are a multiple of this number.
         *
         * For super token contracts, this value is 1 always
         */
    '''
    def granularity(self):
        interface = self.get_interface()
        return interface.functions.granularity().call()

    '''
        /**
         * @dev Moves `amount` tokens from the caller's account to `recipient`.
         *
         * If send or receive hooks are registered for the caller and `recipient`,
         * the corresponding functions will be called with `data` and empty
         * `operatorData`. See {IERC777Sender} and {IERC777Recipient}.
         *
         * Emits a {Sent} event.
         *
         * Requirements
         *
         * - the caller must have at least `amount` tokens.
         * - `recipient` cannot be the zero address.
         * - if `recipient` is a contract, it must implement the {IERC777Recipient}
         * interface.
         */
    '''
    def send(self, _rcepient, _amount, _calldata, account):
        interface = self.get_interface()
        return interface.functions.send(
            _rcepient,
            _amount,
            _calldata
        ).transact({"from": account})
    ''''
        /**
         * @dev Destroys `amount` tokens from the caller's account, reducing the
         * total supply.
         *
         * If a send hook is registered for the caller, the corresponding function
         * will be called with `data` and empty `operatorData`. See {IERC777Sender}.
         *
         * Emits a {Burned} event.
         *
         * Requirements
         *
         * - the caller must have at least `amount` tokens.
         */
    '''
    def burn(self, _amount, _data, account):
        interface = self.get_interface()
        return interface.functions.burn(
            _amount,
            _data
        ).transact({"from": account})


    '''
        /**
         * @dev Returns true if an account is an operator of `tokenHolder`.
         * Operators can send and burn tokens on behalf of their owners. All
         * accounts are their own operator.
         *
         * See {operatorSend} and {operatorBurn}.
         */
    '''
    def is_operator_for(self, _operator, holder):
        interface = self.get_interface()
        return interface.functions.isOperatorFor(
            _operator,
            holder
        ).call()
    '''
        /**
         * @dev Make an account an operator of the caller.
         *
         * See {isOperatorFor}.
         *
         * Emits an {AuthorizedOperator} event.
         *
         * Requirements
         *
         * - `operator` cannot be calling address.
         */
    '''

    def authorize_operator(self, operator, account):
        interface = self.get_interface()
        return interface.functions.authorizeOperator(
            operator
        ).transact({"from": account})
    
    '''
        /**
         * @dev Revoke an account's operator status for the caller.
         *
         * See {isOperatorFor} and {defaultOperators}.
         *
         * Emits a {RevokedOperator} event.
         *
         * Requirements
         *
         * - `operator` cannot be calling address.
         */
    '''
    def revoke_operator(self, operator, account):
        interface = self.get_interface()
        return interface.functions.revokeOperator(
            operator
        ).transact({"from": account})


    '''
        /**
         * @dev Returns the list of default operators. These accounts are operators
         * for all token holders, even if {authorizeOperator} was never called on
         * them.
         *
         * This list is immutable, but individual holders may revoke these via
         * {revokeOperator}, in which case {isOperatorFor} will return false.
         */
    '''
    def default_operators(self):
        interface = self.get_interface()
        return interface.functions.defaultOperators().call()


    '''
        /**
         * @dev Moves `amount` tokens from `sender` to `recipient`. The caller must
         * be an operator of `sender`.
         *
         * If send or receive hooks are registered for `sender` and `recipient`,
         * the corresponding functions will be called with `data` and
         * `operatorData`. See {IERC777Sender} and {IERC777Recipient}.
         *
         * Emits a {Sent} event.
         *
         * Requirements
         *
         * - `sender` cannot be the zero address.
         * - `sender` must have at least `amount` tokens.
         * - the caller must be an operator for `sender`.
         * - `recipient` cannot be the zero address.
         * - if `recipient` is a contract, it must implement the {IERC777Recipient}
         * interface.
         */

    '''

    def operator_send(self, sender, recepient, amount, data, operatorData, account):
        interface = self.get_interface()
        return interface.functions.operatorSend(
            sender,
            recepient,
            amount,
            data,
            operatorData
        ).transact({"from": account})
    '''
        /**
         * @dev Destroys `amount` tokens from `account`, reducing the total supply.
         * The caller must be an operator of `account`.
         *
         * If a send hook is registered for `account`, the corresponding function
         * will be called with `data` and `operatorData`. See {IERC777Sender}.
         *
         * Emits a {Burned} event.
         *
         * Requirements
         *
         * - `account` cannot be the zero address.
         * - `account` must have at least `amount` tokens.
         * - the caller must be an operator for `account`.
         */
    '''
    def operator_burn(self, account_, amount, data, operatorData, account):
        interface = self.get_interface()
        return interface.functions.operatorBurn(
            account_,
            amount,
            data,
            operatorData
        ).transact({"from": account})
    '''
        /**
         * @dev Mint new tokens for the account
         *
         * Modifiers:
         *  - onlySelf
         */
    '''
    def safe_mint(self, account_, amount, account):
        interface = self.get_interface()
        return interface.functions.safeMint(
            account_,
            amount
        ).transact({"from": account})

    '''
       /**
        * @dev Burn existing tokens for the account
        *
        * Modifiers:
        *  - onlySelf
        */
    '''
    def safe_burn(self, account_, amount, userData, account):
        interface = self.get_interface()
        return interface.functions.safeBurn(
            account_,
            amount,
            userData
        ).transact({"from":account})

    '''
        /**
         * @dev Transfer all available balance from `msg.sender` to `recipient`
         */
    '''
    def tranfer_all(self, receipient, account):
        interface = self.get_interface()
        return interface.functions.transferAll(
            receipient
        ).transact(
            {"from":account}
        )


    '''
        /**
         * @dev Upgrade ERC20 to SuperToken.
         * @param amount Number of tokens to be upgraded (in 18 decimals)
         *
         * NOTE: It will use ´transferFrom´ to get tokens. Before calling this
         * function you should ´approve´ this contract
         */
    '''
    def upgrade(self, amount, account):
        interface = self.get_interface()
        return interface.functions.upgrade(
            amount
        ).transact({"from":account})

    '''
        /**
         * @dev Upgrade ERC20 to SuperToken and transfer immediately
         * @param to The account to received upgraded tokens
         * @param amount Number of tokens to be upgraded (in 18 decimals)
         * @param data User data for the TokensRecipient callback
         *
         * NOTE: It will use ´transferFrom´ to get tokens. Before calling this
         * function you should ´approve´ this contract
         */
    '''
    def upgrade_to(self, _to, amount, data, account):
        interface = self.get_interface()
        return interface.functions.upgradeTo(
            _to,
            amount,
            data
        ).transact({"from":account})

    '''
        /**
         * @dev Downgrade SuperToken to ERC20.
         * @dev It will call transfer to send tokens
         * @param amount Number of tokens to be downgraded
         */
    '''
    def downgrade(self, amount, account):
        interface = self.get_interface()
        return interface.functions.downgrade(amount).transact({"from":account})

    '''
        /**
         * @dev Return the underlying token contract
         * @return tokenAddr Underlying token address
         */
    '''
    def get_uderlying_token(self):
        interface = self.get_interface()
        return interface.functions.getUnderlyingToken().call()
    
    