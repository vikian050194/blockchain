from web3 import Web3
from solcx import compile_source
import random
import os
import wrapper


w = wrapper.get_http_wrapper(poa=True)

w.check_connection()

latest_block = w.get_block('latest')

CONTRACT_SOL = 'contracts/storage.sol'
CONTRACT_NAME = 'SimpleStorage'

path_to_first_node = 'node1/keystore'
onlyfiles = [os.path.join(path_to_first_node, f) for f in os.listdir(path_to_first_node) if os.path.isfile(os.path.join(path_to_first_node, f))]

PRIVATE_KEY_FILE=onlyfiles[0]
with open(PRIVATE_KEY_FILE) as keyfile:
   encrypted_key = keyfile.read()
   
PRIVATE_KEY = w.get_private_key(encrypted_key)

alice_account = w.get_account(PRIVATE_KEY)

contract_name, contract_interface = w.compile_contract(CONTRACT_SOL, CONTRACT_NAME)

contract_address = w.deploy_contract(alice_account, contract_interface)

contract = w.create_contract(contract_address, contract_interface)

# call non-transactional method
val = contract.functions.get().call()

assert val == 0

# call transactional method
nonce = w.get_nonce(alice_account)
# from_block_number = w3.eth.blockNumber
new_val = random.randint(1, 100)
contract_func = contract.functions.set(new_val)
print('Invoke set()={}'.format(new_val))
tx_hash = w.exec_contract(alice_account, nonce, contract_func)
print('tx_hash={} waiting for receipt..'.format(tx_hash))
tx_receipt = w.get_receipt(tx_hash)
print("Receipt accepted. gasUsed={gasUsed} blockNumber={blockNumber}". format(**tx_receipt))

# # catch event
# contract_filter = contract.events.Updated.createFilter(fromBlock=from_block_number)
# entries = None
# print('Waiting for event..')
# while not entries: entries = contract_filter.get_all_entries()
# # _new == new_val
# args = entries[0].args
# print(args)
# assert args._old == 0
# assert args._new == new_val
# assert args.by == alice_account.address

# call non-transactional method
val = contract.functions.get().call()
print('Invoke get()={}'.format(val))
assert val == new_val