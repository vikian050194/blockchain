Существует онлайн-IDE для работы со смарт-контрактами
Ссылка https://ethfiddle.com
Особенность IDE - userfriendly интерфейс.
Работа с IDE предпочтительна через браузер Firefox, работа через Chrome нестабильна и вызывает проблемы. Ошибки можно увидеть в констоли браузера. 
Нет необходимости работы с JSON-файлами конфигурации смарт-контракта.
Автоизменение версии компилятора solidity среди доступных(добавляются только стабильные версии (на 09.01.21 максимальная версия 0.7.1, последняя вышедшая 0.8.0))
Автоматическое создание 10 пользователей.

Особенности при работе с IDE
1) Функция имеющая название = названию файла - конструктор при версии solidity<0.5.0
в противном случае конструктор функции пишется так:
 constructor () public
  {
    value = 0
  }
  
  Общий вид такого контракта может иметь вид 
pragma solidity ^0.5.4;// версия solidity
contract SimpleStore {
  function set(uint _value) public {
    value = _value;
  }

  function get() public constant returns (uint) {
    return value;
  }
  constructor () public//конструктор
  {
    value = 0
  }

  uint value;
}

// с 0.4

pragma solidity ^0.4.18;// версия solidity
contract SimpleStorePhrase {

  string[] public flow;
  uint public count;
  function SimpleStorePhrase() public//конструктор
  {
    count = 0;// изначальное число фраз - 0
  }

  function set(uint _value) public {
    value = _value;
  }

  function get() public constant returns (uint) {
    return value;
  }
  function PhraseCounter(string incide) public// увеличение счетчика фраз
   {
          count = count + 1;
   }

   

  uint value;
}

