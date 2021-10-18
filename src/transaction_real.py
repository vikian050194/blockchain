from wrapper import get_http_wrapper


w = get_http_wrapper(poa=True)

w.check_connection()

latest_block = w.get_block('latest')

assert len(w.accounts) == 2

[alice_account, bob_account] = w.accounts
# TODO fetch bob_account somehow
# есть первая нода и там живёт алиса
# враппер подключен к первой ноде
# мы через враппер (читай через web3) умеем получить адреса аккаунтов
# ВОПРОС: можно ли не подключаясь прямо ко второй ноде получить список аккаунтов, которые живут на ней
# судя по всему надо уметь получать список пиров как промежуточный шаг, но это не точно
# bob_account = w.getPeers()[0].accounts[0]

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