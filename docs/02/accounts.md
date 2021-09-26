## Accounts

[Source](https://ethdocs.org/en/latest/contracts-and-transactions/account-types-gas-and-transactions.html#eoa-vs-contract-accounts)

There are two types of accounts in Ethereum
- Externally Owned Accounts
- Contracts Accounts


### Externally owned accounts (EOAs)

An externally controlled account

- has an ether balance,
- can send transactions (ether transfer or trigger contract code),
- is controlled by private keys,
- has no associated code.

### Contract accounts

A contract

- has an ether balance,
- has associated code,
- code execution is triggered by transactions or messages (calls) received from other contracts.
- when executed - perform operations of arbitrary complexity - manipulate its own persistent storage, i.e., can have its own permanent state - can call other contracts
