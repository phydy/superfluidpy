from web3 import Web3
from brownie import chain, network, accounts
import os
from curses.ascii import islower, isupper

'''
    * This file handles easy coonection to an RPC endpoint in a python environment
'''

'''
    * connects to an infura node to the given chain
    * chain should be in lower case
    * @dev: export WEB3_INFURA_PROJECT_ID='infural api key'
'''
def infura_connect(chain):
    return Web3(
        Web3.HTTPProvider(
            f"https://{chain}.infura.io/v3/{os.environ.get('WEB3_INFURA_PROJECT_ID')}"
        )
    )

'''
    * conects to the CHAIN via moralis
    * chain should be upper case
    * @dev: export MORALIS_{CHAIN}_ULS='moralis url' 
'''
def moralis_connect(CHAIN):
    return Web3(
        Web3.HTTPProvider(
            f"{os.environ.get(f'MORALIS_{isupper(CHAIN)}_URL')}"
        )
    )

'''
    * conects to the CHAIN via moralis
    * chain should be upper case
    * @dev: export MORALIS_{CHAIN}_ULS='moralis url' 
'''
def alchemy_connect(CHAIN):
    if islower(CHAIN) == "kovan" or "ropsten" or "goerli" or "rinkeby":
        return Web3(
            Web3.HTTPProvider(
                f"https://eth-{islower(CHAIN)}.alchemyapi.io/v2/{os.environ.get(f'ALCHEMY_{isupper(CHAIN)}_KEY')}"
            )
        )
    elif islower(CHAIN) == "mumbai":
        return Web3(
            Web3.HTTPProvider(
                f"https://polygon-mumbai.g.alchemy.com/v2/{os.environ.get(f'ALCHEMY_{isupper(CHAIN)}_KEY')}"
            )
        )
    elif islower(CHAIN) == "polygon":
        return Web3(
            Web3.HTTPProvider(
                f"https://polygon-mainnet.g.alchemy.com/v2/{os.environ.get(f'ALCHEMY_{isupper(CHAIN)}_KEY')}"
            )
        )
    
    #https://polygon-mumbai.g.alchemy.com/v2/aSB4f4sQyhP4goBApkLYqU4TVMeqI4Vs
    #https://eth-kovan.alchemyapi.io/v2/QRVXuuPuJUI5tfuNpyQJrIZH5Rn2AGBf
    return Web3(
        Web3.HTTPProvider(
            f"{os.environ.get(f'ALCHEMY_{isupper(CHAIN)}_KEY')}"
        )
    )
'''
    listens on port 8545 for an active node
'''
def connect_to_local():
    return Web3(
        Web3.HTTPProvider(
            "http://127.0.0.1:8545"
        )
    )

def provider_connect(chain, provider):
    if provider == "infura":
        return infura_connect(chain)
    if provider == "alchemy":
        return alchemy_connect(chain)
    if provider == "moralis":
        return moralis_connect(chain)
    else:
        return connect_to_local()
