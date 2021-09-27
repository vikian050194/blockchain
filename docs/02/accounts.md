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

Operation Name	Gas Cost	Remark
step	1	default amount per execution cycle
stop	0	free
suicide	0	free
sha3	20	 
sload	20	get from permanent storage
sstore	100	put into permanent storage
balance	20	 
create	100	contract creation
call	20	initiating a read-only call
memory	1	every additional word when expanding memory
txdata	5	every byte of data or code for a transaction
transaction	500	base fee transaction
contract creation	53000	changed in homestead from 21000