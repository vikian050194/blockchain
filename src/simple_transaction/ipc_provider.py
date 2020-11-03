from web3 import Web3, geth
import os

# RPC_ADDRESS = 'http://localhost:8545'
# w3 = Web3(Web3.HTTPProvider(RPC_ADDRESS, request_kwargs={'timeout': 120}))

RPC_ADDRESS = 'data/geth.ipc'
w3 = Web3(Web3.IPCProvider(RPC_ADDRESS))

# ALICE_PRIVATE_KEY = os.environ.get('ALICE_PRIVATE_KEY')
ALICE_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-03-07.804121564Z--3ae17dec4006a5033cc5087b060eedfa3f8c76c0'
with open(ALICE_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   ALICE_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')

# BOB_PRIVATE_KEY = os.environ.get('BOB_PRIVATE_KEY')
BOB_PRIVATE_KEY_FILE='data/keystore/UTC--2020-11-03T07-06-18.204973254Z--6acdf5fbb459bb42df8c29e17b59de0ef84bc559'
with open(BOB_PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   BOB_PRIVATE_KEY = w3.eth.account.decrypt(encrypted_key, '1234')

assert w3.isConnected() == True

block = w3.eth.getBlock('latest')

assert len(w3.eth.accounts) == 2

aliceAccount = w3.eth.account.privateKeyToAccount(ALICE_PRIVATE_KEY)
bobAccount = w3.eth.account.privateKeyToAccount(BOB_PRIVATE_KEY)

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