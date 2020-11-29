import wrapper

w = wrapper.get_http_wrapper(poa=True)

w.check_connection()

latest_block = w.get_block('latest')

assert len(w.accounts) == 1

[alice_account] = w.accounts
bob_account = "0x2dbaf8ED297EDba8ec0565A4b7C0d601dbD29250"

alice_balance_before = w.get_balance(alice_account)
bob_balance_before = w.get_balance(bob_account)

value = w.to_wei(1, 'ether')

tx_hash = w.send_transaction(alice_account, bob_account, value)

tx = w.get_transaction(tx_hash)

alice_balance_after = w.get_balance(alice_account)
bob_balance_after = w.get_balance(bob_account)

first_block = w.get_block('latest')

gas_price = tx.gasPrice
fee = first_block.gasUsed * gas_price

assert fee == 0

assert alice_balance_before == alice_balance_after + value + fee
assert bob_balance_before == bob_balance_after - value