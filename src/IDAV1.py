from brownie import *
from provider import *
from brownie import accounts, chain
from con_addresses import addresses, is_allowed_network
from IDA import abi
import json

'''
    the instand distribution agreement class
'''
class IDA:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider


    def get_address(self):
        return addresses[self.network]["host"]


    def get_interface(self):
        w3 = provider_connect(self.provider, self.network)
        return w3.eth.contract(address=self.get_address(), abi=json.dumps(abi))



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
    def create_index(self, token, indexID, account):
        ida_interface = self.get_interface()
        ida_interface.functions.createIndex(
            token,
            indexID,
            {"from": account}
        ).transact({"from": account})


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
    def get_index(self, token, publisher, indexID):
        ida_interface = self.get_interface()
        ida_interface.functions.getIndex(
            token,
            publisher,
            indexID
        ).call()


    '''
        /**
         * @dev Calculate actual distribution amount
         * @param token Super token address.
         * @param publisher The publisher of the index.
         * @param indexId Id of the index.
         * @param amount The amount of tokens desired to be distributed.
         */
    '''

    def calculate_distribution(self, token, publisher, indexID, amount):
        ida_interface = self.get_interface()
        ida_interface.functions.calculateDistribution(
            token,
            publisher,
            indexID,
            amount
        ).call()


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
    def update_index(self, token, IndexID, indexValue, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.updateIndex(
            token,
            IndexID,
            indexValue,
            ctx
        ).transact({"from": account})

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
    def distribute_ida(self, token, indexID, amount, account):
        ida_interface = self.get_interface()
        ida_interface.functions.distribute(
            token,
            indexID,
            amount
        ).transact({"from": account})

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
    def approve_subscription(self, token, publisher, indexId, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.approveSubscription(
            token,
            publisher,
            indexId,
            ctx
        ).transact({"from": account})


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
    def revoke_subscription(self, token, publisher, indexId, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.revokeSubscription(
            token,
            publisher,
            indexId,
            ctx
        ).transact({"from": account})


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
    def update_subscription(self, token, indexId, subscriber, units, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.updateSubscription(
            token,
            indexId,
            subscriber,
            units,
            ctx
        ).transact({"from": account})


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
    def get_subscription(self, token, publisher, indexId, subscriber):
        ida_interface = self.get_interface()
        ida_interface.functions.getSubscription(
            token,
            publisher,
            indexId,
            subscriber
        ).call()

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
    def get_subscription_byId(self, token, ID):
        ida_interface = self.get_interface()
        ida_interface.functions.getSubscriptionByID(
            token,
            ID
        ).call()


    '''
        /**
         * @dev List subscriptions of an user.
         * @param token Super token address.
         * @param subscriber The user, a subscriber.
         * @return publishers Publishers of the subcriptions.
         * @return indexIds Indexes of the subscriptions.
         * @r
    '''
    def list_subsriptions(self, token, subscriber):
        ida_interface = self.get_interface()
        ida_interface.functions.listSubscriptions(
            token,
            subscriber
        ).call()

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

    def delete_subscription(self, token, publisher, indexId, subscriber, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.deleteSubscription(
            token,
            publisher,
            indexId,
            subscriber,
            ctx
        ).transact({"from": account})

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
    def claim_subscription(self, token, publisher, indexId, subscriber, ctx, account):
        ida_interface = self.get_interface()
        ida_interface.functions.claim(
            token,
            publisher,
            indexId,
            subscriber,
            ctx
        ).transact({"from": account})


