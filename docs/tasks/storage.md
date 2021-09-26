# Storage

## Описание

Хранилище одного целочисленного значения.

## Код

```sol
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0 <0.9.0;

contract SimpleStorage {
    uint storedData;

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

## Сделать

1. получить изначальное значение
2. записать `42` в качестве значения
3. проверить, что новое значение есть `42`
