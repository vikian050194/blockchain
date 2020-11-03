# Простая транзакция

Рассмотрим пример, в котором создадим транзакцию и переведём 42 эфира с одного счёта на другой.

Ссылка на оригинальную статью [вотъ](https://ethereum.org/en/developers/tutorials/a-developers-guide-to-ethereum-part-one/).

# Geth

Пример работает с тестовым провайдером/нодой. Настало время настроить рельнреальную ноду и осуществить тот же самый перевод средств.

Установим `Geth`
```
sudo apt-get install geth
```
Удалим директорию, если они есть
```
rm -rf data/
```
Создадим два аккаунта, дважды вызвав
```
geth account new --datadir=data
```
Проверим, что есть два аккаунта
```
geth account list --datadir=data
```
Теперь можно инициализировать базу данных Эфириума
```
geth init --datadir=data genesis.json
```
Снести базу данных Эфириума
```
geth removedb --datadir=data
```
Запустить клиента майнить блоки, писать логи в файл и разблокировать аккаунт
```
geth --datadir=data --mine --miner.threads=1 --maxpeers=0 --nodiscover --verbosity=4 --unlock=0x0000000000000000000000000000000000000000 2>geth.log
```

Разблокировать аккаунт после запуска ноды
```
geth --exec "personal.unlockAccount(eth.accounts[0], '1234')" attach ipc:data/geth.ipc
```
Кстати
```
logging verbosity: 0=silent, 1=error, 2=warn, 3=info, 4=debug, 5=detail (default: 3)
```