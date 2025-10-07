from src.block import BlockChainManager
from src.transaction import Transaction
from src.validation import is_bc_valid

def test_full_blockchain_flow():
    bc = BlockChainManager()

    bc.create_transaction(Transaction("address1", "address2", 90))
    bc.create_transaction(Transaction("address2", "address1", 45))

    print("Strating minning process...")
    bc.mine_pending_transactions("miner-address")

    print(f"\nBalance of miner's wallet: {bc.get_balance_of_address('miner-address')}")
    print("Mining again to receive the reward...")

    bc.mine_pending_transactions("miner-address")
    print(f"\nBalance of miner's wallet after second mining: {bc.get_balance_of_address('miner-address')}")

    assert is_bc_valid(bc) == True
    assert bc.get_balance_of_address("miner-address") == 100
    assert bc.get_balance_of_address("address1") == -45
    assert bc.get_balance_of_address("address2") == 45
