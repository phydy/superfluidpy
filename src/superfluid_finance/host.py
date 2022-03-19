from random import random
from brownie import accounts, chain, network, convert
from superfluid_finance.con_addresses import addresses, is_allowed_network
from web3 import Web3
import json
from superfluid_finance.Superfluid import abi
from superfluid_finance.provider import *

class Host():

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider
        self.w3=provider_connect(self.network, self.provider)


    def get_address(self):
        return convert.to_address(
            addresses[self.network]["host"]
        )

    def get_w3_instance(self):
        return provider_connect(
            self.network,
            self.provider
        )

    def get_interface(self):
        w3 = provider_connect(self.network, self.provider)
        return w3.eth.contract(
            address=self.get_address(),
            abi=json.dumps(abi)
        )


    '''
        /**************************************************************************
         * Governance
         *************************************************************************/

    '''
    '''
        /**
         * @dev Get the current governace of the Superfluid host
         */
    '''
    def get_governance(self):
        host_interface = self.get_interface()
        return host_interface.functions.getGovernance().call()



    '''
        /**
        * @dev Check if the agreement class is whitelisted
        */
    '''
    def is_AgreementTypeListed(self, agreementType):#bytes
        host_interface = self.get_interface()
        return host_interface.functions.isAgreementTypeListed(agreementType).call()


    '''
        /**
        * @dev Check if the agreement class is whitelisted
        */
    '''
    def is_AgreementClassListed(self, agreementClass):
        host_interface = self.get_interface()
        return host_interface.functions.isAgreementClassListed(agreementClass).call()

    '''
        /**
        * @dev Get agreement class
        */
    '''
    def get_aggrementClass(self, agreementType):
        host_interface = self.get_interface()
        return host_interface.functions.getAgreementClassListed(agreementType).call()

    '''
       /**
        * @dev Map list of the agreement classes using a bitmap
        * @param bitmap Agreement class bitmap
        */
    '''
    def map_agreementClass(self, bitmap):
        host_interface = self.get_interface()
        return host_interface.functions.mapAgreementClass(bitmap).call()


    '''
        SuperToken Factory
    '''

    '''
       /**
         * @dev Get the super token factory
         * @return factory The factory
         */
    '''
    def get_SuperTokenFactory(self):
        host_interface = self.get_interface()
        return host_interface.functions.getSuperTokenFactory().call()

    '''
        /**
         * @dev Get the super token factory logic (applicable to upgradable deployment)
         * @return logic The factory logic
         */
    '''
    def get_SuperTokenFactoryLogic(self):
        host_interface = self.get_interface()
        return host_interface.functions.getSuperTokenFactoryLogic().call()

    '''
        /**
         * @dev Update super token factory
         * @param newFactory New factory logic
         */
    '''
    def update_SuperTokenLogic(self, super_token, account):
        host_interface = self.get_interface()
        return host_interface.functions.updateSuperTokenLogic(
            super_token
        ).transact({"from": account})

    '''
        /**
         * @dev Message sender declares it as a super app
         * @param configWord The super app manifest configuration, flags are defined in
         *                   `SuperAppDefinitions`
         */
    '''
    def register_App(self, configWord, account):
        host_interface = self.get_interface()
        host_interface.functions.registerApp(
            configWord
        ).transact({"from": account})


    '''
        /**
         * @dev Message sender declares it as a super app, using a registration key
         * @param configWord The super app manifest configuration, flags are defined in
         *                   `SuperAppDefinitions`
         * @param registrationKey The registration key issued by the governance
         */
    '''
    def register_AppWith_key(self, configWord, registrationKey, account):
        host_interface = self.get_interface()
        return host_interface.functions.registerAppWithKey(
            configWord,
            registrationKey
        ).transact({"from": account})

    '''
        /**
         * @dev Query if the app is registered
         * @param app Super app address
         */
    '''
    def is_superApp(self, address):
        host_interface = self.get_interface()
        return host_interface.functions.isApp(address).call()

    '''

        /**
         * @dev Query app level
         * @param app Super app address
         */
    '''
    def get_AppLevel(self, host_address):
        host_interface = self.get_interface()
        return host_interface.functions.getAppLevel(
            host_address
        ).call()

    '''
        /**
         * @dev Get the manifest of the super app
         * @param app Super app address
         */
    '''
    def get_AppManifest(self, host_address):
        host_interface = self.get_interface()
        return host_interface.functions.getAppManifest(
            host_address
        ).call()


    '''
        /**
         * @dev Query if the app has been jailed
         * @param app Super app address
         */
    '''
    def is_jailed(self, host_address):
        host_interface = self.get_interface()
        return host_interface.functions.isAppJailed(host_address).call()


    '''
       /**
         * @dev White-list the target app for app composition for the source app (msg.sender)
         * @param targetApp The taget super app address
         */
    '''
    def allow_compisiteApp(self, host_address, account):
        host_interface = self.get_interface()
        return host_interface.functions.allowCompositeApp(
            host_address,
        ).transact({"from": account})


    def is_composite_allowed(self, app, target):
        host_interface = self.get_interface()
        return host_interface.functions.isCompositeAppAllowed(
            app,
            target
        ).call()
    '''
         * Contextless Call Proxies
         *
         * NOTE: For EOAs or non-app contracts, they are the entry points for interacting
         * with agreements or apps.
         *
         * NOTE: The contextual call data should be generated using
         * abi.encodeWithSelector. The context parameter should be set to "0x",
         * an empty bytes array as a placeholder to be replaced by the host
         * contract.
    ''' 
    def call_agreement(self, agreementClass, calldata, userdata, account):
        #w3 = self.get_w3_instance()
        host_interface = self.get_interface()
        trx = host_interface.functions.callAgreement(
            agreementClass,
            calldata,
            convert.to_bytes(userdata),
        ).buildTransaction(
            {   
                "nonce": self.w3.eth.get_transaction_count(account.address),
                "chainId": self.w3.eth.chain_id,
                "gas": 2000000,#self.w3.eth.gas_price
                'maxFeePerGas': self.w3.toWei("2", "gwei"),
                'maxPriorityFeePerGas': self.w3.toWei("1", "gwei"),
            }

        )
        private_key=account.private_key
        signing_tx=self.w3.eth.account.sign_transaction(trx, private_key=private_key)
        self.w3.eth.send_raw_transaction(signing_tx.rawTransaction)
        tx_rc = self.w3.eth.wait_for_transaction_receipt(signing_tx.hash)
        return (
            f"hash: {self.w3.toHex(signing_tx.hash)}",
            f"hash: {self.w3.toHex(tx_rc)}"
        )