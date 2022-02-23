# Imports
import streamlit as st
import numpy as np
import pandas as pd
from typing import List
from dataclasses import dataclass
# Creating the Block data class
from datetime import datetime
from typing import Any
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

input_date = st.text_input("Block Data")
