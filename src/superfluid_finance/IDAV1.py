from brownie import *
from superfluid_finance.provider import *
from brownie import accounts, chain, convert
from superfluid_finance.con_addresses import addresses, is_allowed_network
from superfluid_finance.IDA import abi
import json

'''
    the instand distribution agreement class
'''
class IDA:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider

    def get_w3_istance(self):
        return provider_connect(self.network, self.provider)

    def get_address(self):
        return addresses[self.network]["ida"]


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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.createIndex(
            convert.to_address(token),
            convert.to_uint(indexID)
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
        print(signing_tx)


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
            convert.to_address(token),
            convert.to_address(publisher),
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
            convert.to_address(token),
            convert.to_address(publisher),
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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.updateIndex(
            convert.to_address(token),
            IndexID,
            indexValue,
            convert.to_bytes(ctx)
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
        print(signing_tx)

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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.distribute(
            convert.to_address(token),
            indexID,
            amount
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
        print(signing_tx)

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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.approveSubscription(
            convert.to_address(token),
            convert.to_address(publisher),
            indexId,
            convert.to_bytes(ctx)
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
        print(signing_tx)


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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.revokeSubscription(
            convert.to_address(token),
            convert.to_address(publisher),
            indexId,
            convert.to_bytes(ctx)
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
        print(signing_tx)


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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.updateSubscription(
            convert.to_address(token),
            indexId,
            convert.to_address(subscriber),
            units,
            convert.to_bytes(ctx)
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
        print(signing_tx)


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
            convert.to_address(token),
            convert.to_address(publisher),
            indexId,
            convert.to_address(subscriber)
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
            convert.to_address(token),
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
            convert.to_address(token),
            convert.to_address(subscriber)
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
        w3 =self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.deleteSubscription(
            convert.to_address(token),
            convert.to_address(publisher),
            indexId,
            convert.to_address(subscriber),
            convert.to_bytes(ctx)
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
        print(signing_tx)

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
        w3 = self.get_w3_istance()
        ida_interface = self.get_interface()
        trx = ida_interface.functions.claim(
            convert.to_address(token),
            convert.to_address(publisher),
            indexId,
            convert.to_address(subscriber),
            convert.to_bytes(ctx)
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
        print(signing_tx)


