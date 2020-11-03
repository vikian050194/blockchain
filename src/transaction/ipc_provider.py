from web3 import Web3, geth
import os

# RPC_ADDRESS = 'http://localhost:8545'
# w3 = Web3(Web3.HTTPProvider(RPC_ADDRESS, request_kwargs={'timeout': 120}))

RPC_ADDRESS = 'data/geth.ipc'
w3 = Web3(Web3.IPCProvider(RPC_ADDRESS))

# ALICE_PRIVATE_KEY = os.environ.get('ALICE_PRIVATE_KEY')
ALICE_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-47-44.156921182Z--4261615f91055c19e3d09f2584b47baf1fd58313'
with open(ALICE_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   ALICE_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')

# BOB_PRIVATE_KEY = os.environ.get('BOB_PRIVATE_KEY')
BOB_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-47-52.900024617Z--07358db463ca9449185d75040d8258d9ab564442'
with open(BOB_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   BOB_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')

assert w3.isConnected() == True

block = w3.eth.getBlock('latest')

assert len(w3.eth.accounts) == 3

aliceAccount = w3.eth.account.privateKeyToAccount(ALICE_PRIVATE_KEY)
bobAccount = w3.eth.account.privateKeyToAccount(BOB_PRIVATE_KEY)

# [alice, bob, *_] = w3.eth.accounts 

# aliceBalance = w3.eth.getBalance(alice)
# bobBalance = w3.eth.getBalance(bob)

aliceBalance = w3.eth.getBalance(aliceAccount.address)
bobBalance = w3.eth.getBalance(bobAccount.address)

tx_hash = w3.eth.sendTransaction({
   'from': aliceAccount.address,
   'to': bobAccount.address,
   'value': 1000
})

tx = w3.eth.getTransaction(tx_hash)

aliceBalance = w3.eth.getBalance(aliceAccount.address)
bobBalance = w3.eth.getBalance(bobAccount.address)