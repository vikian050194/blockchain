from ..wrapper import get_test_wrapper


w = get_test_wrapper()

w.check_connection()

zero_block = w.get_block('latest')

assert len(w.accounts) == 10

[alice_account, bob_account, *_] = w.accounts

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
