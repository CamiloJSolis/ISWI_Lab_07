import hashlib
import time
from .transaction import Transaction
from .validation import is_bc_valid

class Block:
    def __init__(self, timestamp, transactions, prior_hash=''):
        self.timestamp = timestamp # The time the block was created
        self.transactions = transactions # The actual transfer data
        self.prior_hash = prior_hash # The hash of the previous block
        self.nonce = 0 # Initialize nonce to zero before creating the block
        self.hash = self.create_hash() # The hash of the current block

    def create_hash(self):
        # Return the SHA-256 hash of the block string with nonce in the hash calculation
        block_string = (str(self.prior_hash) + str(self.timestamp) + str(self.transactions) + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        # Loop until the hash begins with the required number of zeros
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.create_hash()
            print(f"Mining... Current nonce: {self.nonce}, Current hash: {self.hash}")

class BlockChainManager:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # Initialize the blockchain with the genesis block
        self.difficulty = 4 # Set the mining difficulty (number of leading zeros required in the hash)
        self.pending_transactions = [] # List to hold pending transactions
        self.mining_reward = 100 # Set mining reward for miners

    def create_genesis_block(self):
        # Create the first block in the chain with fixed parameters
        return Block(time.time(), [], "0")

    def get_last_block(self):
        return self.chain[-1] # Return the last block in the chain
    
    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty) # Mine the block before adding it to the chain
        self.chain.append(new_block) # Append the new block to the chain

    def mine_pending_transactions(self, mining_reward_address):
        # Create a new block with all pending transactions
        block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)

        # Add the newly mine block to the chain
        self.chain.append(block)

        # Reset the list of pending transactions and add a transaction to the reward winner
        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0 

        for block in self.chain:
            for transaction in block.transactions:
                if transaction.from_address == address:
                    balance -= transaction.amount
                if transaction.to_address == address:
                    balance += transaction.amount
        return balance
    
    def is_bc_valid(self):
        return is_bc_valid(self)