# Простая транзакция

Рассмотрим пример, в котором создадим транзакцию и переведём `1000 wei` с одного счёта на другой.

Ссылка на оригинальную статью [вотъ](https://ethereum.org/en/developers/tutorials/a-developers-guide-to-ethereum-part-one/).

Пример в `test_provider.py` работает с тестовым провайдером. Настроим реальную ноду, чтобы осуществить тот же самый перевод средств.

Установим `Geth` (см. [geth.md](tools/geth.md))

Удалим директорию, если они есть
```
rm -rf data/
```
Создадим два аккаунта, дважды вызвав
```
geth account new --datadir=data --password=password
```
Проверим, что есть два аккаунта
```
geth account list --datadir=data
```
Теперь можно инициализировать базу данных Эфириума
```
geth init --datadir=data genesis.json
```
Снести базу данных Эфириума (на всякий случай)
```
geth removedb --datadir=data
```
Запустить клиента майнить блоки, писать логи в файл и разблокировать аккаунт, адрес которого указан
```
geth --datadir=data --mine --miner.threads=1 --maxpeers=0 --nodiscover --verbosity=4
```
Для разблокировки аккаунта (или даже аккаунтов, для этого их можно перечислить через запятую) при запуске, надо добавить
```
--unlock=0x0000000000000000000000000000000000000000 --password=password
```
Для указания адреса для зачисления вознаграждения за блоки
```
--etherbase=0x0000000000000000000000000000000000000000
```
Для перенаправления вывода в файл
```
2>geth.log
```
Разблокировать первый аккаунт с паролем `1234` после запуска ноды
```
geth --exec "personal.unlockAccount(eth.accounts[0], '1234')" attach ipc:data/geth.ipc
```
Кстати, определены следующие уровни логирования

0. silent
1. error
2. warn
3. info
4. debug
5. detail

Значение по умолчанию - `3`.