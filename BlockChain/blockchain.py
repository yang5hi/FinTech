# Imports
import streamlit as st
import pandas as pd
from typing import List, Any
from dataclasses import dataclass
# Creating the Block data class
from datetime import datetime
import hashlib
#########################################################################
# Creating the Block data class
@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = 0
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Creating a data class called PyChain
@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()

st.markdown("# PyChain: A Python Blockcahin Application")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")


if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()
    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)


st.markdown("## PyChain Ledger")

pychain_df= pd.DataFrame(pychain.chain)
st.write(pychain_df)
st.write("abcd")