from wrapper import get_ipc_wrapper

w = get_ipc_wrapper()

w.check_connection()

zero_block = w.get_block('latest')

assert len(w.accounts) == 3

[alice_account, bob_account, eva_account] = w.accounts

alice_balance_before = w.get_balance(alice_account)
bob_balance_before = w.get_balance(bob_account)

value = w.to_wei(1, 'ether')

tx_hash = w.send_transaction(alice_account, bob_account, value)

tx = w.get_transaction(tx_hash)

alice_balance_after = w.get_balance(alice_account)
bob_balance_after = w.get_balance(bob_account)

first_block = w.get_block('latest')

gas_price = 1
fee = first_block.gasUsed * gas_price

assert fee == 21000

assert alice_balance_before == alice_balance_after + value + fee
assert bob_balance_before == bob_balance_after - value