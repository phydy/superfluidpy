from operator import index
from brownie import *
from brownie import accounts, chain
from django.dispatch import receiver
from con_addresses import addresses, is_allowed_network
from initializer import superfluid
from handler import RPCError, NotFoundError

superfluid.load_config()
'''
    the instand distribution agreement class
'''
class IDA:

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
            return addresses[chain.id]["ida"]
        except ValueError as r:
            print(r)


    def get_ida_interface():
        return superfluid.interface.IInstantDistributionAgreementV1(IDA.get_address())


ida_interface = IDA.get_ida_interface()

'''
    /**************************************************************************
     * Index operations
     *************************************************************************/

    /**
     * @dev Create a new index for the publisher.
     * @param token Super token address.
     * @param indexId Id of the index.
     *
     * # App callbacks
     *
     * None
     */
'''
def create_index(token, indexID, account):
    ida_interface.createIndex(
        token,
        indexID,
        {"from": account}
    )


'''
    /**
     * @dev Query the data of a index.
     * @param token Super token address.
     * @param publisher The publisher of the index.
     * @param indexId Id of the index.
     * @return exist Does the index exist.
     * @return indexValue Value of the current index.
     * @return totalUnitsApproved Total units approved for the index.
     * @return totalUnitsPending Total units pending approval for the index.
     */
'''
def get_index(token, publisher, indexID):
    ida_interface.getIndex(
        token,
        publisher,
        indexID
    )


'''
    /**
     * @dev Calculate actual distribution amount
     * @param token Super token address.
     * @param publisher The publisher of the index.
     * @param indexId Id of the index.
     * @param amount The amount of tokens desired to be distributed.
     */
'''

def calculate_distribution(token, publisher, indexID, amount):
    ida_interface.calculateDistribution(
        token,
        publisher,
        indexID,
        amount
    )


'''
    /**
     * @dev Update index value of an index.
     * @param token Super token address.
     * @param indexId Id of the index.
     * @param indexValue Value of the index.
     *
     * # App callbacks
     *
     * None
     */
'''
def update_index(token, IndexID, indexValue, ctx, account):
    ida_interface.updateIndex(
        token,
        IndexID,
        indexValue,
        ctx,
        {"from": account}
    )

'''
    /**
     * @dev Distribute tokens through the index.
     * @param token Super token address.
     * @param indexId Id of the index.
     * @param amount The amount of tokens desired to be distributed.
     *
     * NOTE:
     * - This is a convenient version of updateIndex. It adds to the index
     *   a delta that equals to `amount / totalUnits`.
     * - The actual amount distributed could be obtained via
     *   `calculateDistribution`. This is due to precision error with index
     *   value and units data range.
     *
     * # App callbacks
     *
     * None
     */ 
'''
def distribute_ida(token, indexID, amount, account):
    ida_interface.distribute(
        token,
        indexID,
        amount,
        {"from": account}
    )

'''
    /**************************************************************************
     * Subscription operations
     *************************************************************************/

    /**
     * @dev Approve the subscription of an index.
     * @param token Super token address.
     * @param publisher The publisher of the index.
     * @param indexId Id of the index.
     *
     * # App callbacks
     *
     * - if subscription exist
     *   - AgreementCreated callback to the publisher:
     *      - agreementId is for the subscription
     * - if subscription does not exist
     *   - AgreementUpdated callback to the publisher:
     *      - agreementId is for the subscription
     */

'''
def approve_subscription(token, publisher, indexId, ctx, account):
    ida_interface.approveSubscription(
        token,
        publisher,
        indexId,
        ctx,
        {"from": account}
    )


'''
    /**
    * @dev Revoke the subscription of an index.
    * @param token Super token address.
    * @param publisher The publisher of the index.
    * @param indexId Id of the index.
    *
    * # App callbacks
    * - AgreementUpdated callback to the publisher:
    *    - agreementId is for the subscription
    */
'''
def revoke_subscription(token, publisher, indexId, ctx, account):
    ida_interface.revokeSubscription(
        token,
        publisher,
        indexId,
        ctx,
        {"from": account}
    )


'''
    /**
     * @dev Update the nuber of units of a subscription.
     * @param token Super token address.
     * @param indexId Id of the index.
     * @param subscriber The subscriber of the index.
     * @param units Number of units of the subscription.
     *
     * # App callbacks
     *
     * - if subscription exist
     *   - AgreementCreated callback to the subscriber:
     *      - agreementId is for the subscription
     * - if subscription does not exist
     *   - AgreementUpdated callback to the subscriber:
     *      - agreementId is for the subscription
     */
'''
def update_subscription(token, indexId, subscriber, units, ctx, account):
    ida_interface.updateSubscription(
        token,
        indexId,
        subscriber,
        units,
        ctx,
        {"from": account}
    )


'''
    /**
     * @dev Get data of a subscription
     * @param token Super token address.
     * @param publisher The publisher of the index.
     * @param indexId Id of the index.
     * @param subscriber The subscriber of the index.
     * @return exist Does the subscription exist?
     * @return approved Is the subscription approved?
     * @return units Units of the suscription.
     * @return pendingDistribution Pending amount of tokens to be distributed for unapproved subscription.
     */
'''
def get_subscription(token, publisher, indexId, subscriber):
    
    ida_interface.getSubscription(
        token,
        publisher,
        indexId,
        subscriber
    )

'''
    /**
     * @dev Get data of a subscription by agreement ID
     * @param token Super token address.
     * @param agreementId The agreement ID.
     * @return publisher The publisher of the index.
     * @return indexId Id of the index.
     * @return approved Is the subscription approved?
     * @return units Units of the suscription.
     * @return pendingDistribution Pending amount of tokens to be distributed for unapproved subscription.
     */
'''
def get_subscription_byId(token, ID):
    ida_interface.getSubscriptionByID(
        token,
        ID
    )


'''
    /**
     * @dev List subscriptions of an user.
     * @param token Super token address.
     * @param subscriber The user, a subscriber.
     * @return publishers Publishers of the subcriptions.
     * @return indexIds Indexes of the subscriptions.
     * @r
'''
def list_subsriptions(token, subscriber):
    ida_interface.listSubscriptions(
        token,
        subscriber
    )

'''
    /**
     * @dev Delete the subscription of an user.
     * @param token Super token address.
     * @param publisher The publisher of the index.
     * @param indexId Id of the index.
     * @param subscriber The user, a subscriber.
     *
     * # App callbacks
     *
     * - if the subscriber called it
     *   - AgreementTerminated callback to the publsiher:
     *      - agreementId is for the subscription
     * - if the publisher called it
     *   - AgreementTerminated callback to the subscriber:
     *      - agreementId is for the subscription
     */
'''

def delete_subscription(token, publisher, indexId, subscriber, ctx, account):
    ida_interface.deleteSubscription(
        token,
        publisher,
        indexId,
        subscriber,
        ctx,
        {"from": account}
    )

'''
    /**
    * @dev Claim pending distributions.
    * @param token Super token address.
    * @param publisher The publisher of the index.
    * @param indexId Id of the index.
    * @param subscriber The user, a subscriber.
    *
    * The subscription should not exist yet.
    *
    * # App callbacks
    *
    * - AgreementUpdated callback to the publisher:
    *    - agreementId is for the subscription
    */
'''
def claim_subscription(token, publisher, indexId, subscriber, ctx, account):
    ida_interface.claim(
        token,
        publisher,
        indexId,
        subscriber,
        ctx,
        {"from": account}
    )


