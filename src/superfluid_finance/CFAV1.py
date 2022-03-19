from brownie import *
from brownie import accounts, chain, convert
from superfluid_finance.provider import *
from superfluid_finance.host import Host
from superfluid_finance.con_addresses import addresses, is_allowed_network
import json
from superfluid_finance.CFA import abi
from web3 import Web3
import web3


class CFA:

    def __init__(self, network, provider):
        self.network=network
        self.provider=provider
        self.w3=provider_connect(
            self.network,
            self.provider
        )

    def get_host(self):
        network = self.network
        provider = self.provider
        return Host(network, provider)

    def get_address(self):
        return convert.to_address(
            addresses[self.network]["cfa"]
        )


    def get_interface(self):
        w3 = provider_connect(
            self.network,
            self.provider
        )
        return w3.eth.contract(address=self.get_address(), abi=json.dumps(abi))


    '''
        /**
         * @dev Get the flow data between `sender` and `receiver`.
         * @param token Super token address.
         * @param sender Flow receiver.
         * @param receiver Flow sender.
         * @return timestamp Timestamp of when the flow is updated.
         * @return flowRate The flow rate.
         * @return deposit The amount of deposit the flow.
         * @return owedDeposit The amount of owed deposit of the flow.
         */
    '''

    def get_flow(self, token, sender, receiver):
        cfa_interface = self.get_interface()
        tx_value = cfa_interface.functions.getFlow(
            token,
            sender,
            receiver
        ).call()
        return tx_value



    '''
        /**
         * @dev Create a flow betwen sender and receiver.
         * @param token Super token address.
         * @param receiver Flow receiver address.
         * @param flowRate New flow rate in amount per second.
         *
         * # App callbacks
         *
         * - AgreementCreated
         *   - agreementId - can be used in getFlowByID
         *   - agreementData - abi.encode(address flowSender, address flowReceiver)
         *
         * NOTE:
         * - A deposit is taken as safety margin for the solvency agents.
         * - A extra gas fee may be taken to pay for solvency agent liquidations.
         */
    '''
    def create_flow(self, token, receiver, flowRate, ctx, account):
        cfa_interface = self.get_interface()
        encoded_data = cfa_interface.encodeABI(
            fn_name="createFlow",
            args=[
                convert.to_address(token),
                convert.to_address(receiver),
                convert.to_int(flowRate),
                ""
            ]
        )
        bytes_data = self.w3.toBytes(hexstr=f"{encoded_data}")
        actual_data = bytes_data[:(len(bytes_data) - 32)]
        host = Host(self.network, self.provider)
        return host.call_agreement(
            self.get_address(),
            actual_data, 
            ctx,
            account
        )

    '''
        /**
         * @dev Update the flow rate between sender and receiver.
         * @param token Super token address.
         * @param receiver Flow receiver address.
         * @param flowRate New flow rate in amount per second.
         *
         * # App callbacks
         *
         * - AgreementUpdated
         *   - agreementId - can be used in getFlowByID
         *   - agreementData - abi.encode(address flowSender, address flowReceiver)
         *
         * NOTE:
         * - Only the flow sender may update the flow rate.
         * - Even if the flow rate is zero, the flow is not deleted
         * from the system.
         * - Deposit amount will be adjusted accordingly.
         * - No new gas fee is charged.
         */
    '''
    def update_flow(self, token, receiver, flowRate, ctx, account):
        cfa_interface = self.get_interface()
        encoded_data = cfa_interface.encodeABI(
            fn_name="updateFlow",
            args=[
                convert.to_address(token),
                convert.to_address(receiver),
                convert.to_int(flowRate),
                ""
            ]
        )
        bytes_data = self.w3.toBytes(hexstr=f"{encoded_data}")
        actual_data = bytes_data[:(len(bytes_data) - 32)]
        host = Host(self.network, self.provider)
        return host.call_agreement(
            self.get_address(), 
            actual_data,
            ctx,
            account
        )


    '''
        /**
         * @dev Delete the flow between sender and receiver
         * @param token Super token address.
         * @param ctx Context bytes.
         * @param receiver Flow receiver address.
         *
         * # App callbacks
         *
         * - AgreementTerminated
         *   - agreementId - can be used in getFlowByID
         *   - agreementData - abi.encode(address flowSender, address flowReceiver)
         *
         * NOTE:
         * - Both flow sender and receiver may delete the flow.
         * - If Sender account is insolvent or in critical state, a solvency agent may
         *   also terminate the agreement.
         * - Gas fee may be returned to the sender.
         */
    '''
    def delete_flow(self, token, sender, receiver, ctx, account):
        cfa_interface = self.get_interface()
        encoded_data = cfa_interface.encodeABI(
            fn_name="updateFlow",
            args=[
                convert.to_address(token),
                convert.to_address(sender),
                convert.to_address(receiver),
                ""
            ]
        )
        bytes_data = self.w3.toBytes(hexstr=f"{encoded_data}")
        actual_data = bytes_data[:(len(bytes_data) - 32)]
        host = Host(self.network, self.provider)
        return host.call_agreement(
            self.get_address(), 
            actual_data,
            ctx,
            account
        )

    '''

        /**
         * @dev Get the net flow rate of the account
         * @param token Super token address.
         * @param account Account for the query.
         * @return flowRate Flow rate.
         */
    '''
    def get_net_flow(self, token, account):
        cfa_interface = self.get_interface()
        return cfa_interface.functions.getNetFlow(
            token,
            account
        ).call()


    '''
        /**
         * @dev Get the maximum flow rate allowed with the deposit
         * @param deposit Deposit amount used for creating the flow
         */
    '''
    def get_MaximumFlowRateFromDeposit(self, token, amount):
        cfa_interface = self.get_interface()
        return cfa_interface.functions.getMaximumFlowRateFromDeposit(
            token,
            amount
        ).call()


    '''
        /**
         * @dev Get flow data using agreement ID
         * @param token Super token address.
         * @param agreementId The agreement ID.
         * @return timestamp Timestamp of when the flow is updated.
         * @return flowRate The flow rate.
         * @return deposit The amount of deposit the flow.
         * @return owedDeposit The amount of owed deposit of the flow.
         */
    '''
    def get_flow_byId(self, token, ID):
        cfa_interface = self.get_interface()
        return cfa_interface.functions.getFlowByID(
            token,
            ID
        ).call()


    '''
        /**
         * @dev Get the deposit required for creating the flow
         * @param flowRate Flow rate to be tested
         * 
         * NOTE: 
         * - if calculated deposit (flowRate * liquidationPeriod) is less
         *   than the minimum deposit, we use the minimum deposit otherwise
         *   we use the calculated deposit
         */
    '''
    def get_DepositRequiredForFlowRate(self, token, flowRate):
        cfa_interface = self.get_interface()
        return cfa_interface.functions.getDepositRequiredForFlowRate(
            token,
            flowRate
        ).call()

    '''
        /**
         * @dev Get the aggregated flow info of the account
         * @param token Super token address.
        * @param account Account for the query.
        */
    '''
    def get_AccountFlowInfo(self, token, account):
        cfa_interface = self.get_interface()
        return cfa_interface.functions.getAccountFlowInfo(
            token,
            account
        ).call()
