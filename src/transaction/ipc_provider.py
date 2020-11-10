from web3 import Web3, geth
import os

RPC_ADDRESS = 'data/geth.ipc'
w3 = Web3(Web3.IPCProvider(RPC_ADDRESS))

assert w3.isConnected() == True

block = w3.eth.getBlock('latest')

assert len(w3.eth.accounts) == 3

[aliceAccount, bobAccount, evaAccount] = w3.eth.accounts

aliceBalanceBefore = w3.eth.getBalance(aliceAccount)
bobBalanceBefore = w3.eth.getBalance(bobAccount)

value = 1000

tx_hash = w3.eth.sendTransaction({
   'from': aliceAccount,
   'to': bobAccount,
   'value': 1000
})

tx = w3.eth.getTransaction(tx_hash)

aliceBalanceAfter = w3.eth.getBalance(aliceAccount)
bobBalanceAfter = w3.eth.getBalance(bobAccount)

fee = 121000 * 100000000000000
assert bobBalanceBefore == bobBalanceAfter - value
assert aliceBalanceBefore == aliceBalanceAfter + value + fee

print("end")