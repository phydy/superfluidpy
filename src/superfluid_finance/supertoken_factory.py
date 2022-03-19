from brownie import *
from brownie import accounts, chain, convert
from superfluid_finance.con_addresses import addresses, is_allowed_network
from superfluid_finance.provider import *
import json
from superfluid_finance.Factory import abi

class SupertokenFatory:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider

    def __str__(self) -> str:
        return "SuperTokenFactory Class"

    def get_w3_instance(self):
        return provider_connect(
            self.network,
            self.provider
        )

    def get_address(self):
        return addresses[self.network]["factory"]


    def get_interface(self):
        w3 = provider_connect(self.provider, self.network)
        return w3.eth.contract(
            address=self.get_address(),
            abi=json.dumps(abi)
        )



    '''
        /// @dev Initialize the contract
    '''
    def initialize(self, account):
        w3 = self.get_w3_instance()
        factory_interface = self.get_interface()
        trx = factory_interface.functions.initialize(
        ).buildTransaction(
            {   
                "nonce": w3.eth.get_transaction_count(account.address),
                "chainId": w3.eth.chain_id,
                "gas": 2000000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei')
            }

        )
        private_key=account.private_key
        signing_tx=w3.eth.account.sign_transaction(trx, private_key=private_key)
        w3.eth.send_raw_transaction(signing_tx.rawTransaction)
        return f"hash: {signing_tx.hash}"

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
    def create_ERC20Wraper_decimals(
        self, underlying_token, underlyingDecimals, upgradability, name, symbol, account
    ):
        w3 = self.get_w3_instance()
        factory_interface = self.get_interface()
        trx = factory_interface.functions.createERC20Wrapper(
            underlying_token,
            underlyingDecimals,
            upgradability,
            name,
            symbol
        ).buildTransaction(
            {   
                "nonce": w3.eth.get_transaction_count(account.address),
                "chainId": w3.eth.chain_id,
                "gas": 2000000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei')
            }

        )
        private_key=account.private_key
        signing_tx=w3.eth.account.sign_transaction(trx, private_key=private_key)
        w3.eth.send_raw_transaction(signing_tx.rawTransaction)
        return f"hash: {signing_tx.hash}"


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
        w3 = self.get_w3_instance()
        factory_interface = self.get_interface()
        trx = factory_interface.functions.createERC20Wrapper(
            underlying_token,
            upgradability,
            name,
            symbol
        ).buildTransaction(
            {   
                "nonce": w3.eth.get_transaction_count(account.address),
                "chainId": w3.eth.chain_id,
                "gas": 2000000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei')
            }

        )
        private_key=account.private_key
        signing_tx=w3.eth.account.sign_transaction(trx, private_key=private_key)
        w3.eth.send_raw_transaction(signing_tx.rawTransaction)
        return f"hash: {signing_tx.hash}"


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
        w3 = self.get_w3_instance()
        factory_interface = self.get_interface()
        trx = factory_interface.functions.initializeCustomSuperToken(
            customSuperTokenProxy
        ).buildTransaction(
            {   
                "nonce": w3.eth.get_transaction_count(account.address),
                "chainId": w3.eth.chain_id,
                "gas": 2000000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei')
            }

        )
        private_key=account.private_key
        signing_tx=w3.eth.account.sign_transaction(trx, private_key=private_key)
        w3.eth.send_raw_transaction(signing_tx.rawTransaction)
        return f"hash: {signing_tx.hash}"