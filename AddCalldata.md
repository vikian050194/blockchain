```
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
        if (balances[msg.sender] >= amount) {//если на балансе достаточно средств
            balances[msg.sender] -= amount;//списать средства со счета
            msg.sender.transfer(amount);//передать средства
        }
    }

    function getMyBalance() public view returns(uint) {//функция возвращает текущий баланс, доступен вывод
        return balances[msg.sender];
    }
    function getMyBalance2() external view returns(uint) {//реагирует на внешний вызов call
        return balances[msg.sender];
    }

    function kill() public {//убийство объекта, защита от нелегального списания
        if (msg.sender == owner)
            selfdestruct(owner);
    }
}
```