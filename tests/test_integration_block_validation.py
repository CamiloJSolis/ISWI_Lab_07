from src.block import Block, BlockChainManager
from src.validation import is_bc_valid
import time

def test_blockchain_validation():
    bc = BlockChainManager()
    # Pass a list for transactions
    bc.add_block(Block(time.time(), ["amount = 1500M"]))  
    bc.add_block(Block(time.time(), ["amount = 2500M"]))

    assert is_bc_valid(bc) == True, "The blockchain should be valid"

def test_blockchain_tampering():
    bc = BlockChainManager()
    bc.add_block(Block(time.time(), ["amount = 1500M"]))
    bc.add_block(Block(time.time(), ["amount = 2500M"]))

    # Tamper with the transactions of the second block
    bc.chain[1].transactions = ["amount = you've been hacked ツ"]

    # Recalculate the tampered block's hash to simulate a malicious change
    bc.chain[1].hash = bc.chain[1].create_hash()

    assert is_bc_valid(bc) == False, "The blockchain should be invalid due to tampering"