abi = [
	{
		"inputs": [
			{
				"internalType": "contract ISuperfluid",
				"name": "host",
				"type": "address"
			},
			{
				"internalType": "contract IInstantDistributionAgreementV1",
				"name": "ida",
				"type": "address"
			},
			{
				"internalType": "contract IConstantFlowAgreementV1",
				"name": "cfa",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "publisher",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "address",
				"name": "subscriber",
				"type": "address"
			}
		],
		"name": "approveSubscription",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "int96",
				"name": "flowRate",
				"type": "int96"
			}
		],
		"name": "createFLowCXT",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			}
		],
		"name": "createIndex",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "int96",
				"name": "flowRate",
				"type": "int96"
			}
		],
		"name": "deleteFLowCXT",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "publisher",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "address",
				"name": "subscriber",
				"type": "address"
			}
		],
		"name": "deleteSubscription",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "distribute",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "publisher",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "address",
				"name": "subscriber",
				"type": "address"
			}
		],
		"name": "revokeSubscription",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "int96",
				"name": "flowRate",
				"type": "int96"
			}
		],
		"name": "updateFLowCXT",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "uint128",
				"name": "indextvalue",
				"type": "uint128"
			},
			{
				"internalType": "bytes",
				"name": "ctx",
				"type": "bytes"
			}
		],
		"name": "updateIndex",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "contract ISuperToken",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "uint32",
				"name": "id_",
				"type": "uint32"
			},
			{
				"internalType": "address",
				"name": "subscriber",
				"type": "address"
			},
			{
				"internalType": "uint128",
				"name": "units",
				"type": "uint128"
			}
		],
		"name": "updateSubscription",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]