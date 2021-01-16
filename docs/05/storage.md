## Storage

Теперь попробуем смарт-контракт `Storage`. Всё должно работать из коробки.

**Смарт-контракты Storage**

**Что такое смарт-контракты Storage？**

Каждый смарт-контракт, развернутый в блокчейне Neo, владеет частным
хранилищем, где только сам контракт может читать, записывать, изменять и
удалять данные. Данные в хранилище хранятся в виде пар ключ-значение,
где Key может быть строкой или массивом байтов (ByteArray), а Value
может быть любого типа.

В Neo большинство операций с хранилищем выполняется через StorageMap,
которая добавляет префикс к ключу хранилища. Различные префиксы
эквивалентны разным таблицам базы данных. Использование StorageMap для
управления хранилищем более безопасно.

Операции хранения смарт-контрактов включают в себя следующие интерфейсы:

-   Storage.Find () ： просматривает все записи в хранилище

-   Storage.Get () ： возвращает конкретную запись по указанному ключу

-   Storage.Put () ： изменяет или записывает новую запись в
    соответствии с указанным ключом

-   Storage.Delete () ： удаляет запись по указанному ключу

Обычно контракт может только читать и записывать данные в собственное
хранилище, но есть исключения:

-   В случае, если контракты вызывают друг друга, вызванный контракт
    может получить доступ к хранилищу вызывающего абонента через
    междоменные запросы, если он был авторизован вызывающим.

-   Для дочернего контракта, который динамически создается во время
    выполнения контракта, родительский контракт немедленно получает
    доступ для чтения и записи к хранилищу дочернего контракта.

**Объявление StorageMap**

Если хранилище контракта эквивалентно базе данных, StorageMap
эквивалентен таблицам в этой базе данных.

Чтобы объявить StorageMap:

StorageMap Hash = Storage.CurrentContext.CreateMap (nameof (Hash));

или же

var Hash = Storage.CurrentContext.CreateMap («Hash»);

**Операции хранения**

Обратитесь к классам Storage и StorageMap. Класс Helper предоставляет
StorageMap расширенные методы для операций хранения. Вот несколько
примеров кода.

**Запись и изменение**

Без StorageMap ：

Storage.Put("hello-1", new byte\[\]{ 1, 2, 3});

Storage.Put("hello-2", "world");

С StorageMap ：

StorageMap Hash = Storage.CurrentContext.CreateMap (nameof (Hash));

Hash.Put("hello-1", new byte\[\]{ 1, 2, 3});

Hash.Put("hello-2", "world");

**Запрос**

Без StorageMap ：

Storage.Get("hello-1");

С StorageMap ：

StorageMap Hash = Storage.CurrentContext.CreateMap(nameof(Hash));

Hash.Get("hello-1");

**Удаление**

Без StorageMap ：

Storage.Delete("hello-1");

С StorageMap ：

StorageMap Hash = Storage.CurrentContext.CreateMap(nameof(Hash));

Hash.Delete("hello-1");

**Перемещение**

var result = Storage.Find("Hash");

while (result.Next())

{

//process result.Key;

//process result.Value;

}

**Пример простого контракта**

Этот контракт имеет хранилище в следующей структуре:

-   ключ: сообщение как строковый тип ；

-   значение: высота блока как тип блока

Этот контракт содержит следующие методы:

-   put: помещает сообщение в хранилище

-   get: получает сообщение из хранилища

-   exists: проверяет, есть ли сообщение в хранилище

Код ：

using Neo.SmartContract.Framework;

using Neo.SmartContract.Framework.Services.Neo;

using Neo.SmartContract.Framework.Services.System;

using System;

using System.Collections.Generic;

using System.ComponentModel;

using System.Numerics;

namespace StorageExample

{

public class Contract1 : SmartContract

{

\[DisplayName("saved")\]

public static event Action&lt;string, uint&gt; Saved;

public static object Main(string method, object\[\] args)

{

if (Runtime.Trigger == TriggerType.Application)

{

if (method == "put") return Put((string)args\[0\]);

if (method == "get") return Get((string)args\[0\]);

if (method == "exists") return Exists((string)args\[0\]);

}

return true;

}

\[DisplayName("put")\]

public static bool Put(string message)

{

if (Exists(message)) return false;

var blockChainHeight = Blockchain.GetHeight();

Storage.Put(message, blockChainHeight);

Saved(message, blockChainHeight);

return true;

}

\[DisplayName("get")\]

public static int Get(string message)

{

if (!Exists(message)) return -1;

return (int)Storage.Get(message).ToBigInteger();

}

\[DisplayName("exists")\]

public static bool Exists(string message)

{

return Storage.Get(message) != null;

}

}

}

Где используется \[DisplayName ("getSavedBlock")\] - для совместимости с
правилами именования методов смарт-контрактов (Camel) и правилами
именования методов C \# (Pascal).

Имя в \[DisplayName ("getSavedBlock")\] можно найти в файле
manifest.json. Оно должно совпадать с именем метода, определяющего
переход в основном методе.

Примечания:*В смарт-контракте количество cases в операторе Main () не
должно превышать 7, в противном случае при вызове контракта будет выдана
ошибка, даже если он может быть скомпилирован. В этом случае
рекомендуется использовать оператор if.*

*Если вы используете StorageMap, вы должны объявить StorageMap внутри
метода как локальную переменную, иначе при вызове контракта будет
сообщено об ошибке, даже если он может быть скомпилирован.*
