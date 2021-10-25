from web3 import Web3
from web3.middleware import geth_poa_middleware
from solcx import compile_source


def connect_via_test():
    return Web3(Web3.EthereumTesterProvider())


def connect_via_ipc(rpc_address='sandbox/node1/geth.ipc'):
    return Web3(Web3.IPCProvider(rpc_address))


def connect_via_http(rpc_address='http://localhost:8545', timeout=120):
    return Web3(Web3.HTTPProvider(rpc_address, request_kwargs={'timeout': timeout}))


class Wrapper():
    def __init__(self, w3=None):
        self.w3 = w3


    def to_wei(self, number, unit):
        return self.w3.toWei(number, unit)


    def send_transaction(self, address_from, address_to, value):
        return self.w3.eth.sendTransaction({
            'from': address_from,
            'to': address_to,
            'value': value
        })

    def compile_contract(self, contract_source_file, contractName=None):
        """
        Reads file, compiles, returns contract name and interface
        """
        with open(contract_source_file, "r") as f:
            contract_source_code = f.read()
        compiled_sol = compile_source(contract_source_code)
        if not contractName:
            contractName = list(compiled_sol.keys())[0]
            contract_interface = compiled_sol[contractName]
        else:
            contract_interface = compiled_sol['<stdin>:' + contractName]        
        return contractName, contract_interface


    def deploy_contract(self, account, contract_interface, contract_args=None):
        """
        deploys contract using self-signed tx, waits for receipt, returns address
        """
        contract = self.w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        constructed = contract.constructor() if not contract_args else contract.constructor(*contract_args)
        tx = constructed.buildTransaction({
            'from': account.address,
            'nonce': self.w3.eth.getTransactionCount(account.address),
        })
        print ("Signing and sending raw tx ...")
        signed = account.signTransaction(tx)
        tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
        print ("tx_hash = {} waiting for receipt ...".format(tx_hash.hex()))
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)
        contractAddress = tx_receipt["contractAddress"]
        print ("Receipt accepted. gasUsed={gasUsed} contractAddress={contractAddress}".format(**tx_receipt))
        return contractAddress


    def exec_contract(self, account, nonce, func):
        """
        call contract transactional function func
        """
        construct_txn = func.buildTransaction({'from': account.address, 'nonce': nonce})
        signed = account.signTransaction(construct_txn)
        tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
        return tx_hash.hex()


    def check_connection(self, connented = True):
        assert self.w3.isConnected() == connented

    def getaccounts(self):
        return self.w3.eth.accounts

    accounts=property(getaccounts)

    def get_accounts(self):
        return self.w3.eth.accounts

    def get_account(self, private_key):
        return self.w3.eth.account.privateKeyToAccount(private_key)


    def create_contract(self, contract_address, contract_interface):
        return self.w3.eth.contract(address=contract_address, abi=contract_interface['abi'])

    
    def get_nonce(self, account):
        return self.w3.eth.getTransactionCount(account.address)


    def get_receipt(self, tx_hash, timeout=120):
        return self.w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)

    
    def get_transaction(self, tx_hash):
        return self.w3.eth.getTransaction(tx_hash)

    
    def get_private_key(self, encrypted_key, password='1234'):
        return self.w3.eth.account.decrypt(encrypted_key, password)

    def get_block(self, index):
        return self.w3.eth.getBlock(index)

    def get_block_number(self):
        return self.w3.eth.blockNumber

    def get_balance(self, account):
        return self.w3.eth.getBalance(account)


def get_wrapper(w3, poa):
    if poa:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return Wrapper(w3)

def get_test_wrapper(poa=False):
    return get_wrapper(connect_via_test(), poa)

def get_http_wrapper(poa=False):
    return get_wrapper(connect_via_http(), poa)

def get_ipc_wrapper(poa=False):
    return get_wrapper(connect_via_ipc(), poa) 
    

__all__ = [
    'get_test_wrapper',
    'get_http_wrapper',
    'get_ipc_wrapper'
]