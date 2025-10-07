from src.block import Block, BlockChainManager
import time

def test_genesis_block_exists():
    bc = BlockChainManager()
    assert len(bc.chain) == 1, "Should be 1"
    assert bc.chain[0].transactions == [], "Should be an empty list"

def test_add_block():
    bc = BlockChainManager()
    bc.add_block(Block(time.time(), ["amount = 97"]))
    assert len(bc.chain) == 2, "The length should be 2"

def test_previous_hash():
    bc = BlockChainManager()
    bc.add_block(Block(time.time(), ["amount = 97"]))
    last_block = bc.get_last_block()
    prev_block = bc.chain[-2]

    assert last_block.prior_hash == prev_block.hash, "Should have the same hash"