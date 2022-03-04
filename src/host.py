from brownie import *
from brownie import accounts, chain
from con_addresses import addresses, is_allowed_network
from initializer import superfluid
from handler import NotFoundError, RPCError


superfluid.load_config()
class Host():

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
            return addresses[chain.id]["host"]
        except ValueError as r:
            print(r)

    def get_host_interface():
        return superfluid.interface.ISuperfluid(
            Host.get_address()
        )

host_interface = Host.get_host_interface()


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
def get_governance():
    return host_interface.getGovernance()



'''
    /**
    * @dev Check if the agreement class is whitelisted
    */
'''
def is_AgreementTypeListed(agreementType):#bytes
    return host_interface.isAgreementTypeListed(agreementType)


'''
    /**
    * @dev Check if the agreement class is whitelisted
    */
'''
def is_AgreementClassListed(agreementClass):
    return host_interface.isAgreementClassListed(agreementClass)

'''
    /**
    * @dev Get agreement class
    */
'''
def get_aggrementClass( agreementType):
    return host_interface.isAgreementClassListed(agreementType)

'''
   /**
    * @dev Map list of the agreement classes using a bitmap
    * @param bitmap Agreement class bitmap
    */
'''
def map_agreementClass(bitmap):
    return host_interface.mapAgreementClass(bitmap)


'''
    SuperToken Factory
'''

'''
   /**
     * @dev Get the super token factory
     * @return factory The factory
     */
'''
def get_SuperTokenFactory():
    return host_interface.getSuperTokenFactory()

print(get_SuperTokenFactory())
'''
    /**
     * @dev Get the super token factory logic (applicable to upgradable deployment)
     * @return logic The factory logic
     */
'''
def get_SuperTokenFactoryLogic():
    return host_interface.getSuperTokenFactoryLogic()

'''
    /**
     * @dev Update super token factory
     * @param newFactory New factory logic
     */
'''
def update_SuperTokenLogic(super_token, account):
    return host_interface.updateSuperTokenLogic(
        super_token,
        {"from": account}
    )

'''
    /**
     * @dev Message sender declares it as a super app
     * @param configWord The super app manifest configuration, flags are defined in
     *                   `SuperAppDefinitions`
     */
'''
def register_App(configWord, account):
    host_interface.registerApp(
        configWord,
        {"from": account}
    )


'''
    /**
     * @dev Message sender declares it as a super app, using a registration key
     * @param configWord The super app manifest configuration, flags are defined in
     *                   `SuperAppDefinitions`
     * @param registrationKey The registration key issued by the governance
     */
'''
def register_AppWith_key(configWord, registrationKey, account):
    return host_interface.registerAppWithKey(
        configWord,
        registrationKey,
        {"from": account}
    )

'''
    /**
     * @dev Query if the app is registered
     * @param app Super app address
     */
'''
def is_superApp(address):
    return host_interface.isApp(address)

'''

    /**
     * @dev Query app level
     * @param app Super app address
     */
'''
def get_AppLevel(host_address):
    return host_interface.getAppLevel(
        host_address
    )

'''
    /**
     * @dev Get the manifest of the super app
     * @param app Super app address
     */
'''
def get_AppManifest(host_address):
    return host_interface.getAppManifest(
        host_address
    )


'''
    /**
     * @dev Query if the app has been jailed
     * @param app Super app address
     */
'''
def is_jailed(host_address):
    return host_interface.isAppJailed(host_address)


'''
   /**
     * @dev White-list the target app for app composition for the source app (msg.sender)
     * @param targetApp The taget super app address
     */
'''
def allow_compisiteApp(host_address, account):
    return host_interface.allowCompositeApp(
        host_address,
        {"from":account}
    )


def is_composite_allowed(app, target):
    return host_interface.isCompositeAppAllowed(
        app,
        target
    )


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
def call_agreement(agreementClass, calldata, userdata, account):
    return host_interface.callAgreement(
        agreementClass,
        calldata,
        userdata,
        {"from": account}
    )
