import streamlit as st
import numpy as np
import pandas as pd
# Imports
from dataclasses import dataclass
# Creating the Block data class
from datetime import datetime
from typing import Any

# Creating the Block data class
@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
# Creating a new block
new_block = Block(data="My First Block!", creator_id=42)

# Print the new block
print(new_block)

##########################################################################
st.write("# Python Web App")
st.write("## This is a Test Run")
st.write("Hi, this is our first web app in Python! :sunglasses: My Boss My Hero")
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write(df)
input_value = st.text_input("Enter a Message")
if st.button("Display Message"):
    st.write(input_value)