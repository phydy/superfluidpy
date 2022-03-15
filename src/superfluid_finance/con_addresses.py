
'''
    a dictionary of superfluid network addresses mapped with their network IDs
'''

addresses = {
    "polygon": {
        "host":"0x3E14dC1b13c488a8d5D310918780c983bD5982E7",
        "cfa" :"0x6EeE6060f715257b970700bc2656De21dEdF074C",
        "ida" : "0xB0aABBA4B2783A72C52956CDEF62d438ecA2d7a1",
        "factory": "0x2C90719f25B10Fc5646c82DA3240C76Fa5BcCF34"
    },
    "gnosis" : {
        "host": "0x2dFe937cD98Ab92e59cF3139138f18c823a4efE7",
        "cfa" :"0xEbdA4ceF883A7B12c4E669Ebc58927FBa8447C7D",
        "ida" :"0x7888ac96F987Eb10E291F34851ae0266eF912081",
        "factory": "0x23410e2659380784498509698ed70E414D384880"
    },
    "kovan" : {
        "host":"0xF0d7d1D47109bA426B9D8A3Cde1941327af1eea3",
        "cfa" :"0xECa8056809e7e8db04A8fF6e4E82cD889a46FE2F",
        "ida" :"0x556ba0b3296027Dd7BCEb603aE53dEc3Ac283d2b",
        "factory": "0xF5F666AC8F581bAef8dC36C7C8828303Bd4F8561"
    },
    "mumbai": {
        "host": "0xEB796bdb90fFA0f28255275e16936D25d3418603",
        "cfa" : "0xEd6BcbF6907D4feEEe8a8875543249bEa9D308E8",
        "ida" : "0xfDdcdac21D64B639546f3Ce2868C7EF06036990c",
        "factory": "0x200657E2f123761662567A1744f9ACAe50dF47E6"
    },
    "goerli": {
        "host" :"0x22ff293e14F1EC3A09B137e9e06084AFd63adDF9", 
        "cfa" :"0xEd6BcbF6907D4feEEe8a8875543249bEa9D308E8", 
        "ida" :"0xfDdcdac21D64B639546f3Ce2868C7EF06036990c",
        "factory": "0x94f26B4c8AD12B18c12f38E878618f7664bdcCE2"
    },
    "rinkeby" : {
        "host": "0xeD5B5b32110c3Ded02a07c8b8e97513FAfb883B6",
        "cfa": "0xF4C5310E51F6079F601a5fb7120bC72a70b96e2A",
        "ida": "0x32E0ecb72C1dDD92B007405F8102c1556624264D",
        "factory": "0xd465e36e607d493cd4CC1e83bea275712BECd5E0"
    },
    "ropsten" : {
        "host": "0xF2B4E81ba39F5215Db2e05B2F66f482BB8e87FD2",
        "cfa": "0xaD2F1f7cd663f6a15742675f975CcBD42bb23a88",
        "ida": "0xAD1e87F0C74341ecAFc1d27349dD6e650f5bAdD7",
        "factory": "0x6FA165d10b907592779301C23C8Ac9d1F79ca930"
    }
}

def is_allowed_network(id):
    if id in addresses:
        return True
    else:
        return False
