from brownie import *
from brownie import accounts, chain
from con_addresses import addresses, is_allowed_network
from initializer import superfluid
from handler import RPCError, NotFoundError

superfluid.load_config()

class SupertokenFatory:

    @classmethod
    def get_address(cls):
        try:
            if network.is_connected() == False:
                raise RPCError(
                    "connect to a network"
                )
            if is_allowed_network(chain.id) == False:
                raise NotFoundError(
                    f'network {chain.id} not found'
                )
            return addresses[chain.id]["factory"]
        except ValueError as r:
            print(r)


    def get_factory_interface():
        return superfluid.interface.IInstantDistributionAgreementV1(
            SupertokenFatory.get_address()
        )


    factory_interface = get_factory_interface()

    '''
        /// @dev Initialize the contract
    '''
    def initialize(self, account):
        return SupertokenFatory.get_factory_interface.initialize(
            {"from": account}
        )

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
        return SupertokenFatory.factory_interface.createERC20Wrapper(
            underlying_token,
            underlyingDecimals,
            upgradability,
            name,
            symbol,
            {"from":account}
        )


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
        return SupertokenFatory.factory_interface.createERC20Wrapper(
            underlying_token,
            upgradability,
            name,
            symbol,
            {"from":account}
        )


    '''
        /**
         * @dev Get superfluid host contract address
         */
    '''
    def get_host(self):
        return SupertokenFatory.factory_interface.getHost()

    '''
        /**
         * @dev Get the current super token logic used by the factory
         */
    '''
    def get_supertoken_logic(self):
        return SupertokenFatory.factory_interface.getSuperTokenLogic()

    def initialize_custom_supertoken(self, customSuperTokenProxy, account):
        return SupertokenFatory.factory_interface.initializeCustomSuperToken(
            customSuperTokenProxy,
            {"from":account}
        )