from web3 import Web3, geth
import os

RPC_ADDRESS = 'data/geth.ipc'
w3 = Web3(Web3.IPCProvider(RPC_ADDRESS))

assert w3.isConnected() == True

block = w3.eth.getBlock('latest')

assert len(w3.eth.accounts) == 2

[aliceAccount, bobAccount] = w3.eth.accounts

aliceBalance = w3.eth.getBalance(aliceAccount)
bobBalance = w3.eth.getBalance(bobAccount)

aliceBalance = w3.eth.getBalance(aliceAccount)
bobBalance = w3.eth.getBalance(bobAccount)

tx_hash = w3.eth.sendTransaction({
   'from': aliceAccount,
   'to': bobAccount,
   'value': 1000
})

tx = w3.eth.getTransaction(tx_hash)

aliceBalance = w3.eth.getBalance(aliceAccount)
bobBalance = w3.eth.getBalance(bobAccount)

fee = 21000

assert aliceBalanceBefore == aliceBalanceAfter + wei + fee
assert bobBalanceBefore == bobBalanceAfter - wei