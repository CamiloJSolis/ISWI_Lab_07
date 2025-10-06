from src.block import Block, BlockChainManager
from src.validation import is_bc_valid

def test_blockchain_validation():
    bc = BlockChainManager()
    bc.add_block(Block(1, "13/12/2012", "amount = 1500M"))
    bc.add_block(Block(2, "14/12/2012", "amount = 2500M"))

    assert is_bc_valid(bc) == True, "The blockchain should be valid"

def test_blockchain_tampering():
    bc = BlockChainManager()
    bc.add_block(Block(1, "13/12/2012", "amount = 1500M"))
    bc.add_block(Block(2, "14/12/2012", "amount = 2500M"))

    # Tamper with the data of the second block
    bc.chain[1].data = "amount = you've been hacked ツ"

    assert is_bc_valid(bc) == False, "The blockchain should be invalid due to tampering"