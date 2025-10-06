def is_bc_valid(self):
    for i in range(1, len(self.chain)):
        current_block = self.chain[i]
        previous_block = self.chain[i-1]

        # Check if the current block's hash is correct
        if current_block.hash != current_block.create_hash():
            return False
        
        # Check if the current block points to the correct previous block
        if current_block.prior_hash != previous_block.hash:
            return False
          
    return True