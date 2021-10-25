from wrapper import get_http_wrapper


w1 = get_http_wrapper(poa=True, node_index=1)
w2 = get_http_wrapper(poa=True, node_index=2)


w1.check_connection()
w2.check_connection()

latest_block = w1.get_block('latest')

assert len(w1.accounts) == 1
assert len(w2.accounts) == 1

[alice_account] = w1.accounts
[bob_account] = w2.accounts
# TODO fetch bob_account somehow
# есть первая нода и там живёт алиса
# враппер подключен к первой ноде
# мы через враппер (читай через web3) умеем получить адреса аккаунтов
# ВОПРОС: можно ли не подключаясь прямо ко второй ноде получить список аккаунтов, которые живут на ней
# судя по всему надо уметь получать список пиров как промежуточный шаг, но это не точно
# bob_account = w.getPeers()[0].accounts[0]
# UPD: на данный момент вопрос решёл созданием второго экземпляра враппера

alice_balance_before = w1.get_balance(alice_account)
bob_balance_before = w1.get_balance(bob_account)

value = w1.to_wei(1, 'ether')

tx_hash = w1.send_transaction(alice_account, bob_account, value)

tx = w1.get_transaction(tx_hash)

alice_balance_after = w1.get_balance(alice_account)
bob_balance_after = w1.get_balance(bob_account)

first_block = w1.get_block('latest')

gas_price = tx.gasPrice
fee = first_block.gasUsed * gas_price

assert fee == 0

assert alice_balance_before == alice_balance_after + value + fee
assert bob_balance_before == bob_balance_after - value