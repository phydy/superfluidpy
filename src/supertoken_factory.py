from brownie import *
from brownie import accounts, chain
from con_addresses import addresses, is_allowed_network
from provider import *
import json
from Factory import abi

class SupertokenFatory:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider


    def get_address(self):
        return addresses[self.network]["host"]


    def get_interface(self):
        w3 = provider_connect(self.provider, self.network)
        return w3.eth.contract(address=self.get_address(), abi=json.dumps(abi))



    '''
        /// @dev Initialize the contract
    '''
    def initialize(self, account):
        factory_interface = self.get_interface()
        return factory_interface.functions.initialize(
        ).transact({"from":account})

    '''
        /**
         * @dev Create new super token wrapper for the underlying ERC20 token
         * @param underlyingToken Underlying ERC20 token
         * @param underlyingDecimals Underlying token decimals
         * @param upgradability Upgradability mode
         * @param name Super token name
         * @param symbol Super token symbol
         */
    '''
    def create_ERC20Wraper_decimals(self, underlying_token, underlyingDecimals, upgradability, name, symbol, account):
        factory_interface = self.get_interface()
        return factory_interface.functions.createERC20Wrapper(
            underlying_token,
            underlyingDecimals,
            upgradability,
            name,
            symbol
        ).transact({"from":account})


    '''
        /**
         * @dev Create new super token wrapper for the underlying ERC20 token with extra token info
         * @param underlyingToken Underlying ERC20 token
         * @param upgradability Upgradability mode
         * @param name Super token name
         * @param symbol Super token symbol
         *
         * NOTE:
         * - It assumes token provides the .decimals() function
         */
    '''
    def create_ERC20Wraper(self, underlying_token, upgradability, name, symbol, account):
        factory_interface = self.get_interface()
        return factory_interface.functions.createERC20Wrapper(
            underlying_token,
            upgradability,
            name,
            symbol
        ).transact({"from":account})


    '''
        /**
         * @dev Get superfluid host contract address
         */
    '''
    def get_host(self):
        factory_interface = self.get_interface()
        return factory_interface.functions.getHost().call()

    '''
        /**
         * @dev Get the current super token logic used by the factory
         */
    '''
    def get_supertoken_logic(self):
        factory_interface = self.get_interface()
        return factory_interface.functions.getSuperTokenLogic().call()

    def initialize_custom_supertoken(self, customSuperTokenProxy, account):
        factory_interface = self.get_interface()
        return factory_interface.functions.initializeCustomSuperToken(
            customSuperTokenProxy
        ).transact({"from":account})