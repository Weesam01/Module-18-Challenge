# PyChain Ledger
################################################################################
# You’ll make the following updates to the provided Python file for this
# Challenge, which already contains the basic `PyChain` ledger structure that
# you created throughout the module:

# Step 1: Create a Record Data Class
# * Create a new data class named `Record`. This class will serve as the
# blueprint for the financial transaction records that the blocks of the ledger
# will store.

# Step 2: Modify the Existing Block Data Class to Store Record Data
# * Change the existing `Block` data class by replacing the generic `data`
# attribute with a `record` attribute that’s of type `Record`.

# Step 3: Add Relevant User Inputs to the Streamlit Interface
# * Create additional user input areas in the Streamlit application. These
# input areas should collect the relevant information for each financial record
# that you’ll store in the `PyChain` ledger.

# Step 4: Test the PyChain Ledger by Storing Records
# * Test your complete `PyChain` ledger.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Step 1:
# Create a Record Data Class

# Define a new Python data class named `Record`. Give this new class a
# formalized data structure that consists of the `sender`, `receiver`, and
# `amount` attributes. To do so, complete the following steps:
# 1. Define a new class named `Record`.
# 2. Add the `@dataclass` decorator immediately before the `Record` class
# definition.
# 3. Add an attribute named `sender` of type `str`.
# 4. Add an attribute named `receiver` of type `str`.
# 5. Add an attribute named `amount` of type `float`.
# Note that you’ll use this new `Record` class as the data type of your `record` attribute in the next section.


# @TODO
# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes

@dataclass
class Record:
    sender: str
    receiver: str
    amount: float
################################################################################
# Step 2:
# Modify the Existing Block Data Class to Store Record Data

# Rename the `data` attribute in your `Block` class to `record`, and then set
# it to use an instance of the new `Record` class that you created in the
# previous section. To do so, complete the following steps:
# 1. In the `Block` class, rename the `data` attribute to `record`.
# 2. Set the data type of the `record` attribute to `Record`.


@dataclass
class Block:
    # The `Block` class represents a block in the PyChain ledger.

    # @TODO
    # Rename the `data` attribute to `record`, and set the data type to `Record`
    # This attribute holds the financial transaction record for the block.
    # Replace `data` with `record` to make the code more descriptive.
    record: Record

    # The ID of the creator of the block.
    creator_id: int

    # The hash of the previous block in the chain.
    prev_hash: str = "0"

    # The timestamp of when the block was created.
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    # A random number used in the proof-of-work algorithm.
    nonce: int = 0

    def hash_block(self):
        # This method calculates the hash of the block using the SHA-256 algorithm.

        # Create a new SHA-256 hash object.
        sha = hashlib.sha256()

        # Convert the record to a string and encode it, then update the hash object.
        record = str(self.record).encode()
        sha.update(record)

        # Convert creator_id to a string and encode it, then update the hash object.
        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        # Convert timestamp to a string and encode it, then update the hash object.
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        # Convert prev_hash to a string and encode it, then update the hash object.
        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        # Convert nonce to a string and encode it, then update the hash object.
        nonce = str(self.nonce).encode()
        sha.update(nonce)

        # Return the hexadecimal representation of the hash.
        return sha.hexdigest()


@dataclass
class PyChain:
    # The `PyChain` class represents the blockchain ledger.

    # List to store blocks in the blockchain.
    chain: List[Block]

    # Difficulty level for the proof-of-work algorithm.
    difficulty: int = 4

    def proof_of_work(self, block):
        # Performs proof-of-work to mine a new block.

        # Calculate the hash of the given block.
        calculated_hash = block.hash_block()

        # Define a string with the required number of leading zeros.
        num_of_zeros = "0" * self.difficulty

        # Keep incrementing the nonce until the hash meets the difficulty criteria.
        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        print("Winning Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        # Adds a new block to the blockchain.

        # Mine the candidate block using proof-of-work.
        block = self.proof_of_work(candidate_block)

        # Add the mined block to the blockchain.
        self.chain += [block]

    def is_valid(self):
        # Checks the validity of the entire blockchain.

        # Get the hash of the first block in the chain.
        block_hash = self.chain[0].hash_block()

        # Iterate through the remaining blocks in the chain for validation.
        for block in self.chain[1:]:
            # Check if the hash of the current block matches the previous block's hash.
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            # Update the block_hash for the next iteration.
            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True


################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

################################################################################
# Step 3:
# Add Relevant User Inputs to the Streamlit Interface

# Code additional input areas for the user interface of your Streamlit
# application. Create these input areas to capture the sender, receiver, and
# amount for each transaction that you’ll store in the `Block` record.
# To do so, complete the following steps:
# 1. Delete the `input_data` variable from the Streamlit interface.
# 2. Add an input area where you can get a value for `sender` from the user.
# 3. Add an input area where you can get a value for `receiver` from the user.
# 4. Add an input area where you can get a value for `amount` from the user.
# 5. As part of the Add Block button functionality, update `new_block` so that `Block` consists of an attribute named `record`, which is set equal to a `Record` that contains the `sender`, `receiver`, and `amount` values. The updated `Block`should also include the attributes for `creator_id` and `prev_hash`.

# @TODO:
# Delete the `input_data` variable from the Streamlit interface.
# input_data = st.text_input("Block Data")

# @TODO:
# Add an input area where you can get a value for `sender` from the user.
sender = st.text_input("Input Sender Information")

# @TODO:
# Add an input area where you can get a value for `receiver` from the user.
receiver = st.text_input("Input Receiver Information")

# @TODO:
# Add an input area where you can get a value for `amount` from the user.
amount = st.text_input("Transaction Amount")

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # @TODO
    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        # data=input_data,
        record=Record(sender, receiver, amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

################################################################################
# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################
# Step 4:
# Test the PyChain Ledger by Storing Records

# Test your complete `PyChain` ledger and user interface by running your
# Streamlit application and storing some mined blocks in your `PyChain` ledger.
# Then test the blockchain validation process by using your `PyChain` ledger.
# To do so, complete the following steps:

# 1. In the terminal, navigate to the project folder where you've coded the
#  Challenge.

# 2. In the terminal, run the Streamlit application by
# using `streamlit run pychain.py`.

# 3. Enter values for the sender, receiver, and amount, and then click the "Add
# Block" button. Do this several times to store several blocks in the ledger.

# 4. Verify the block contents and hashes in the Streamlit drop-down menu.
# Take a screenshot of the Streamlit application page, which should detail a
# blockchain that consists of multiple blocks. Include the screenshot in the
# `README.md` file for your Challenge repository.

# 5. Test the blockchain validation process by using the web interface.
# Take a screenshot of the Streamlit application page, which should indicate
# the validity of the blockchain. Include the screenshot in the `README.md`
# file for your Challenge repository.
