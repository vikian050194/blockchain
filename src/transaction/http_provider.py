from web3 import Web3, geth
import os

RPC_ADDRESS = 'http://localhost:8545'
w3 = Web3(Web3.HTTPProvider(RPC_ADDRESS, request_kwargs={'timeout': 120}))
