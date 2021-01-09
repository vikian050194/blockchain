Memory и Calldata - ключевые слова, определющие место обработки данных и где будут храниться переменные.
Memory декларирует используемые переменные, Calldata используестя при описании внешних параметров декларируемых функций
Простейший способ определить разницу между calldata и немодифицируемой зоной.
Время жизни памяти ограничено вызовом функции и предназначено для временного хранения переменных и их значений. Значения, хранящиеся в памяти, не сохраняются в сети после завершения транзакции

Некоторые примечания относительно параметра памяти Memory
1)Его можно использовать как для параметров объявления функции, так и в логике функции.
2)Он изменяемый (его можно перезаписывать и изменять)
3)Он непостояннен (значение не сохраняется после завершения транзакции)
Сalldata очень похожа на память в том смысле, что это место для хранения данных. 
Это специальное расположение данных, содержащее аргументы функции,
доступное только для параметров вызова внешней функции.
При этом, при вызове calldata функции могут быть ограничены по количеству используемых аргументов
Примечания к работе с calldata:
1)Сalldata-вызов неизменен( не может быть перезаписан и изменен)
2)Сalldata-вызов должен быть использован для вызова динамических параметров внешне настроенной функции
3)Сalldata-вызов стирается после завершения транзакции

Пример контракта с использованием Memory и Calldata
``` solidity
pragma solidity 0.5.11;

contract Test {

    string stringTest;

    function memoryTest(string memory _exampleString) public returns (string memory) {
        stringTest = "example";  // You can modify memory
        string memory newString = stringTest;  // You can use memory within a function's logic
        return stringTest;  // You can return memory
    }

    function calldataTest(string calldata _exampleString) external returns (string memory) {
        // cannot modify or return _exampleString
    }
}
```
Пример смарт-контракта с использованием Calldata и хранением вспомогательных значений в Memory
``` solidity
pragma solidity ^0.4.18;
contract Bank {
    address owner;
    mapping(address => uint) balances;
    
    function Bank() public{//конструктор
    owner = msg.sender;//определение объекта
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {//списание со счета
	// amount - значение хранится в Memory
        if (balances[msg.sender] >= amount) {//если на балансе достаточно средств
            balances[msg.sender] -= amount;//списать средства со счета
            msg.sender.transfer(amount);//передать средства
        }
    }
	// функция доступна только для любого вызова контракта( просмотр вашего баланса вами)
    function getMyBalance() public view returns(uint) {//функция возвращает текущий баланс, доступен вывод
        return balances[msg.sender];
    }
	// функция доступна только для внешнего вызова (просмотр вашего баланса внешним аккаунтом)
    function getMyBalance2() external view returns(uint) {//реагирует на внешний вызов call
        return balances[msg.sender];
    }

    function kill() public {//убийство объекта, защита от нелегального списания
        if (msg.sender == owner)
            selfdestruct(owner);
    }
}
```
calldata вызовы бывают следующие:
public - все имеют доступ

external - Только внешний вызов

internal - Вызов только внутри контракта и всех подконтрактов внутри этого контракта

private - Вызов только в текущем котракте
