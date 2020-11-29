## Тестовая сеть из нескольких узлов

Вот ссылки на [три](https://www.c-sharpcorner.com/article/setup-your-private-ethereum-network-with-geth2/) [толковые](https://medium.com/coinmonks/private-ethereum-by-example-b77063bb634f) [статьи](https://habr.com/ru/post/481052/), на основе которых написана эта cтраница. Правда, они уже устарели и авторы сразу предлагают использовать контейнеры, поэтому материал переработан и актуализирован (на момент написания).

Итак, для начала убедимся, что у нас есть файл `password`. В нём находится пароль от всех аккаунтов на всех клиентах, которые мы будем создавать.

Создадим две папки
```
mkdir node1 node2
```
В каждой из них создадим по одному аккаунту
```
geth account new --datadir=node1 --password=password
geth account new --datadir=node2 --password=password
```
Сохраним адрес аккаунта в файл `account` (заменив `0x0...1` на реальное значение, конечно), чтобы всегда были под рукой
```
echo 0x0000000000000000000000000000000000000001 > node1/account
echo 0x0000000000000000000000000000000000000002 > node2/account
```
Теперь создадим `genesis.json`, который используем для инициализации клиентов. Возпользуемся утилитой `puppeth`.
Вызовем
```
puppeth
```
На первый вопрос в качестве имени укажем `genesis`
```
+-----------------------------------------------------------+
| Welcome to puppeth, your Ethereum private network manager |
|                                                           |
| This tool lets you create a new Ethereum network down to  |
| the genesis block, bootnodes, miners and ethstats servers |
| without the hassle that it would normally entail.         |
|                                                           |
| Puppeth uses SSH to dial in to remote servers, and builds |
| its network components out of Docker containers using the |
| docker-compose toolset.                                   |
+-----------------------------------------------------------+

Please specify a network name to administer (no spaces, hyphens or capital letters please)
> genesis
```
Теперь выберем пункт `2`
```
Sweet, you can set this via --network=genesis next time!

INFO [11-29|15:46:37.453] Administering Ethereum network           name=genesis
WARN [11-29|15:46:37.519] No previous configurations found         path=/home/kirill/.puppeth/genesis

What would you like to do? (default = stats)
 1. Show network stats
 2. Configure new genesis
 3. Track new remote server
 4. Deploy network components
 > 2
```
Хотим создать - `1`
```
What would you like to do? (default = create)
 1. Create new genesis from scratch
 2. Import already existing genesis
> 1
```
Выбираем PoA - `2`
```
Which consensus engine to use? (default = clique)
 1. Ethash - proof-of-work
 2. Clique - proof-of-authority
> 2
```
В нашем случае не имеет значения, пусть будет `15`
```
How many seconds should blocks take? (default = 15)
> 15
```
Укажим только первый аккаунт, он будет "авторитетным"
```
Which accounts are allowed to seal? (mandatory at least one)
> 0x0000000000000000000000000000000000000001
> 0x
```
Укажем оба аккаунта, т.к. этот `genesis.json` будет использован для инициализации обоих клиентов
```
Which accounts should be pre-funded? (advisable at least one)
> 0x0000000000000000000000000000000000000001
> 0x0000000000000000000000000000000000000002
> 0x
```
Пожалуй, не будем добавлять кучу ненужных адресов
```
Should the precompile-addresses (0x1 .. 0xff) be pre-funded with 1 wei? (advisable yes)
> no
```
Пусть будет `1234`
```
Specify your chain/network ID if you want an explicit one (default = random)
> 1234
```
Осталось сохранить всё в файл
```
What would you like to do? (default = stats)
 1. Show network stats
 2. Manage existing genesis
 3. Track new remote server
 4. Deploy network components
> 2
```
и ещё раз `2`
```
1. Modify existing configurations
 2. Export genesis configurations
 3. Remove genesis configuration
> 2
```
Ага, прямо сюда
```
Which folder to save the genesis specs into? (default = current)
  Will create genesis.json, genesis-aleth.json, genesis-harmony.json, genesis-parity.json
>
```
Отлично
```
INFO [11-29|16:12:09.564] Saved native genesis chain spec          path=genesis.json
ERROR[11-29|16:12:09.564] Failed to create Aleth chain spec        err="unsupported consensus engine"
ERROR[11-29|16:12:09.629] Failed to create Parity chain spec       err="unsupported consensus engine"
INFO [11-29|16:12:09.629] Saved genesis chain spec                 client=harmony path=genesis-harmony.json
```
Для выхода из `puppeth` жмём `Ctrl+C`
Далее удалим `genesis-harmony.json`, т.к. он нам не нужен
```
rm genesis-harmony.json
```
Подправим значение периода, чтобы новый блок создавался только если есть новая транзакция. `git diff -- genesis.json` после исправления должен выдать что-то типа
```
git diff -- genesis.json
diff --git a/genesis.json b/genesis.json
index 93f2e4c..b328421 100644
--- a/genesis.json
+++ b/genesis.json
@@ -11,7 +11,7 @@
     "petersburgBlock": 0,
     "istanbulBlock": 0,
     "clique": {
-      "period": 15,
+      "period": 0,
       "epoch": 30000
     }
   },
```
Инициализируем клиентов
```
geth --datadir=node1 init genesis.json
geth --datadir=node2 init genesis.json
```
Создадим файл `command`, в который запишем `bash` скрипт для запуска клиента
```
geth --nousb --datadir=$pwd --syncmode=full --port=30310 --miner.gasprice=0 --miner.gastarget=470000000000 --http --http.addr=localhost --http.port=8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock=0x0000000000000000000000000000000000000001 --password=../password --nodiscover --verbosity=4 console 2>geth.log
```
И для второго
```
geth --nousb --datadir=$pwd --syncmode=full --port=30311 --miner.gasprice=0 --miner.gastarget=470000000000 --http --http.addr=localhost --http.port=8546 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock=0x0000000000000000000000000000000000000002 --password=../password --nodiscover --verbosity=4 console 2>geth.log
```

> Если хочется запустить "в фоновом режиме", то надо дописать перед всей командой `nohup` и удалить `console` из ключей. Но для того, чтобы воспользоваться консолью придётся делать `attach`.

Запустим два терминала, перейдём в `node1` и `node2` соответсвенно и выполним `bash command`. Должно появиться что-то вида
```
Welcome to the Geth JavaScript console!

instance: Geth/v1.9.24-stable-cc05b050/linux-amd64/go1.15.5
coinbase: 0x4753811b64845535945dafc6a10c1fbe6ca916f7
at block: 0 (Sun Nov 29 2020 15:49:23 GMT+0300 (MSK))
 datadir: /home/kirill/git/personal/blockchain/node1
 modules: admin:1.0 clique:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

To exit, press ctrl-d
> 
```
В каждом из `log` файлов найдём строку с адресом. В ней есть такой текст `Started P2P networking`. А интересующее нас значение имеет вид
```
enode://что-то-там@127.0.0.1:30310
```
Приписка `?discport=0` видимо обусловлена использонием ключа `--nodiscover`.

Прервём оба процесс по `Ctrl+D`. Нам необходимо создать конфигурационный файл, который будет содержать адреса пиров. Можно это сделать и в консоли, но во имя автоматизации делаем через файл.
> Альтернативным способом является создание дампа конфигурации клиента. Для этого при запуске надо добавить ключ `dumpconfig`. Можно перенаправить вывод: `dumpconfig > config.toml`. Хотя там есть тонкости, связанные с тем статический или нет пир получается, инбаунд или нет.
```
touch config.toml
```
Структура файла слудующая
```
[Node.P2P]
StaticNodes = ["enode://что-то-там@127.0.0.1:30310", "enode://что-тотам@127.0.0.1:30311", "enode://что-тотам@127.0.0.1:30312"]
```

Для всех клиентов добавим в команду ключ
```
--config=../config.toml
```
Так или иначе получаем после запуска два (или если почему-то хочется или интересно, то более) клиента, которые знаю друг о друге.