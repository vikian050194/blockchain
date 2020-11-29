## Geth

[Документация](https://geth.ethereum.org/) по Geth

[Medium](https://medium.com/@chim/ethereum-how-to-setup-a-local-test-node-with-initial-ether-balance-using-geth-974511ce712)

### Установка

Устанавливается так
```
sudo apt-get install geth
```
Проверяем версию
```
geth version
```
Получаем сообщение вида
```
Geth
Version: 1.9.23-stable
Git Commit: 8c2f271528f9cccf541c6ea1c022e98407f26872
Architecture: amd64
Protocol Versions: [65 64 63]
Go Version: go1.15
Operating System: linux
GOPATH=
GOROOT=go
```

### Эксплуатация

БД Etherium и прочие данных хранятся в директории `data`. При необходимости её можно удалить
```
rm -rf data/
```

Создание аккаунта с паролем из файла `password`. Для учебных целей это будет `1234`, но никогда так не делайте в реальной жизни
```
geth account new --datadir=data --password=password
```
Список аккаунтов
```
geth account list --datadir=data
```
Инициализация БД Etherium
```
geth init --datadir=data genesis.json
```
Удаление БД (аккаунты остаются)
```
geth removedb --datadir=data
```
Подключение к уже запущенной ноде
```
geth attach data/geth.ipc
```
Запуск клиента, майнящего блоки на CPU в один поток
```
geth --datadir=data --mine --miner.threads=1 --nodiscover --verbosity=4
```
Для разблокировки аккаунта (или даже аккаунтов, для этого их можно перечислить через запятую) при запуске, надо добавить
```
--unlock=0x0000000000000000000000000000000000000000 --password=password
```
Для указания адреса зачисления вознаграждения за блоки
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
Существуют следующие уровни логирования

0. silent
1. error
2. warn
3. info
4. debug
5. detail

Значение по умолчанию `3`.