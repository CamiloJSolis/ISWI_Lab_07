import hashlib

class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index # The position of the block in the chain
        self.timestamp = timestamp # The time the block was created
        self.data = data # The actual transfer data
        self.prior_hash = prior_hash # The hash of the previous block
        self.hash = self.create_hash() # The hash of the current block

    def create_hash(self):
        # Convert all properties into a string and encode it
        block_string = f"{self.index}{self.prior_hash}{self.timestamp}{self.data}".encode()
        # Return the SHA-256 hash of the block string
        return hashlib.sha256(block_string).hexdigest()

class BlockChainManager:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # Initialize the blockchain with the genesis block
    
    def create_genesis_block(self):
        # Create the first block in the chain with fixed parameters
        return Block(0, "12/12/2012", "ethereum.org", "0")

    def get_last_block(self):
        return self.chain[-1] # Return the last block in the chain
    
    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.hash = new_block.create_hash() 
        self.chain.append(new_block) # Append the new block to the chain