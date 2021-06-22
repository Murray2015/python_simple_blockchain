import random
from blockchain import BlockChain


def new_block(blockchain, sender, recipient, quantity):
    last_block = blockchain.latest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(
        sender=sender,
        recipient=recipient,
        quantity=quantity,
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)


def main():
    blockchain = BlockChain()

    print("\n***Mining about to start***")
    print(blockchain.chain)

    last_block = blockchain.latest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(
        sender="0",
        recipient="Hannah",
        quantity=1,
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)

    print("\n***Mining has been successful***")
    print(blockchain.chain)
    print()

    # Add more blocks
    for i in range(1, 40):
        last_block = blockchain.latest_block
        last_proof_no = last_block.proof_no
        proof_no = blockchain.proof_of_work(last_proof_no)
        new_block(blockchain=blockchain, sender=random.randint(0, 5), recipient=random.choice(
            ['Murray', 'Hannah']), quantity=random.randint(0, 1000))
        last_hash = last_block.calculate_hash
        block = blockchain.construct_block(proof_no, last_hash)
        print(f"\n***Mining has been successful for block {i}***")
        print(blockchain.chain)
        print()

    print(blockchain.chain)


if __name__ == "__main__":
    main()
