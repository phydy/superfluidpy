from superfluid_finance import helper_ABI
from superfluid_finance.provider import provider_connect
import json
from brownie import convert
from superfluid_finance.con_addresses import addresses

abi = helper_ABI.abi

class AgreementDataGiver:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider
        self.w3=provider_connect(self.network, self.provider)

    def get_address(self):
        return convert.to_address(
            addresses[self.network]["giver"]
        )

    def get_interface(self):
        w3 = provider_connect(
            self.network,
            self.provider
        )
        return w3.eth.contract(address=self.get_address(), abi=json.dumps(abi))

    def get_create_flow(self, token, receiver, flowRate):
        context_interface = self.get_interface()
        return context_interface.functions.createFLowCXT(
            token,
            receiver,
            flowRate
        ).call()

    def get_update_flow(self, token, receiver, flowRate):
        context_interface = self.get_interface()
        return context_interface.functions.updateFLowCXT(
            token,
            receiver,
            flowRate
        ).call()

    def get_delete_flow(self, token, receiver, flowRate):
        context_interface = self.get_interface()
        return context_interface.functions.deleteFLowCXT(
            token,
            receiver,
            flowRate
        ).call()

    def get_update_index(self, token, indexId, indexAmount):
        context_interface = self.get_interface()
        return context_interface.functions.updateIndex(
            token,
            indexId,
            indexAmount
        ).call()
    
    def get_delete_sub(self, token, publisher, indexId, subscriber):
        context_interface = self.get_interface()
        return context_interface.functions.deleteSubscription(
            token,
            publisher,
            indexId,
            subscriber
        ).call()

    def get_create_index(self, token, indexId):
        context_interface = self.get_interface()
        return context_interface.functions.createIndex(
            token,
            indexId
        ).call()

    def get_distribute(self, token, indexId, amount):
        context_interface = self.get_interface()
        return context_interface.functions.distribute(
            token,
            indexId,
            amount
        ).call()

    def get_update_sub(self, token, indexId, subscriber, units):
        context_interface = self.get_interface()
        return context_interface.functions.updateSubscription(
            token,
            indexId,
            subscriber,
            units
        ).call()

    def get_approve_sub(self, token, publisher, indexId, subscriber):
        context_interface = self.get_interface()
        return context_interface.functions.approveSubscription(
            token,
            publisher,
            indexId,
            subscriber
        ).call()

    def get_revoke_sub(self, token, publisher, indexId, subscriber):
        context_interface = self.get_interface()
        return context_interface.functions.revokeSubscription(
            token,
            publisher,
            indexId,
            subscriber
        ).call()