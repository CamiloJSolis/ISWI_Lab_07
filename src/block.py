import hashlib

class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index # The position of the block in the chain
        self.timestamp = timestamp # The time the block was created
        self.data = data # The actual transfer data
        self.prior_hash = prior_hash # The hash of the previous block
        self.nonce = 0 # Initialize nonce to zero before creating the block
        self.hash = self.create_hash() # The hash of the current block

    def create_hash(self):
        # Return the SHA-256 hash of the block string with nonce in the hash calculation
        return hashlib.sha256(f"{self.index}{self.prior_hash}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()
    
    def mine_block(self, difficulty):
        # Loop until the hash begins with the required number of zeros
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.create_hash()
            print(f"Mining... Current nonce: {self.nonce}, Current hash: {self.hash}")

class BlockChainManager:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # Initialize the blockchain with the genesis block
        self.difficulty = 4 # Set the mining difficulty (number of leading zeros required in the hash)

    def create_genesis_block(self):
        # Create the first block in the chain with fixed parameters
        return Block(0, "12/12/2012", "ethereum.org", "0")

    def get_last_block(self):
        return self.chain[-1] # Return the last block in the chain
    
    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty) # Mine the block before adding it to the chain
        self.chain.append(new_block) # Append the new block to the chain