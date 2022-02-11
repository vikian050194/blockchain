import os
import random
from wrapper import get_http_wrapper as get_wrapper


w = get_wrapper(poa=True)

w.check_connection()

latest_block = w.get_block('latest')

CONTRACT_SOL = 'contracts/storage.sol'
CONTRACT_NAME = 'SimpleStorage'

path_to_first_node = 'sandbox/node1/keystore'
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
new_val = random.randint(1, 100)
contract_func = contract.functions.set(new_val)
print('Invoke set()={}'.format(new_val))
tx_hash = w.exec_contract(alice_account, nonce, contract_func)
print('tx_hash={} waiting for receipt..'.format(tx_hash))
tx_receipt = w.get_receipt(tx_hash)
print("Receipt accepted. gasUsed={gasUsed} blockNumber={blockNumber}". format(**tx_receipt))

# call non-transactional method
val = contract.functions.get().call()
print('Invoke get()={}'.format(val))
assert val == new_val