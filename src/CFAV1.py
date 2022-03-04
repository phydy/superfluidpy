from brownie import *
from brownie import accounts, chain
from django.dispatch import receiver
from con_addresses import addresses, is_allowed_network
from initializer import superfluid
from handler import RPCError, NotFoundError

superfluid.load_config()
class CFA():

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
            return addresses[chain.id]["cfa"]
        except ValueError as r:
            print(r)


    def get_cfa_interface():
        return superfluid.interface.IConstantAggreementC1(CFA.get_address())


cfa_interface = CFA.get_cfa_interface()


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

def get_flow(token, sender, receiver):
    return cfa_interface.getFlow(
        token,
        sender,
        receiver
    )


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
def create_flow(token, receiver, flowRate, account, ctx):
    return cfa_interface.createFlow(
        token,
        receiver,
        flowRate,
        ctx,
        {"from": account}
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
def update_flow(token, receiver, flowRate, account, ctx):
    return cfa_interface.getFlow(
        token,
        receiver,
        flowRate,
        ctx,
        {"from": account}
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
def delete_flow(token, sender, receiver, ctx, account):
    return cfa_interface.deleteFlow(
        token,
        sender,
        receiver,
        ctx,
        {"from":account}
    )


'''

    /**
     * @dev Get the net flow rate of the account
     * @param token Super token address.
     * @param account Account for the query.
     * @return flowRate Flow rate.
     */
'''
def get_net_flow(token, account):
    return cfa_interface.getNetFlow(
        token,
        {"from":account}
    )


'''
    /**
     * @dev Get the maximum flow rate allowed with the deposit
     * @param deposit Deposit amount used for creating the flow
     */
'''
def get_MaximumFlowRateFromDeposit(token, amount):
    return cfa_interface.getMaximumFlowRateFromDeposit(
        token,
        amount
    )


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
def get_flow_byId(token, ID):
    return cfa_interface.getFlowByID(
        token,
        ID
    )


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
def get_DepositRequiredForFlowRate(token, flowRate):
    return cfa_interface.getDepositRequiredForFlowRate(
        token,
        flowRate
    )

'''
    /**
     * @dev Get the aggregated flow info of the account
     * @param token Super token address.
    * @param account Account for the query.
    */
'''
def get_AccountFlowInfo(token, account):
    return cfa_interface.getAccountFlowInfo(
        token,
        {"from":account}
    )

