
from brownie import *
from brownie import accounts, chain
from superfluid_finance.con_addresses import addresses, avaibale_chains, is_allowed_network

class ERC20:
    def __init__(self, address):
        self.address = address

    
    def get_interface(self):
        return superfluid.interface.IERC20(self.address)

    interface = get_interface()

    '''
        /// @param _owner The address from which the balance will be retrieved
        /// @return balance the balance
    '''
    def balance_of(address):
        return ERC20.interface.balanceOf(address)


    '''
        /// @notice send `_value` token to `_to` from `msg.sender`
        /// @param _to The address of the recipient
        /// @param _value The amount of token to be transferred
        /// @return success Whether the transfer was successful or not

    '''

    def transfer(self, _to, _value, account):
        return ERC20.interface.transfer(
            _to,
            _value,
            {"from":account})

    '''
        * @param _owner The address of the account owning tokens
        * @param _spender The address of the account able to transfer the tokens
        * @return remaining Amount of remaining tokens allowed to spent

    '''
    def allowance(self, _owner, _spender):
        return ERC20.interface.allowance(
            _owner,
            _spender
        )

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
        return ERC20.interface.transferFrom(
            _from,
            _to,
            _value,
            {"from":account}
        )
    '''
    * @notice `msg.sender` approves `_addr` to spend `_value` tokens
    * @param _spender The address of the account able to transfer the tokens
    * @param _value The amount of wei to be approved for transfer
    * @return success Whether the approval was successful or not

    '''
    def approve(self, _spender, _value, account):
        return ERC20.interface.approve(
            _spender,
            _value,
            {"from":account}
        )