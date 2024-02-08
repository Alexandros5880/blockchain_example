import json
from blockchain import Blockchain

    
def transfer(blockchain, sender, recipient, amount):
    # Create a new transaction
    blockchain.new_transaction(sender, recipient, amount)

    # Mine the block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    
    # Forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    blockchain.new_block(proof, previous_hash)


if __name__=="__main__":
    # Instantiate the Blockchain
    blockchain = Blockchain()

    transfer(blockchain, "Alice", "Bob", 10)
    transfer(blockchain, "Alice", "Jaims", 10)
    transfer(blockchain, "Alice", "Alexander", 1000000000)

    # Print the full blockchain
    print(json.dumps(blockchain.chain, indent=4))
