import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.block import Block, BlockChainManager

def test_genesis_blobk_exists():
    bc = BlockChainManager()
    assert len(bc.chain) == 1
    assert bc.chain[0].data == "ethereum.org"
    assert bc.chain[0].index == 0

def test_add_block():
    bc = BlockChainManager()
    bc.add_block(Block(1, "12/12/2012", "amount = 97"))
    assert len(bc.chain) == 2

def test_privious_hash():
    bc = BlockChainManager()
    bc.add_block(Block(1, "12/12/2012", "amount = 97"))
    last_block = bc.get_last_block()
    prev_block = bc.chain[-2]

    assert last_block.prior_hash == prev_block.hash