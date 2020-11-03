from web3 import Web3

w3 = Web3(Web3.EthereumTesterProvider())

assert w3.isConnected() == True

wei = w3.toWei(42, 'ether')

block = w3.eth.getBlock('latest')

assert len(w3.eth.accounts) == 10

[aliceAccount, bobAccount, *_] = w3.eth.accounts

aliceBalanceBefore = w3.eth.getBalance(aliceAccount)
bobBalanceBefore = w3.eth.getBalance(bobAccount)

zeroBlock = w3.eth.getBlock('latest')

tx_hash = w3.eth.sendTransaction({
   'from': aliceAccount,
   'to': bobAccount,
   'value': wei
})

tx = w3.eth.getTransaction(tx_hash)

aliceBalanceAfter = w3.eth.getBalance(aliceAccount)
bobBalanceAfter = w3.eth.getBalance(bobAccount)

aliceBlock = w3.eth.getBlock('latest')

fee = 21000

assert aliceBalanceBefore == aliceBalanceAfter + wei + fee
assert bobBalanceBefore == bobBalanceAfter - wei